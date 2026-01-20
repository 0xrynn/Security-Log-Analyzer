import re
from collections import Counter

LOG_FILE = "sample.log"
FAILED_LIMIT = 3

def analyze_log(file_path):
    failed_ips = []
    all_ips = []

    with open(file_path, "r") as log:
        for line in log:
            ip_match = re.search(r'ip=([\d\.]+)', line)
            if ip_match:
                ip = ip_match.group(1)
                all_ips.append(ip)

                if "Login failed" in line:
                    failed_ips.append(ip)

    return all_ips, failed_ips


def main():
    all_ips, failed_ips = analyze_log(LOG_FILE)

    print("=== Security Log Analyzer ===\n")

    print("[+] Total IP activity:")
    for ip, count in Counter(all_ips).items():
        print(f" - {ip}: {count} times")

    print("\n[!] Failed login attempts:")
    for ip, count in Counter(failed_ips).items():
        print(f" - {ip}: {count} failed attempts")

        if count >= FAILED_LIMIT:
            print(f"   ⚠️  Suspicious activity detected from {ip}")

if __name__ == "__main__":
    main()