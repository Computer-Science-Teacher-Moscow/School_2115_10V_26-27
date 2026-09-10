from itertools import permutations

table = '1246 216 357 415 5347 6127 7356'
graph = 'AGCB BEGA CADF DFC EBF FEDC GBA'

print(*'1234567')
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('ABCDEFG'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x, y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)


