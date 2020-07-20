from mako.template import Template
from templator import apply_template, parse_arguments


def test_apply_template_with_one_arg():
    template = Template('a ${args}')
    result = apply_template(template, ('world'))
    assert result == 'a world'

def test_apply_template_with_multiple_arg():
    template = Template('a ${args[0]} in the ${args[1]}')
    result = apply_template(template, ('hello', 'world'))
    assert result == 'a hello in the world'

def test_parsing_arguments():
    res = parse_arguments(('test', '-t', 'template'))
    assert res.template_name == 'template'
    assert res.template_arguments == ()

