Install clips from source

```python
try
    chkinputdatatype(x,p);
catch ME
    throwAsCaller(ME);
end

Error: Not parseable, gives
File "/path/to/libermate-0.4/translate_new.py", line 190, in do_try
    b=self.write_node(node.children[1], "")
IndexError: list index out of range
```

Solution: Comment it out, throwAsCaller is what fails here.  Later on change the function behaviour to throw a python error as desired.

---

```python
if any( w(:)<0 ) && realFlag
  Error: Not parseable, gives
  File "./libermate.py", line 236, in bop
    if(python_priority[ptoken]>python_priority[op]):
KeyError: 'np.any((w.flatten(1)<0.))'
```

Solution: Comment it out, ```&& realFlag``` fails here because in MATLAB is bool and in the translation becomes a float (1.0) which can't be ```&&```-ed. Later on correct that flag to a bool value by hand.

---

```python
if any( (w>pi) | (w<0) ) && realFlag

Not parseable, gives:
  File "./libermate.py", line 236, in bop
    if(python_priority[ptoken]>python_priority[op]):
  KeyError: 'np.any(np.logical_or(w > np.pi, w<0.))'
```

Solution: Comment it out, ```&& realFlag``` fails because the evaluation of realFlag as it's parsed as a float in python and it's originally intended to be a boolean. Later correct by hand this value to a boolean.

---

```python
a = [1; -H2\h1].';

Not parseable, gives:

  File "./libermate.py", line 251, in preop
    if(python_priority[ptoken]>python_priority[op]):
KeyError: ', '
```

Solution: Make H2 negative before then it will work. i.e. 
```
H2_minus = -H2
a = [1; H2_minus\h1].';
```



---

```python
c = T(:,2:p+q+2)\(T_minus(:,1));

Not parseable, gives:

  File "/path/to/libermate-0.4/translate_new.py", line 265, in do_backdiv
    b=self.write_node(node.children[1], ", ")
IndexError: list index out of range
```

Solution: This is too complicated for the parser, try to divide it in parts, i.e.:
   T_minus = -T;
   T_left = T(:,2:p+q+2);
   T_right = (T_minus(:,1));
   c = T_left \ T_right;


---
```python
  File "/path/to/libermate-0.4/translate_new.py", line 271, in do_colon
    sstr=self.colonop(ptoken, cc)
  File "./libermate.py", line 269, in colonop
    a=cc[0]
IndexError: list index out of range
```

---

#### After work:

1.  Correct identations of ifs
2.  Correct the matcompat.max found in the code, you can safely change them to just max
3.  Correct other import issues:
    linalg.solve -> from scipy.linalg import solve
    toeplitz not found
    from scipy.linalg import toeplitz
    etc... I google them to know where they are in scipy
4.  matdiv not found
    change it to a division "/"
5.  some np.zeros(1,K) should be np.zeros(K)
6.  length -> len can be safely changed usually
7.  Indices are floats sometimes, change them to ints (remove the "." from "1.")
8.  Indices are wrong lots of times

---

Info about libermate:
[https://groups.google.com/forum/#!topic/scipy-user/6tx6ORxOr_I](https://groups.google.com/forum/#!topic/scipy-user/6tx6ORxOr_I)

Official website:
[http://libermate.sourceforge.net/](http://libermate.sourceforge.net/)

Useful info:
[http://wiki.scipy.org/NumPy_for_Matlab_Users](http://wiki.scipy.org/NumPy_for_Matlab_Users)

Alternatives:
[https://github.com/ocefpaf/python-mlabwrap](https://github.com/ocefpaf/python-mlabwrap)


