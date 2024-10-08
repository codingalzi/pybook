#!/usr/bin/env python
# coding: utf-8

# (ch:environment_setting)=
# # 온&middot;오프라인 개발 환경 설정 안내

# 파이썬 프로그래밍을 하려면 개발환경을 준비해야 한다.
# 여기서는 다음 중 하나의 방법을 선택하여 개발 환경을 구축할 것을 추천한다.
# 
# * 오프라인 개발 환경
#     * 아나콘다 설치 &rarr; 스파이더 사용
#     * 아나콘다 설치 &rarr; 주피터 노트북 사용
#     * 아나콘다 & VS Code 설치 &rarr; VS Code 사용
# 
# * 온라인 개발 환경
#     * 레플릿 사용
#     * 구글 코랩 사용

# (sec:anaconda_install)=
# ## 아나콘다 설치

# 아나콘다를 설치하려면 먼저 설치 프로그램을 다운로드해야 한다. 

# * [아나콘다 사이트](https://www.anaconda.com/products/individual)에 접속한 후
#     화면 오른쪽에 있는 Download 버튼을 눌러 아나콘다 설치 프로그램을 다운로드한다. 
#     아나콘다 사이트에 접속하면, 접속자의 운영체제를 확인하여 설치 가능한 파이썬 최신 버전을 보여준다. 
#     이 글을 작성하는 시점에는 파이썬 3.9가 최신 버전이다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda01.png" style="width:800px;">
# </div>

# * 다운로드한 Anaconda3-Window_64.exe 실행파일을 더블 클릭하여 설치를 시작한다. 설치화면이 아래와 같이 나오면 Next 버튼을 눌러서 다음 화면으로 넘어간다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda02.png" style="width:400px;">
# </div>

# * 약관이 나타나면, 동의하는 I Agree 버튼을 눌러 다음 화면으로 넘어간다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda03.png" style="width:400px;">
# </div>

# * 사용자 환경에 따라 권한을 설정한 다음, Next 버튼을 눌러 다음 화면으로 넘어간다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda04.png" style="width:400px;">
# </div>

# * 설치 경로를 지정한다.
#     특별한 경우가 아니라면, 기본 경로를 그대로 두고 
#     Next 버튼을 눌러 다음 화면으로 넘어간다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda05.png" style="width:400px;">
# </div>

# * 아나콘다를 기본 파이썬으로 설정하고, Install 버튼을 눌러 설치를 진행한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda06.png" style="width:400px;">
# </div>

# * 설치 시간은 보통 1~3분 정도 걸리며, 컴퓨터 환경에 따라 5분이상 소요되기도 한다. 설치 완료가 되면, Next를 눌러 다음 화면으로 넘어간다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda08.png" style="width:400px;">
# </div>

# 그 다음 화면도 Next 버튼을 누르면 된다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda09.png" style="width:400px;">
# </div>

# * Finish 버튼을 눌러 설치를 완료한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/anaconda10.png" style="width:400px;">
# </div>

# ## 스파이더 실행법

# 스파이더는 과학프로그래밍을 위한 IDE로, 아나콘다를 설치하면 스파이더를 사용할 수 있다.

# * 윈도우키를 누른 후 스파이더를 선택한다. 시작까지 오랜 시간이 걸릴 수도 있다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/spyder01.png" style="width:400px;">
# </div>

# * 스파이더는 편집기 기능과 터미널 기능을 동시에 제공한다. 아래 화면에서 왼쪽이 편집기 부분(빨간색)이고, 오른쪽 아래가 터미널 부분(녹색)이다. 편집기 부분은 긴 코드를 작성할 때 사용하고, 터미널 부분은 짧은 코드를 테스트할 때 사용한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/spyder05.png" style="width:800px;">
# </div>

# 편집기에 `print('Hello, world')`라고 코드를 작성한 다음 실행 버튼(노란색)<font size = "2">또는 F5</font>을 눌러보자. 
# 실행 버튼을 처음 누르면 아래와 같이 파이썬 인터프리터와 관련된 설정창이 뜬다. 설정 변경 없이 Run 버튼을 누르면 된다. 그러면 터미널에 `Hello, world`가 출력되는 것을 볼 수 있다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/spyder03.png" style="width:400px;">
# </div>

#  편집기 부분과 터미널 부분은 파이썬 인터프리터를 공유한다. 그래서 편집기 부분에 코드를 입력 후 실행하면, 터미널 부분에서도 편집기 부분에서 정의된 변수나 함수 등을 사용할 수 있다. 

# (sec:jupyter_notebook)=
# ## 주피터 노트북 실행법

# 주피터 노트북은 대화형 파이썬 인터프리터로, 웹브라우저에서 파이썬 코드를 작성하고 실행 결과를 바로 확인할 수 있다. 아나콘다를 설치하면 주피터 노트북을 사용할 수 있다. 

