-----------
layout: post
title: installing jekyll & applying lanyon theme
category:web
tag:jekyll, install, lanyon, theme
-----------

# jekyll
'''bash
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
'''
