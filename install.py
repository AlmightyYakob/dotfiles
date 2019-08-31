#!/usr/bin/env python3

import os
import sys
import subprocess
import json

MAPPING_FILENAME = "links.json"
SCRIPT_FILENAME = "install"


def main(force=None, no_map=None, no_script=None):
    DOTFILES = os.path.abspath((os.path.dirname(__file__)))

    # Get root dirs, ignore hidden dirs like .git
    root_dirs = sorted(
        [
            os.path.join(DOTFILES, folder)
            for folder in list(os.walk(DOTFILES))[0][1]
            if folder[0] != "."
        ]
    )

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


def help_func():
    print("Insert help text here")


if __name__ == "__main__":
    force = True if "-f" in sys.argv else None
    no_map = True if "--no-map" in sys.argv else None
    no_script = True if "--no-script" in sys.argv else None
    help_arg = True if "--help" in sys.argv else None

    if help_arg:
        help_func()
        exit()

    main(force=force, no_map=no_map, no_script=no_script)
