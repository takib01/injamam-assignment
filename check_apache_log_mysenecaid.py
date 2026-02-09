#!/usr/bin/env python3
# OPS435 Assignment 1
# check_apache_log_mysenecaid.py
# Author: Injamammul Haque 

import sys
import time
def display_title(title):
    """Prints a title and a dynamic line of '=' below it."""
    print(title)
    print("=" * len(title))
   
def load_logs(list_of_filenames):
    """Prints each filename that would be opened and read."""
    for filename in list_of_filenames:
        print(f"Loading {filename}")

def total_200_requests():
    """Stub for total requests (Code 200)."""
    print("Not implemented yet")

def requests_from_seneca():
    """Stub for requests from Seneca (IPs starting with 142.204)."""
    print("Not implemented yet")

def requests_for_ops435_lab():
    """Stub for requests for OPS435_Lab."""
    print("Not implemented yet")

def total_404_requests():
    """Stub for total 'Not Found' requests (Code 404)."""
    print("Not implemented yet")

def hidebots_404_requests():
    """Stub for 404 requests containing 'hidebots' in the URL."""
    print("Not implemented yet")

def print_404_ips():
    """Stub for printing all IP addresses that caused a 404 response."""
    print("Not implemented yet")

def successful_requests_menu():
    """Displays the Successful Requests Menu and handles user input."""
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
    """Displays the Failed Requests Menu and handles user input."""
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
    if len(sys.argv) < 2: #["check_apache_log_mysenecaid.py"]
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
    for i in range(10):
        print(f"Loading {sys.argv[1]} {(i)}")
       
    load_logs(args)

    if is_default:
        total_200_requests()
    else:
        main_menu()
