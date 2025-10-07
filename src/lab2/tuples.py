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

#TESTS
print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record( ("Петров Пётр Петрович", "IKBO-12", 4.6) ))
print(format_record( ("  сидорова   анна   сергеевна", "ABB-01", 3.999) ))
print(format_record( ("Иванов Иван Иванович", "BIVT-25", 'asdsda') ))
print(format_record( ("Иванов Иван Иванович", 7575, 5.0) ))
print(format_record( ("Иванов", "BIVT-25", 5.00) ))