import ast
import inspect

import astunparse as astunparse
import networkx as nx

from ast_visitor import ASTVisitor
from fib_numbers import fib_numbers

if __name__ == '__main__':
    ast_visitor = ASTVisitor()
    ast_visitor.visit(ast.parse(inspect.getsource(fib_numbers)))
    # print(astunparse.dump(ast.parse(inspect.getsource(fib_numbers))))
    nx.drawing.nx_pydot.to_pydot(ast_visitor.graph).write_png("../artifacts/fib_num_ast.png")
