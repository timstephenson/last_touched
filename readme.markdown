Sample Last Accessed File
=========================

-  Write a brief program in one of the above programming languages that, given a list of file names, will display the name of the mostly recently accessed file.  For example, if /tmp/a was the most recently accessed file, then

  - $ program /tmp/a /tmp/b /tmp/c
  - /tmp/a

  would be correctly formatted invocation and output.  In a comment at the top of the file, please explain the conditions under which your program might fail.

- Provide an equivalent implementation of #1 in any other programming language you like.  In this program's comments, please explain any different limitations that apply to this implementation from that in #1.

Implementations
---------------

I've provided two implementations as requested. The first uses Node.js, and the second with Python.

How to run:

```./last_touched.js fixtures/file_b.txt fixtures/file_a.txt fixtures/file_c.txt fixtures/file
```

And the output:

```-> Sorry, something went wrong.
->  Error: ENOENT, no such file or directory 'fixtures/file'
fixtures/file_b.txt
```

Running the Python version is very similar:

```./last_touched.py fixtures/file_b.txt fixtures/file_a.txt fixtures/file_c.txt fixtures/file
```

The output is slightly different:

```-> Sorry 'fixtures/file' was not a file.
fixtures/file_b.txt
```