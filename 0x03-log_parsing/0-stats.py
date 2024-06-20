#!/usr/bin/python3
'''A script for parsing HTTP request logs with status codes'''

import sys
import signal

total_size = 0
status_codes_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) != 10:
        continue
    ip, dash, date, method, url, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[9]
    
    try:
        total_size += int(file_size)
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
    except ValueError:
        continue
    
    line_count += 1
    if line_count % 10 == 0:
        print_stats()
