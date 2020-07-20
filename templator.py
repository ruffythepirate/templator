import os
from mako.template import Template

def get_path(path):
    return os.path.expanduser(path)

def load_template(template_name):
    return Template(filename=get_path(f'~/.templates/${template_name}'))

def apply_template(template, args):
    tempate.render(:
    pass


