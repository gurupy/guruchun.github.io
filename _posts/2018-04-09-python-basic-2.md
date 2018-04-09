---
layout: post
title: Python 기초 2
category: [python]
tags: [python, string]
---

## 복습
<details><summary>연습문제 해설</summary>
``` python
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
```
</details>

## 문자열 포맷팅
``` python
# printf 형식의 포맷 문자열 사용
>>> "I eat %10d apples." % 3
'I eat          3 apples.'

# 여러개를 대입하기
>>> "I eat %d %s." %(3, "apples")
'I eat 3 apples.'

# float를 자리수 지정해서 출력
>>> import math
>>> math.pi
3.141592653589793
>>> "pi = %3.5f" %math.pi
'pi = 3.14159'
```

## 현재 시간
``` python
import time

start = time.time()
# do something
str1 = input("input number #1:")
end = time.time()
diff = end - start
print(diff)
```
