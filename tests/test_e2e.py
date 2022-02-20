from os import environ
import subprocess
import os
import glob
import pathlib
import tempfile

def test_basic():
    environ["PATH"] = f"{os.getcwd()}:{environ['PATH']}"
    print(environ["PATH"])

    path_to_gpp = subprocess.check_output(["which", "g++"]).decode("utf-8")
    assert os.getcwd() + os.sep + "g++" == path_to_gpp.strip()
    rc = subprocess.run(["g++", "tests/cpp/main.cpp"])
    assert rc.returncode == 0
    temp = tempfile.NamedTemporaryFile(mode="w")
    temp_dir_path = pathlib.Path(temp.name).parent
    temp_prefix = os.environ.get("COMPDB_PREFIX", "comp_")
    pattern = f"{temp_prefix}*"
    comp_file_glob = str(temp_dir_path) + os.sep + pattern
    command_file_list = list (glob.glob(comp_file_glob))
    assert(len(command_file_list) == 1)
