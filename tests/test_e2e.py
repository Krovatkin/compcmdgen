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
    if os.getcwd() + os.sep + "g++" != path_to_gpp.strip():
        os.environ["PATH"] = f"{os.getcwd()}:{os.environ['PATH']}"
    print(os.environ["PATH"])
    rc = subprocess.run(["which", "g++"], env=environ)
    rc = subprocess.run(["echo", "bla $PATH"], env=environ)
    rc = subprocess.run(["g++", "tests/cpp/main.cpp"], env=environ)
    assert rc.returncode == 0
    temp = tempfile.NamedTemporaryFile(mode="w")
    temp_dir_path = pathlib.Path(temp.name).parent
    temp_prefix = os.environ.get("COMPDB_PREFIX", "comp_")
    pattern = f"{temp_prefix}*"
    comp_file_glob = str(temp_dir_path) + os.sep + pattern
    command_file_list = list (glob.glob(comp_file_glob))
    assert(len(command_file_list) == 1)
