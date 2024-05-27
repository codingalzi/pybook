import math

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
