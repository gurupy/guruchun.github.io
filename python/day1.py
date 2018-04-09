# 1st
for i in range(10):
    print("*"*(i*2+1))

for i in range(3):
    print("*")

# 2nd
for i in range(10):
    print(" "*(10-i), "*"*(i*2+1))

for i in range(3):
    print(" "*10, "*")

# 3rd
h = int(input("input height of tree: "))
for i in range(h):
    print(" "*(h-i), "*"*(i*2+1))

for i in range(int(h/3)):
    w = (h//10+1)
    print(" "*(h-w), "*"*w*2)
