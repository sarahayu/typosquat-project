"""

"""

import argparse
import logging
from core.detectors import classify_typosquat


def make_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description = 'displays typo-squatting categories exhibited by adversarial package WRT base package')
    parser.add_argument('base_package', help='name of original package')
    parser.add_argument('adv_package', help='name of potentially malicious package')
    parser.add_argument('--outfile_path', '-of', help='specify that file is path to output')
    return parser


def main():
    argparser = make_argparser()
    args = argparser.parse_args()
    base_pkg_spec: str = args.base_package
    adv_pkg_spec: str = args.adv_package
    outfile_path: str = args.outfile_path

    logging.basicConfig(filename="logs/run.log", filemode='a', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    logging.info("Typomind Detector Starting ....")

    with open(outfile_path, 'a') as file:
        with open(base_pkg_spec, 'r') as f:
            base_pkgs = [pkg.strip() for pkg in f]

        with open(adv_pkg_spec, 'r') as f:
            count = 0

            for adv_pkg_line in f:
                adv_pkg = adv_pkg_line.strip()
                
                for base_pkg in base_pkgs:
                    try:
                        classifications = [f'{name}: {c}' for (_, name), c in classify_typosquat(base_pkg, adv_pkg).items()]
                        if classifications:
                            out_str = f'{base_pkg},{adv_pkg};{','.join(classifications)}';

                            file.write(out_str)
                            file.write('\n')

                            print(out_str)
                    except Exception as e:
                        logging.error(f"Unhandled exception for base: {base_pkg}  and adv: {adv_pkg}. Error{e}, ")
                        continue
                    count += 1

                    if count % 100000 == 0:
                        logging.info(f"Packages checked: {count}")

    print("Total product: ", count)


if __name__ == '__main__':
    main()