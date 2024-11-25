import csv
import subprocess
import sys

popular_csv = "pypi_popular.csv"
oss_gadget = "/mnt/c/Users/sarah/Documents/grad/ECS235A/OSSGadget/src/oss-find-squats/bin/Debug/net8.0/oss-find-squats.exe"

# semver

# reading csv file
with open(popular_csv, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        pkg_name = row[0]

        print(f"Starting to process {pkg_name}...")
        
        p = subprocess.run([oss_gadget, '--output-file', f"output/popular/{pkg_name}.txt", '--format', 'text', '--quiet', f"pkg:pypi/{pkg_name}"])
        
        print(f"Finished processing {pkg_name}!")