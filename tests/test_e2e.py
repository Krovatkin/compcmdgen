from os import environ
import subprocess
import os
import glob
import tempfile
import stat
import sys


def test_basic():
    environ["PATH"] = f"{os.getcwd()}:{environ['PATH']}"
    st = os.stat('g++')
    os.chmod('g++', st.st_mode | stat.S_IEXEC)

    path_to_gpp = subprocess.check_output(["which", "g++"]).decode("utf-8")
    if os.getcwd() + os.sep + "g++" != path_to_gpp.strip():
        os.environ["PATH"] = f"{os.getcwd()}:{os.environ['PATH']}"

    rc = subprocess.run(["g++", "tests/cpp/main.cpp"], env=environ)
    assert rc.returncode == 0
    temp_dir_path = tempfile.gettempdir()
    temp_prefix = os.environ.get("COMPDB_PREFIX", "comp_")
    pattern = f"{temp_prefix}*"
    comp_file_glob = str(temp_dir_path) + os.sep + pattern
    command_file_list = list(glob.glob(comp_file_glob))
    assert(len(command_file_list) == 1)

    sys.path.append(".")
    import merge
    merge.merge()
    assert(os.path.exists("compile_commands.json"))
