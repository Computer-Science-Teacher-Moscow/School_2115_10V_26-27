from re import finditer

with open('24_31368.txt') as file:
    s = file.readline()
print((ls:=len(s)))

num = r'([1-9][0-9]*|0)'
prod = rf'(({num}\*)*0(\*{num})*)'
expression = fr'({prod}(\+{prod})*)'
expression = fr'(?=({expression}))'

m = max([x.group(1) for x in finditer(expression, s)], key = len)
# m = max([x for x in m if eval(x) == 0], key=len)
print(len(m), m)



from string import printable

# print(printable)
# for x in printable[:19][::-1]:
#     expr = int(f'76{x}79645', 19) + int(f'35{x}42', 19) + int(f'332{x}6', 19)
#     if not expr % 18:
#         print(expr//18)
#         break
