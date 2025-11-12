# lib/intai/action_logger.py
# Kayıt: her komut, sonucu, hata durumunu ve süreyi JSON dosyasına yazar.
import json
import os
import time
from datetime import datetime
from typing import Optional

class ActionLogger:
    def __init__(self, logfile="~/.intframework_actions.json", max_entry_size=2000):
        self.logfile = os.path.expanduser(logfile)
        self.max_entry_size = max_entry_size
        self._ensure_file()

    def _ensure_file(self):
        folder = os.path.dirname(self.logfile)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        if not os.path.exists(self.logfile):
            with open(self.logfile, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2)

    def _read(self):
        try:
            with open(self.logfile, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _write(self, data):
        with open(self.logfile, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def log(self, command: str, status: str = "ok", result: Optional[str] = None, error: Optional[str] = None, duration: Optional[float] = None):
        logs = self._read()
        entry = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "command": command,
            "status": status,
            "duration_seconds": round(duration, 3) if isinstance(duration, (int, float)) else None,
            "result": (result or "")[: self.max_entry_size],
            "error": (error or "")[: self.max_entry_size]
        }
        logs.append(entry)
        # rotate if file too large (very basit)
        if len(logs) > 5000:
            logs = logs[-4000:]
        self._write(logs)

    def tail(self, n=10):
        logs = self._read()
        for entry in logs[-n:]:
            ts = entry.get("timestamp")
            cmd = entry.get("command")
            status = entry.get("status")
            dur = entry.get("duration_seconds")
            print(f"[{ts}] {cmd} -> {status} (took: {dur}s)")

    def export_json(self, outpath):
        data = self._read()
        with open(outpath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return outpath