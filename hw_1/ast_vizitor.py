import ast
import networkx as nx


class ASTVisitor(ast.NodeVisitor):
    def __init__(self):
        self.graph = nx.DiGraph()

    def visit_FunctionDef(self, node):
        self.graph.add_node(node, shape='box', label=f'FunctionDef: {node.name}', fillcolor='#F26A5B', style='filled')
        for arg in self.visit(node.args):
            self.graph.add_edge(node, arg)
        for item in node.body:
            self.graph.add_edge(node, self.visit(item))
        return node

    def visit_arguments(self, node):
        self.graph.add_node(node, shape='box', label='arguments', fillcolor='#95DED6', style='filled')
        for arg in node.args:
            self.graph.add_node(arg, shape='box', label=f'arg: {arg.arg}', fillcolor='#64ACA4', style='filled')
            self.graph.add_edge(node, arg)
        return [node]

    # body
    def visit_Assign(self, node):
        self.graph.add_node(node, shape='box', label='Assign', fillcolor='grey', style='filled')
        for t in node.targets:
            self.graph.add_edge(node, self.visit(t))
        self.graph.add_edge(node, self.visit(node.value))
        return node

    def visit_Name(self, node):
        self.graph.add_node(node, shape='box', label=f'Name: {node.id}', fillcolor='pink', style='filled')
        return node

    def visit_Constant(self, node):
        self.graph.add_node(node, shape='box', label=f'Constant: {node.value}', fillcolor='#E6E7E8', style='filled')
        return node

    def visit_For(self, node):
        self.graph.add_node(node, shape='box', label='For', fillcolor='#EBE0D0', style='filled')
        self.graph.add_edge(node, self.visit(node.target))
        self.graph.add_edge(node, self.visit(node.iter))
        for item in node.body:
            self.graph.add_edge(node, self.visit(item))
        return node

    def visit_Call(self, node):
        self.graph.add_node(node, shape='box', label='Call', fillcolor='#B27883', style='filled')
        self.graph.add_edge(node, self.visit(node.func))
        for arg in node.args:
            self.graph.add_edge(node, self.visit(arg))
        return node

    def visit_BinOp(self, node):
        self.graph.add_node(node, shape='box', label=f'BinOp: {type(node.op).__name__}', fillcolor='#FF0833',
                            style='filled')
        self.graph.add_edge(node, self.visit(node.left))
        self.graph.add_edge(node, self.visit(node.right))
        return node

    def visit_Return(self, node):
        self.graph.add_node(node, shape='box', label='Return', fillcolor='#EC9EC0', style='filled')
        self.graph.add_edge(node, self.visit(node.value))
        return node
