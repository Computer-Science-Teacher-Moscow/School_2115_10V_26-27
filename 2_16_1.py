from itertools import permutations

table = '1246 216 357 415 5347 6127 7356'
graph = 'ABCG BAEG CADF DFC EBF FEDC GAB'

print(*'1234567')

graph = {x[0]: set(x[1:]) for x in graph.split()}
print(graph)

