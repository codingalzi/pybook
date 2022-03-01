#!/usr/bin/env python
# coding: utf-8

# # 프로그래밍 개발 환경

# 파이썬으로 프로그래밍을 하려면 적절한 개발환경을 준비해야 하며,
# 오프라인과 온라인 두 가지 방식이 있다.
# 프로그래밍이 처음이라면 먼저 온라인 방식을 사용해서 
# 파이썬과 어느 정도 친숙해진 다음에 오프라인 방식을 시도할 것을 추천한다.

# ## 오프라인 개발 환경

# ### 파이썬 설치

# 파이썬 개발환경 설치가 처음이라면 
# 데이터 분석 관련 중요 라이브러리,
# 스파이더 편집기, 
# 주피터 노트북을 모두 포함하는 
# [아나콘다<font size = "2">Anaconda</font>](https://www.anaconda.com/products/individual) 패키지를 설치할 것을 추천한다.

# ### 주피터 노트북

# 간단한 파이썬 코드 설명은 **대화식 프로그래밍**<font size="2">interactive programming</font>을
# 지원하는 **주피터 노트북**<font size="2">Jupyter notebook</font>을 사용한다.
# 주피터 노트북이 지원하는 대화식 프로그래밍은 IPython 콘솔 기능을 이용한다.
# IPython 콘솔의 대화식 프로그래밍은 아래 모양을 갖는다.
# 
# ```python
# In [1]: print('Hello world')
# Hello world
# ```
# 
# 반면에 파이썬 자체가 지원하는 콘솔은 다음 모양의 대화식 코딩을 지원한다.
# 
# ```python
# >>> print('Hello world')
# Hello world
# ```
# 
# IPython 콘솔은 파이썬 프로그래밍 이외에 보다 다양한 기능을 지원하며
# 앞으로 필요한 기능을 하나씩 언급할 것이다.

# :::{admonition} 아나콘다 설치와 주피터 노트북 사용법
# :class: tip
# 
# [유튜버 나도코딩의 동영상](https://www.youtube.com/watch?v=dJfq-eCi7KI&t=2298s)에서 아나콘다의 설치 과정과
# 주피터 노트북의 기초 사용법에 대한 상세한 설명을 들을 수 있다.
# :::

# ### 통합 개발 환경(IDE)

# 보다 복잡한 파이썬 프로그래밍을 위해서는 코드 편집과 실행, 디버깅 등 
# 프로그래밍 관련 모든 작업을 통합해서 지원하는 
# 통합 개발 환경을 사용한다.
# 일명 **IDE**<font size="2">Interactive Development Environment</font>라고 불리는
# 통합 개발 환경을 지원하는 대표적인 앱은 다음과 같다.
# 
# * [스파이더<font size="2">Spyder</font>](https://www.spyderide.org/): 아나콘다 패키지에 포함됨.
# * [파이참<font size="2">Pycharm</font>](https://www.jetbrains.com/pycharm): 가장 인기있는 상용 프로그램.
#     Pro 와 Community 두 버전을 지원하며 입문자는 무료 버전인 Community 추천.
# * [비주얼 스튜디오 코드<font size="2">Visual Studio Code</font>](https://code.visualstudio.com/docs/languages/python): 
#     마이크로소프트에서 지원하며, 현재 가장 인기 있는 무료 프로그램.
#     파이썬 뿐만 아니라 거의 모든 프로그래밍 언어를 위한 통합 개발 환경 지원.
# * [아톰<font size="2">Atom</font>](https://atom.io): 소스코드 저장소로 가장 유명한 
#     [깃허브<font size="2">GitHub</font>](https://github.com/)에서 개발한 IDE. 
#     거의 모든 프로그래밍 언어 지원.
# 
# 여기서는 일명 **VS Code**라 불리는 
# 비주얼 스튜디오 코드를 사용할 것을 추천한다.

# :::{admonition} VS Code 설치와 사용법
# :class: tip
# 
# [생활코딩의 동영상](https://www.youtube.com/watch?v=K8qVH8V0VvY&t=337s)에서 
# VS Code의 설치와 사용법에 대한 상세한 설명을 들을 수 있다.
# :::

# ## 온라인 개발 환경

# 파이썬 개발 환경을 지원하는 많은 인터넷 사이트가 존재한다.
# 여기서는 **레플릿**과 **구글 코랩**을 추천한다.

# ### 레플릿

# [레플릿<font size="2">repl.it</font>](https://replit.com/)은 웹브라우저를 사용하여 
# 온라인 상에서 코드를 작성하여 프로그램을 구현할 수 있는
# 기능을 지원하는 웹사이트이며
# 파이썬, C, C++, C#, 자바 등을 포함해 50여개 이상의 프로그래밍 언어를 지원한다. 
# 
# 회원가입 후 로그인하면 바로 선택한 언어의 통합 개발 환경을 사용할 수 있다.
# 회원가입 시 구글 계정을 이용하면 나중에 구글 코랩 사이트와 연동할 때 좀 더 편리할 수 있다.
# 무료 회원인 경우 일부 제한이 있지만 프로그래밍 입문에 필요한 요소는 모두 제공된다.

# :::{admonition} 레플릿 사용법
# :class: tip
# 
# [유튜버 알파쿠의 동영상](https://www.youtube.com/watch?v=YVHX62wX_zg)에서 레플릿 사이트의 사용법에 대한 상세한 설명을 들을 수 있다.
# :::

# ### 구글 코랩

# [구글 코랩<font size="2">Google Colab</font>](https://colab.research.google.com/?hl=ko)은 
# 구글에서 제공하는 파이썬 전용 온라인 주피터 노트북이다.
# 웹브라우저를 이용하여 어떤 준비 없이 바로 파이썬 프로그래밍을 시작할 수 있다.

# :::{admonition} 구글 코랩 사용법
# :class: tip
# 
# 구글 코랩의 사용법은 
# [유튜버 봉수골 개발자 이선비의 동영상](https://www.youtube.com/watch?v=91E0qenm7W4)을 참고한다.
# 그리고 입문용은 아니지만 구글 코랩만이 지원하는 유용한 고급 기능을 
# [TensorFlow 팀의 동영상](https://www.youtube.com/watch?v=rNgswRZ2C1Y)에서 확인할 수 있다.
# :::

# ## 온&middot;오프라인 개발 환경 설정 안내

# 지금까지 소개한 다양한 앱과 웹사이트의 설치 및 사용법을 
# {ref}`ch:environment_setting`에서 캡처 이미지를 활용한 문서 형식으로 
# 자세히 설명한다.
