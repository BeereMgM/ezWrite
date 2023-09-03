## ezWrite
- What is ezWrite? ezWrite is an package for Python, that lets you write, read and delete files with just some simple code!
- For what do you need ezWrite? With ezWrite you can improve your coding speed very easily.
- What will come in the future? ezWrite will get Multiple updates such as an ezEncrypt and ezDecrypt. 

# Stay Tuned!

## Examples of ezWrite

Write to a file
```python
    from ezWrite import write_file
    #Syntax: write_file(filename, content, path)
    write_file('hello.txt', 'Hello World!')
```

Adding a path
```python
    from ezWrite import write_file
    #Syntax: write_file(filename, content, path)
    write_file('hello.txt', 'Hello World', 'C:\\Users\\User\\Desktop')
```

Append to a file

```python
    from ezWrite import append_file
    #Syntax: append_file(filename, content, path)
    append_file('hello.txt', 'Hello World')
```

Read file

```python
    from ezWrite import read_file
    #Syntax: read_file(filename, path, line)
    output = read_file('hello.txt', 'C:\\Users\\User\\Desktop')
    print(output)
```

Read specific line of file

```python
    from ezWrite import read_file
    #Syntax: read_file(filename, path, line)
    output = read_file('hello.txt', 'C:\\Users\\User\\Desktop', 1)
    print(output)
```

Read multiple lines

```python
    from ezWrite import read_lines
    #Syntax: read_lines(filename, path, fromLine, toLine)
    output = read_lines('hello.txt', 'C:\\Users\\User\\Desktop', 1, 5)
    print(output)
```

Delete a File

```python
    from ezWrite import deleteFile
    #Syntax: deleteFile(filename, path)
    deleteFile('hello.txt', 'C:\\Users\\User\\Desktop')
```

### Connect with me:
[![website](https://raw.githubusercontent.com/codeSTACKr/codeSTACKr/master/img/twitter-light.svg)](https://twitter.com/MgmBeere#gh-light-mode-only)
[![website](https://raw.githubusercontent.com/codeSTACKr/codeSTACKr/master/img/twitter-dark.svg)](https://twitter.com/MgmBeere#gh-dark-mode-only)
