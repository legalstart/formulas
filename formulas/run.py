#!/usr/bin/env python

# [TODO] - use an ast parser instead of raw `eval`

import json

from rules import RULESETS


if __name__ == '__main__':
    data = json.load(
        open('./formulas_test/rules_inputs/incorporation.json', 'r'))

    for ruleset in RULESETS:
        print '--------------- %s ----------------' % ruleset.name
        print ruleset.process_all_rules(data)
