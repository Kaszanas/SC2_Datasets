# Generate documentation automatically

In our project we use Sphinx to automatically generate documentation.

All of the files that are used to generate the html version of the docs are available in ```source```


## Done previously

Initially to generate the makefiles the following command was used:
```
sphinx-quickstart docs
```

## Commands

To automatically generate documentation use the following commands from the top directory:

Generating source:
```
sphinx-apidoc -f -o .\docs\source\ .\src\
```

Building the html versions:
```
sphinx-build .\docs\source\ .\docs\build\html\
```