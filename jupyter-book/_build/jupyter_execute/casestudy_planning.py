#!/usr/bin/env python
# coding: utf-8

# (case:guessing_numbers)=
# # 사례 연구: 프로그램 구상

# 특정 문제를 해결하는 프로그램을 구현하기 위해
# 먼저 해결 방법과 과정을 상세하게 묘사한 
# **알고리즘**<font size="2">algorithm</font>을 설계한다.
# 그런 다음 알고리즘을 프로그램으로 구현하기 위해 필요한 
# **프로그래밍 요소**와 요소들의 **논리적 배치**를 
# 구체적으로 구상하면서 구현한다. 
# 
# 여기서는 **수 알아맞히기** 게임을 구현하는 과정을
# 단계별로 확인하면서 프로그램 구상 및 구현 과정을 자세히 살펴본다.

# ## 수 알아맞히기 게임

# 하나의 수를 입력받는 방식으로 숨겨진 수 17을 맞히면
# `"맞았습니다"`를, 틀리면 `"틀렸습니다"`를 출력하는
# **수 알아맞히기** 게임을 다음과 같이 간단하게 구현할 수 있다.
# 수의 선택 범위를 좁혀주기 위해 1부터 100까지의로 제한한다는 
# 안내문을 표시한다.

# ```python
# secret = 17
# guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
# 
# if guess == secret:
#     print("맞았습니다!")
# else:
#     print("틀렸습니다!")
# 
# print("게임 종료!")
# ```

# 위 프로그램에 사용된 프로그래밍 요소는 다음과 같으며,
# 언급된 요소의 의미와 역할은 그리 어렵지 않게 파악할 수 있을 것이다.
# 
# - 변수 할당 
#     - `secret`: 숨겨진 수 지정
#     - `guess`: 입력값 지정
# - 함수 호출
#     - `input()`: 입력값 받기
#     - `int()`: `input()` 함수가 반환한 문자열을 정수로 변환
#     - `print()`: 정답 여부 및 게임 종료 확인 출력
# - `if` 조건문: 숨겨진 수를 맞혔는지 여부 출력

# :::{admonition} `input()` 함수
# :class: info
# 
# `input()` 함수는 사용자로부터 입력받은 값을 저장할 때 사용한다.
# 아래와 같이 `input()`을 입력하고 코드를 실행하면, 그 아래에 값을 입력하라는 창이 나온다. 
# 예를 들어 `Hello, python!`을 입력하고 엔터 키 <kbd>Enter</kbd>를 누르면 
# 입력한 내용이 그대로 출력된다.
# 
# ```python
# >>> input()
# Hello, Python!
# 'Hello, Python!'
# ```
# 
# 문자열을 `input()` 함수의 인자로 지정하여 입력할 사항에 대한 안내를 할 수 있다.
# 
# ```python
# >>> input_num = input("정수를 입력하세요 : ")
# 정수를 입력하세요 : 23
# >>> print("입력하신 정수는 " + input_num + "입니다.")
# 입력하신 정수는 23입니다.
# ```
# 
# `input()` 함수를 이용하여 입력받은 내용을 변수에 할당할 수 있다.
# 
# ```python
# >>> like = input()
# 파이썬 좋아!
# >>> print('진짜로 ' + like)
# 진짜로 파이썬 좋아!
# ```
# 
# 그런데 저장되는 값은 모두 문자열로 처리된다.
# 사용자가 숫자를 입력하더라도 마찬가지다.
# 
# ```python
# >>> num = input()
# 17
# >>> type(num)
# <class 'str'>
# ```
# 
# 따라서 입력받은 정수를 연산에 활용하려면 
# 먼저 `int()` 함수 또는 `float()` 함수를 이용하여 정수 또는 부동소수점으로 
# 자료형을 변환해야 한다. 
# 
# ```python
# >>> int(num) / 3
# 5.666666666666667
# ```
# :::

# ## 업그레이드 1편: `if-elif-else` 조건문

