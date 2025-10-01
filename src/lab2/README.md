
# GooDy-PiraTe (Саргаева Анна БИВТ-25-1)

## Лабораторная работа 1

### Задание A
Функция min_max
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: raise ValueError
    return min(nums), max(nums)
```
![Картинка 1](./images/lab2/arrays_min_max.png)
![Картинка 2](./images/lab2/arrays_min_max_error.png)
Функция unique_sorted
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    uni_nums = list(set(nums))
    uni_nums.sort() 
    return uni_nums
```
![Картинка 1](./images/lab2/arrays_unique_sorted.png)
Функция flatten
```python
def flatten(mat: list[list | tuple]) -> list:
    new_list = []
    for elem in mat:
        if type(elem) == list or type(elem) == tuple:
            new_list.extend(elem)
        else: 
            raise TypeError
    return new_list
```
![Картинка 1](./images/lab2/arrays_flatten.png)
![Картинка 2](./images/lab2/arrays_flatten_error.png)


### Задание B
Фукнция transpose
```python
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
```
![Картинка 3](./images/lab2/matrix_transpose.png)
![Картинка 3](./images/lab2/matrix_transpose_error.png)
Фукнция row_sums
```python
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
            
```
![Картинка 3](./images/lab2/matrix_row_sums.png)
![Картинка 3](./images/lab2/matrix_row_sums_error.png)
Фукнция col_sums
```python
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
```
![Картинка 3](./images/lab2/matrix_col_sums.png)
![Картинка 3](./images/lab2/matrix_col_sums_error.png)


### Задание C
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) != tuple and type(rec) != list: raise TypeError
    if len(rec) == 3:
        fio, group, gpa = rec
        if type(fio) == str and type(group) == str and type(gpa) == float:
            fio, group = fio.strip(), group.strip()
            f_i_o = fio.split()
            if len(f_i_o) == 2:
                initials = f'{f_i_o[0].capitalize()} {(f_i_o[1].capitalize())[0]}.'
            elif len(f_i_o) == 3:
                initials =  f'{f_i_o[0].capitalize()} {(f_i_o[1].capitalize())[0]}.{(f_i_o[2].capitalize())[0]}.'
            else: raise ValueError('FIO is wrong')
            gpa = f"{gpa:.2f}"
            return f"{initials}, гр. {group}, GPA {gpa}"
        else: raise ValueError
    else: raise ValueError('3 elements needed')
```
![Картинка 1](./images/lab2/tuples.png)
![Картинка 1](./images/lab2/tuples_wrong_gpa.png)
![Картинка 1](./images/lab2/tuples_wrong_group.png)
![Картинка 1](./images/lab2/tuples_wrong_type_fio.png)
![Картинка 1](./images/lab2/tuples_wrong_value_fio.png)


```
![Картинка 1](./images/lab1/img7.png)
