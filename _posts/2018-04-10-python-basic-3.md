---
layout: post
title: Python 기초 3
category: [basic]
tags: [python, file]
---

## 파일 다루기
``` python
# 파일 열기, 닫기
>>> f1 = open("ch1.py", "r")
>>> f1.close()
```

### 열기 모드
* r: read only
* w: writable
* a: append
* rb: binary read
* wb: binary write
* ab: binary append

### 파일 읽기
