
## 선택
* 임의의 한 문자 ( `.` )
  - 행 바꿈 문자를 제외한 어떤 문자에도 대응이 가능하다
  - 예) `A.ple = Apple(O), Alple(O), Aplle(X)`

* 둘 중 하나 선택 ( `|` )
  - `|` 기호를 기준으로 앞뒤의 값들 중의 하나 선택
  - 예) `gr(a|e)y` = gray 또는 grey 로 둘 중 하나에 매치된다
  - 괄호가 없을 경우 gra|ey 는 gra 또는 ey 로 인식
  - 예) `(First|1st)` => `(Fir|1)st`

* 앞의 문자를 0회 또는 1회 반복 ( `?` )
  - `?` 문자는 앞의 문자가 있거나 없는 경우를 찾을 때 사용
  - 예) `apples? apple(O), apples(O)`
  - 복수와 단수를 구분하는 경우 많이 사용

* 앞의 문자를 0회 이상 반복 ( `*` )
  - 문자가 입력된 이전의 문자가 출력이 되지 않거나 여러번 출력이 되는 것을 지정한다
  - 예) `apple* = appl(O), apple(O), appleeeeeee(O)`

* 앞의 문자를 1회 이상 반복 ( `+` )
  - `+` 문자가 입력된 이전의 문자가 1번 이상 입력이 되는 것을 지정
  - 예) `apple+ = apple(X), apple(O), appleeeeeeeeeee(O)`

* 정규표현식 그룹 ( `()` )
  - ()는 정규식 내에서 패턴을 그룹화 할 때 사용
  - 예) `(apple)* = apple(O), appleapple(O), appleappleapple(O)`

* n회 반복 ( `{n}` )
  - 바로 앞의 문자를 정확히 n번 반복한다
  예) `A.{3}e  = Apple(O), Abcde(O), AAAAA(X),AAAAe(O)`

* n회 이상 반복 ( `{n,}` )
  - 바로 앞의 문자를 n회 이상 반복한다
  - 예) `Ap{2,}le = Apple(O), Appple(O), Aple(X), Apble(X)`

* n회 이상 m회 이하 반복 ( `{n, m}` )
  - 바로 앞의 문자를 n회 이상 m회 이하 반복한다
  - 예) `s.{3,4}ing = sleeping(O), shopping(O), swimming(O)`

* 문자 클래스 ( `[ ]` )
  - `[` 와 `]` 안에 가능한 문자를 명시 할 수 있다
  - 예) `[ 0 2 4 6 8 ]` = 0,2,4,6,8 중의 하나를 찾는다

* 문자 클래스 안의 특수문자 ( ^ , - )
  - 문자는 최초의 문자열과 마지막 문자열을 모두 명시한다
  - 예) `[a-z]` = a에서 z까지의 모든 문자를 찾는다
  - ^ 문자 뒤에 나오는 조건을 만족하지 않는 문자를 찾는다
  - 예) `[^a-z]` = a에서 z까지의 문자를 제외한 문자를 뜻한다
  - 문자 클래스에 정의된 특수문자 표현
    - `\w` `[0-9a-zA-Z_]` 숫자, 영문자(대, 소문자), `_`(언더바)
    - `\W` `[^0-9a-zA-Z_]` 숫자, 영문자(대, 소문자), `_`(언더바) 이외
    - `\s` `[\t\n\r\f]` 공백(스페이스, 탭, 개행)
    - `\S` `[^\t\n\r\f]` 공백 이외의 문자
    - `\d` `[0-9]` 숫자
    - `\D` `[^0-9]` 숫자 이외의 문자

## 패턴매칭(Pattern Matching)
문자열의 패턴이 일치하는 것을 조사한다.  
패턴은 `/`문자로 비교하고자 하는 문자열을 감싸서 표현한다

* `=~` 문자열의 패턴이 일치하는 것이 있다면 참을 반환
* `!~` 문자열의 패턴이 일치하는 것이 있을 때 거짓을 반환

### 매칭 결과
패턴 매칭의 결과를 나타내는 특수변수

* `$&` 매치하는 문자열 전체
* `$`` (Grave Accent) 매치하는 부분보다 앞에 있는 문자열
* `$'` (Single Quotation) 매치하는 부분보다 뒤에 있는 문자열
* `$1, $2, $3 ...` 첫 번째, 두 번째 그룹에 매치하는 문자열
* `$+` 마지막 그룹에 매치하는 문자열

### 매칭 연습
``` bash
$String Don't be afraid, when Things Go wrong, Just be strong!
$String =~ /Just/;
```
- `$`` Don't be afraid, when Things Go wrong,
- `$&` Just
- `$'` be Strong!

``` bash
$String =~ /,(.+),(.+)!/;
```
- `$&` , when Things Go wrong, Just be Strong !
- `$1` when Things Go wrong -> (.+)
- `$2` Just be Strong -> (.+)
- `$+` Just be Strong