# 앞서 소개한 게임은 숨겨진 수에 대한 아무런 정보를 주지 않기 때문에 불공정하다.
# 공정성을 높이기 위해 두 수를 대상으로 크기 비교도 실행해서
# 참여자가 입력한 값이 너무 큰지 또는 너무 작은지 여부를 알려주도록 해보자.
# 
# 이를 위해 `else` 본문에 `guess` 와 `secret`의 크기를 비교하는 `if` 조건문을
# 추가한다.
# 또한 게임의 시작을 알리는문장도 시작과 함께 출력하도록 한다.

# ```python
# print("수 알아맞히기 게임에 환영합니다.")  # 게임 시작 안내
# 
# secret = 17
# guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
# 
# if guess == secret:
#     print("맞았습니다!")
# else:
#     if guess > secret:                   # 크기 비교
#         print("너무 커요!")
#     else:
#         print("너무 작아요!")
# 
# print("게임 종료!")
# ```

# 위 코드에는 `if` 조건문이 중첩으로 사용되었다.
# 하지만 자세히 보면
# `guess` 와 `secret` 이 가리키는 두 값이 같거나, 크거나, 그렇지 않을 때 등 
# 세 가지 경우를 다룬다.
# 이런 경우 아래와 같이 일반화된 조건문을 사용하는 것이 권장된다. 
# 이유는 아무래도 중첩 조건문은 코드 이해를 보다 어렵게 하기 때문이다.

# ```python
# print("수 알아맞히기 게임에 환영합니다.")
# 
# secret = 17
# guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
# 
# if guess == secret:
#     print("맞았습니다!")
# elif guess > secret:
#     print("너무 커요!")
# else:
#     print("너무 작아요!")
# 
# print("게임 종료!")
# ```

# ## 업그레이드 2편: `while` 반복문

# 게임의 공정성이 조금 개선되었지만 아직 부족하다.
# 예를 들어, 추측이 틀려도 게임이 바로 멈추기 때문에 참여자 입장에서는 조금 허무해질 수 있다.
# 이점을 보완하기 위해 참여자가 숨겨진 수를 맞힐 때까지 프로그램이 실행되도록 해보자.

# 참여자가 몇 번만에 문제를 맞힐지를 미리 알 수 없기에
# 특정 조건이 만족되는 한 동일 작업을 반복하도록 하는
# `while` 반복문을 사용한다.
# 요구되는 조건식과 본체 명령문은 아래 내용을 담아야 한다.
# 
# * 조건식: 참여자가 입력한 수가 정답과 다른지 여부 판단.
# 
#     ```python
#     guess != secret
#     ```
#     
# * 본체 명령문: 참여자로부터 새로운 수를 입력 받아 
#     정답 여부 또는 크기 비교 여부 전달.
# 
#     ```python
#     guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
# 
#     if guess == secret:
#         print("맞았습니다!")
#     elif guess > secret:
#         print("너무 커요!")
#     else:
#         print("너무 작아요!")
#     ```

# `while` 반복문의 본문이 최소한 한 번은 실행되도록 하기 위해
# 참여자로부터 값을 입력받기 전에 먼저 
# `guess = -1`로 지정한다.
# 음의 정수로 설정한 이유는 숨겨진 수가 1보다 큰 양수이기에
# `guess != secret` 이 참이되도록 하기 위함이다.
# 
# 업그레이드된 프로그램은 다음과 같다.

# ```python
# print("수 알아맞히기 게임에 환영합니다.")
# 
# secret = 17
# guess = -1   # 이어지는 while 반복문이 최소 한 번은 실행되도록 함
# 
# while guess != secret:
#     guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
#     if guess == secret:
#         print("맞았습니다!")
#     elif guess > secret:
#         print("너무 커요!")
#     else:
#         print("너무 작아요!")
# 
# print("게임 종료!")
# ```

# ## 업그레이드 3편: `random` 모듈

