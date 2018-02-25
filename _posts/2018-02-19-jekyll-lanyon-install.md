---
layout: post
title: installing jekyll & applying lanyon theme
category: [web]
tags: [jekyll, install, lanyon, theme]
---

## install jekyll

``` console
$ sudo gem install jekyll
프로그램 'gem'을(를) 설치하지 않습니다. 다음을 입력해 설치할 수 있습니다:
sudo apt install ruby
$ sudo apt install ruby
$ sudo gem install jekyll
...
ERROR:  Error installing jekyll:
	ERROR: Failed to build gem native extension.
    current directory: /var/lib/gems/2.3.0/gems/http_parser.rb-0.6.0/ext/ruby_http_parser
/usr/bin/ruby2.3 -r ./siteconf20180219-18596-13wi3ti.rb extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h
...
$ sudo apt install ruby-dev
$ sudo gem install jekyll
...
configure.ac:376: the top level
autoreconf: configure.ac: not using Libtool
...
configure.ac:41: error: possibly undefined macro: AC_PROG_LIBTOOL
      If this token and others are legitimate, please use m4_pattern_allow.
      See the Autoconf documentation.
configure:7624: error: possibly undefined macro: AC_PROG_LD
...
$ sudo apt install libtool
$ sudo gem install jekyll
...
Successfully installed jekyll-3.7.2
```

## download sample with lanyon theme

- theme, http://lanyon.getpoole.com/
- download, https://github.com/poole/lanyon
- github에서 lanyon theme를 zip으로 다운로드 받은 후 적당한 디렉토리에 푼다.
- 디렉토리 이동 후 `$ jekyll serv`를 실행하면 `_sites` 디렉토리에 컨텐츠가 생성되고 이를 jekyll이 호스팅한다.
- browser에서 `http://localhost:4000`으로 접속해 생성된 페이지를 볼 수 있다.

## troubleshootings

- `_post`에 생성한 md 페이지들이 보이지 않는다.
``` console
$ jekyll serve
Configuration file: /home/chunhc/ws-blog/lanyon-master/_config.yml
       Deprecation: You appear to have pagination turned on, but you haven't included the `jekyll-paginate` gem. Ensure you have `plugins: [jekyll-paginate]` in your configuration file.
            Source: /home/chunhc/ws-blog/lanyon-master
       Destination: /home/chunhc/ws-blog/lanyon-master/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
                    done in 0.168 seconds.
 Auto-regeneration: enabled for '/home/chunhc/ws-blog/lanyon-master'
    Server address: http://127.0.0.1:4000/
  Server running... press ctrl-c to stop.
```
- 한참을 헤맸는데, 구글링해보니 해결책은 있다.
- `_config.yml`을 아래와 같이 수정했다. 왜 이렇게 해야하는지 모르겠다. 찝찝하다.
```yml
# Dependencies
gems:                [jekyll-paginate]   # <----- inserted

# Permalinks
# Use of `relative_permalinks` ensures post links from the index work properly.
permalink:           pretty
#relative_permalinks: true               # <--- commented
```
