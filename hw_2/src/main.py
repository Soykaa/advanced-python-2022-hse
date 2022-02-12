def dim_is_ok(lists):
    return len(list(filter(lambda line: len(line) != len(lists), lists))) == 0


def generate_table(lists):
    if not dim_is_ok:
        return ''
    return '\\begin{tabular}{' + 'l' * len(lists[0]) + '}\n' + \
           '\\\\\n'.join(map(lambda line: '&'.join(line), lists)) + '\n\\end{tabular}\n'


def generate_tex_file(table):
    return '\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\begin{document}\n\n' \
           + generate_table(table) + '\n\\end{document}'


if __name__ == '__main__':
    with open('../artifacts/easy_task.tex', 'w') as file:
        file.write(generate_tex_file([['hello1', 'hello22', 'hello333'], ['hello4444', 'hello55555', 'hello666666'],
                                      ['hello7', 'hello8', 'hello9']]))
