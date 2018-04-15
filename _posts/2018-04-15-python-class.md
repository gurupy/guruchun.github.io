---
layout: post
title: Python 클래스 활용하기
category: [topic]
tags: [python, class, object, instance, classmethod, 생성자, 소멸자]
---

# 클래스
## 클래스란?
  - 자세한 설명은 <http://byteofpython-korean.sourceforge.net/byte_of_python.html#oop>
  - 클래스는 내 맘대로 만드는 오브젝트 타입이다.
  - 클래스는 그 안에 변수와 함수를 가지고 있다.
  - 클래스의 변수, 함수에 대한 접근제한은...

### 클래스 만들기
  - 클래스 안쪽에 정의된 함수를 메소드라고 부르는데 클래스에 소속된 함수이다.
  - 클래스 변수는 클래스 안쪽, 함수 바깥쪽에 정의한다.
  - 파이썬에서는 값을 주지 않고 변수를 만들 수 없으므로, 선언과 함께 값을 넣거나 `None` 값을 넣어 두었다가 생성자에서 진짜 값을 넣을 수도 있다.
  - 예시
    ```python
    class MyClass:
        # 클래스 변수 만들기
        object_count = 0
        # common_obj_data       # 이것은 값을 주지 않고 클래스 변수만 정의했으므로 에러
        common_obj_data = None  # `None`이라는 특별한 값을 할당한 것

        # 클래스 함수 만들기
        def say(self, _message):
            print (_message)

    obj = MyClass()
    obj.say("hi! steve")
    ```

### 생성자와 소멸자
* 클래스로부터 객체가 새로 만들어질 때마다 또는 객체가 없어질 때마다 해야 하는 일이 있다면?
* `__init__`은 생성자라고 부르는 특별한 메소드인데, 객체가 새로 만들어질 때마다 해야할 일을 적어준다.
* `__del__`은 소멸자라고 부르는 특별한 메소드인데, 객체가 없어질 때마다 해야할 일을 적어준다.
  ```python
  class MyClass:
      object_count = 0
      def __init__(self, _family):
          MyClass.object_count += 1
          print ("class created... count=", MyClass.object_count)

      def __del__(self):
          MyClass.object_count += 1
          print ("class destroyed... count=", MyClass.object_count)
  ```

### 클래스와 객체
- 데이터 초기화와 접근
  * 클래스 밖에서 클래스 데이터는 클래스 이름으로 접근하고, 객체 데이터는 객체 이름으로 접근한다.
    ```python
    # 클래스 정의
    class MyClass:
        # 클래스 안쪽, 변수
        my_name = "class"

        # 클래스 안쪽, 함수 --> 메소드
        def say(self, _message):
            print(_message)
            print(MyClass.my_name)

        # 클래스 안쪽, 클래스 함수 --> 클래스 메소드
        @classmethod
        def say_name(cls):
            print("my name is {}".format(cls.my_name))       

    # 클래스 바깥 쪽
    obj = MyClass()
    obj.say("hi! ")
    MyClass.say_name()
    ```
- 메소드의 첫번째 입력변수와 접근
  * 객체 메소드는 첫번째 인자로 `self`를 받는다. `self`를 사용해서 객체의 변수나 메소드에 접근한다.
  * 클래스 메소드는 첫번째 인자로 `cls`를 받는다. `cls`를 사용해서 클래스 변수나 메소드에 접근한다.
  * 객체 메소드와 클래스 메소드를 구분하기 위해서 클래스 메소드를 정의할 때는 `@classmethod`를 첫줄에 적어주어야 한다. 이것을 데코레이션 decoration 또는 어노테이션 annotation이라고 한다.

## 클래스 사용하기
