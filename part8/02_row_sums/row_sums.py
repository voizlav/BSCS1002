def row_sums(matrix: list):
    for x in matrix:
        x.append(sum(x))


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