# 앞서 개선한 코드는 참여자가 숨겨진 값을 맞출 수 있도록 유도한다.
# 그런데 숨겨진 수가 17로 고정되었기 때문에 한 번만 할 수 있는 게임이다.
# 게임을 보다 흥미롭게 만들기 위해 게임이 실행될 때마다 숨겨진 수가
# 달라지도록 해보자.

# 임의의 정수를 생성하기 위해 `random` 모듈의 `randint()` 함수를 이용한다.
# `randint()` 함수는 인자로 지정된 두 정수를 양끝으로 갖는 구간에서
# 무작위로 값을 지정하여 반환한다.
# 예를 들어, 1부터 100까지의 정수 중에서 임의의 값을 선택하려면
# `randint(1, 100)` 을 호출한다.

# ```python
# >>> from random import randint
# >>> randint(1, 100)
# 69
# >>> randint(1, 100)
# 36
# ```

# :::{admonition} `random` 모듈
# :class: info
# 
# `random` 모듈은 무작위 수 생성과 관련된 다양한 함수를 포함한다.
# 간단한 예제는  [random 모듈 사용법](https://www.daleseo.com/python-random/)을
# 참고한다.
# :::

# 게임이 시작할 때마다 숨겨진 수를 임의로 지정하기 위해 
# `secret` 변수가 `randint()` 함수가 생성하는 임이의 수로 지정할 수 있다.
# 
# ```python
# secret = randint(1, 100)
# ```
# 
# 위 코드를 추가해서 업그레이든 프로그램은 다음과 같다.

# ```python
# from random import randint  # 모듈 불러오기를 맨 먼저 실행
# 
# print("수 알아맞히기 게임에 환영합니다.")
# 
# secret = randint(1,100)     # 1부터 100까지의 수 중에서 무작위로 선택
# guess = -1
# 
# while guess != secret:
#     guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
#     if guess == secret:
#         print("맞았습니다!")
#     elif guess > secret:
#         print("너무 커요!")
#     else:
#         print("너무 작아요!")
# 
# print("게임 종료!")
# ```

# ## 업그레이드 4편: `break` 명령문

# 숨겨진 수를 맞히지 못하더라도 참여자가 언제나 게임을 종료하게 만들 수 있게 해보자.
# 예를 들어 사용자가 숫자 0을 입력하면
# `while` 반복문의 실행을 바로 멈추게 하기 위해 `break` 명령문을 이용할 수 있다.
# 
# `guess` 가 가리키는 입력값이 업데이트된 후 바로 입력값이 0인지 여부를 바로 확인하여
# 참이면 `break` 명령문을 실행한다. 
# 
# ```python
# if guess == 0:
#     break
# ```
# 
# `break` 명령문은 현재 실행되고 있는 `while` 반복문을 바로 종료시키고
# 이어지는 명령문으로 넘어가도록 한다.
# 새롭게 업그레이드된 프로그램은 다음과 같다.

# ```python
# from random import randint  # 모듈 불러오기를 맨 먼저 실행
# 
# print("수 알아맞히기 게임에 환영합니다.")
# 
# secret = randint(1,100)     # 1부터 100까지의 수 중에서 무작위로 선택
# guess = -1
# 
# while guess != secret:
#     guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
# 
#     if guess == 0:          # 0이 입력되면 바로 종료
#         break
#         
#     if guess == secret:
#         print("맞았습니다!")
#     elif guess > secret:
#         print("너무 커요!")
#     else:
#         print("너무 작아요!")
# 
# print("게임 종료!")
# ```

# :::{admonition} `break` 와 `for` 반복문
# :class: info
# 
# `break` 명령문은 `for` 반복문과도 함께 동일한 기능으로 사용될 수 있다.
# 예를 들어 아래 코드를 실행하면 1과 2만 출력한 후에 
# `for` 반복문의 실행이 종료되고 다음 명령문으로 진행한다.
# 
# ```python
# for num in [1, 2, 3, 4, 5]:
#     if num == 3:
#         break
#     print(num)
# 
# print("num =", num, "에서 멈췄습니다.")    
# ```
# 
# ```python
# 1
# 2
# num = 3 에서 멈췄습니다.
# ```
# :::

