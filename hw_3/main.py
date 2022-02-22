import numpy as np

from hw_3.matrix import Matrix

if __name__ == '__main__':
    np.random.rand(4)
    first_matrix = Matrix(np.random.randint(0, 10, (10, 10)))
    second_matrix = Matrix(np.random.randint(0, 10, (10, 10)))
    with open(f'artifacts/easy/matrix+.txt', 'w') as file:
        file.write((first_matrix + second_matrix).__str__())
    with open(f'artifacts/easy/matrix*.txt', 'w') as file:
        file.write((first_matrix * second_matrix).__str__())
    with open(f'artifacts/easy/matrix@.txt', 'w') as file:
        file.write((first_matrix @ second_matrix).__str__())
