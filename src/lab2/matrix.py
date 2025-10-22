def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []: return []
    res = [[0] * len(mat) for _ in range(len(mat[0]))]
    ref_len = len(mat[0])
    for y in range(len(mat)): 
        el_y = mat[y]
        if ref_len != len(el_y):
            raise ValueError
        for x in range(len(el_y)): 
            res[x][y] = mat[y][x]
    return res
            

def row_sums(mat: list[list[float | int]]) -> list[float]: #сумма каждой строки
    res = [0] * len(mat)
    ref_len = len(mat[0])
    for y in range(len(mat)):
        el_y = mat[y]
        if len(el_y) != ref_len:
            raise ValueError
        for x in range(len(el_y)):
            res[y] += el_y[x]
    return res
            


def col_sums(mat: list[list[float | int]]) -> list[float]:
    res = [0] * len(mat[0]) 
    ref_len = len(mat[0])
    for y in range(len(mat)):
        el_y = mat[y]
        if len(el_y) != ref_len:
            raise ValueError
        for x in range(len(el_y)):
            res[x] += el_y[x]
    return res

#TRANSPOSE TESTS
print(transpose( [[10], [20], [30]] ))
print(transpose( [[10, 20, 30]] ))
print(transpose( [[10, 20], [30, 40]] ))
print(transpose( [] ))
print(transpose( [[10, 20], [30]] ))

#ROW_SUMS TESTS
print(row_sums( [[10, 20, 30], [40, 50, 60]] ))
print(row_sums( [[-10, 10], [20, -20]] ))
print(row_sums( [[0, 0], [0, 0]] ))
print(row_sums( [[10, 20], [30]] ))

#COL_SUMS
print(col_sums( [[10, 20, 30], [40, 50, 60]] ))
print(col_sums( [[-10, 10], [100, -100]] ))
print(col_sums( [[0, 0], [0, 0]]))
print(col_sums( [[10, 20], [30]] ))
