# lib/intai/report_manager.py
# Hem PDF (reportlab yüklüyse) hem de HTML fallback ile rapor üretir.
import os
from datetime import datetime
import html
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False

class ReportManager:
    def __init__(self, outdir="~/.intframework_reports"):
        self.outdir = os.path.expanduser(outdir)
        os.makedirs(self.outdir, exist_ok=True)

    def _safe_filename(self, title):
        safe = "".join([c if c.isalnum() or c in "-_ " else "_" for c in title]).strip()
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{safe}_{ts}"

    def generate_pdf(self, title, content, filename=None):
        if not REPORTLAB_AVAILABLE:
            raise RuntimeError("reportlab not available")
        filename = filename or self._safe_filename(title) + ".pdf"
        outpath = os.path.join(self.outdir, filename)
        c = canvas.Canvas(outpath, pagesize=A4)
        width, height = A4
        margin = 50
        y = height - margin
        c.setFont("Helvetica-Bold", 16)
        c.drawString(margin, y, title)
        y -= 30
        c.setFont("Helvetica", 10)
        for line in content.splitlines():
            # wrap long lines simply
            while len(line) > 120:
                c.drawString(margin, y, line[:120])
                y -= 14
                line = line[120:]
                if y < margin:
                    c.showPage()
                    y = height - margin
            c.drawString(margin, y, line)
            y -= 14
            if y < margin:
                c.showPage()
                y = height - margin
        c.save()
        return outpath

    def generate_html(self, title, content, filename=None):
        filename = filename or self._safe_filename(title) + ".html"
        outpath = os.path.join(self.outdir, filename)
        html_content = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/><title>{html.escape(title)}</title>
<style>body{{font-family:monospace;white-space:pre-wrap;background:#0f0f0f;color:#e6e6e6;padding:18px}}</style></head>
<body><h2>{html.escape(title)}</h2><pre>{html.escape(content)}</pre></body></html>"""
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(html_content)
        return outpath

    def generate(self, title, content, prefer_pdf=True):
        # tercih edilen çıktı = PDF, değilse HTML
        if prefer_pdf and REPORTLAB_AVAILABLE:
            try:
                return self.generate_pdf(title, content)
            except Exception:
                return self.generate_html(title, content)
        else:
            return self.generate_html(title, content)