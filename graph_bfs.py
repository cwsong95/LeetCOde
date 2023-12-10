node = ['m', 'a', 'k', 'i', 't', 'c']

g = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 0],
     [1, 1, 0, 1, 0, 0],
     [0, 1, 1, 0, 1, 1],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0]]

q = []
v = []

q.append('m')
v.append('m')

while q:
  x = q.pop(0)
  print (x, end = ' ')
  idx = node.index(x)

  for i in range(len(g[idx])):
    if g[idx][i] == 1:
      if node[i] not in v:
        q.append(node[i])
        v.append(node[i])