---
layout: post
title: Python 기초 1
category: [basic]
tags: [python, 기초, basic]
---

## 개발환경 만들다가 지쳐요. 바로 코딩합시다.
* 브라우저에서 온라인으로 파이썬 코딩을 연습할 수 있는 곳
  - <https://www.tutorialspoint.com/execute_python3_online.php> 원조?
  - <https://repl.it/> 로그인 필요, 가끔씩 느려요
  - <https://ideone.com/> 하나의 창에서 모든 프로그래밍 언어 선택 가능
* 잘 안보겠지만... 알고는 있어야죠.
  * Python Language Reference
    - <https://docs.python.org/3.6/reference/index.html> (원문)
    - <http://python.flowdas.com/reference/index.html> (한글)
  * Python Standard Library
    - <https://docs.python.org/3/library/> (원문)

## print
  - 숫자, 문자열
    ``` python
    print("hello world")
    print(123)
    ```
  - 상수와 변수
    ``` python
    name = "gurupy"
    print("my name is", name)
    ```

## 변수와 자료형
- 프로그램에서 `=`은 할당이지 eual `==`이 아니다.
  ```
  3 + 4 = 7  # 수학에서 맞으나 프로그램에서는 허용 안됨
  3 + 4 == 7 # 프로그램에서 같다는 의미로 쓰이고 결과는 True
  3 + 4 == 6 # 수학에서는 틀림, 프로그램에서는 허용되고 결과는 False
  ```
- 변수는 값이 할당될 때 자료형이 결정된다.
- 값이 할당되지 않은 변수를 사용할 수는 없다.
- 정수
  ``` python
  a = 123
  b = -345
  ```
- 실수
  ``` python
  # 소수점이 있으면 실수로 입력된다.
  c = 1.23
  d = -3.45
  # 123과 123.0은 다르다.
  e = 123.0
  # 정수를 실수로 바꿔서 입력해도 된다.
  f = float(123)
  ```

- bool
  ```python
  isOk = True
  ```
- 문자열
  - 표현방법: 작은따옴표, 큰따옴표 또는 따옴표3개를 사용하여 둘러싼다.
  ``` python
  a = "It's a desk"
  b = 'You are a girl'
  c = """
      Usage: mcptool function parameters
          - function: diag, dup, check ...
          multi lines are here
      """
  ```
  - 이스케이프코드: `\n, \t, \\, \', \"`

## 연산자

- `+, -, *`, `*`는 문자열에서도 동작한다.
- `/`: 나눗셈, 2.7에서 정수나눗셈은 정수로 결과를 반환하지만 3.4에서는 실수로 반환한다.
- `**`: 제곱
- `//`: 나눗셈 몫
- `%`: 나눗셈 나머지
- `@`: 행렬 곱
- 객체비교: `is, is not`
- 논리연산: `and, or, not`
- 비트연산: `&, |, ^, ~, >>, <<`

## 블럭과 들여쓰기
- 블럭은 콜론':'으로 표시한다.
- ':' 다음줄에 들여쓰기를 하면서 블럭이 시작되고 들여쓰기를 끝내면 블럭이 끝난다.
- 들여쓰기는 공백문자(space) 4개를 권장한다.

## if, while, for, ...
- 조건절에 괄호는 필요없지만 있어도 된다. 코딩가이드에서는 쓰지 말라고 한다.
- `if, elif, else`
  ``` python
  if a >= 90:
      print("A")
  else:
      print("B")
      print("lazy boy...")

  for x in range(10):
      print(x)
  print("end")
  ```
- 반복횟수를 알 수 있을 때는 for를 쓴다.
  ``` python
  for i in range(1,10):
    do_something()
  ```
- 조건이 만족하는 동안 반복해야할 때는 while을 쓴다.
  ``` python
  while isOk:
    isOk = do_something()
  ```
## 컨솔 입력받기
* 입력은 항상 문자열로 들어온다.
  ``` python
  str1 = input("input number #1:"))
  # 숫자로 바꾸려면 변환해야 한다.
  num2 = int(input("input number #2:"))
  ```
## 더 읽을 거리
* <https://www.python.org/dev/peps/pep-0008/> (코딩 가이드 원문)
* <https://b.luavis.kr/python/python-convention> (번역)

## MISSION

* `*`와 `print, for`를 사용해서 나무를 그려보세요.
```
     *
     ***
     *****
     *******
     *
     *
```
* 가운데 정렬하면 그럴듯한 나무 모양이 나오겠네요.
```
        *
       ***
      *****
     *******
        *
        *
```
* `input`으로 나무의 높이를 입력받아 그려보세요.
```
        *         ---    
       ***         |
      *****        | --> 편의상 나무의 높이    
     *******       |
    *********     ---  
        *          | --> 줄기(trunk)는 절반으로
        *         ---
```
