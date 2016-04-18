import os
import yaml
from collections import OrderedDict

from meta_test import TestableList


_RULES_DIR = os.path.dirname(os.path.realpath(__file__))


# From https://gist.github.com/weaver/317164
def construct_odict(load, node):
    """This is the same as SafeConstructor.construct_yaml_omap(),
    except the data type is changed to OrderedDict() and setitem is
    used instead of append in the loop.
    >>> yaml.load('''
    ... !!omap
    ... - foo: bar
    ... - mumble: quux
    ... - baz: gorp
    ... ''')
    OrderedDict([('foo', 'bar'), ('mumble', 'quux'), ('baz', 'gorp')])
    >>> yaml.load('''!!omap [ foo: bar, mumble: quux, baz : gorp ]''')
    OrderedDict([('foo', 'bar'), ('mumble', 'quux'), ('baz', 'gorp')])
    """

    omap = OrderedDict()
    yield omap
    if not isinstance(node, yaml.SequenceNode):
        raise yaml.constructor.ConstructorError(
            "while constructing an ordered map",
            node.start_mark,
            "expected a sequence, but found %s" % node.id, node.start_mark
        )
    for subnode in node.value:
        if not isinstance(subnode, yaml.MappingNode):
            raise yaml.constructor.ConstructorError(
                "while constructing an ordered map", node.start_mark,
                "expected a mapping of length 1, but found %s" % subnode.id,
                subnode.start_mark
            )
        if len(subnode.value) != 1:
            raise yaml.constructor.ConstructorError(
                "while constructing an ordered map", node.start_mark,
                "expected a single mapping item, but found %d items"
                % len(subnode.value),
                subnode.start_mark
            )
        key_node, value_node = subnode.value[0]
        key = load.construct_object(key_node)
        value = load.construct_object(value_node)
        omap[key] = value


def extract_rules(filepath):
    yaml.add_constructor(u'tag:yaml.org,2002:omap:', construct_odict)
    with open(filepath, 'r') as f:
        return yaml.load(f)


RULESETS = [
    TestableList(
        name=filename[:len(filename) - 4],  # "xxx.yml"
        rules=extract_rules(os.path.join(_RULES_DIR, filename)).items()
    )

    for filename in os.listdir(_RULES_DIR)
    if filename.endswith('.yml')
    ]
