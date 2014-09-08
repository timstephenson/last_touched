Sample Last Accessed File
=========================

-  Write a brief program in one of the above programming languages that, given a list of file names, will display the name of the mostly recently accessed file.  For example, if /tmp/a was the most recently accessed file, then

  - $ program /tmp/a /tmp/b /tmp/c
  - /tmp/a

  would be correctly formatted invocation and output.  In a comment at the top of the file, please explain the conditions under which your program might fail.

- Provide an equivalent implementation of #1 in any other programming language you like.  In this program's comments, please explain any different limitations that apply to this implementation from that in #1.

Implementations
---------------

I've provided two implementations as requested. The first uses Node.js, and the second uses Python.

### Running the JS version:

```
./last_touched.js fixtures/file_b.txt fixtures/file_a.txt fixtures/file_c.txt fixtures/file
```

And the output:

```
-> Sorry, something went wrong.
->  Error: ENOENT, no such file or directory 'fixtures/file'
fixtures/file_b.txt
```

It assumes that spaces for files have been escaped. If one of the paths does not point to a file,
a message is printed to let you know what happened. The same is true if the file
cannot be found.

If the spaces are not escaped, it will report that two files couldn't be found.
The script does not attempt to handle anything that is not a file.

### Running the Python version is very similar:

```
./last_touched.py fixtures/file_b.txt fixtures/file_a.txt fixtures/file_c.txt fixtures/file
```

The output is slightly different:

```
-> Sorry 'fixtures/file' was not a file.
fixtures/file_b.txt
```

It assumes that spaces for files have been escaped. If one of the paths does not point to a file,
a message is printed to let you know what happened. The same is true if the file
can not be found.

If the spaces are not escaped, it will report that two files couldn't be found.
The script does not attempt to handle anything that is not a file.

This implementation will not provide as much error information if the path does
not lead to a file. If it is not a file it ignores it and moves to the next item
in the list.
