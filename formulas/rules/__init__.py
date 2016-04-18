import os
import yaml


_RULES_DIR = os.path.dirname(os.path.realpath(__file__))


def extract_rules(filepath):
    with open(filepath, 'r') as f:
        return yaml.load(f)


RULESETS = {
    filename[:len(filename) - 4]:  # "xxx.yml"
        extract_rules(os.path.join(_RULES_DIR, filename))
    for filename in os.listdir(_RULES_DIR)
    if filename.endswith('.yml')
}
