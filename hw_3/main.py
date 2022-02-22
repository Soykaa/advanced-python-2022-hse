import numpy as np

from hw_3.matrix import Matrix
from hw_3.save_mixin import MMatrix

if __name__ == '__main__':
    np.random.rand(4)

    first_matrix = Matrix(np.random.randint(0, 10, (10, 10)))
    second_matrix = Matrix(np.random.randint(0, 10, (10, 10)))

    with open("artifacts/easy/matrix+.txt", "w") as file:
        file.write((first_matrix + second_matrix).__str__())
    with open("artifacts/easy/matrix*.txt", "w") as file:
        file.write((first_matrix * second_matrix).__str__())
    with open("artifacts/easy/matrix@.txt", "w") as file:
        file.write((first_matrix @ second_matrix).__str__())

    first_matrix = MMatrix(np.random.randint(0, 10, (10, 10)))
    second_matrix = MMatrix(np.random.randint(0, 10, (10, 10)))

    (first_matrix + second_matrix).save_to_file("artifacts/medium/matrix+.txt")
    (first_matrix * second_matrix).save_to_file("artifacts/medium/matrix*.txt")
    (first_matrix @ second_matrix).save_to_file("artifacts/medium/matrix@.txt")
