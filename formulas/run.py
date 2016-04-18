#!/usr/bin/env python

# [TODO] - use an ast parser instead of raw `eval`

import json
import yaml
import __builtin__
from copy import deepcopy

# The module that contains helper functions
# Used for evaluating formulas and casting formulas results
import helpers


# [TODO] - Make type_caster_name optional
def process_formula(formula, type_caster_name, variables):
    """
    :param formula: str - the formula to evaluate.
    :param type_caster_name: str - the output type (builtin type or defined in
    `.helpers`), used as a caster function.
    :param variables: dict - the variables already calculated, used potentially
    as input of the formula.
    :returns: output of the formula, of type defined by ``type_caster_name``
    """
    # [TODO] - perf improvement necessary?
    eval_context = deepcopy(variables)
    eval_context.update(helpers.__dict__)
    return_value = eval(formula, eval_context)

    # Cast result if possible:
    type_caster = getattr(
        helpers, type_caster_name,
        getattr(
            __builtin__, type_caster_name))
    if type_caster is not None:
        return_value = type_caster(return_value)

    return return_value


def process_list_formula(formula, type_caster_name, variables):
    """ See above, differences: ``formula`` returns always a `list` and
    ``type_caster_name`` is mapped on the output list.
    """
    eval_context = deepcopy(variables)
    eval_context.update(helpers.__dict__)
    return_list = eval(formula, eval_context)

    type_caster = getattr(
        helpers, type_caster_name,
        getattr(
            __builtin__, type_caster_name))

    if type_caster is not None:
        return_list = [type_caster(_) for _ in return_list]

    return return_list


def process_all_rules(rules, data):
    """
    :param rules: list of rules containing ``type`` and ``formula``.
    :param data: dict - user data.
    """
    for varname, rule in rules.iteritems():
        # list => varname with .
        if isinstance(rule['type'], list):
            list_varname, nested_varname = varname.split('.')
            results = process_list_formula(
                    rule['formula'], rule['type'][0], data)
            for el, result in zip(data[list_varname], results):
                el[nested_varname] = result
        else:
            data[varname] = process_formula(
                rule['formula'], rule['type'], data)
    return data


if __name__ == '__main__':
    rules = yaml.load(open('./formulas/rules/incorporation.yml', 'r'))

    data = json.load(
        open('./formulas_test/rules_inputs/incorporation.json', 'r'))

    print process_all_rules(rules, data)
