import streamlit as st
import pygame
import random
import time

# Pygame 초기화
pygame.init()

# 게임 화면 크기
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 캐릭터 클래스
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 50
        self.width = 40
        self.height = 40
        self.speed = 5

    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# 계단 클래스
class Stair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 20

    def move(self):
        self.y += 5

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# 게임 루프
def game_loop():
    player = Player()
    stairs = []
    score = 0
    game_over = False
    clock = pygame.time.Clock()

    while not game_over:
        screen.fill(WHITE)

        # 계단 랜덤 생성
        if random.randint(1, 20) == 1:  # 일정 확률로 계단 생성
            stair_x = random.randint(0, SCREEN_WIDTH - 60)
            stairs.append(Stair(stair_x, 0))

        # 계단 이동
        for stair in stairs:
            stair.move()
            stair.draw()

            # 충돌 확인
            if (player.x < stair.x + stair.width and
                player.x + player.width > stair.x and
                player.y < stair.y + stair.height and
                player.y + player.height > stair.y):
                game_over = True

        # 플레이어 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed)

        player.draw()

        # 점수 증가
        score += 1

        # 게임 종료 텍스트
        if game_over:
            font = pygame.font.SysFont(None, 55)
            text = font.render("Game Over!", True, BLACK)
            screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 30))
        
        # 점수 출력
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)  # FPS 설정

        # 잠시 대기
        time.sleep(0.1)

# Streamlit을 사용하여 게임 실행
def main():
    st.title("무한의 계단")
    start_game = st.button("게임 시작")
    
    if start_game:
        st.write("게임을 시작합니다!")
        game_loop()

if __name__ == "__main__":
    main()
