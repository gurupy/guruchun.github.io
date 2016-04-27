---
layout: post
title: Sublime Text Setting for C/C++ Developer
---

설치
----

-   https://www.sublimetext.com/3
-   개발에 필요한 패키지 추가 설치
    -   C++ Starting Kit
    -   SFTP
    -   Sublime Linter
    -   Sublime Linter-cppcheck
    -   Terminal

사용법
------

-   단축키
    -   패키지 컨트롤: ^~P
    -   폴더구조 보이기/숨기기: ^KB
    -   편집창 레이아웃
        - 세로 레이아웃: `@~1(, 2, 3, 4)' -> 1컬럼 ~ 4컬럼
        - 가로 레이아웃: `@~8(, 9)' -> 2행 ~ 3행

C/C++ 환경
----------

-   Sublime Text 설정
    -   C++ Starting Kit
        -   Syntax highlighter 변경
            -   View -> Syntax -> Open all with ... -> C++ Starting Kit -> C++
    -   Linter-cppcheck
        -   `preferences -> package settings -> sublime linter -> settings - user
        -   다음 내용을 추가함
            ```
            "linters": {
                "cppcheck": {
                "@disable": false,
                "args": [],
                "enable": "style",
                "excludes": [],
                "std": [c++11]
            }
            ```

-   g++이나 msvc 컴파일러를 사용하고(에러 무시) 구문분석을 통한 syntax highlighting과 code assistant 기능만 활용할 것임
    -   g++ 환경
        -   minGW 설치
        -   minGW에서 boost, hiredis 등 컴파일…
    -   msvc 환경
        -   Windows 용 라이브러리 사용: boost, hiredis 등
-   Git for Windows

프로젝트
--------

-   프로젝트 생성
