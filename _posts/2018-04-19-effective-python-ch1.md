---
layout: post
title: Chapter 1. Pythonic Thinking
category: [book]
tags: [effective python, pythonic thinking]
---

## Chapter 1: Pythonic Thinking
### Item 1: Know Which Version of Python You’re Using
사용 중인 파이썬의 버전을 알고 쓰자.  
당연한거 아닌가? 하지만 난 2.7.x에는 관심 없다.
``` python
>>> import sys
>>> sys.version
'3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)]'
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0)
```

### Item 2: Follow the PEP 8 Style Guide
Python Enhancement Proposal 8 스타일 가이드를 따라라.  
* <https://www.python.org/dev/peps/pep-0008/>
* <https://b.luavis.kr/python/python-convention> (번역)
* Namming
  - Functions(함수), Variables(변수), Attributes(속성)은 lowercase_underscore 형식을 따른다. --> camelCase를 좋아하는데 아쉽다.
  - Protected instance attributes는 `_leading_underscore` 형식을 따른다.
  - Private instance attributes는 `__double_leading_underscore` 형식을 따른다.
  - Class, Except는 CapitalizedWord 형식을 따른다
* Expressions and Statements
  - import는 '표준 라이브러리 모듈, Third-Party 모듈, 자신이 만든 모듈' 순으로 한다.

### Item 3: Know the Differences Between bytes, str, and unicode
bytes, str, unicode의 차이를 알자
* 문자열은 bytes와 str에 담을 수 있다.
* bytes는 문자를 바이트의 시퀀스로, str은 유니코드의 시퀀스로 표현한다.  
* 유니코드는 전세계의 모든 문자를 하나의 코드체계에 넣은 것이다. 2바이트 코드이다.
* 유니코드를 그대로 쓰면 latin 문자에 2바이트를 할당하게 되어 메모리 낭비가 심하다. 그래서 유니코드를 어떻게 표현할지 지정하는 인코딩이라는게 있다.  
UTF-8은 자주 쓰는 문자를 1바이트로 표현하고(ASCII코드표와 호환된다), 자주 안쓰이는 글자를 4바이트로 표현해서 유니코드를 지원하면서 메모리 사용은 최소화하고 있다.  
프로그래머가 접하는 유니코드 문자열은 거의 전부 UTF-8이라고 생각해도 된다.
* 처음에 설명한 `bytes는 문자를 바이트의 시퀀스로, str은 유니코드의 시퀀스로 표현한다`는 말은 `'글'`이라는 문자를 bytes는 utf-8로 인코딩된 **2바이트** 로 다루고, str은 `'글'`이라는 utf-8로 인코딩된 유니코드 **1문자** 로 다룬다.

문자열을 bytes와 str으로 표현할 수 있다면 상호변환이 필요하겠다.
* `str.encode('utf-8')`는 유니코드 문자열을 `utf-8`로 인코딩된 bytes로 변환한다.
* `bytes.decode('utf-8')`는 `utf-8`로 인코딩된 bytes를 유니코드 문자열 str로 변환한다.
```python
>>> a = "천해철"
>>> a.encode('utf-8')
b'\xec\xb2\x9c\xed\x95\xb4\xec\xb2\xa0'
>>> b = a.encode('utf-8')
>>> b.decode('utf-8')
'천해철'
```

### Item 4: Write Helper Functions Instead of Complex Expressions
### Item 5: Know How to Slice Sequences
### Item 6: Avoid Using start, end, and stride in a Single Slice
### Item 7: Use List Comprehensions Instead of map and filter
### Item 8: Avoid More Than Two Expressions in List Comprehensions
### Item 9: Consider Generator Expressions for Large Comprehensions
### Item 10: Prefer enumerate Over range
### Item 11: Use zip to Process Iterators in Parallel
### Item 12: Avoid else Blocks After for and while Loops
### Item 13: Take Advantage of Each Block in try/except/else/finally
