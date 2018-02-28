---
layout: post
title: Python 기초 2
category: [python]
tags: [python, string]
---

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
