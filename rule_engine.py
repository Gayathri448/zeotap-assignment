class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Condition (e.g., 'age > 30')

def create_rule(rule_string):
    # Example logic for parsing the rule_string and creating an AST
    # This is a placeholder for rule parsing logic.
    if 'age > 30' in rule_string:
        return Node("operand", value="age > 30")
    # Similarly parse for other conditions and combine using Node objects

def combine_rules(rules):
    # Combine multiple ASTs into a single tree
    root = Node("AND")
    root.left = rules[0]
    root.right = rules[1]
    return root

def evaluate_rule(ast, data):
    # Recursively evaluate the AST
    if ast.node_type == "operand":
        return eval_condition(ast.value, data)
    elif ast.node_type == "AND":
        return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
    elif ast.node_type == "OR":
        return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)

def eval_condition(condition, data):
    # Example: Parse 'age > 30' into actual comparison
    if 'age > 30' in condition:
        return data['age'] > 30
    