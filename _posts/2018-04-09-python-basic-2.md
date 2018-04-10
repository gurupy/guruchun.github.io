---
layout: post
title: Python 기초 2
category: [python]
tags: [python, string]
---

## 복습
* 나무 모양 그리기
  ``` python
  # 1st: 나무크기 고정, 왼쪽 정렬
  for i in range(10):
      print("*" * (i*2+1))
  for i in range(3):
      print("*")

  # 2nd, 나무크기 고정, 오른쪽 정렬
  for i in range(10):
      print(" " * (10-i), "*" * (i*2+1))
  for i in range(3):
      print(" "*10, "*")

  # 3rd, 나무크기를 입력 받아 그리기
  h = int(input("input height of tree: "))
  for i in range(h):
    print(" " * (h-i), "*" * (i*2+1))
  for i in range(int(h/3)):
    w = h//10
    print(" " * (h-w), "*" * (w*2+1))
  ```
* string.format를 활용해서 다시 그리기
  ``` python
  h = int(input("input height of tree: "))
  for i in range(h):
    print("{0:^{width}}".format("*" * (i*2+1), width=h*2))
  for i in range(int(h/3)):
    w = h//10
    print("{0:^{width}}".format("*" * (w*2+1), width=h*2))
  ```
  
## 문자열 포맷팅
* <https://pyformat.info/>
* old style `'%s %s' % ('one', 'two')`
  ``` python
  print("I eat %10d apples." % 3)
  print("I eat %d %s." % (3, "apples"))

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
* new style: `'{} {}'.format('one', 'two')`
  ``` python
  print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11))
  print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058))

  # {0}은 0번째 argument
  >>> "First argument: {0}, second one: {1}".format(47,11)
  'First argument: 47, second one: 11'
  # printf style의 format specifier는 그대로 유효
  >>> "Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11)
  'Second argument:  11, first one:   47.42'
  # {0} argument 재사용: 같은 값을 다른 format으로 출력
  >>> "various precisions: {0:6.2f} or {0:6.3f}".format(1.4148)
  'various precisions:   1.41 or  1.415'
  ```
* padding, alignment
  ``` python
  # 오른쪽 정렬
  >>> '{:>10}'.format('test')
  '      test'
  # 왼쪽 정렬
  >>> '{:10}'.format('test')
  'test      '
  # 가운데 정렬
  >>> '{:10}'.format('test')
  '   test   '
  # padding character '_'
  >>> '{:_<10}'.format('test')
  'test______'
  ```

## 문자열 다루기
* TBD

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