# * 윈도우 키를 누른 후 주피터 노트북을 선택한다.  

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/jupyter01.png" style="width:400px;">
# </div>

# '이 파일을 열 때 사용할 앱을 선택하세요.'라는 문구가 나온다면 사용하는 브라우저(예, Google Chrome 또는 Microsoft Edge 등)를 선택하면 된다. 그러면 주피터 노트북이 실행된다. 

# * 아래 화면에서 오른쪽 위에 있는 New를 선택한 다음 Python 3를 선택하여 새로운 파이썬 파일을 만들자.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/jupyter04.png" style="width:800px;">
# </div>

# * 새로운 파이썬 파일은 아래 화면과 같다. 코드셀(빨간색)에 `print('Hello, world')`라고 코드를 작성한 다음 실행버튼(노란색)<font size = "2">또는 shift+enter나 ctrl+enter</font>를 누르면, 코드셀 바로 아래(녹색) `Hello, world`가 출력되는 것을 볼 수 있다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/jupyter06.png" style="width:800px;">
# </div>

# (sec:vs_code)=
# ## 비주얼 스튜디오 코드 설치

# VS Code는 마이크로소프트에서 만든 소스 코드 에디터로 다양한 프로그래밍 언어를 지원하며 대부분의 OS에서 실행된다. 에디터는 들여쓰기나 코드 자동 완성, 문법 오류 감지 등 개발할 때 편리한 기능을 제공하기 때문에 개발 속도를 높이는 데 도움을 줄 수 있다.  

# VS Code를 설치하려면 먼저 설치 프로그램을 다운로드해야 한다.  
# * [비주얼 스튜디오 코드 사이트](https://code.visualstudio.com/)에 접속한 후
#     화면 왼쪽에 있는 Download 버튼을 눌러 사용하는 운영체제에 맞는
#     설치 프로그램을 다운로드한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode01.png" style="width:800px;">
# </div>

# * 다운로드한 VSCodeUserSetup.exe 실행파일을 더블 클릭하여 설치를 시작한다. 약관이 나타나면, 동의합니다를 선택하고, 다음을 눌러서 다음 화면으로 넘어간다.  

# * 설치 경로를 지정한다. 
#     특별한 경우가 아니면, 기본 경로를 그대로 두고 다음으로 넘어가면 된다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode02.png" style="width:400px;">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode03.png" style="width:400px;">
# </div>

# * 시작 메뉴에 비주얼 스튜디오 코드가 보이도록 하고 싶다면 다음을 누르고, 아니라면 시작 메뉴 폴더를 만들지 않음을 선택하고 다음을 눌러 다음으로 넘어가면 된다. 

# * 추가로 필요한 작업이 있다면, 선택하고 다음을 눌러 다음 화면으로 넘어가면 된다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode04.png" style="width:400px;">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode05.png" style="width:400px;">
# </div>

# * 아래 왼쪽 화면은 앞에서 선택한 항목들을 보여준다. 확인 후 설치를 눌러 설치를 진행한다.  

# * 설치 시간은 보통 1~3분 정도 걸리며, 컴퓨터 환경에 따라 5분이상 소요되기도 한다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode06.png" style="width:400px;">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode07.png" style="width:400px;">
# </div>

# * 종료 버튼을 눌러 설치를 완료한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode08.png" style="width:400px;">
# </div>

# * 이제 VS Code를 실행해보자. 윈도우 키를 누른 후 visual studio code를 선택하면 된다.  

# * VS Code에서 파이썬을 사용하기 위하여 확장<font size="2">Extensions</font>을 설치해야 한다. 아래 화면 왼쪽 아래에 있는 확장 아이콘(빨간색)<font size = "2">또는 ctrl + shift + x </font>을 클릭한 다음, python을 검색(노란색)한다. 그리고 아래(녹색) python과 python for VS Code를 install를 클릭하여 설치한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode11.png" style="width:800px;">
# </div>

# * 그 다음 작업영역에 폴더를 추가해야 한다. 우선 원하는 위치에 폴더를 하나 만든다(예, 바탕화면에 python이라는 이름의 폴더 생성). 그 다음 VS Code 메뉴 중 File 아래 Open Folder를 클릭한 다음, 생성한 폴더를 선택하여 연다.   

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode12.png" style="width:800px;">
# </div>

# * 폴더명 옆에 마우스를 가져가면 파일을 추가할 수 있는 아이콘(빨간색)이 생긴다. 이 아이콘을 누른 다음, 아래 만들어지는 영역(노란색)에 파이썬 파일명과 확장자(.py)를 입력한다. 아래 화면에서는 1.py 파일을 만들었다.   

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode13.png" style="width:500px;">
# </div>

