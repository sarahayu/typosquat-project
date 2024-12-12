import re
import os
import pathlib
import csv

targets_filename = 'pypi_popular.txt'

tool_dirs = [os.path.join('data', 'ossgadget'), os.path.join('data', 'typomind')]

found_pkgs = set()

with open(os.path.join('data', 'ossgadget', 'confusers.csv'), 'r') as read_file:
    csvreader = csv.reader(read_file)

    next(csvreader)

    for row in csvreader:
        confuser = row[0]
        found_pkgs.add(confuser)


with open(os.path.join('data', 'typomind', 'confusers.csv'), 'r') as read_file:
    signal_count = {}
    signal_ov = {}

    csvreader = csv.reader(read_file)

    # skip header
    header = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        confuser = row[0]
        signals = [ signal.split(':')[0] for signal in row[2].split(';') ]

        for signal in signals:
            if signal not in signal_count:
                signal_count[signal] = 0
                signal_ov[signal] = 0

            signal_count[signal] += 1

            if confuser in found_pkgs:
                signal_ov[signal] += 1

    for signal, count in signal_count.items():
        print(f'{signal}\t{count}\t{signal_ov[signal]}')