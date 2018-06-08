---
layout: post
title: Python 문자열 다루기
category: [topic]
tags: [python, string]
---

## 문자열에서 문자 얻기
- 차례대로 전부
  ``` python
  abc = "0abcd5eng9"
  for c in abc:
    print(c)

  # index 사용하기
  for i in range(0, len(abc)):
    print(i, abc[i])
  # 또는
  i = 0
  while i < len(abc):
    print(i, abc[i])
  ```

## 문자열에서 일부 문자열 잘라내기
* `text1[i]`: text 문자열에서 i번째 문자 얻기,
  - i가 음수이면 뒤에서 시작해서 i번째 문자, `-0`은 0과 같아서 앞에서 첫번째 문자
* 문자열 슬라이싱
  * `text1[i:j]`: i번째 문자부터 j번째 문자 바로 앞까지 문자열 얻기, `range(i, j)` 처럼 j는 포함하지 않는다.
  * i, j가 음수이면 뒤에서부터 앞쪽으로 위치를 계산한다.
  * `text1[:j]`: 0번째 문자부터 j번째 문자 바로 앞까지 문자열 얻기
  * `text1[i:]`: i번째 문자부터 끝까지 문자열 얻기
* 문자열 자르기(슬라이싱) 연습
  ``` python
  abc = "0abcd5eng9"
  print(abc[1])     # 'a'
  print(abc[-1])    # '9'
  print(abc[1:5])   # 'abcd'
  print(abc[-5:-2]) # '5en'
  print(abc[-2:-5]) # '' --> 문자열의 i위치가 j위치보다 커서 문자열이 선택되지 않음.
  print(abc[5:])    # '5eng9'
  print(abc[-3:])   # 'ng9'
  print(abc[7:])    # 'ng9'
  print(abc[:7])    # '0abcd5e'
  print(abc[:-3])   # '0abcd5e'
  ```
* 문자열 슬라이싱 스텝 지정
  ``` python
  abc = "0abcd5eng9"
  a = abc[:]        # 시작위치:0, 끝위치:len()
  print(a)          # '0abcd5eng9'
  a = abc[::1]      # 시작위치:0, 끝위치:len(), 슬라이싱 폭: 1문자
  print(a)          # '0abcd5eng9'
  a = abc[::2]      # 시작위치:0, 끝위치:len(), 슬라이싱 폭: 2문자
  print(a)          # '0bdeg'
  a = abc[1:5:2]    # 시작위치:1, 끝위치:5, 슬라이싱 폭: 2문자
  print(a)          # 'ac'
  ```

## 문자열 찾기
* 문자가 있는지? `in`
  - `'a' in abc`: 변수 abc에 문자 a가 있는지?
  - 결과: `True/False`
* 문자열이 있는지?
  - 파이썬은 문자와 문자열을 구분하지 않는다. 동일한 방법을 사용한다.
* 찾는 문자열이 몇 번이나 나오는지? `str.count()`
* 찾는 문자열의 시작 위치는? `str.find()`
  - `find('find_str', start_pos=0)`

## 문자열 검사하기
* `abc.isalpha()`: 모든 요소가 문자이면 True, 한글도 True, 숫자나 기호가 하나라도 있으면 False
* `abc.isdigit()`: 모든 요소가 숫자이면 True, '12.345'가 들어 있어도 False
* `abc.isalnum()`: 모든 요소가 문자이거나 숫자이면 True, '12.345'가 들어 있어도 False

## 문자열 조작하기
- 문자열 자체를 조작하지 않습니다. 조작된 문자열을 반환합니다.
- 문자열 합치기: `+`
- 문자열 반복하기: `*`
- 대소문자 변환: `uppper, lower`
  ``` python
  a = "Abc"
  b = "Cde"
  print(a + b)      # 'AbcCde'
  print('=' * 5)    # '====='
  a.upper()         # a는 그대로, 리턴값은 'ABC'
  b.lower()         # b는 그대로, 리턴값은 'cde'
  ```
- 문자열 좌/우측 끝에 있는 공백 지우기: `lstrip, rstrip, strip`
  ``` python
  abc = '  abcd\tend  \n'
  print(abc)
  b = abc.lstrip()
  print(b)          # 'abcd\tend  \n'
  c = b.rstrip()
  print(c)          # 'abcd\tend'

  # 공백문자(' ', '\t', '\n')외에 다른 문자를 직접 지정해서 제거할 수 있다.
  abc = "========= title ========="
  print(abc.strip('='))     # ' title '
  ```
- 나누기와 합치기: split(), join()
  ``` python
  # sep: ', '
  abc = "2018-04-05, logger, debug, value is empty"
  aaa = abc.split(", ")
  print(aaa)       # ['2018-04-05', 'logger', 'debug', 'value is empty']
  # sep: '|'
  bbb = "|"
  bbb.join(aaa)
  print(bbb)       # '2018-04-05|logger|debug|value is empty'
  ```
- 문자 바꾸기: `replace(find_str, replace_str, replace_count=all)`
  ``` python
  abc = "0abcd5eng9"
  # abc[4] = '4' # error, not allowed
  # 모두 바꾸거나 지정된 횟수만큼 바꾸거나...
  b = abc.replace(abc[4:5], "4", 1)
  print(b)  # '0abc45eng9'
  ```

## 연습문제
* 다음 코드를 수행한 후에
  ``` python
  abc = "0abcd5eng9"
  str1 = 12.34.5
  str2 = 12.345
  str3 = -12.345
  ```
* `abc`에서 짝수번째 문자열만 출력해 보세요.
  - 출력: `ac5n9`
  - 코드: `print(abc[1::2])`
* `abc`문자열을 거꾸로 출력해 보세요.
  - 출력: `9gne5dcba0`
  - 코드: `print(abc[::-1])`
* `-12.34`같은 float 변환 가능한 문자열을 True로 반환하는 is_number() 함수를 작성하세요.
  - 코드
    ``` python
    def is_number(instr):
      return instr.lstrip('-').replace('.','',1).isdigit()

    print(is_number(str1))  # False
    print(is_number(str2))  # True
    print(is_number(str3))  # True
    ```
* 콤마(,)로 구분된 문자열을 list로 변경하시오. 콤마 다음에 공백문자가 있는 경우 제거하시오.
