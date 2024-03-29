#!/usr/bin/env python
# coding: utf-8

# # 반복문

# 특정 명령문을 반복<font size="2">iteration</font> 실행하는 명령문인 
# **반복문**<font size='2'>iteration</font>을 소개한다.
# 파이썬은 세 종류의 반복문을 제공한다. 
# 
# - `for` 반복문
# - `while` 반복문
# - 재귀
# 
# `for` 반복문은 {numref}`%s절 <sec:for_loop>` 에서 간단한 활용법을 살펴보았다.
# 여기서는 `while` 반복문을 보다 자세히 소개하며,
# 재귀는 {numref}`%s장 <ch:recursion>`에서 다룬다.
# 앞으로 문자열, 리스트, 튜플, 사전 등 모음 자료형을 소개할 때
# `for` 반복문과 `while` 반복문의 보다 다양한 활용법을 보게 될 것이다.

# **슬라이드**
# 
# 본문 내용을 요약한 [슬라이드](https://github.com/codingalzi/pybook/raw/master/slides/slides-iterations.pdf)를 
# 다운로드할 수 있다.

# (sec:variable_reassignment)=
# ## 변수 재할당/업데이트

# `while` 반복문의 작동 과정을 이해하려면 먼저 변수가 가리키는 값을 변경하는 변수 재할당과
# 변수 업데이트를 이해해야 한다. 
# 
# **변수 재할당**
# 
# 변수 재할당은
# 변수가 가리키는 값을 변경하는 것이다.
# 예를 들어 아래 코드는 변수 `x`가 가리키는 값을 5에서 7로 재할당한다.

# In[1]:


x = 5
y = x
x = 7


# 반면에 변수 `y`는 계속해서 5를 가리킨다.
# 실제로 `x + y`는 12로 계산된다.

# In[2]:


Z = x + y
print(Z)


# `y = x` 가 실행될 당시에 `x`가 5를 가리키고 있었기 때문에
# `y` 또한 5를 가리키도록 지정되었다.
# 하지만 이후에 `x`가 가리키는 값을 변경해도 `y`에게는 전혀 영향을 주지 않는다.
# 메모리 상에서의 변화를 [PythonTutor: 변수 재할당](https://pythontutor.com/visualize.html#code=x%20%3D%205%0Ay%20%3D%20x%0Ax%20%3D%207%0Az%20%3D%20x%20%2B%20y&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서 확인할 수 있다.

# **변수 업데이트**
# 
# 반복문의 핵심은 
# 변수가 가리키던 값을 이용하여 새로이 생성한 값을 다시 
# 동일한 변수에 재할당하는 것이며, 이를 
# **변수 업데이트**<font size="2">variable update</font>라 한다. 
# 대표적으로 아래와 같은 표현식이 반복문에 자주 사용된다.

# In[3]:


x = x + 1


# 위 할당문은 변수 `x`가 가리키던 값에 1을 더한 값을 다시 
# 변수 `x`에 할당하라고 명령한다. 
# 만약에 변수 `x` 가 0을 가리키고 있었다면 위 명령문이 반복 실행될 때마다
# `x`가 가리키는 값은 1, 2, 3, ... 등 계속해서 변한다.
# 반면에 아래 명령문은 변수 `x`가 가리키던 값을 
# 1만큼 줄여서 재할당한다.

# In[4]:


x = x - 1


# **변수 간편 업데이트**
# 
# `x = x+1`, `x = 2 * x` 등과 같은 간단한 변수 업데이트는 `x += 1`, `x *= 2` 등으로 
# 간편하게 나타낼 수 있다. 
# 
# | 활용 | 의미 |
# |:----------:|:----------:|
# |`x += 1` |`x = x + 1`|
# | `x -= 1` | `x = x - 1`|
# | `x *= 2` | `x = 2*x`|
# |`x /= 2`|`x = x / 2`|
# |`x **= 2`|`x = x**2`|
# |`x //= 2`|`x = x //2`|
# |`x %= 2`|`x = x % 2`|

# In[5]:


x = 5
x /= 2
print(x)


# ## `while` 반복문

