import re
import os
import pathlib

oss_output_dir = os.path.join('output', 'typomind')
minified_output_dir = os.path.join('output')

all_packages = [pathlib.Path(f).stem for f in os.listdir(oss_output_dir) if os.path.isfile(os.path.join(oss_output_dir, f))]

with open(os.path.join(minified_output_dir, 'targets.csv'), 'w') as targets_file,   \
    open(os.path.join(minified_output_dir, 'confusers.csv'), 'w') as confusers_file:
    targets_file.write('target_pkg,confuser_pkgs\n')
    confusers_file.write('confuser_pkg,target_pkg,signals\n')

    
    with open(os.path.join(oss_output_dir, f'output.txt'), 'r') as log_file:
        target_to_confusers = {}

        i = 0

        for log_line in log_file:
            print(f'Line {i}')
            tokens = log_line.strip().split(';')
            pkgs = tokens[0]
            signals = tokens[1]
            signals = ';'.join(signals.split(','))

            tokens = pkgs.split(',')
            target = tokens[0]
            confuser = tokens[1]

            if not target in target_to_confusers:
                target_to_confusers[target] = []

            target_to_confusers[target].append(confuser)

            confusers_file.write(f'{confuser},{target},{signals}\n')

            i += 1

        for target in target_to_confusers:
            confusers = target_to_confusers[target]

            confusers = ';'.join(confusers)
            
            targets_file.write(f'{target},{confusers}\n')