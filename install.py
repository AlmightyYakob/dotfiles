#!/usr/bin/env python3

import argparse
import os
import sys
import subprocess
import json


MAPPING_FILENAME = "links.json"
SCRIPT_FILENAME = "install"

parser = argparse.ArgumentParser(description="Install dotfiles.")
parser.add_argument(
    "-f", "--force", action="store_true", help="Force re-linking of files."
)
parser.add_argument(
    "--no-map", action="store_true", help="Skip the file linking stage."
)
parser.add_argument(
    "--no-script", action="store_true", help="Skip the custom install stage."
)
parser.add_argument(
    "dirs",
    nargs="*",
    help="The dotfiles you wish to run the install script on."
    "If none specified, the script runs on all present.",
)


def main(dirs=[], force=None, no_map=None, no_script=None):
    DOTFILES = os.path.abspath((os.path.dirname(__file__)))

    # Get root dirs, ignore hidden dirs like .git
    base_root_dirs = [
        folder
        for folder in list(os.walk(DOTFILES))[0][1]
        if folder[0] != "." and (len(dirs) == 0 or folder in dirs)
    ]
    root_dirs = sorted([os.path.join(DOTFILES, folder) for folder in base_root_dirs])

    if len(base_root_dirs) == 0 and len(dirs) != 0:
        print(f"Error: Invalid directory names: {', '.join(dirs)}")
        exit()

    for entry in root_dirs:
        dirs = os.listdir(entry)
        processed = False

        if MAPPING_FILENAME in dirs and not no_map:
            processed = True

            mapping_file = os.path.join(entry, MAPPING_FILENAME)
            mapping = json.load(open(mapping_file))

            print(f"Linking files in entry: {os.path.basename(entry)}")

            for part_source, part_dest in mapping.items():
                source = os.path.join(DOTFILES, os.path.expandvars(part_source))
                dest = os.path.expandvars(part_dest)
                dest_dir = os.path.dirname(dest)

                if not os.path.exists(os.path.dirname(dest)):
                    subprocess.run(["mkdir", "-p", dest_dir])

                subprocess.run(["ln", f"-ns{'f' if force else ''}", source, dest])

            print("...done\n")

        if SCRIPT_FILENAME in dirs and not no_script:
            processed = True

            print(f"Running scripts in entry: {entry}")

            script_file = os.path.join(entry, SCRIPT_FILENAME)
            subprocess.run([script_file])

            print("...done\n")

        if processed:
            print("----------------------------------")


if __name__ == "__main__":
    args = parser.parse_args()
    main(dirs=args.dirs, force=args.force, no_map=args.no_map, no_script=args.no_script)
