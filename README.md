LiberMate
---

LiberMate - A MATLAB to Python (SciPy/NumPy) Translator

All credit goes to Eric C. Schug for this incredible work.

Check ```notes_on_using_libermate.txt``` if you use it and it doesn't work properly (it's normal!) I give many hints there on how to correct problems I had while translating [https://github.com/awesomebytes/parametric_modeling](https://github.com/awesomebytes/parametric_modeling)

(Almost) Original README
---
> from [http://sourceforge.net/p/libermate/code/HEAD/tree/](http://sourceforge.net/p/libermate/code/HEAD/tree/)

LiberMate - A MATLAB to Python (SciPy/NumPy) Translator 

```bash
git clone https://github.com/awesomebytes/libermate.git
```

Setup
---

Libermate needs pyclips: [http://pyclips.sourceforge.net/web/](http://pyclips.sourceforge.net/web/)

Download pyclips-1.0.7.348.tar.gz

Extract and install (there is a README if you have doubts)

```bash
tar -zxvf pyclips-1.0.7.348.tar.gz
cd pyclibs
sudo python setup.py build
sudo python setup.py install
```

Run
---
```bash
# Change directory to the libermate directorie e.g.
cd libermate
# To get command line help use  
python libermate.py -h
# To convert a single test file type
python libermate.py tests/colon.m
# and will print the following output
#   Opening File tests/colon.m
#   Starting Parser
#   Parser Complete
#   Starting Translator
#   Translation Complete
#   writing to file tests/colon.py

# To convert all test files type
python libermate.py tests/*.m
# To output Abstract Syntax Tree from colon.m
python libermate.py --astdump tests/colon.m
#   Opening File tests/colon.m
#   Starting Parser
#   Parser Complete
#   writing to file tests/colon.ast
#   Starting Translator
#   Translation Complete
#   writing to file tests/colon.py
```

This will create a file called tests/colon.ast which contains the AST for the parsed file. The AST file can be useful to track where the Parser may have had problems.

LiberMate will attempt to convert MATLAB source files to python.
The MATLAB files must end with .m and the translated python code will
be written to python files, of the same name but ending with .py.

Known Issues
---
* LiberMate does not handle command style MATLAB expressions such as ```grid on``` instead use function expressions such as ```grid('on')```

* LiberMate does not map all MATLAB functions to SciPy/NumPy equivalents.  It does map several common functions.

* LiberMate does not completely support freeform matrix expressions, e.g.

```
./libermate.py tests/matrix_tests.m

# Opening File tests/matrix_tests.m
# Starting Parser
# syntax error: unexpected symbol at line 10 (column 4): "
#  "
# syntax error: unexpected symbol at line 11 (column 3): " "
# Parser Complete
# Starting Translator
# error: unexpected end of subtree
# Translation Complete
# writing to file tests/matrix_tests.py
```
The output shows two errors on lines 10 and 11 that are cause by an initial newline and final newline in matrix expression for variable d.

* numpy does not automatically grow arrays
* python scalars behave differently from matlab arrays
* plot title,ylabel do not take extra arguments
* missing waitbar function
* 

TODO
---
* replace a.copy() with copy(a)
