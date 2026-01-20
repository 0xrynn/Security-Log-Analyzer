# Security Log Analyzer

Security Log Analyzer is a lightweight Python-based command-line tool designed to analyze authentication log files and identify potential security issues.

This tool helps summarize IP activity, detect repeated failed login attempts, and flag suspicious behavior based on configurable thresholds. It also supports exporting suspicious results into CSV format for reporting and further analysis.

The project is intended to demonstrate fundamental skills in log parsing, basic security monitoring, and Python CLI development, which are commonly required for entry-level system administration and security roles.

---

## Features

- Command-line interface (CLI)
- Analyze authentication log files
- Detect repeated failed login attempts
- Summarize IP address activity
- Configurable failed login threshold
- Export suspicious IP addresses to CSV
- Simple, clean, and readable code structure

---

## Use Cases

- Basic security log review
- Entry-level security monitoring
- System administration practice
- Learning log analysis concepts
- Technical assessment or portfolio project

---

## Project Structure

Security-Log-Analyzer/ ├── analyzer.py ├── sample.log └── README.md

---

## Requirements

- Python 3.x  
- No external libraries required (uses Python standard library only)

---

## Usage

### Analyze a log file
```bash
python analyzer.py --file sample.log

Set a custom failed login threshold

python analyzer.py --file sample.log --limit 2

Export suspicious IPs to CSV

python analyzer.py --file sample.log --limit 2 --export suspicious_ips.csv


---

Output Overview

The tool provides:

A summary of IP address activity

The number of failed login attempts per IP

Warnings for suspicious behavior

Optional CSV export for reporting purposes


Example CSV output:

IP Address,Failed Attempts
192.168.1.10,3
10.0.0.5,2


---

Disclaimer

This project is intended for educational and defensive purposes only.
It does not perform any offensive actions, exploitation, or real-world attacks.


---

Author

Created as a learning and portfolio project to demonstrate basic security log analysis and Python scripting skills.
