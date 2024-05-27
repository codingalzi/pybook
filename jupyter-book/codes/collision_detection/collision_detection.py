import math
import turtle

## 스프라이트 클래스 선언


class Sprite():

    ## 생성자: 스프라이트의 위치, 가로/세로 크기, 이미지 지정
    def __init__(self, x, y, width, height, image):
        """
        x: x-좌표
        y: y-좌표
        width: 가로 크기
        height: 세로 크기
        image: 모양
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    ## 인스턴스 메서드

    # 지정된 위치로 스프라이트 이동 후 도장 찍기
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    # 충돌 감지 방법 1: 두 객체의 중심이 일치할 때
    def is_overlapping_collision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    # 충돌 감지 방법 2: 두 객체 사이의 거리가 두 객체 너비의 평균값 보다 작을 때
    def is_distance_collision(self, other):
        distance = (((self.x - other.x)**2) + ((self.y - other.y)**2))**0.5
        if distance < (self.width + other.width) / 2.0:
            return True
        else:
            return False

    # 충돌 감지 방법 3: 객체를 둘러썬 경계상자가 겹칠 때
    # aabb: Axis Aligned Bounding Box
    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width +
                                                           other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height +
                                                           other.height)
        return (x_collision and y_collision)


## 게임 세팅

# 도화지 객체 설정
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Collision Detection")
wn.tracer(0)  # 도화지 내용 한 번에 업데이트 되도록 지정

# 거북이 객체 설정
pen = turtle.Turtle()
pen.speed(0)  # 가장 빠르게 이동
pen.hideturtle()  # 숨김

# 스프라이트 이미지 7개 등록
shapes = [
    "wizard.gif", "goblin.gif", "pacman.gif", "cherry.gif", "bar.gif",
    "ball.gif", "x.gif"
]

for shape in shapes:
    wn.register_shape(shape)

## 스프라이트 생성

wizard = Sprite(-128, 200, 128, 128, "wizard.gif")
goblin = Sprite(128, 200, 108, 128, "goblin.gif")

pacman = Sprite(-128, 0, 128, 128, "pacman.gif")
cherry = Sprite(128, 0, 128, 128, "cherry.gif")

bar = Sprite(0, -400, 128, 24, "bar.gif")
ball = Sprite(0, -200, 32, 32, "ball.gif")

# 스프라이트 리스트
sprites = [wizard, goblin, cherry, pacman, bar, ball]

## 이벤트 처리

# 마우스로 선택된 스프라이트 기억 장치
# 마우스가 눌린 위치 정보를 활용하는 이벤트 처리 함수 fxn()에 의해 지정됨
sprite_idx = None


# (콜백) 이동 화살표 키 이벤트 처리 함수
def move_left():
    sprites[sprite_idx].x -= 32

def move_right():
    sprites[sprite_idx].x += 32

def move_up():
    sprites[sprite_idx].y += 24

def move_down():
    sprites[sprite_idx].y -= 24

# (콜백) 마우스로 선택된 스프라이트 인덱스 지정
def sprite_idx_fn(x_, y_):
    global sprite_idx  # 전역 변수 활용

    for idx, sprite in enumerate(sprites):
        distance = (((sprite.x - x_)**2) + ((sprite.y - y_)**2))**0.5
        if distance < sprite.width / 2:
            sprite_idx = idx


# 마우스 클릭 감지 후 콜백 함수 바로 실행
wn.listen()
wn.onclick(sprite_idx_fn)

# 이벤트 처리: 선택된 이동 화살표에 따른 이벤트 지정
turtle.listen()
turtle.onkey(move_left, "Left")  # 왼쪽 방향 화살표 입력
turtle.onkey(move_right, "Right")  # 오른쪽 방향 화살표 입력
turtle.onkey(move_up, "Up")  # 위쪽 방향 화살표 입력
turtle.onkey(move_down, "Down")  # 아래쪽 방향 화살표 입력

## 게임 진행

while True:

    # 각 스프라이트 위치 이동 및 도장 찍기
    for sprite in sprites:
        sprite.render(pen)

    wn.update()  # 도화지 내용 업데이트
    pen.clear()  # 스프라이트 이동흔적 삭제

    # 충돌 여부 확인
    if wizard.is_overlapping_collision(goblin):
        wizard.image = "x.gif"

    if pacman.is_distance_collision(cherry):
        cherry.image = "x.gif"

    if bar.is_aabb_collision(ball):
        ball.image = "x.gif"

wn.mainloop()
