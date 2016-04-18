import os
import yaml

from formulas.lib import construct_odict

from formulas.rules_list import RulesList


_RULES_DIR = os.path.dirname(os.path.realpath(__file__))

_INITIAL_VARS_DIR = os.path.join(os.path.dirname(_RULES_DIR), 'initial_vars')

yaml.add_constructor(u'tag:yaml.org,2002:omap:', construct_odict)


def extract_yaml_obj(filepath):
    with open(filepath, 'r') as f:
        return yaml.load(f)


RULESETS = [
    RulesList(
        filename[:len(filename) - 4],  # "xxx.yml"
        extract_yaml_obj(os.path.join(_RULES_DIR, filename)).items(),
        extract_yaml_obj(os.path.join(_INITIAL_VARS_DIR, filename))
    )

    for filename in os.listdir(_RULES_DIR)
    if filename.endswith('.yml')
]
