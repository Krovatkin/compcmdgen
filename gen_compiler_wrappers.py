import shutil

compilers = (
    ("g++", (7, 11)),
    ("gcc", (7, 11)),
    ("clang", (7, 11)),
    ("clang++", (7, 11)),
    ("g++", None),
    ("gcc", None),
    ("clang", None),
    ("clang++", None),
)

for compiler in compilers:

    if not compiler[1]:
        shutil.copy("template.py", compiler[0])
    else:
        for suffix in range(compiler[1][0], compiler[1][1]):
            shutil.copy("template.py", f"{compiler[0]}-{suffix}")
