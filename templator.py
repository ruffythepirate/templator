import os
from mako.template import Template
import sys
from getopt import getopt

def get_path(path):
    return os.path.expanduser(path)

def load_template(template_name):
    return Template(filename=get_path(f'~/.templates/${template_name}'))

def apply_template(template, args):
    return template.render(args = args)

def main():
    getopt(sys.argv, "t:")

def parse_arguments(argv):
    return Settings('name', ())

class Settings:
    def __init__(self, template_name, template_arguments):
        self.template_name = template_name
        self.template_arguments = template_arguments

if __name__ == "__main__":
    main()
