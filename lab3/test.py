from lab_python_fp.unique import Unique
from lab_python_fp.gen_random import gen_random
from lab_python_fp.field import field

print('\n' + '='*6 + 'task1' + '='*6)

goods = [
    {'title' : 'Ковер', 'price': 2000, 'color': 'green'},
    {'title' : 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title' : None, 'price': None, 'color': 'red' },
    {'title' : None, 'price' : 3300 },
    {'title' : 'Жизнь', 'price' : None}
]

gen1 = field(goods, 'title')
for i in gen1:
    print(i)

print()

gen2 = field(goods, 'title', 'price')
for i in gen2:
    print(i)

print('\n' + '='*6 + 'task2' + '='*6)

for num in gen_random(5, 1, 3):
    print(num)

print('\n' + '='*6 + 'task3.1' + '='*6)

data = ['a', 'A', 'b', 'B', 'c', 'C']
for i in Unique(data):
    print(i)

print('\n' + '='*6 + 'task3.2' + '='*6)

for i in Unique(data, ignore_case=True):
    print(i)