# ## 프로그램 오류와 디버깅

# 변수 이름으로 `class` 등의 지정어를 사용하거나, `odd~job` 또는 `US$`처럼 
# 허용되지 않은 기호를 포함하는 경우에 파이썬 실행기는 
# **오류**<font size="2">error</font>를 발생시키며 곧바로 프로그램의 실행을 멈춘다.
# 예를 들어, 아래와 같이 변수 이름에 공백을 사용하여 실행한 결과를 확인해 보자.
# 
# ```python
# >>> bad name = 5
#   File "<stdin>", line 1
#     bad name = 5
#         ^
# SyntaxError: invalid syntax
# ```    
# 
# 오류가 발생하면 오류의 원인을 찾아 해결해야 한다.
# 이렇게 프로그램의 오류를 찾아 해결하는 과정을 **디버깅**(debugging)이라 부른다.
# 
# 프로그램의 오류는 크게 세 가지 유형으로 나뉜다.

# **구문 오류**

# 변수의 이름을 잘못 지정하면 `SyntaxError: invalid syntax`와 
# 같은 **구문 오류**<font size="2">syntax error</font>가 발생한다.
# 구문 오류는 실행기가 프로그램을 실행하기 전에 일종의 문법 검사를 통해 찾아낸다.

# **런타임 오류**

# **런타임 오류**<font size="2">runtime error</font>는 
# 프로그램이 실행되는 중간에 발생하는 오류이다.
# 프로그램 실행 중간에 예외 상황을 발생시키는 오류라는 의미에서 런타임 오류를 
# **예외**<font size="2">exception</font>라고 부르기도 한다.
# 런타임 오류는 다양한 경우에 발생한다.
# 여기서는 두 가지 경우를 살펴본다.

# ::::{prf:example} ZeroDivisionError
# :label: zerodivision
# 
# 런타임 에러의 대표적인 예는 **0으로 나누기 오류**이다.
# 
# ```python
# >>> num = 0
# >>> print(3/num)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# ```
# 
# `ZeroDivisionError` 라고 표시되는데,
# 이는 0으로 나눗셈을 시도하는 경우 발생한다. 
# `3/num`은 문법적으로 전혀 문제가 없지만 실제 계산 중에 `num`에 할당된 값이 0이라는 것으로 확인되어
# 오류가 발생한다.
# ::::

# ::::{prf:example} NameError
# :label: nameerror
# 
# 아래 코드를 실행하면 'a_number' 라는 이름이 선언되어 있지 않기 때문에 문제가 발생한다.
# 
# ```python
# >>> a_Number = 327.68
# >>> b = a_number * 3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a_number' is not defined
# ```
# 
# 자세히 살펴보면 'a_number'와 'a_Number' 둘 중에 하나는 오타임을 알 수 있다.
# ::::

# **의미 오류**

# 프로그램 실행은 잘 되지만 원하는 결과를 가져오지 못한다면 프로그램
# 어딘가에 논리적 오류가 존재한다는 의미이다.
# 이와같은 오류를 
# **의미 오류**<font size="2">semantic error</font>라 부르며,
# 발생원인은 다양하며,
# 프로그램이 정상적으로 작동하기 때문에 구문 오류나 런타임 오류와는 다르게
# 오류의 원인을 바로 확인하기 어려울 수 있다.
# 
# 수학 문제를 풀다가 계산실수를 하거나, 기호를 다르게 적거나, 
# 문제를 잘못 이해했거나 해서
# 풀 수 있었던 문제를 틀렸던 경험이 있을 것이다.
# 프로그래밍 과정에서도 유사한 실수를 수없이 하게 된다.
# 예를 들어, 아래 프로그램은 두 배 계산 대신에 제곱 계산을 하는 실수를 보여준다.

# In[1]:


num = 3
doubleNum = num ** 2