# `while` 반복문의 형식은 다음과 같다.
# 함수, 조건문, `for` 반복문의 경우에서처럼
# 헤더는 콜론(`:`)으로 마무리하고 본문은 들여쓴다.
# 
# ```python
# while 논리식:
#     명령문
# ```

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/while-loop.png" style="width:250px"></div>

# 위 명령문의 실행은 아래 세 단계로 이루어진다.
# 
# 1. 헤더의 `논리식`의 참, 거짓 여부를 확인한다.
# 1. 헤더의 `논리식` 이 `False` 인 경우: `while` 반복문 전체를 건너 뛰고 다음 명령문을 실행한다.
# 1. 헤더의 `논리식` 이 `True` 인 경우: 
#     본문에 위치한 명령문을 실행한 후에 
#     다시 1단계로 이동한다.

# 아래 `while` 반복문은 `n` 이 0보다 큰 동안은 계속해서 `n`을 출력한 다음에
# 마지막에 '발사'를 추가로 출력한다. 단, `n`은 반복할 때마다 1씩 줄어든다.

# In[6]:


n = 3
while n > 0:
    print(n)
    n = n - 1

print("발사")


# 위 코드를 함수화하면 다음과 같이 하나의 매개변수를 이용하도록 할 수 있다.

# In[7]:


def countdown(n):
    while n > 0:     # n 이 0 보다 큰 경우
        print(n)
        n = n - 1
        
    print('발사!')    # 기저 조건: n 이 0 인 경우


# In[8]:


countdown(3)


# In[9]:


countdown(5)


# 참고로 위 코드를 `for` 반복문으로 구현하면 다음과 같다.

# In[10]:


def countdown_for(n):
    for n in range(n, 0, -1):
        print(n)
    
    print('발사!')


# In[11]:


countdown_for(3)


# ## 무한 반복

# 헤더의 조건을 나타내는 논리식이 계속해서 참이면 `while` 반복문이 무한정 반복되어 실행될 수 있다.
# 
# 예를 들어 다음 함수를 살펴보자.

# ```python
# def count_infinitely(n):
#     while n > 0:
#         print(n)
#         n = n + 1
# ```

# `count_infinitely(1)`을 호출하면 `while` 반복문이 무한 반복된다.
# 이유는 `n`이 무한정 커지기 때문이다.
# 이런 현상을 **무한 반복**<font size="2">infinite loop</font>라 한다.

# `while` 반복문으로 인해 무한 반복이 발생하는지 여부를
# 경우에 따라 판단하기 매우 어렵거나 불가능할 수 있다. 
# 여기서는 콜라츠 추측에 사용된 알고리즘을 이용하여
# 판단이 매우 어려운 경우를 소개한다.

# **콜라츠 추측과 무한 반복**

# 아래 함수를 인자 `n`과 함께 호출하면 `n`을 출력한 후에 짝수 또는 홀수인 경우에 따라 `n`의 값을 업데이트하는 과정을 반복한다.

# In[12]:


def collatz(n):
    while n != 1:
        print(n, end=" -> ")
        if n%2 == 0:          # 짝수인 경우
            n = n//2
        else:                 # 홀수인 경우
            n = n*3 + 1
            
    print(1)                  # 기저 조건


# In[13]:


collatz(3)


# In[14]:


collatz(7)


# In[15]:


collatz(111)


# **콜라츠 추측**<font size='2'>Collatz cojecture</font>은 
# 위 함수가 임의의 양의 정수 `n`에 대해 
# 항상 언젠가는 1을 출력하고 실행을 멈춘다는 가정이다.
# 그런데 `collatz()` 함수의 실행이 항상 멈춘다는 증명도,
# 멈추지 않는 경우가 있다는 증명도 아직 없다.
# 즉, 콜라츠 추측은 여전히 미해결 문제로 남아 있다.

# **무한루프와 `break` 명령문**

