import re
import argparse
import csv
from collections import Counter

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


def export_csv(data, output_file):
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Failed Attempts"])
        for ip, count in data.items():
            writer.writerow([ip, count])


def main():
    parser = argparse.ArgumentParser(description="Security Log Analyzer")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--limit", type=int, default=3, help="Failed login threshold")
    parser.add_argument("--export", help="Export suspicious IPs to CSV file")
    args = parser.parse_args()

    all_ips, failed_ips = analyze_log(args.file)

    print("\n=== Security Log Analyzer ===\n")

    print("[+] IP Activity Summary:")
    ip_counter = Counter(all_ips)
    for ip, count in ip_counter.items():
        print(f" - {ip}: {count} activities")

    print("\n[!] Failed Login Attempts:")
    failed_counter = Counter(failed_ips)
    suspicious_ips = {}

    for ip, count in failed_counter.items():
        print(f" - {ip}: {count} failed attempts")
        if count >= args.limit:
            print("   ⚠️ Suspicious activity detected")
            suspicious_ips[ip] = count

    if args.export and suspicious_ips:
        export_csv(suspicious_ips, args.export)
        print(f"\n[+] Suspicious IPs exported to {args.export}")

if __name__ == "__main__":
    main()
