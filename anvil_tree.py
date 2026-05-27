import os
import re
import sys
from itertools import product
from tree_spec import tree
from anvil_config_base import text as base_text


def fill_template(text, variables):
    """
    Replace all ((key)) placeholders in text with values from the variables dict.
    Raises KeyError if a placeholder has no matching key in variables.
    """
    def replacer(match):
        key = match.group(1)
        if key not in variables:
            raise KeyError(f"No value provided for template variable: '{key}'")
        return str(variables[key])
    return re.sub(r'\(\((\w+)\)\)', replacer, text)

def parse_tree(tree):
    """
    Expand a tree spec into a list of dicts (cartesian product of all axes).

    Each element of tree is either:
      - A tuple of (key, values) pairs  ->  zip them together (indices stay linked)
        e.g. (('from_foundation', [...]), ('model_names', [...]))
      - A single (key, values) pair     ->  iterate independently
        e.g. ('targets', [...])
    """
    groups = []
    names = []
    for element in tree:
        if isinstance(element[0], tuple):
            keys = [pair[0] for pair in element]
            value_lists = [pair[1] for pair in element]
            group = [dict(zip(keys, combo)) for combo in zip(*value_lists)]
            names.append(keys[0])
        else:
            key, values = element
            group = [{key: v} for v in values]
            names.append(key)
        groups.append(group)

    yaml_vars = []
    for combo in product(*groups):
        merged = {}
        for d in combo:
            merged.update(d)
        yaml_vars.append(merged)

    return yaml_vars, names


def write_yaml_dirs(yaml_vars, names, out_root="."):
    """
    For each variable combo in yaml_vars, fill the base config template and
    write it to <out_root>/<dir_name>/config.yaml, where dir_name is built
    from the first name in each axis joined by underscores.
    """
    for variables in yaml_vars:
        dir_name = "_".join(str(variables[n]) for n in names if n in variables)
        dir_path = os.path.join(out_root, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        config = fill_template(base_text, variables)
        with open(os.path.join(dir_path, "config.yaml"), "w") as f:
            f.write(config)

yaml_vars, names = parse_tree(tree)
write_yaml_dirs(yaml_vars, names)
