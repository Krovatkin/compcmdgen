#!/usr/bin/env python

import subprocess
import sys
import tempfile
import json
import os


opt_sep = ":"
compiler_name = os.path.basename(sys.argv[0])


def compile():
    os.environ["PATH"] = os.environ["PATH"][1:]
    completed = subprocess.run(
        [compiler_name] + sys.argv[1:],
        env=os.environ
    )
    return completed.returncode


def get_filename():
    suffixes = ["cc", "cpp", "c"]
    filename = ""
    for a in sys.argv[1:]:
        for suffix in suffixes:
            if a.lower().endswith(suffix):
                filename = a
                break

    return filename


if __name__ == "__main__":
    rc = compile()

    filename = get_filename()

    if filename:
        command = {
            "directory": os.getcwd(),
            "arguments": ([compiler_name] + sys.argv[1:]),  # noqa: E501
            "file": filename
        }

        temp_prefix = os.environ.get("COMPDB_PREFIX", "comp_")
        with tempfile.NamedTemporaryFile(mode="w", prefix=temp_prefix, delete=False) as temp:  # noqa: E501
            # print(f"saving to {temp.name}")
            json.dump([command], temp)

    exit(rc)
