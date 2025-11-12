# lib/intai/lyzron_assist.py
"""
Advanced LyzronAssist (Metasploit-like, English).
- Backwards compatible: summarize(text, max_sentences=3) still works.
- New features: exploit/result automatic analysis, severity scoring,
  auto-recommendations, structured JSON reports for modules/sessions.
- CLI additions: ai report-module <module> key=val;...
"""

import time
import json
import traceback
from typing import Dict, Any, List, Optional
from .action_logger import ActionLogger
from .report_manager import ReportManager
from .summarizer import summarize  # existing summarizer kept

# ---------- Helper utilities ----------
def _safe(func, *args, fallback=None, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception:
        return fallback

def _now_ts() -> float:
    return time.time()

# ---------- Main class ----------
class LyzronAssist:
    def __init__(self, modules_dir: str = "modules"):
        self.logger = ActionLogger()
        self.reporter = ReportManager()
        self.modules_dir = modules_dir
        self.known_commands = [
            "use", "set", "setg", "run", "search", "sessions",
            "jobs", "back", "exit", "help", "ai", "report", "report-module"
        ]

    def suggest_command(self, user_input: str) -> Optional[str]:
        parts = user_input.strip().split()
        if not parts:
            return None
        cmd = parts[0].lower()
        if cmd not in self.known_commands:
            possibilities = [c for c in self.known_commands if c.startswith(cmd[0])]
            if possibilities:
                return f"Suggestion: command '{cmd}' is unknown. Did you mean '{possibilities[0]}'?"
            return f"Warning: unknown command '{cmd}'. Use 'help' to list commands."
        return None

    # ---------- Result handling ----------
    def assist_command_result(self, command: str, result: Optional[str] = None,
                              error: Optional[Exception] = None,
                              start_time: Optional[float] = None) -> None:
        duration = (time.time() - start_time) if start_time else None
        if error:
            err_txt = str(error) or "Unknown error"
            err_summary = _safe(summarize, err_txt, max_sentences=2, fallback=err_txt[:2000])
            print(f"[Lyzron Assist] Error detected: {err_txt}")
            print(f"[Lyzron Assist] Summary: {err_summary}")
            try:
                self.logger.log(command, status="error", result=None, error=err_txt, duration=duration)
            except Exception as e:
                print(f"[Lyzron Assist] Logger failed: {e}")
        else:
            try:
                self.logger.log(command, status="ok", result=(result or "")[:2000], error=None, duration=duration)
            except Exception as e:
                print(f"[Lyzron Assist] Logger failed: {e}")

    # ---------- Exploit / Result analysis ----------
    def analyze_exploit_result(self, text: str) -> Dict[str, Any]:
        """
        Heuristic analysis of exploit/module output.
        Returns structured dict:
        {
          target, vulnerability, evidence[], exploit_steps[], impact, severity(0-10), confidence(0-1), keywords[], summary
        }
        """
        if not text:
            return {
                "target": None,
                "vulnerability": None,
                "evidence": [],
                "exploit_steps": [],
                "impact": None,
                "severity": 0,
                "confidence": 0.0,
                "keywords": [],
                "summary": ""
            }

        summary = _safe(summarize, text, max_sentences=3, fallback=text[:500])
        # Simple heuristics (regex-lite) without heavy deps to keep Android compatibility
        import re
        ip_re = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        url_re = re.compile(r'https?://[^\s,;]+')
        cve_re = re.compile(r'\bCVE-\d{4}-\d+\b', re.IGNORECASE)
        evidence_kws = ["error", "trace", "stack", "segfault", "panic", "dump", "output", "sql error", "unauthorized", "denied"]
        exploit_kws = ["exploit", "payload", "poc", "proof of concept", "use", "command", "exec", "shell", "reverse", "bind"]
        impact_kws = ["root", "rce", "remote code", "read", "write", "exfiltrate", "confidential", "privilege", "dos", "crash"]

        lines = [l.strip() for l in re.split(r'[\r\n]+', text) if l.strip()]
        words = re.findall(r"[A-Za-z0-9\-\_]{2,}", text)
        # keywords simplest: frequent words excluding very common tokens
        freq = {}
        for w in words:
            lw = w.lower()
            if len(lw) <= 2:
                continue
            freq[lw] = freq.get(lw, 0) + 1
        keywords = sorted(freq.keys(), key=lambda k: freq[k], reverse=True)[:8]

        target = None
        vuln = None
        evidence = []
        exploit_steps = []
        impact = None
        hits = {"evidence": 0, "exploit": 0, "impact": 0, "cve": 0}

        for ln in lines:
            lnl = ln.lower()
            if not target:
                ipm = ip_re.search(ln)
                urlm = url_re.search(ln)
                if ipm:
                    target = ipm.group(0)
                elif urlm:
                    target = urlm.group(0)
            if not vuln:
                cvem = cve_re.search(ln)
                if cvem:
                    vuln = cvem.group(0)
                    hits["cve"] += 1
            # classify line as evidence / exploit step / impact candidate
            if any(k in lnl for k in evidence_kws):
                evidence.append(ln)
                hits["evidence"] += 1
            if any(k in lnl for k in exploit_kws):
                exploit_steps.append(ln)
                hits["exploit"] += 1
            if any(k in lnl for k in impact_kws):
                impact = impact or ln
                hits["impact"] += 1

        # severity heuristic (0-10): base on hits and presence of root/rce/cve
        severity = 0.0
        severity += min(4.0, hits["exploit"] * 0.8)
        severity += min(3.0, hits["impact"] * 0.6)
        if hits["cve"]:
            severity += 2.0
        # boost if keywords include 'root' or 'rce'
        if any(k in ["root", "rce", "remote", "privilege"] for k in keywords[:6]):
            severity += 1.0
        severity = max(0.0, min(10.0, round(severity, 2)))

        # confidence heuristic
        confidence = 0.1
        confidence += 0.25 if evidence else 0.0
        confidence += 0.25 if exploit_steps else 0.0
        confidence += 0.25 if vuln else 0.0
        confidence = min(1.0, round(confidence, 2))

        return {
            "target": target,
            "vulnerability": vuln,
            "evidence": evidence,
            "exploit_steps": exploit_steps,
            "impact": impact,
            "severity": severity,
            "confidence": confidence,
            "keywords": keywords,
            "summary": summary
        }

    # ---------- Automatic recommendations ----------
    def recommendations_from_analysis(self, analysis: Dict[str, Any]) -> List[str]:
        """
        Create prioritized, actionable recommendations from analysis dict.
        Returns list of recommendation strings (ordered).
        """
        recs: List[str] = []
        vuln = analysis.get("vulnerability")
        sev = analysis.get("severity", 0)
        confidence = analysis.get("confidence", 0)
        target = analysis.get("target")

        # If CVE present, first action: patch vendor CVE
        if vuln:
            recs.append(f"Check vendor advisory and apply vendor patch for {vuln} if available.")
        # If high severity
        if sev >= 8:
            recs.append("Immediate containment: isolate the affected host from network and revoke exposed credentials.")
        elif sev >= 5:
            recs.append("Quick mitigation: apply temporary workarounds (WAF rules, firewall blocks) and schedule urgent patching.")
        else:
            recs.append("Investigate logs and monitor the host; schedule remediation according to SLA.")

        # Generic recommendations based on exploit steps/evidence
        if analysis.get("exploit_steps"):
            recs.append("Review input validation and parameterized queries or safe parsing for exposed endpoints.")
        if analysis.get("evidence"):
            recs.append("Collect and preserve evidence (logs, memory dump, screenshots) for post-incident analysis.")
        # Target-specific tip
        if target:
            recs.append(f"Run a targeted vulnerability scan against {target} to discover related issues.")
        # Always recommend least privilege and monitoring
        recs.append("Apply principle of least privilege, rotate credentials, and enable EDR/IDS monitoring for suspicious activity.")

        # De-duplicate preserving order
        seen = set()
        final = []
        for r in recs:
            if r not in seen:
                final.append(r)
                seen.add(r)
        return final

    # ---------- Module / session report generation ----------
    def generate_module_report(self, module_meta: Dict[str, Any], run_output: str,
                               start_time: float, end_time: float, status: str = "completed",
                               prefer_pdf: bool = True) -> Dict[str, Any]:
        """
        Build a comprehensive report (dictionary), store via ReportManager, and return metadata.
        module_meta should contain keys like: name, author, target, options
        """
        duration = end_time - start_time if end_time and start_time else None
        analysis = self.analyze_exploit_result(run_output)
        recommendations = self.recommendations_from_analysis(analysis)

        report = {
            "framework": "Lyzron",
            "format_version": "1.0",
            "module": {
                "name": module_meta.get("name"),
                "author": module_meta.get("author"),
                "path": module_meta.get("path")
            },
            "target": analysis.get("target") or module_meta.get("target") or module_meta.get("options", {}).get("RHOST"),
            "options": module_meta.get("options", {}),
            "status": status,
            "start_time": start_time,
            "end_time": end_time,
            "duration": duration,
            "analysis": analysis,
            "recommendations": recommendations,
            "raw_output_excerpt": (run_output or "")[:8000],
        }

        # Make a human-friendly summary block
        human_summary_lines = []
        human_summary_lines.append(f"Module: {report['module'].get('name')}")
        if report["target"]:
            human_summary_lines.append(f"Target: {report['target']}")
        human_summary_lines.append(f"Status: {status}")
        human_summary_lines.append(f"Severity: {analysis.get('severity')} / 10 (confidence: {analysis.get('confidence')})")
        human_summary_lines.append("Summary: " + analysis.get("summary", "")[:400])
        human_summary_lines.append("Top recommendations: " + "; ".join(recommendations[:3]))
        report["human_readable_summary"] = "\n".join(human_summary_lines)

        # Persist JSON via ReportManager
        try:
            title = f"{module_meta.get('name') or 'module'}_{int(time.time())}"
            json_payload = json.dumps(report, indent=2)
            # ReportManager.generate should accept prefer_pdf; pass JSON content
            path = self.reporter.generate(title, json_payload, prefer_pdf=prefer_pdf)
            report["report_path"] = path
            print(f"[Lyzron Assist] Report saved: {path}")
        except Exception as e:
            print(f"[Lyzron Assist] Failed to save report: {e}")
            report["report_path"] = None

        return report

    # ---------- Convenience wrapper for CLI/module usage ----------
    def generate_and_print_module_report(self, module_meta: Dict[str, Any],
                                         run_output: str, start_time: float, end_time: float,
                                         status: str = "completed", prefer_pdf: bool = True) -> None:
        """
        Builds report, prints the human summary and top recommendations.
        """
        report = self.generate_module_report(module_meta, run_output, start_time, end_time, status, prefer_pdf)
        print("\n--- Module Execution Summary ---")
        print(report.get("human_readable_summary", "No summary"))
        print("\nRecommendations:")
        for i, r in enumerate(report.get("recommendations", [])[:10], 1):
            print(f"{i}. {r}")
        print(f"\nReport path: {report.get('report_path')}")

    # ---------- CLI integration ----------
    def handle_ai_command(self, help_input: str) -> None:
        """
        Extended CLI commands:
        - ai summarize <num_sentences> <text>
        - ai report <title> key=val;key2=val
        - ai report-module <module_name> key=val;...   -> builds module_meta from keys and last run output (passed via keys or logs)
        """
        parts = help_input.strip().split(None, 2)
        if len(parts) < 2:
            print("Usage: ai summarize <num_sentences> <text> OR ai report-module <module> key=val;...")
            return

        sub = parts[1].lower()

        if sub.startswith("summ"):
            # summarize branch (same behavior)
            cnt = 3
            text = ""
            if len(parts) == 3 and parts[2].strip():
                rest = parts[2].strip()
                first, *rest_tail = rest.split(None, 1)
                if first.isdigit():
                    cnt = int(first); text = rest_tail[0] if rest_tail else ""
                else:
                    text = rest
            if not text:
                print("Error: No text provided to summarize.")
                return
            print(self.summarize_text(text, max_sentences=cnt))

        elif sub == "report-module":
            # Build module_meta from payload; require run_output key or fetch from logger
            if len(parts) < 3:
                print("Usage: ai report-module <module_name> key=val;key2=val (required: run_output=<text> OR fetch via logger)")
                return
            payload = parts[2].strip()
            if " " in payload:
                module_name, kv = payload.split(" ", 1)
            else:
                module_name = payload
                kv = ""
            kv_pairs = {}
            for pair in kv.split(";"):
                pair = pair.strip()
                if not pair:
                    continue
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    kv_pairs[k.strip()] = v.strip()
                else:
                    kv_pairs[pair] = ""
            module_meta = {
                "name": module_name,
                "author": kv_pairs.get("author"),
                "path": kv_pairs.get("path"),
                "options": json.loads(kv_pairs.get("options")) if kv_pairs.get("options") else {},
                "target": kv_pairs.get("target")
            }
            # run_output may be passed inline (base64 or raw). Prefer run_output key.
            run_output = kv_pairs.get("run_output")
            if not run_output:
                # try to fetch last log for module via ActionLogger if supported
                try:
                    run_output = self.logger.fetch_latest_output_for_module(module_name)
                except Exception:
                    run_output = ""
            start_ts = float(kv_pairs.get("start_ts")) if kv_pairs.get("start_ts") else _now_ts()
            end_ts = float(kv_pairs.get("end_ts")) if kv_pairs.get("end_ts") else _now_ts()
            status = kv_pairs.get("status", "completed")
            # generate & print
            self.generate_and_print_module_report(module_meta, run_output, start_ts, end_ts, status, prefer_pdf=True)

        elif sub.startswith("report"):
            # existing report behavior
            if len(parts) < 3:
                print("Usage: ai report <title> key1=val;key2=val")
                return
            payload = parts[2].strip()
            if " " in payload:
                title, kv = payload.split(" ", 1)
            else:
                title = payload
                kv = ""
            data = {}
            for pair in kv.split(";"):
                pair = pair.strip()
                if not pair:
                    continue
                if "=" in pair:
                    k, v = pair.split("=", 1); data[k.strip()] = v.strip()
                else:
                    data[pair] = ""
            self.export_session_report(title, data)
        else:
            print("Unknown ai sub-command. Available: (summarize | report | report-module)")

    # ---------- Simple wrapper to keep backward compatibility ----------
    def summarize_text(self, text: str, max_sentences: int = 3) -> str:
        return _safe(summarize, text, max_sentences=max_sentences, fallback="")

# End of file