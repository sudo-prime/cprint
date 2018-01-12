### Tired of python's simple, short, elegant print statements?

### Used to program in c++ and find yourself struggling to remember python's print syntax?

### Do you prefer doing things the hard way even when there's an easy solution?

### Have I got the module for you!

# cprint

A python module that makes c++ print syntax just work, for some reason.

## Usage

First, import the module like so:

```python
from cprint import *
```

After that, anything is possible!
*Just kidding - only one very specific and unhelpful thing is possible that wasn't possible before!*

You can now use the following syntax in python:

```python
cout << "Hello " << "World" << endl;
```

```
Hello World
```

There are a few catches, though.

1. To actually print to the screen, `endl` must be called. For example:

```python
cout << "test";
```

This won't print anything.
However,

```python
cout << "test" << endl;
```

This will print the string "test".


