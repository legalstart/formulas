#!/usr/bin/env python

# [TODO] - use an ast parser instead of raw `eval`

from collections import defaultdict
import json

from rules import RULESETS


if __name__ == '__main__':
    for ruleset in RULESETS:
        data = json.load(
            open('./formulas_test/rules_inputs/%s.json' % ruleset.name, 'r'))

        data_flattened = defaultdict(list)

        for k, v in data.iteritems():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                for subel in v:
                    for kk, vv in subel.iteritems():
                        flat_key = k + '__' + kk
                        data_flattened[flat_key].append(vv)
            elif isinstance(v, dict):
                for kk, vv in v.iteritems():
                    flat_key = k + '__' + kk
                    data_flattened[flat_key] = vv
            else:
                data_flattened[k] = v

        print '--------------- %s ----------------' % ruleset.name
        print ruleset.process_all_rules(data_flattened)