# * 만든 파이썬 파일(1.py)은 아래 화면과 같다. 
#     편집기(빨간색)에 `print('Hello, world')`라고 코드를 작성한 다음 ctrl + F5를 누르면, 
#     아래 터미널에 `Hello, world`가 출력되는 것(노란색)을 볼 수 있다. 
# 
#     터미널에 `Hello, world`가 출력되지 않는다면, 파이썬 설치 경로가 제대로 입력되었는지 확인하자. 
#     VS Code에서 ctrl + shift + p를 누르면 뜨는 창에 Python: Select Interpreter를 선택한다. 
#     그 다음 열리는 창에 python이 설치된 경로를 적어준다. 
#     보통은 설치 경로를 입력하는 창 아래에 파이썬 설치 경로를 보여준다.  

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/vscode14.png" style="width:800px;">
# </div>

# (sec:replit)=
# ## 레플릿 사용법

# 레플릿은 온라인 IDE로 별도의 프로그램 설치 없이 파이썬을 사용할 수 있다. 사용 방법은 간단하다. 

# * [레플릿 사이트](https://replit.com/)에 접속한 후 
#     오른쪽 위의 Sign up을 눌러 회원가입을 하고, 로그인을 한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/replit01.png" style="width:800px;">
# </div>

# * 로그인하면 아래와 같은 화면이 나온다. 오른쪽 위의 + 버튼(빨간색)을 누르면, Create a repl 창이 나온다. 물론, 왼쪽 위의 햄버거 버튼(녹색)를 누른 다음 +Create 버튼을 눌러도 되고, 화면 아래에 있는 + Python(노란색)를 눌러도 된다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/replit02.png" style="width:800px;">
# </div>

# * Create a repl 창이 나오면, Template은 Python을 선택하고, 제목Title은 적당한 것으로 변경(예, 1)한 다음 오른쪽 아래에 보이는 +Create Repl 버튼을 누르면 된다.  

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/replit03.png" style="width:400px;">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/replit04.png" style="width:465px;">
# </div>

# * 그러면 아래와 같이 파이썬 파일이 만들어진다. 왼쪽 편집기(빨간색)에 `print('Hello, world')`라고 코드를 작성한 다음 실행버튼(노란색)<font size = "2"> 또는 ctrl + enter</font>를 누르면, 오른쪽 터미널에 `Hello, world`가 출력되는 것(녹색)을 볼 수 있다. 

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/replit05_r.png" style="width:800px;"></div>

# (sec:google_colab)=
# ## 구글 코랩 사용법

# 구글 코랩은 구글에서 제공하는 주피터 노트북이다. 레플릿과 마찬가지로 사용 방법은 간단하다.

# * 구글 https://www.google.com/ 에 접속한다. 그리고 구글 계정으로 로그인을 한다. 이때, 사용할 웹 브라우저는 크롬을 추천한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab01.png" style="width:800px;">
# </div>

# * 웹 브라우저에서 오른쪽 위를 보면 여러 개의 아이콘이 보인다. 그 중 세 번째에 있는 Google 앱 아이콘을 누른 다음 구글 드라이브에 접속한다.  
# 
# * 구글 드라이브 화면에서 왼쪽 위를 보면 새로 만들기 버튼(빨간색)이 있다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab02.png" style="width:300px; padding-right:20px">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab03.png" style="width:400px;">
# </div>

# * 새로 만들기 버튼을 누르면 아래와 같은 창이 뜬다. 이 창에서 연결할 앱 더보기를 선택한다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab04.png" style="width:500px;">
# </div>

# * 그러면 아래와 같은 창이 뜬다. 설치 가능한 앱 중 Colaboratory(빨간색)를 찾은 다음 클릭한다. 코랩을 검색(노란색)하여 찾는 것도 가능하다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab05.png" style="width:600px;">
# </div>

# * Colaboratory 창에서 설치 버튼을 눌러 설치를 시작한다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab06.png" style="width:600px;">
# </div>

# * 아래 왼쪽 화면처럼 권한을 요구할 수도 있다. 그러면 계속 버튼을 클릭한다.
# 
# * 다음으로 계정 선택 창이 나온다면, 사용할 구글 계정을 선택하면 된다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab07.png" style="width:400px;">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab08.png" style="width:300px;">
# </div>

# * 그러면 코랩 설치가 완료된다. 확인, 완료 등의 버튼을 눌러 모든 창을 닫아준다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab09.png" style="width:400px;">
# </div>

# * 다시 구글 드라이브로 와서 새로 만들기 버튼을 누른 다음, 목록에서 Google Colaboratory를 선택한다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab10.png" style="width:500px;">
# </div>

# * 그러면 아래와 같은 주피터 노트북이 만들어진다. 코드셀(빨간색)에 `print('Hello, world')`라고 코드를 작성한 다음 실행버튼(실행하고자 하는 코드셀 앞에 있는 동그라미 안의 삼각형)<font size = "2">또는 shift+enter나 ctrl+enter</font>를 누르면, 코드셀 바로 아래(노란색) `Hello, world`가 출력되는 것을 볼 수 있다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/colab11.png" style="width:800px;">
# </div>
