# -*- coding=utf-8 -*-

import pygame
from sys import exit  # 向sys模块借一个exit函数用来退出程序

import win32api
import win32con

from api import *
from widget import *
from sort import *

WHITE = (255, 255, 255)
GREEN = (200, 221, 139)
BLUE = (65, 193, 227)
BLACK = (0, 0, 0)
Color = (238, 227, 188)

suites = {
    '$': 'spade',  # 黑桃
    '&': 'heart',  # 红桃
    '*': 'club',  # 梅花
    '#': 'diamond'  # 方块
}

faces = {
    'A': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    'J': '11',
    'Q': '12',
    'K': '13'
}


def main():
    pygame.init()  # 初始化pygame
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((658, 369), 0, 32)  # 设置窗口
    screen.fill((226, 226, 226))  # 填充颜色
    pygame.display.set_caption("福建十三水")  # 设置标题
    tb_username = TextBox(200, 30, 300, 177)
    tb_password = TextBox(200, 30, 300, 216)
    tb_numpass = TextBox(200, 30, 300, 138)
    tb_num = TextBox(200, 30, 300, 99)
    card_dirt = {}
    card = []
    card_list = []
    rank_data = []
    history_data = []
    text_list_rank = TextList(rank_data, 0, 0, 5, 3, [100, 100, 100], 49, 1)
    text_list_history = TextList(history_data, 0, 0, 5, 3, [100, 100, 100], 49, 1)

    # 主界面
    background_screen_main = pygame.image.load('background/background_main.png').convert()
    # 登录
    background_screen_login = pygame.image.load('background/background_login.png').convert()
    # 注册界面
    background_screen_register = pygame.image.load('background/background_register.png').convert()
    # 房间界面
    background_screen_room = pygame.image.load('background/background_room.png').convert()
    # 游戏界面
    background_screen_game = pygame.image.load('background/background_game.jpg').convert()
    # 历史记录界面
    background_screen_history = pygame.image.load('background/background_history.png').convert_alpha()
    # 排行榜界面
    background_screen_ranking = pygame.image.load('background/background_history.png').convert_alpha()

    for suite in suites:
        for face in faces:
            key = suite + face
            res = 'puke_small/' + suites[suite] + '_' + faces[face] + " " + "拷贝" + '.png'
            img = pygame.image.load(res).convert()
            card_dirt[key] = img
    # 1
    buttonto_login = Button('img/login.png', 74, 280)
    buttonto_register = Button('img/register.png', 400, 280)
    # 2
    buttonto_screen_login = Button('img/login.png', 74, 280)
    buttonto_loginback = Button('img/back_main.png', 400, 280)  # 2
    # 3
    buttonto_screen_register = Button('img/register.png', 74, 280)
    buttonto_registerback = Button('img/back_main.png', 400, 280)
    # 4
    buttonto_logout = Button('img/back.png', 600, 10)
    buttonto_begingame = Button('img/begin.png', 120, 200)
    buttonto_history = Button('img/history.png', 270, 200)
    buttonto_ranking = Button('img/rank.png', 420, 200)

    # 5
    buttonto_exitback = Button('img/back.png', 20, 14)
    # 6
    # history\7rank
    button_back = Button('img/back.png', 367, 540)

    # 将使用到的组件绑定到对应的页
    page = [[] for _ in range(8)]
    page[1].append(buttonto_login)
    page[1].append(buttonto_register)

    page[2].append(buttonto_screen_login)
    page[2].append(buttonto_loginback)
    page[2].append(tb_username)
    page[2].append(tb_password)

    page[3].append(buttonto_screen_register)
    page[3].append(buttonto_registerback)
    page[3].append(tb_username)
    page[3].append(tb_password)
    page[3].append(tb_num)
    page[3].append(tb_numpass)

    page[4].append(buttonto_logout)
    page[4].append(buttonto_begingame)
    page[4].append(buttonto_history)
    page[4].append(buttonto_ranking)

    page[5].append(buttonto_exitback)
    # history
    page[6].append(buttonto_exitback)
    page[6].append(text_list_history)
    # ranking
    page[7].append(buttonto_exitback)
    page[7].append(text_list_rank)

    current_page = 1

    p1 = Player('xiAoC', '123456')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                p1.logout()
                exit()
            # 键盘活动
            if event.type == pygame.KEYDOWN:
                if current_page == 2 or 3:
                    mouse = pygame.mouse.get_pos()
                    if (tb_username.pressed(mouse)):
                        tb_username.key_down(event)
                    if (tb_password.pressed(mouse)):
                        tb_password.key_down(event)
                    if (tb_numpass.pressed(mouse)):
                        tb_numpass.key_down(event)
                    if (tb_num.pressed(mouse)):
                        tb_num.key_down(event)
            # 鼠标活动
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # 1
                if current_page == 1:
                    if buttonto_login.pressed(mouse):
                        current_page = 2
                    if buttonto_register.pressed(mouse):
                        current_page = 3
                # 2 登入
                elif current_page == 2:
                    if buttonto_loginback.pressed(mouse):
                        current_page = 1
                    if buttonto_screen_login.pressed(mouse):
                        p1 = Player(tb_username.get_text(), tb_password.get_text())
                        p1.login()
                        if p1.check_login_status():
                            current_page = 4
                        else:
                            win32api.MessageBox(0, "登录失败，请检查信息是否正确", "提醒", win32con.MB_ICONWARNING)

                # 3 注册
                elif current_page == 3:
                    if buttonto_registerback.pressed(mouse):
                        current_page = 1
                    if buttonto_screen_register.pressed(mouse):
                        p1 = Player(tb_username.get_text(), tb_password.get_text(), tb_num.get_text(),
                                    tb_numpass.get_text())
                        p1.register()
                        if p1.check_register_status():
                            current_page = 2
                        else:
                            win32api.MessageBox(0, "注册失败，请检查信息是否正确", "提醒", win32con.MB_ICONWARNING)
                # 4 游戏主界面
                elif current_page == 4:
                    if buttonto_logout.pressed(mouse):
                        current_page = 1
                    if buttonto_begingame.pressed(mouse):
                        card = p1.getCard()  # getcard函数就是游戏开局标志
                        current_page = 5
                    if buttonto_ranking.pressed(mouse):
                        current_page = 7
                        rank_data = p1.get_rank()
                        text_list_rank.update(0, rank_data)
                    if buttonto_history.pressed(mouse):
                        current_page = 6
                        history_data = p1.get_history(0, 20, p1.user_id)
                        text_list_history.update(0, history_data)
                        text_list_history.draw(background_screen_history)

                # 5 进入游戏
                elif current_page == 5:
                    if buttonto_exitback.pressed(mouse):
                        current_page = 4
                # 6 历史记录
                elif current_page == 6:
                    if buttonto_exitback.pressed(mouse):
                        current_page = 4

                # 7 游戏排行榜
                elif current_page == 7:
                    if buttonto_exitback.pressed(mouse):
                        current_page = 4
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        if (current_page == 5):
            card = p1.getCard()
            print(card)
            list_output = sort(card)  # 组牌
            string1 = list_output[0] + " " + list_output[1] + " " + list_output[2]
            string2 = list_output[3] + " " + list_output[4] + " " + list_output[5] + " " + list_output[6] + " " + \
                      list_output[7]
            string3 = list_output[8] + " " + list_output[9] + " " + list_output[10] + " " + list_output[11] + " " + \
                      list_output[12]
            card_list.append(string1)
            card_list.append(string2)
            card_list.append(string3)
            print(card_list)
            p1.submitCard(card_list)
            card = []
            card_list = []
            string1 = []
            string2 = []
            string3 = []

        # display update
        if current_page == 1:
            screen.blit(background_screen_main, (0, 0))
            for w in page[1]:
                w.draw(screen)
        elif current_page == 2:
            screen.blit(background_screen_login, (0, 0))
            for w in page[2]:
                w.draw(screen)
        elif current_page == 3:
            screen.blit(background_screen_register, (0, 0))
            for w in page[3]:
                w.draw(screen)
        elif current_page == 4:
            screen.blit(background_screen_room, (0, 0))
            for w in page[4]:
                w.draw(screen)
        elif current_page == 5:
            screen.blit(background_screen_game, (0, 0))
            for w in page[5]:
                w.draw(screen)
            draw_card(screen, 100, 125, list_output, card_dirt)
            list_output = []
        elif current_page == 6:
            screen.blit(background_screen_history, (0, 0))
            for w in page[6]:
                w.draw(screen)

        elif current_page == 7:
            screen.blit(background_screen_ranking, (0, 0))
            for w in page[7]:
                w.draw(screen)
        pygame.display.update()

        pygame.time.delay(33)
        pygame.display.flip()
        clock.tick(20)


if __name__ == '__main__':
    main()
