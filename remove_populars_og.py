import re
import os
import pathlib
import csv

targets_filename = 'pypi_popular.txt'
csv_output_dir = os.path.join('output')
remove_populars_output_dir = os.path.join('data', 'ossgadget')

all_packages = [pathlib.Path(f).stem for f in os.listdir(csv_output_dir) if os.path.isfile(os.path.join(csv_output_dir, f))]

popular_pkgs = []

with open(targets_filename, 'r') as targets_file:
    for confuser in targets_file:
        popular_pkgs.append(confuser.strip('\n').lower())

with open(os.path.join(csv_output_dir, 'targets.csv'), 'r') as read_file,   \
    open(os.path.join(remove_populars_output_dir, 'targets_remove_populars.csv'), 'w') as write_file:

    csvreader = csv.reader(read_file)

    # skip header
    header = next(csvreader)

    write_file.write(','.join(header))
    write_file.write('\n')

    # extracting each data row one by one
    for row in csvreader:
        target = row[0]
        confusers = row[1].split(';')
        confusers_without_populars = [c for c in confusers if not c.lower() in popular_pkgs]

        write_file.write(f'{target},')
        write_file.write(';'.join(confusers_without_populars))
        write_file.write('\n')

with open(os.path.join(csv_output_dir, 'confusers.csv'), 'r') as read_file,   \
    open(os.path.join(remove_populars_output_dir, 'confusers_remove_populars.csv'), 'w') as write_file:

    csvreader = csv.reader(read_file)

    # skip header
    header = next(csvreader)

    write_file.write(','.join(header))
    write_file.write('\n')

    # extracting each data row one by one
    for row in csvreader:
        confuser = row[0]
        if confuser.lower() in popular_pkgs:
            continue

        write_file.write(','.join(row))
        write_file.write('\n')