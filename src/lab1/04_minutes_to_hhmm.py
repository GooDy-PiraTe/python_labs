minutes = int(input("Минуты: "))
h = minutes // 60
print(f"{(minutes//60)%24}:{(minutes%60):02d}")
