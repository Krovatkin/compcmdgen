### 1-sentence Pitch

A non-dependency python-based wrapper around g++/gcc for generating `compile_commands.json` for c/c++ projects

### How to Use

* Prepend the path to this folder to `$PATH`
* Each compile command will generate its own command file with the default prefix "comp_"
* Change the default prefix by setting `COMPDB_PREFIX` to `custom_prefix_`
* Compile a project w/ `make`. Caveat if a compiler is referred to a full path it won't work
* Run `python merge.py` 

### Alternatives

This project is very similar to `bear`, `compdb`. `bear` is super powerful and less manual. Unfortunately, it comes with a large number of dependencies which makes it very difficult to use
on non-Ubuntu Linux flavours.