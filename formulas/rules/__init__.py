import os
import yaml

from formulas.lib import construct_odict

from formulas.rules_list import RulesList


_RULES_DIR = os.path.dirname(os.path.realpath(__file__))


def extract_rules(filepath):
    yaml.add_constructor(u'tag:yaml.org,2002:omap:', construct_odict)
    with open(filepath, 'r') as f:
        return yaml.load(f)


RULESETS = [
    RulesList(
        filename[:len(filename) - 4],  # "xxx.yml"
        extract_rules(os.path.join(_RULES_DIR, filename)).items()
    )

    for filename in os.listdir(_RULES_DIR)
    if filename.endswith('.yml')
]
