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
