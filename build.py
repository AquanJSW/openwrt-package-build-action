#!/usr/bin/env python3

import subprocess
from dataclasses import dataclass
import yaml
import argparse

Url = str

parser = argparse.ArgumentParser()
parser.add_argument('ipk_dir', help='Output directory for ipk files')


@dataclass
class Package:
    name: str
    patches: list[Url]


def load_packages():
    db_path = 'build_db.yaml'
    with open(db_path) as fs:
        db = yaml.safe_load(fs)
    return [Package(**pkg) for pkg in db]


def main():
    args = parser.parse_args()
    packages = load_packages()
    for pkg in packages:
        pkg_dir = (
            subprocess.run(
                f'find feeds/ -name {pkg.name} -type d'.split(),
                capture_output=True,
                check=True,
            )
            .stdout.decode()
            .split()[0]
        )
        patch_dir = f'{pkg_dir}/patches'
        for patch in pkg.patches:
            subprocess.run(['wget', '-P', patch_dir, patch])
        subprocess.run(f'make package/{pkg.name}/compile -j V=s'.split(), check=True)
        subprocess.run(
            f'find bin/ -name *{pkg.name}*.ipk -type f -exec cp {{}} {args.ipk_dir}'.split(),
            check=True,
        )


if __name__ == '__main__':
    main()
