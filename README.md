# GooDy-PiraTe (Саргаева Анна БИВТ-25-1)

## Лабораторная работа 1

### Задание 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![Картинка 1](./images/lab1/img1.png)

### Задание 2
```python
a = float( input("a: ").replace(',', '.') )
b = float( input("b: ").replace(',', '.') )
print(f"sum={(a+b):.2f}; avg={((a+b)/2):.2f}")
```
![Картинка 1](./images/lab1/img2.png)

### Задание 3
```python
price, discount, vat = map(float, input("Введите price, discount, vat: ").split())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f"НДС:               {vat_amount:.2f} ₽")
print(f'Итого к оплате:    {total:.2f} ₽')
```
![Картинка 1](./images/lab1/img3.png)

### Задание 4
```python
minutes = int(input('Минуты: '))
h = minutes//60
print(f"{(minutes//60)%24}:{(minutes%60):02d}")
```
![Картинка 1](./images/lab1/img4.png)

### Задание 5
```python
st = input('ФИО: ')
ln, n, nof = st.split()
print(ln, n, nof)
print(f"Инициалы: {ln[0]+n[0]+nof[0]}.") 
print(f'Длина (символов): {len(ln) + len(n) + len(nof) + 2}')
```
![Картинка 1](./images/lab1/img5.png)

### Задание 6
```python
n = int(input())
och, zaoch = 0, 0
for i in range(n):
    try:
        last_name, name, age, format = list(input(f"in_{i+1}: ").split())
        age = int(age)
        if format == 'False': zaoch += 1
        elif format == 'True': och += 1 
    except: pass
print(f'out: {och} {zaoch}')
```
![Картинка 1](./images/lab1/img6.png)


### Задание 7
```python
line = input("in: ")
word_started = False
origin = []
step = 0
f_i = 0
s_i = 0
for i in range(len(line)):
    symb = line[i]
    if symb.isupper() and not word_started:
        word_started = True
        f_i = i
        origin.append(symb)
    if word_started and symb.isdigit() and not s_i:
        s_i = i+1
        step = s_i - f_i
    if word_started and step and (i-f_i)%step == 0:
        origin.append(symb)
    if word_started and symb == '.':
        break
print(f"out: {''.join(origin)}")

```
![Картинка 1](./images/lab1/img7.png)

