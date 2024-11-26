import csv
import subprocess
import sys

popular_csv = "pypi_popular.csv"
oss_gadget = "/mnt/c/Users/sarah/Documents/grad/ECS235A/OSSGadget/src/oss-find-squats/bin/Debug/net8.0/oss-find-squats.exe"

start = False           # turn this True if we want to start from the beginning
last_pkg = "sox"        # this is to start off processing somewhere midway through because i need to stop script sometimes midway

with open(popular_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # skip header
    next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        pkg_name = row[0]

        if pkg_name == last_pkg:
            start = True
            continue

        if not start:
            continue

        print(f"Starting to process {pkg_name}...")
        
        p = subprocess.run([oss_gadget, '--output-file', f"output/popular/{pkg_name}.txt", '--format', 'text', '--quiet', f"pkg:pypi/{pkg_name}"])
        
        print(f"Finished processing {pkg_name}!")