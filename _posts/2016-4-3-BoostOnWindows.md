---
layout: post
title: Boost on Windows
---

Visual Studio에서 c++11과 boost 라이브러리를 사용할 수 있는 개발환경을 설정한다.

## 설치
- Visual Studio Express Desktop 2015 설치
- Boost 라이브러리 설치
  - http//boost.org에서 다운로드 한다.
  - 소스를 받아서 직접 빌드해도 되겠지만 미리 만들어 놓은 파일을 받아 설치하는 것이 빠르다.
  - http://www.boost.org/users/download/ 중간 쯤에 보면 `Prebuilt windows binaries`가 있다.
  - 적당한 위치에 설치한다. 여기서는 `D:/boost_1_60_0`에 설치한 것으로 본다.

## 프로젝트 생성
- Console Application 프로젝트를 하나 생성한다.
- 프로젝트 설정에 다음 내용을 추가한다.
  * Properties > C/C++ > General > Additional Include Directories
    - Boost 설치시의 설치 폴더 위치를 지정한다.
  * Properties > C/C++ > Precompiled Headers
    - 미리 컴파일된 헤더 사용 안 함으로 설정한다.
- 모든 프로젝트에서 boost를 사용할 수 있게 하려면 `VC++ 디렉터리` 설정에 추가한다.
  * `포함 디렉터리` 설정값에 boost 설치 경로를 추가한다. 
  * `$(VC_IncludePath);$(WindowsSDK_IncludePath);D:\boost_1_60_0`
  
## Boost sample application 실행
- Boost 홈페이지에서 tutorial이나 example에 있는 소스를 가져다가 실행한다.
