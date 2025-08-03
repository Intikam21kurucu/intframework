import requests
import re

class WPDatabaseScanner:
    def __init__(self, url):
        """WordPress veritabanı tarayıcı başlatır"""
        self.url = url.rstrip('/')
        self.db_info = {}

    def check_wp_config(self):
        """wp-config.php dosyasının erişilebilir olup olmadığını kontrol eder"""
        config_url = self.url + "/wp-config.php"
        response = requests.get(config_url)

        if "DB_NAME" in response.text or "MySQL" in response.text:
            self.db_info["wp_config"] = "EXPOSED"
        else:
            self.db_info["wp_config"] = "SECURE"

    def detect_database_type(self):
        """Hata mesajlarından veritabanı türünü belirler"""
        test_url = self.url + "/?id=1'"
        response = requests.get(test_url)

        if "MySQL" in response.text:
            self.db_info["database_type"] = "MySQL"
        elif "MariaDB" in response.text:
            self.db_info["database_type"] = "MariaDB"
        elif "PostgreSQL" in response.text:
            self.db_info["database_type"] = "PostgreSQL"
        else:
            self.db_info["database_type"] = "UNKNOWN"

    def check_for_sql_vulnerabilities(self):
        """Temel SQL Injection açıklarını test eder"""
        sql_payloads = ["'", "1' OR '1'='1", "' UNION SELECT 1,2,3 -- "]
        vulnerable = False

        for payload in sql_payloads:
            test_url = self.url + f"/?id={payload}"
            response = requests.get(test_url)

            if "SQL syntax" in response.text or "Warning: mysql_fetch" in response.text:
                vulnerable = True
                break

        self.db_info["sql_injection"] = "VULNERABLE" if vulnerable else "SECURE"

    def run(self):
        """Tüm veritabanı testlerini çalıştırır ve sonuçları scanner'a gönderir"""
        self.check_wp_config()
        self.detect_database_type()
        self.check_for_sql_vulnerabilities()

        return self.db_info  # Scanner’a gönderilecek sonuçlar