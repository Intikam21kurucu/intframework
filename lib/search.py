import json
import pandas as pd
import re
from rich.console import Console
from rich.table import Table

DB_PATH = "db/modules.json"

class ModuleSearch:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.console = Console()
        self.modules_df = self.load_modules()

    def load_modules(self):
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                modules = json.load(f)
            df = pd.DataFrame.from_dict(modules, orient="index").fillna("Unknown")
            return df
        except (FileNotFoundError, json.JSONDecodeError):
            self.console.print("[red][!] Error loading database.[/red]")
            return pd.DataFrame()

    def wildcard_to_regex(self, pattern):
        pattern = re.escape(pattern)
        pattern = pattern.replace(r'\*', '.*').replace(r'\?', '.')
        return f'^{pattern}$'

    def search(self, query="", filters={}, limit=10):
        if self.modules_df.empty:
            return pd.DataFrame()

        df = self.modules_df.copy()

        if query:
            if "*" not in query and "?" not in query:
                query += "*"  # Otomatik olarak sonuna joker karakter ekle
            regex = self.wildcard_to_regex(query)
            df = df[
                df["name"].str.contains(regex, case=False, na=False, regex=True) |
                df["description"].str.contains(regex, case=False, na=False, regex=True) |
                df["title"].str.contains(regex, case=False, na=False, regex=True)
            ]

        for key, value in filters.items():
            if key in df.columns:
                regex = self.wildcard_to_regex(value)
                df = df[df[key].astype(str).str.contains(regex, case=False, na=False, regex=True)]

        return df.head(limit)

    def display_results(self, results):
        if results.empty:
            self.console.print("\n[red][-] No results found.[/red]\n")
            return

        table = Table(show_header=True, show_lines=False, pad_edge=False)
        table.add_column("Name", style="cyan", width=15, no_wrap=True)
        table.add_column("Path", style="bright_blue", width=45, no_wrap=True)
        table.add_column("Type", style="magenta", width=10, no_wrap=True)
        table.add_column("CVE", style="red", width=10, no_wrap=True)
        table.add_column("Google Dork", style="blue", width=12, no_wrap=True)
        table.add_column("Author", style="yellow", width=12, no_wrap=True)
        table.add_column("Size (KB)", style="white", width=8, no_wrap=True)
        table.add_column("Last Modified", style="green", width=16, no_wrap=True)

        for _, module in results.iterrows():
            table.add_row(
                module["name"][:15],
                module["path"][:45],
                module["type"][:10],
                module["cve"][:10],
                module["google_dork"][:12],
                module["author"][:12],
                str(module["size_kb"]),
                module["last_modified"][:16]
            )

        self.console.print(table)

    def process_command(self, command):
        parts = command.split()
        if len(parts) < 2:
            self.console.print("[red]Usage: search <query> [filters][/red]")
            return

        query_parts = []
        filters = {}
        limit = 10

        for part in parts[1:]:
            if ":" in part:
                key, value = part.split(":", 1)
                if key.lower() == "limit":
                    try:
                        limit = int(value)
                    except ValueError:
                        self.console.print("[red][!] Limit değeri sayısal olmalı.[/red]")
                        return
                else:
                    filters[key.lower()] = value
            else:
                query_parts.append(part)

        query = " ".join(query_parts)

        results = self.search(query, filters, limit)
        self.display_results(results)