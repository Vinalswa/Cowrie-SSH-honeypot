# Cowrie SSH Honeypot / Python Port Scanner

**Author:** Vinayaspoorthi Swamy – MSc Cybersecurity, University of Aberdeen  
**Date:** 09-Nov-2025

## Overview
This project demonstrates network security skills using:
- **Cowrie SSH Honeypot** (instructions included) to capture SSH brute-force attempts and attacker behavior  
- **Python Port Scanner** (easy fallback) to scan a target IP for open ports

It is intended as a portfolio piece for internship applications.

## Files
- `port_scanner.py` — simple Python script to scan common ports
- `README.md` — this file
- `screenshots/` — folder containing sample outputs and logs
- `report.pdf` — optional 1-page summary (if added)

## How to run (Python port scanner)
1. Ensure Python 3 is installed.
2. Open a terminal / command prompt in this folder.
3. Run:
```
python port_scanner.py
```
4. Enter `127.0.0.1` (localhost) or a safe test IP.

## Example output
```
Scanning target: 127.0.0.1
Port 22 is OPEN
Port 80 is OPEN
Scan complete ✅
```

## Skills Demonstrated
- Python scripting and automation  
- Basic network scanning and enumeration  
- Log analysis (if using Cowrie)  
- Linux environment setup and security tooling

## Notes
- Run only on systems/networks you own or have permission to test.
