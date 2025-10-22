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
print(min_max( [4, 14, 4.5, 20, 20.5] )) 
print(min_max( [100] ))
print(min_max( [-1, -6.7, -6,] ))
print(min_max( [1.6, -4, 6.0, -4.1] ))
print(min_max( [] ))

#UNIQUE_SORTED TESTS
print(unique_sorted( [5, 3, 1, 3, 5] ))
print(unique_sorted( [] ))
print(unique_sorted( [-10, -10, 0, 20, 20] ))
print(unique_sorted( [2.0, 2, 5.2, 5.2, 0] ))

#FLATTEN TESTS
print(flatten( [[11, 21], [33, 44]] ))
print(flatten( [[11, 21], (33, 40, 50)] ))
print(flatten( [[11], [], [22, 30]] ))
#print(flatten( [[12, 22], 'abhfjsjdhfjs'] ))
