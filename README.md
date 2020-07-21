# Templator.py

A simple template engine that you can easily run locally. It was created because I noticed I needed to create many similar `C++` makefiles where just the filenames were different.

## Installing / Getting started

The best practice of this is still pending. At the moment you can create a virtual environment for the project 

```
python -m venv .venv
```

and then you can activate it
```
. .venv/bin/activate
```
Finally you install the dependencies through
```
pip install -r requirements.txt
```

Now you can execute the templator by writing `./templator.py -t <template name> arg0 arg1 ...`. To use the tool you must give `-t <template name>`, where the template name must be a file placed in `~/.templates/<template name>`. The arguments can be any number. If there is only one argument you use it as `${args}` in your template file. If you have multiple you use `${args[0]}`, `${args[1]}` etc.. The underlying template engine is `Mako` for python, you can read more on its webpage regarding accepted syntax.

## Developing

See installing section.

## Features

* A lightweight local template engine
* No internet needed

## Contributing

Well, if you'd like, give it a shot. The project is very small, and I don't think it needs much more, but I'm open to suggestions.

## Licensing

The code in this project is licensed under MIT license.
