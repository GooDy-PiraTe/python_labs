def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
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
