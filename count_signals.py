import re
import os
import pathlib
import csv

targets_filename = 'pypi_popular.txt'

tool_dirs = [os.path.join('data', 'ossgadget'), os.path.join('data', 'typomind')]


for tool_dir in tool_dirs:
    print('-' * 20)
    with open(os.path.join(tool_dir, 'confusers.csv'), 'r') as read_file:
        signal_count = {}

        csvreader = csv.reader(read_file)

        # skip header
        header = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            signals = [ signal.split(':')[0] for signal in row[2].split(';') ]

            for signal in signals:
                if signal not in signal_count:
                    signal_count[signal] = 0

                signal_count[signal] += 1

        for signal, count in signal_count.items():
            print(f'{signal}\t{count}')