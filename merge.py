import tempfile
import glob
import pathlib
import os
import json

temp = tempfile.NamedTemporaryFile(mode="w", prefix='comp_')
temp_dir_path = pathlib.Path(temp.name).parent

def build_commands(temp_dir_path):
    commands = []
    temp_prefix = os.environ.get("COMPDB_PREFIX", "comp_")
    pattern = f"{temp_prefix}*"
    comp_file_glob = str(temp_dir_path) + os.sep + pattern
    command_file_list = list (glob.glob(comp_file_glob))
    for f in command_file_list:
        commands.extend(read_single_compile_command(f))

    return commands

def read_single_compile_command(filename):
    return json.load(open(filename))

if __name__ == "__main__":
    commands_list = build_commands(temp_dir_path)
    with open("compile_commands.json", "w") as compdb:
        json.dump(commands_list, compdb, indent=4, sort_keys=True)