# 사용자로부터 `'중지'` 단어가 입력될 때 까지
# 단어를 입력 받는 프로그램은 다음과 같다.
# 
# ```python
# while True:
#     line = input('단어입력: ')
#     if line == '중지':
#         break
#     print(line)
# 
# print('종료합니다!')
# ```
# 
# `True` 는 항상 참이기에 위 `while` 반복문은 무한 반복을 유발하여
# 사용자로부터 계속해서 문장을 입력받는다.
# 하지만 입력된 문장이 '중지'가 되는 순간 `break` 명령문이 
# 실행되어 `while` 반복문을 벗어나게 된다.
# 
# 예를 들어, 위 코드를 실행한 후에 파이썬, 좋아요, 중지 를 차례대로 입력하면
# 아래 결과를 얻는다.
# 
# ```
# 단어입력: 파이썬
# 파이썬
# 단어입력: 좋아요
# 좋아요
# 단어입력: 중지
# 종료합니다!
# ```
# 
# 마지막 줄의 '종료합니다!' 는 `while` 반복문 밖에 위치한
# 코드 마지막 줄의 `print('종료합니다!')` 가 실행되었음을 확인해준다.
# 이와 같이 반복 횟수를 미리 지정할 수 없지만 
# 특별한 상황이 발생하면 무한 반복을 중지시켜야 할 때
# `while True`와 `break`를 함께 활용한다.

# :::{admonition} `while 1`
# :class: info
# 
# `while True` 대신에 `while 1`을 사용하곤 한다.
# 이유는 `while` 다음에는 논리식이 위치해야 하기에 `1`이 참으로 간주되기 때문이다. 
# :::

# ##  무한 반복 활용

# ### 게임 프로그래밍

# 무한 반복은 게임 프로그래밍에서 자주 사용된다.
# 게임 종료가 언제 이뤄지는가는 게임의 전개 과정에 의존하기에 미리 알 수 없다.
# 게임 사용자가 언제든지 게임을 그만 둘 수도 있다.
# 따라서 게임 진행 전체를 관장하는 코드는 기본적으로 `while True`로 시작하는 무한 반복을 활용한다.
# 
# 아래 코드는 게임 프로그램의 전형적인 무한 반복 활용을 보여준다.

# ```python
# # Run the game loop.
# while True:
#     # Check for events.
#     for event in pygame.event.get():
#         if event.type == QUIT:   # ESC 키 누르기
#             pygame.quit()
#             sys.exit()
#         if event.type == KEYDOWN:
#             # Change the keyboard variables.
#             if event.key == K_LEFT or event.key == K_a:
#                 moveRight = False
#                 moveLeft = True
#             if event.key == K_RIGHT or event.key == K_d:
#                 moveLeft = False
#                 moveRight = True
#                 ...
#  ```

# 위 코드에서 아래 명령문이 <kbd>ESC</kbd> 키를 누를 때 게임을 종료시키는 조건을 지정한다.

# ```python
# if event.type == QUIT:   # ESC 키 누르기
#     pygame.quit()
#     sys.exit()
# ```

# ### 제곱근 계산: 뉴튼 방법

# 무한 반복을 어떤 값의 근사치를 계산하는 데에 활용하곤 한다.
# 예를 들어, 제곱근을 계산하기 위해
# **뉴튼 방법**<font size="2">Newton's method</font>에 사용된 알고리즘을
# 무한 반복을 이용하여 구현할 수 있다.

# **점화식과 변수 업데이트**

# $a$ 의 제곱근 $\sqrt{a}$ 는 아래 점화식을 따르는 수열을 이용하여 구할 수 있다.
# 
# $$
# \begin{align*}
# x_0 &= a\\[1ex]
# x_{n+1} & = \frac{x_n + \frac{a}{x_n}}{2}
# \end{align*}
# $$
# 
# 점화식은 파이썬에서 아래와 같은 변수 업데이트로 구현한다.
# 
# ```python
# x = a
# x = (x + a/x) / 2
# ```

# **$\sqrt{2}$ 계산**

# $\sqrt{2}$ 를 뉴튼 방법으로 계산해보자.
# 먼저 넘파이 모듈의 `sqrt()` 함수로 계산된 결과를 확인한다.

# In[16]:


import numpy as np

np.sqrt(2)


# 이제 뉴튼 방법을 적용하기 위해 먼저 `a` 와 `x` 를 지정한다.

# In[17]:


a = 2
x = a


# 변수 업데이트를 한 번 해보자.

# In[18]:


x = (x + a/x) / 2
x


# 한 번 더 하자.

# In[19]:


x = (x + a/x) / 2
x


