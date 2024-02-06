#!/usr/bin/python3

import sys


def print_metrics(total_size, status_codes):
    """
    Prints the metrics
    based on the given total size and status codes dictionary.
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        if count:
            print("{}: {}".format(code, count))


def parse_line(line):
    """
    Parses a line and returns the status code and file size.
    """
    parts = line.split()
    return int(parts[-2]), int(parts[-1])


def main():
    """
    Main function to compute metrics from stdin.
    """
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0,
                    '405': 0, '500': 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            total_size += parse_line(line)[1]
            status_code = parse_line(line)[0]
            if str(status_code) in status_codes:
                status_codes[str(status_code)] += 1

            if count % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
