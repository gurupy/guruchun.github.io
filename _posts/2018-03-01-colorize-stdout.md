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

## 그래서?
- 제공되는 grc의 기능이면 충분하다.
- `/usr/share/grc/conf.xx, /etc/grc.conf`를 입맛에 맞게 configuration하면 된다.
