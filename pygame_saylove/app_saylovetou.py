
# coding=utf-8
import pygame
import random
import sys



HEIGHT ,WIDTH= 703,1254

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 32)
pygame.display.set_caption('这只是一个小游戏')


# 添加文本信息
def title(text, screen, scale, color=(0, 0, 0)):
    font = pygame.font.SysFont('SimHei', 27)
    textRender = font.render(text, True, color)
    # 鍒濆鍖栨枃鏈殑鍧愭爣
    screen.blit(textRender, (WIDTH / scale[0], HEIGHT / scale[1]))


# 按钮
def button(text, x, y, w, h, color, screen):
        pygame.draw.rect(screen, color, (x, y, w, h))
        font = pygame.font.SysFont('SimHei', 20)
        textRender = font.render(text, True, (255, 255, 255))
        textRect = textRender.get_rect()
        textRect.center = ((x+w/2), (y+h/2))
        screen.blit(textRender, textRect)


# 生成随机的位置坐标
def get_random_pos():
        x, y = random.randint(10, 600), random.randint(20, 500)
        return x, y


# 点击答应按钮后显示的页面
def show_like_interface(screen):
    screen.fill((255, 255, 255))
    # background1 = pygame.image.load(r'C:\Users\little\Desktop\hah\1.png').convert()
    # screen.blit(background1, (0, 0))
    background = pygame.image.load(r'C:\Users\little\Desktop\hah\321.png').convert()
    screen.blit(background, (0, 0))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    # 设置不同意按钮属性
    unlike_pos_x = 130
    unlike_pos_y = 375
    unlike_pos_width = 400
    unlike_pos_height = 85
    unlike_color = (115, 76, 243)
    # 设置同意按钮属性
    like_pos_x = 130
    like_pos_y = 280
    like_pos_width = 350
    like_pos_height = 85
    like_color = (115, 76, 243)

    running = True
    while running:
        #填充窗口
        screen.fill((255, 255, 255))
        # 添加背景图
        # background = pygame.image.load(r'C:\Users\little\Desktop\hah\321.png').convert()
        # screen.blit(background, (0, 0))
        # 获取鼠标坐标
        pos = pygame.mouse.get_pos()
        # 判断鼠标位置,不同意时,按钮不断变化
        if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
            while True:
                unlike_pos_x, unlike_pos_y = get_random_pos()
                if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
                    continue
                break

        # 设置标题及按钮文本信息
        title('1.你喜欢吃火锅嘛', screen, scale=[8, 3])
        button('A.当然拉', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen)
        button('B.不喜欢', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, unlike_color, screen)
        # 设置关闭选项属性
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 当鼠标点击同意按钮后,跳转结束页面
        if pos[0] < like_pos_x + like_pos_width + 5 and pos[0] > like_pos_x - 5 and pos[1] < like_pos_y + like_pos_height + 5 and pos[1] > like_pos_y - 5:
            if event.type == pygame.MOUSEBUTTONDOWN:
                show_like_interface(screen)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
