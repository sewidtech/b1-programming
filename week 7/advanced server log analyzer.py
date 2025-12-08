import logging
import re

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("analysis_audit.log"),
        logging.StreamHandler()
    ]
)

log_pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<date>.*?)\] '
    r'"(?P<request>.*?)" (?P<status>\d{3}) (?P<size>\d+|-)'
)

new_log = input("Enter new log entry: ")
new_log = new_log.replace("\n", "\\n").replace("\r", "\\r")

with open("analyzer.txt", "a") as f:
    f.write(new_log + "\n")

match = log_pattern.search(new_log)
if match:
    status = match.group("status")
    if status == "404":
        with open("error_logs.txt", "a") as error_file:
            error_file.write(new_log + "\n")
            error_file.write("404 Error detected in log entry.\n")
    elif status == "403":
        with open("forbidden_access.txt", "a") as forbidden_file:
            forbidden_file.write(new_log + "\n")
            forbidden_file.write("403 Forbidden access detected in log entry.\n")

class LogAnalyzer:
    log_pattern = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<date>.*?)\] '
        r'"(?P<request>.*?)" (?P<status>\d{3}) (?P<size>\d+|-)'
    )

    def __init__(self, logfile):
        self.logfile = logfile
        self.total_requests = 0
        self.unique_ips = set()
        self.http_methods = {}
        self.urls = {}
        self.status_codes = {}
        self.errors = []

    def analyze(self):
        with open(self.logfile, "r") as f:
            for line in f:
                line = line.strip()
                match = self.log_pattern.search(line)
                if match:
                    self.total_requests += 1
                    ip = match.group("ip")
                    request = match.group("request")
                    status = match.group("status")
                    log_time = match.group("date")
                    self.unique_ips.add(ip)
                    try:
                        method, url, protocol = request.split()
                    except ValueError:
                        method = "UNKNOWN"
                        url = request
                    self.http_methods[method] = self.http_methods.get(method, 0) + 1
                    self.urls[url] = self.urls.get(url, 0) + 1
                    self.status_codes[status] = self.status_codes.get(status, 0) + 1
                    if status == "404":
                        with open("error_logs.txt", "a") as error_file:
                            error_file.write(line + "\n")
                            error_file.write("404 Error detected in log entry.\n")
                    elif status == "403":
                        with open("forbidden_access.txt", "a") as forbidden_file:
                            forbidden_file.write(line + "\n")
                            forbidden_file.write("403 Forbidden access detected in log entry.\n")
                else:
                    self.errors.append(line)
                    logging.warning(f"Unrecognized log format: {line}")

    def report(self):
        print("\n----- ANALYSIS SUMMARY -----")
        print(f"Total Requests: {self.total_requests}")
        print(f"Unique IPs: {len(self.unique_ips)}")
        print(f"HTTP Methods: {self.http_methods}")
        print(f"Most Requested URLs: {dict(sorted(self.urls.items(), key=lambda x: x[1], reverse=True)[:5])}")
        print(f"Status Codes: {self.status_codes}")
        if self.errors:
            print(f"Unrecognized lines: {len(self.errors)}")
        print("\nDetails logged to analysis_audit.log")
        print("404 errors logged to error_logs.txt")
        print("403 errors logged to forbidden_access.txt")

if __name__ == "__main__":
    analyzer = LogAnalyzer("analyzer.txt")
    analyzer.analyze()
    analyzer.report()
