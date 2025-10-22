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

#TESTS
print(format_record( ("Базов Евгений Петрович", "BPM-25", 4.4) ))
print(format_record( ("Владимир Кожемиров", "IKBO-17", 5.0) ))
print(format_record( ("Сергей Сергеевич Сергеев", "IKBO-12", 4.6) ))
print(format_record( ("  шляпина   анастастия   владимировна", "ABB-02", 4.777) ))

print(format_record( ("Иванов Иван Иванович", "BIVT-25", 'djfhskjvhfdk') ))
print(format_record( ("Иванов Иван Иванович", 365475637, 4.0) ))
print(format_record( ("Иванов", "BIVT-25", 5.00) ))
print(format_record( (34234234, "IKBO-12", 5.00) ))