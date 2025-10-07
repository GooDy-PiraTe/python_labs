def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: raise ValueError
    return min(nums), max(nums)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    uni_nums = list(set(nums))
    uni_nums.sort() 
    return uni_nums

def flatten(mat: list[list | tuple]) -> list:
    new_list = []
    for elem in mat:
        if type(elem) == list or type(elem) == tuple:
            new_list.extend(elem)
        else: 
            raise TypeError
    return new_list


#MIN_MAX TESTS
print(min_max( [3, -1, 5, 5, 0] )) 
print(min_max( [42] ))
print(min_max( [-5, -2, -9] ))
print(min_max( [1.5, 2, 2.0, -3.1] ))
print(min_max( [] ))

#UNIQUE_SORTED TESTS
print(unique_sorted( [3, 1, 2, 1, 3] ))
print(unique_sorted( [] ))
print(unique_sorted( [-1, -1, 0, 2, 2] ))
print(unique_sorted( [1.0, 1, 2.5, 2.5, 0] ))

#FLATTEN TESTS
print(flatten( [[1, 2], [3, 4]] ))
print(flatten( [[1, 2], (3, 4, 5)] ))
print(flatten( [[1], [], [2, 3]] ))
print(flatten( [[1, 2], 'ab'] ))

