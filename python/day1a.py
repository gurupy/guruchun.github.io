h = int(input("input height of tree: "))
for i in range(h):
  print("{0:^{width}}".format("*" * (i*2+1), width=h*2))
for i in range(int(h/3)):
  w = h//10
  print("{0:^{width}}".format("*" * (w*2+1), width=h*2))
