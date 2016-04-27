---
layout: post
title: Redmine 설치 가이드(Windows)
---

Redmine 설치/관리 가이드
========================

설치
----

패키지 다운로드

-   Redmine을 사용하기 위해 설치할 것이 많으므로 Bitnami Stack을 쓰기로 한다.
-   ​https://bitnami.com/stack/redmine

Windows 설치

-   설치경로 `C:/Bitnami`(기본값) 사용

설정 변경 및 추가 설치
----------------------

-   Theme 설치
    1.  다운로드
        -   https://github.com/HolonGlobe/PurpleMine2
        -   Modern & popular theme

    2.  설치
        -   Unzip it into `$RedmineInstallDir$/apps/redmine/htdocs/public/themes`.
        -   Restart Redmine

    3.  Theme 선택: “Administration ~~<span style="text-align:right;">Settings"</span>~~&gt; ”Display -&gt; Theme"
    4.  Optional; `themes/$ThemeName$/stylesheets/application.css 수정
        *** 폰트 변경
        <pre>
        // CSS파일의 맨위에 사용할 폰트 위치 추가
        `import url(http://fonts.googleapis.com/earlyaccess/nanumgothic.css);

//폰트를 적용할 class나 tag의 font-family 속성에 폰트 추가
body{…; font-family:“Nanum Gothic”,…;}

</pre>
****\* Sidebar 폭 줄이기

-   플러그인 추가 설치
    -   Progressive Projects List
    -   Redmine screenshot paste
    -   Redmine Backlogs
    -   WBS 일괄 등록: import/export excel WBS
    -   Checklist to issues
-   외부 접속을 위한 방화벽 열기
    -   httpd 80, mysql 3306, subversion 3690
    -   참고, \[\[mcp:LinuxAdminManual| Linux 관리 매뉴얼\]\]
-   Eclipse Mylyn 연동
    -   참고, http://pseg.or.kr/pseg/?mid=infouse&document\_srl=3342&listStyle=viewer

관리
----

필요한 모든 것은 여기에 설명되어 있다.

-   ​Quick Guide, https://wiki.bitnami.com/Native\_Installers\_Quick\_Start\_Guide
-   User Manual, https://wiki.bitnami.com/Applications/BitNami\_Redmine

자주쓰는 몇가지만 적어보자면…

-   Start, restart redmine
    -   cmd line: `$installDir/ctlscript.sh start`, `$installDir/ctlscript.sh restart serviceName`
    -   GUI: double-click `manager-linux-x64.run`

백업 및 복구
------------

Redmine은 대부분의 자료(프로젝트정보, 일감, 위키 등)를 DB에 저장한다.
DB에 저장되지 않는 자료는 Wiki/Forum/Documents/Files 메뉴에 첨부되는 파일들이다.
SVN (혹은 Git)도 Redmine과 별도로 동작하는 시스템이기 때문에 Repository를 따로 백업해 두어야 한다.

    // backup redmine db
    C:\Bitnami\redmine-3.2.0-1>mysqldump -uroot -p bitnami_redmine > d:\redmine_data\backup\20160321-redminedb.sql
    // backup attached files
    C:\Bitnami\redmine-3.2.0-1>"%ProgramFiles%\7-Zip\7z.exe" a "d:\redmine_data\backup\20160321-htdocs-files.zip" "C:\Bitnami\redmine-3.2.0-1\apps\redmine\htdocs\files"
    // backup svn repository
    C:\Bitnami\redmine-3.2.0-1>svnadmin dump "D:\redmine_data\svnRepo\mcp" | "%ProgramFiles%\7-Zip\7z.exe" a "d:\redmine_data\backup\20160321-svn-repo.zip
