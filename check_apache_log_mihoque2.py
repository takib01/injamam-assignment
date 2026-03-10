#!/usr/bin/env python3
# OPS435 Assignment 1
# check_apache_log_mihoque2.py
# Author: Injamammul Haque

import sys
import re

# Global list to store every line from all loaded log files.
all_log_lines = []


def display_title(title):
    """Prints a title with a row of '=' characters underneath it."""
    print(title)
    print("=" * len(title))


def load_logs(list_of_filenames):
    """
    Opens each file in list_of_filenames, reads all lines, and stores them
    in the global all_log_lines list so every parsing function can use them.
    """
    global all_log_lines
    for filename in list_of_filenames:
        print(f"Loading {filename}...")
        try:
            with open(filename, 'r') as f:
                all_log_lines.extend(f.readlines())
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except PermissionError:
            print(f"Error: Permission denied reading '{filename}'.")
    print(f"Total lines loaded: {len(all_log_lines)}")


def total_200_requests():
    """
    Counts and prints the number of log lines where the HTTP response code
    is 200 (successful request).
    """
    global all_log_lines
    count = 0
    for line in all_log_lines:
        match = re.match(r'([\d\.]+) - - \[(.*?)\] "(.*?)" (\d+) ((\d+)|-).*', line)
        if match is not None:
            if match.group(4) == '200':
                count += 1
    print(f"Total requests with Code 200: {count}")


def requests_from_seneca():
    """
    Counts and prints the number of log lines where the client IP address
    starts with '142.204' (Seneca College IP range).
    """
    global all_log_lines
    count = 0
    for line in all_log_lines:
        match = re.match(r'([\d\.]+) - - \[(.*?)\] "(.*?)" (\d+) ((\d+)|-).*', line)
        if match is not None:
            if match.group(1).startswith('142.204'):
                count += 1
    print(f"Total requests from Seneca (142.204.*): {count}")


def requests_for_ops435_lab():
    """
    Counts and prints the number of log lines where the requested URL
    contains the string 'OPS435_Lab'.
    """
    global all_log_lines
    count = 0
    for line in all_log_lines:
        match = re.match(r'([\d\.]+) - - \[(.*?)\] "(.*?)" (\d+) ((\d+)|-).*', line)
        if match is not None:
            # re.search() checks anywhere inside the request string, not just the start
            if re.search(r'OPS435_Lab', match.group(3)):
                count += 1
    print(f"Total requests for OPS435_Lab: {count}")


def total_404_requests():
    """
    Counts and prints the number of log lines where the HTTP response code
    is 404 (Not Found).
    """
    global all_log_lines
    count = 0
    for line in all_log_lines:
        match = re.match(r'([\d\.]+) - - \[(.*?)\] "(.*?)" (\d+) ((\d+)|-).*', line)
        if match is not None:
            if match.group(4) == '404':
                count += 1
    print(f'Total "Not Found" requests (Code 404): {count}')


def hidebots_404_requests():
    """
    Counts and prints the number of log lines where the response code is 404
    AND the requested URL contains 'hidebots'.
    """
    global all_log_lines
    count = 0
    for line in all_log_lines:
        match = re.match(r'([\d\.]+) - - \[(.*?)\] "(.*?)" (\d+) ((\d+)|-).*', line)
        if match is not None:
            if match.group(4) == '404':
                if re.search(r'hidebots', match.group(3)):
                    count += 1
    print(f'Total 404 requests containing "hidebots": {count}')


def print_404_ips():
    """
    Collects every unique IP address that received a 404 response and prints
    them. A dictionary is used so duplicate IPs are automatically removed.
    """
    global all_log_lines
    ip_dict = {}
    for line in all_log_lines:
        match = re.match(r'([\d\.]+) - - \[(.*?)\] "(.*?)" (\d+) ((\d+)|-).*', line)
        if match is not None:
            if match.group(4) == '404':
                ip_dict[match.group(1)] = True
    print("IP addresses that caused a 404 response:")
    for ip in ip_dict.keys():
        print(f"  {ip}")


def successful_requests_menu():
    """Displays the Successful Requests sub-menu and handles user input."""
    while True:
        print()
        display_title("Apache Log Analyser - Successful Requests Menu")
        print("1) How many total requests (Code 200)")
        print("2) How many requests from Seneca (IPs starting with 142.204)")
        print("3) How many requests for OPS435_Lab")
        print("q) Return to Main Menu")
        choice = input("What would you like to do? ").lower()

        if choice == '1':
            total_200_requests()
        elif choice == '2':
            requests_from_seneca()
        elif choice == '3':
            requests_for_ops435_lab()
        elif choice == 'q':
            break


def failed_requests_menu():
    """Displays the Failed Requests sub-menu and handles user input."""
    while True:
        print()
        display_title("Apache Log Analyser - Failed Requests Menu")
        print('1) How many total "Not Found" requests (Code 404)')
        print('2) How many 404 requests contained "hidebots" in the URL')
        print("3) Print all IP addresses that caused a 404 response")
        print("q) Return to Main Menu")
        choice = input("What would you like to do? ").lower()

        if choice == '1':
            total_404_requests()
        elif choice == '2':
            hidebots_404_requests()
        elif choice == '3':
            print_404_ips()
        elif choice == 'q':
            break


def main_menu():
    """Displays the Main Menu and handles user input."""
    while True:
        print()
        display_title("Apache Log Analyser - Main Menu")
        print("1) Successful Requests")
        print("2) Failed Requests")
        print("q) Quit")
        choice = input("What would you like to do? ").lower()

        if choice == '1':
            successful_requests_menu()
        elif choice == '2':
            failed_requests_menu()
        elif choice == 'q':
            break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No log files provided.")
        print(f"Usage: {sys.argv[0]} [--default] filename [filename2 ...]")
        sys.exit(1)

    args = sys.argv[1:]
    is_default = False

    if args[0] in ['--default', '-d']:
        is_default = True
        args = args[1:]

    if not args:
        print("Error: No log files provided.")
        sys.exit(1)

    load_logs(args)

    if is_default:
        total_200_requests()
    else:
        main_menu()
