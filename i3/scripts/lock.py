#!/usr/bin/env python3

import os
import subprocess

FEHBG_FILE = os.path.abspath(os.path.expandvars("$HOME/.fehbg"))

with open(FEHBG_FILE) as fehbg:
    cmd = fehbg.readlines()[1]
    file = cmd.strip().split(" ")[-1].strip("'").strip('"')

subprocess.run(["i3lock", "-i", file, "-t"])
