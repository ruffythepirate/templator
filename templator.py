#!/usr/bin/env python

import os
from mako.template import Template
import sys
from getopt import getopt

def get_path(path):
    return os.path.expanduser(path)

def load_template(template_name):
    return Template(filename=get_path(f'~/.templates/{template_name}'))

def apply_template(template, args):
    return template.render(args = args)

def main():
    settings = parse_arguments(sys.argv[1:])
    template = load_template(settings.template_name)
    result = apply_template(template, settings.template_arguments)
    print(result)

def parse_arguments(argv):
    optlist, args = getopt(argv, 't:')
    template = next(x for x in optlist if x[0] == '-t')[1]
    return Settings(template, args)

class Settings:
    def __init__(self, template_name, template_arguments):
        self.template_name = template_name
        self.template_arguments = template_arguments

if __name__ == "__main__":
    main()