# 반복할 수록 점점 더 $\sqrt{2}$에 근접함을 볼 수 있다.

# In[20]:


x = (x + a/x) / 2
x


# In[21]:


x = (x + a/x) / 2
x


# In[22]:


x = (x + a/x) / 2
x


# `np.sqrt(2)`의 값과 소수점 이하 15 자리까지 값이 동일해졌다.
# 눈에 보이지 않지만 두 수는 여전히 오차를 갖는다.

# In[23]:


x == np.sqrt(2)


# **무한 반복문 활용**

# 그럼에도 불구하고 일반적으로 제곱근에 충분히 가까운 근사치를 구했다.
# 뉴튼 방법 알고리즘을 반복 적용할 수록 근사치의 정확도는 점점 더 올라간다.
# 즉, 아래 `while` 명령문을 실행하면 `x` 가 가리키는 값은 `a` 의 제곱근이 되거나
# 무한정 가까워진다.
# 
# ```python
# x = a
# while True:
#     x = (x + a/x) / 2                # x 업데이트
# ```

# 그런데 위 `while` 반복문은 무한 반복에 빠진다.
# 이를 방지하기 위한 제동장치가 필요하며 
# `(x + a/x) / 2`가 가리키는 값을 다른 변수 `y`에 할당하여
# `x` 와 `y` 의 차이가 없어질 때까지만
# `while` 반복문이 실행되도록 한다.
# 정리하면 임의의 수 `a`에 대해 아래 명령문을 반복 실행하여 제곱근의 근사치를 계산할 수 있다.
# 
# 1. `y = (x + a/x) / 2` 를 실행한다.
# 1. `x` 와 `y` 가 동일한 값을 가리키면 실행을 멈추고 `y`를 반환한다.
# 1. 그렇지 않으면 `x` 를 `y`의 값으로 업데이트한 후에 1단계로 돌아간다.
# 
# 즉, `np.sqrt()` 함수처럼 작동하는 제곱근 함수를 다음과 같이 정의할 수 있다.
# 
# ```python
# def my_sqrt(a):
#     x = a
#     while True:
#         y = (x + a/x) / 2
#         if x == y:                  # 등가이면 실행 중지
#             break
#         x = y                       # x 업데이트
#     return y
# ```

# 그런데 이렇게 해도 무한루프에 빠질 가능성이 높다.
# 이유는 아래 조건문에서 사용되는 두 부동소수점의 비교가
# 참이될 가능성이 높지 않기 때문이다.
# 
# ```python
# if x == y:
#     break
# ```
# 
# 일반적으로 두 부동소수점<font size="2">floating point</font>의 등가성을 
# 비교하는 일은 매우 조심해서 사용해야 한다.
# 예를 들어 아래와 기대와 다른 결과를 얻을 수 있기 때문이다.

# In[24]:


0.1 + 0.1 + 0.1 == 0.3


# 이에 대한 이유는 이 강의노트의 수준을 많이 벗어나기에 더 이상 설명하지 않는다.

# **오차 허용 한도**

# 부동소수점의 등가성 대신 보통은 두 수의 오차가 충분히 작으면
# 실행을 멈추도록 한다.
# 이 아이디어를 `my_sqrt()` 함수에 적용하면 다음과 같다.
# 
# - `abs()` 함수는 절댓값을 반환한다.
# - `epsilon`은 오차의 한도를 지정하는 역할을 수행하는 매개 변수이다. 
#     "엡실론" 이라고 읽으며 오차 한도를 나타내는 변수 이름으로 많이 사용된다.

# In[25]:


def my_sqrt(a, epsilon):
    x = a
    while True:
        y = (x + a/x) / 2
        if abs(x - y) < epsilon:    # 오차 범위 안이면 실행 중지
            break
        x = y                       # x 업데이트
    return y


# 오차 허용 한도를 0.0001로 지정하고 2의 제곱근을 구해보자.

# In[26]:


my_sqrt(2, 0.0001)


# 오차 허용 한도를 0.000001로 지정하면 보다 엄밀한 근사치를 얻는다.

# In[27]:


my_sqrt(2, 0.000001)


# ## 연습문제

# 참고: [(실습) 반복문](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-iterations.ipynb)