print("입력한 값", num, "의 두 배는", doubleNum, "입니다.")


# 두 배하려면 `num * 2`를 사용했어야 하는데 실수로 `num ** 2`를 사용하여서
# 결과적으로 입력한 값의 제곱을 계산하게 된다.
# 수천, 수만 줄로 이루어진 프로그램에서 이런 형식의 오류의 원인을 찾는 일은
# 경우에 따라 모래사장에서 바늘찾기처럼 매우 어렵거나 불가능할 수 있다.

# :::{admonition} `print()` 함수의 인자
# :class: info
# 
# `print()` 함수가 여러 개의 인자를 받으면
# 모든 인자를 한 줄에 차례대로 출력한다.
# 인자들 사이는 스페이스 여백으로 구분한다.
# `print()` 에 대해서는 {numref}`%s절 <sec:keyword-arguments>`에서
# 보다 자세히 설명한다.
# :::

# ## 업그레이드 5편: `try-except`, `continue` 명령문

# 정수가 아닌 값을 입력하면 오류가 발생하면서 게임 자체의 실행이 멈춘다.
# 이유는 아래 할당문에서 사용된 `int()` 함수가 정수 모양의 문자열만
# 형변환할 수 있기 때문이다.
# 
# ```python
# guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
# ```
# 
# 그런데 이렇게 특정 명령문의 실행 과정에서 오류가 발생하면
# 전체 프로그램을 멈추게 하는 대신
# 다른 지정된 명령문을 실행하게 할 수 있다.
# 
# 이를 위해 `try-except` 라는 
# **예외 처리**<font size="2">exception handlig</font> 명령문을 이용한다.
# 사용법은 오류가 발생할 수 있는 명령문을 `try` 와 `except` 키워드로 감싼다.
# 예를 들어, 아래 코드를 실행할 때 
# 참여자가 정수가 아닌 다른 값을 입력하면 
# 오류가 발생하도록 하는 대신
# `정수를 입력하세요.` 라는 문장이 출력된다.

# ```python
# try:
#     guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
# except:
#     print("정수를 입력하세요.")
# ```

# 아래 코드는 `except` 부분에 에 `continue` 를 대신 사용한다. 
# `continue` 는 현재 실행중인 `while` 반복문을
# 다시 시작하라고 지정할 때 사용하는 명령문이다.
# 따라서 정수가 아닌 값이 입력되면 `while` 명령문의 처음으로 돌아가서 
# 게임 참여자에게 입력값을 다시 요구한다.

# ```python
# from random import randint
# 
# print("수 알아맞히기 게임에 환영합니다.")
# 
# secret = randint(1,100)
# guess = -1
# 
# while guess != secret:
#     
#     try:  # 정수 입력이 아닌 경우 대처             
#         guess = int(input("1부터 100 사이의 정수 하나를 입력하세요: "))
#     except: 
#         continue  # while 반복문의 처음으로 돌아가기
# 
#     if guess == 0:
#         break
# 
#     if guess == secret:
#         print("맞았습니다!")
#     elif guess > secret:
#         print("너무 커요!")
#     else:
#         print("너무 작아요!")
# 
# print("게임 종료!")
# ```

# :::{admonition} `continue` 와 `for` 반복문
# :class: info
# 
# `continue` 명령문은 `for` 반복문과 사용되면
# 현재의 경우를 무시하고 다음 경우로 이동하라는 기능으로 작동한다.
# 예를 들어 아래 코드를 실행하면 `num` 변수가 홀수를 가리킬 때는 무시되어 
# 결국 짝수만 출력한다.
# 
# ```python
# for num in [1, 2, 3, 4, 5]:
#     if num != 0:
#         continue
#     print(num)
# 
# print("홀수는 무시했습니다.")    
# ```
# 
# ```python
# 2
# 4
# 홀수는 무시했습니다.
# ```
# :::

# ## 연습문제

# 참고: [(실습) 사례 연구: 프로그램 구상](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-casestudy_planning.ipynb)
