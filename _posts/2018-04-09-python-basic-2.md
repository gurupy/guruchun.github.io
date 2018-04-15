---
layout: post
title: Python 기초 2
category: [basic]
tags: [python, string, format string, time, random]
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
  >>> '{:<10}'.format('test')
  'test      '
  # 가운데 정렬
  >>> '{:^10}'.format('test')
  '   test   '
  # padding character '_'
  >>> '{:_<10}'.format('test')
  'test______'
  ```

## 현재 시간

* `time` 모듈을 사용합니다.
  ``` python
  import time

  start = time.time()
  # do something
  str1 = input("input number #1:")
  end = time.time()

  # 시간은 뺄셈으로 시간차를 구할 수 있어요, 숫자는 초(sec)로 나와요
  diff = end - start
  print(diff)
  ```

## 난수(random) 함수
* random 모듈을 사용해서 난수를 만들어 봅니다.
* 우리말로는 난수이지만 숫자만 되는 것은 아닙니다. `무작위`가 더 맞을 것 같습니다.
  ``` python
  import random

  # 0부터 1 미만의 숫자를 아무거나 만들어 줍니다. (0 ~ 0.99999... ) 사이의 숫자
  r = random.random()
  # 이 숫자를 0부터 100 미만의 숫자로 만들려면 100을 곱하면 됩니다.
  r = random.random()*100
  # -50 ~ 50 사이의 값으로 만들려면 이렇게 하면 되겠지요.
  r = random.random()*100 - 50

  # 보통은 어떤 범위의 정수 중에서 뽑아서 쓰고 싶은 경우가 많아요.
  # 편하게 쓰라고 이런 걸 만들어 놓았어요.
  r = random.randint(0, 100)  # 0부터 100 사이의 정수
  r = random.randint(5, 8)    # 5, 6, 7, 8 중에서 하나의 정수
  # 비슷한 기능으로 randrange()도 있어요. 차이는 range처럼 마지막 숫자는 빠져요
  r = random.randrange(5, 8)    # 5, 6, 7 중에서 하나의 정수, 8은 절대로 안나와요

  # random은 무작위라고 했어요. 섞을 수도 있어요.
  abc = list(range(1, 7))     # [1, ... 6]
  random.shuffle(abc)         # 순서를 섞어줘요.
  abc = list('abcde')
  random.shuffle(abc)         # 순서를 섞어줘요.

  # random은 무작위라고 했어요. 고를 수도 있어요. 행운권 추첨하듯이~
  abc = ['kim', 'chunhc', 'djlee', 'jicho']
  lucky = random.choice(abc)
  # choice()가 없었다면 이렇게 했겠지요.
  lucky = abc[random.randrange(0, len(abc))]
  ```
