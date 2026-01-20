# Security Log Analyzer

Security Log Analyzer is a lightweight Python tool designed to analyze authentication log files and identify potential security issues.

This tool helps summarize IP activity, detect repeated failed login attempts, and flag suspicious behavior based on configurable thresholds.

## Key Objectives
- Practice reading and parsing log files
- Understand basic security event patterns
- Build a defensive and ethical security-related tool
- Showcase clean code structure and documentation

## Features
- Detect failed login attempts
- Summarize IP activity
- Highlight suspicious IP addresses

## Intended Use
- Learning and educational purposes
- Basic log review for system administrators
- Entry-level security or system administration assessment

## Usage
python analyzer.py --file sample.log --limit 2 --export suspicious_ips.csv
