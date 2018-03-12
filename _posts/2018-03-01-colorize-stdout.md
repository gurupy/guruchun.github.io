---
layout: post
title: Colorizing stdout in linux terminal
category: [linux, admin]
tags: [admin, shell, terminal, colorizer, grc, linux]
---

## 이런기능을 찾는 사람이 많았을텐데?
- 그렇다.
- https://unix.stackexchange.com/questions/148/colorizing-your-terminal-and-shell-environment

## 기존에 만들어진 프로그램 활용하기
- grc, Generic Colouriser
  - https://github.com/garabik/grc

## STDOUT에 ANSI Color Sequence를 덧붙여 출력하기
- sed, regular expression을 사용해 color를 적용할 문자열 선택
- 선택한 문자열 앞뒤로 color sequence 끼워넣기
- ex) xcol.sh
  - https://ownyourbits.com/2017/01/23/colorize-your-stdout-with-xcol/

## 그래서 선택은?
- 제공되는 grc의 기능이면 충분하다.
- `/usr/share/grc/conf.xx, /etc/grc.conf`를 입맛에 맞게 configuration하면 된다.
- `/etc/grc.conf`에서는 쉘 명령어를 보고 어떤 conf 파일을 적용할 것인지 자동으로 선택할 수 있게 한다.
- `/usr/share/grc/conf.xx`는 선택된 color scheme(conf)을 정의한다. 어떤 단어를 어떤 색상으로 표현할지 정규식을 사용해 정의한다.
- `grc -c netstat ifconfig -a` 처럼 적용할 color scheme 파일 이름을 직접 지정해 줄 수도 있다. 여기서는 ifconfig -a 출력이 netstat 컬러 설정이 적용되어 출력된다.
