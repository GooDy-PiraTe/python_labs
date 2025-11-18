n = int(input())
och, zaoch = 0, 0
for i in range(n):
    try:
        last_name, name, age, format = list(input(f"in_{i+1}: ").split())
        age = int(age)
        if format == "False":
            zaoch += 1
        elif format == "True":
            och += 1
    except:
        pass
print(f"out: {och} {zaoch}")
# Фамилия Имя Возраст Формат_участия
