#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import copy
import os

score = 0
list_input = []
list_2 = []
list_2_backup = []
list_output = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
list_qian = ['0', '0', '0']
list_zhong = ['0', '0', '0', '0', '0']
list_hou = ['0', '0', '0', '0', '0']

# 1   2   3   4   5   6   7   8   9   T   J   Q   K   A
dict1 = {'sanpai': [0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 4, 7, 14, 33],
         'duizi': [0, 46, 48, 50, 51, 54, 56, 60, 63, 68, 74, 81, 89, 97],
         'liangdui': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'santiao': [0, 99, 99, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
         'shunzi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'tonghua': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'hulu': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'zhadan': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'tonghs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
dict2 = {'sanpai': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         'duizi': [0, 2, 3, 4, 4, 5, 7, 8, 10, 12, 15, 19, 24, 33],
         'liangdui': [0, 0, 36, 37, 38, 40, 44, 46, 49, 54, 57, 62, 64, 72],
         'liandui': [0, 0, 37, 38, 39, 41, 45, 47, 50, 55, 58, 63, 65, 73],
         'santiao': [0, 63, 65, 69, 71, 72, 73, 73, 73, 74, 74, 75, 75, 75],
         'shunzi': [0, 0, 0, 0, 77, 78, 81, 83, 85, 87, 88, 90, 91, 92],
         'tonghua': [0, 0, 0, 0, 0, 0, 93, 93, 93, 93, 94, 95, 97, 98],
         'hulu': [0, 98, 98, 99, 99, 99, 100, 100, 100, 100, 100, 100, 100, 100],
         'zhadan': [0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
         'tonghs': [0, 0, 0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0]}
dict3 = {'sanpai': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'duizi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3],
         'liangdui': [0, 0, 2, 3, 4, 4, 6, 7, 8, 10, 11, 13, 13, 14],
         'liandui': [0, 0, 3, 4, 5, 5, 7, 8, 9, 11, 12, 14, 14, 15],
         'santiao': [0, 11, 12, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15],
         'shunzi': [0, 0, 0, 0, 16, 17, 20, 22, 24, 26, 28, 32, 33, 36],
         'tonghua': [0, 0, 0, 0, 0, 0, 36, 36, 37, 38, 40, 44, 49, 61],
         'hulu': [0, 64, 67, 70, 71, 73, 75, 77, 80, 82, 85, 88, 91, 94],
         'zhadan': [0, 93, 94, 95, 95, 96, 96, 96, 97, 97, 98, 98, 98, 98],
         'tonghs': [0, 0, 0, 0, 98, 98, 99, 99, 99, 99, 99, 99, 100, 100]}


def func_1(str):
    if (str[1] <= '9' and str[1] >= '2'):
        return int(str[1]) - 1
    elif (str[1] == 'J'):
        return 10
    elif (str[1] == 'Q'):
        return 11
    elif (str[1] == 'K'):
        return 12
    elif (str[1] == 'A'):
        return 13
    elif (str[1] == '1'):
        return 9


def check_tonghuashun(i, dict):
    global score
    # print("this is tonghuashun")
    if (check_shunzi(i, dict) != 0):
        score = score - dict["shunzi"][func_1(list_2[i][4])]
        if (check_tonghua(i, dict) != 0):
            score = score - dict["tonghua"][func_1(list_2[i][4])]
            score = score + dict["tonghs"][func_1(list_2[i][4])]
            # print(score)
            return func_1(list_2[i][4]) + 117
        else:
            return 0
    else:
        return 0


def check_zhadan(i, dict):
    global score
    # print("this is zhadan")
    if (list_2[i][0][1] == list_2[i][1][1] and list_2[i][1][1] == list_2[i][2][1] and list_2[i][2][1] == list_2[i][3][
        1]):
        score = score + dict["zhadan"][func_1(list_2[i][0])]
        return func_1(list_2[i][0]) + 104
    elif (list_2[i][1][1] == list_2[i][2][1] and list_2[i][2][1] == list_2[i][3][1] and list_2[i][3][1] == list_2[i][4][
        1]):
        score = score + dict["zhadan"][func_1(list_2[i][1])]
        return func_1(list_2[i][1]) + 104
    else:
        return 0


def check_hulu(i, dict):
    global score
    # print("this is hulu")
    if (list_2[i][0][1] == list_2[i][1][1] and list_2[i][1][1] == list_2[i][2][1]):
        if (list_2[i][3][1] == list_2[i][4][1]):
            score = score + dict["hulu"][func_1(list_2[i][2])]
            return func_1(list_2[i][2]) + 91
        else:
            return 0
    elif (list_2[i][2][1] == list_2[i][3][1] and list_2[i][3][1] == list_2[i][4][1]):
        if (list_2[i][0][1] == list_2[i][1][1]):
            score = score + dict["hulu"][func_1(list_2[i][2])]
            return func_1(list_2[i][2]) + 91
        else:
            return 0
    else:
        return 0


def check_tonghua(i, dict):
    global score
    # print("this is tonghua")
    if (list_2[i][0][0] == list_2[i][1][0] and list_2[i][1][0] == list_2[i][2][0] and list_2[i][2][0] == list_2[i][3][
        0] and list_2[i][3][0] == list_2[i][4][0]):
        score = score + dict["tonghua"][func_1(list_2[i][4])]
        return func_1(list_2[i][4]) + 78
    else:
        return 0


def check_shunzi(i, dict):
    global score
    # print("this is shunzi")
    if (func_1(list_2[i][4]) == func_1(list_2[i][3]) + 1 and func_1(list_2[i][3]) == func_1(
            list_2[i][2]) + 1 and func_1(list_2[i][2]) == func_1(list_2[i][1]) + 1 and func_1(list_2[i][1]) == func_1(
        list_2[i][0]) + 1):
        score = score + dict["shunzi"][func_1(list_2[i][4])]
        return func_1(list_2[i][4]) + 65
    else:
        return 0


def check_santiao(i, dict):
    global score
    # print("this is santiao")
    if (list_2[i][0][1] == list_2[i][1][1] and list_2[i][1][1] == list_2[i][2][1]):
        score = score + dict["santiao"][func_1(list_2[i][0])]
        return func_1(list_2[i][0]) + 52
    elif (list_2[i][1][1] == list_2[i][2][1] and list_2[i][2][1] == list_2[i][3][1]):
        score = score + dict["santiao"][func_1(list_2[i][1])]
        return func_1(list_2[i][1]) + 52
    elif (list_2[i][2][1] == list_2[i][3][1] and list_2[i][3][1] == list_2[i][4][1]):
        score = score + dict["santiao"][func_1(list_2[i][2])]
        return func_1(list_2[i][2]) + 52
    else:
        return 0


def check_liangdui(i, dict):
    global score
    # print("this is liangdui")
    if (list_2[i][0][1] == list_2[i][1][1]):
        if (list_2[i][2][1] == list_2[i][3][1] or list_2[i][3][1] == list_2[i][4][1]):
            if (func_1(list_2[i][3]) == func_1(list_2[i][1]) + 1):
                score = score + dict["liandui"][func_1(list_2[i][3])]
                return func_1(list_2[i][3]) + 39
            else:
                score = score + dict["liangdui"][func_1(list_2[i][3])]
                return func_1(list_2[i][3]) + 26
        else:
            return 0
    elif (list_2[i][1][1] == list_2[i][2][1]):
        if (list_2[i][3][1] == list_2[i][4][1]):
            if (func_1(list_2[i][3]) == func_1(list_2[i][2]) + 1):
                score = score + dict["liandui"][func_1(list_2[i][3])]
                return func_1(list_2[i][3]) + 39
            else:
                score = score + dict["liangdui"][func_1(list_2[i][3])]
                return func_1(list_2[i][3]) + 26
        else:
            return 0
    else:
        return 0


def check_duizi(i, dict):
    global score
    # print("this is duizi")
    if (list_2[i][0][1] == list_2[i][1][1]):
        score = score + dict["duizi"][func_1(list_2[i][0])]
        return func_1(list_2[i][0]) + 13
    elif (list_2[i][1][1] == list_2[i][2][1]):
        score = score + dict["duizi"][func_1(list_2[i][1])]
        return func_1(list_2[i][1]) + 13
    elif (list_2[i][2][1] == list_2[i][3][1]):
        score = score + dict["duizi"][func_1(list_2[i][2])]
        return func_1(list_2[i][2]) + 13
    elif (list_2[i][3][1] == list_2[i][4][1]):
        score = score + dict["duizi"][func_1(list_2[i][3])]
        return func_1(list_2[i][3]) + 13
    else:
        return 0


def check_sanpai(i, dict):
    global score
    # print("this is sanpai")
    score = score + dict["sanpai"][func_1(list_2[i][4])]
    return func_1(list_2[i][4])


def get_weight(i, weight_flag):
    if (weight_flag != 0):
        dict_flag = dict2
    else:
        dict_flag = dict3
    weight = check_tonghuashun(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_zhadan(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_hulu(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_shunzi(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_tonghua(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_shunzi(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_santiao(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_liangdui(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_duizi(i, dict_flag)
    if (weight != 0):
        return weight
    weight = check_sanpai(i, dict_flag)
    return weight


def get_weight_qian():
    # print("this is weight_qian")
    global score
    if (list_2_backup[0][1] == list_2_backup[1][1] or list_2_backup[1][1] == list_2_backup[2][1]):
        score = score + dict1["duizi"][func_1(list_2_backup[1])]
        return func_1(list_2_backup[1]) + 13
    elif (list_2_backup[0][1] == list_2_backup[1][1] and list_2_backup[1][1] == list_2_backup[2][1]):
        score = score + dict1["santiao"][func_1(list_2_backup[1])]
        return func_1(list_2_backup[1]) + 52
    else:
        score = score + dict1["sanpai"][func_1(list_2_backup[2])]
        # print("qiandunjiazhi: %d"%dict1["sanpai"][func_1(list_2_backup[2])])
        return func_1(list_2_backup[2])


def get_score(i):
    score_max_private = 0
    global score
    global list_2
    global list_2_backup
    list_zhong_private = ['', '', '', '', '']
    weight_hou = get_weight(i, 0)
    # print("后墩权重：%d" %weight_hou)
    list_hou[0] = list_2[i][0]
    list_hou[1] = list_2[i][1]
    list_hou[2] = list_2[i][2]
    list_hou[3] = list_2[i][3]
    list_hou[4] = list_2[i][4]
    # print("后墩牌：",end = "")
    ##print(list_hou)
    # print("firstscore:%d" %score)
    # print(list_input)
    # list_copyright = copy.copy(list_hou)
    list_copyright = list(set(list_input).difference(set(list_hou)))
    list_copyright.sort(key=func_1)
    # print(list_copyright)
    # os.system("pause")
    list_2 = list(itertools.combinations(list_copyright, 5))
    score_copyright = score
    for index_zhong in range(len(list_2)):
        score = score_copyright
        list_2 = list(itertools.combinations(list_copyright, 5))
        # print(len(list_2))
        weight_zhong = get_weight(index_zhong, weight_hou)
        # print("中墩权重：%d" %weight_zhong)
        # print("secondscore:%d" %score)
        if (weight_zhong > weight_hou):
            score = 0
            continue
        list_zhong_private[0] = list_2[index_zhong][0]
        list_zhong_private[1] = list_2[index_zhong][1]
        list_zhong_private[2] = list_2[index_zhong][2]
        list_zhong_private[3] = list_2[index_zhong][3]
        list_zhong_private[4] = list_2[index_zhong][4]
        # print("中墩牌private：",end = "")
        # print(list_zhong_private)
        list_copyright_backup = copy.copy(list_copyright)
        list_copyright_backup = list(set(list_copyright).difference(set(list_zhong_private)))
        list_copyright_backup.sort(key=func_1)
        list_2_backup = list_copyright_backup
        weight_qian = get_weight_qian()
        # print("前墩权重：%d" %weight_qian)
        # print(score)
        if (weight_qian > weight_zhong):
            continue
        if (score > score_max_private):
            score_max_private = score
            # print("中墩权重：%d" %weight_zhong)
            list_zhong[0] = list_zhong_private[0]
            list_zhong[1] = list_zhong_private[1]
            list_zhong[2] = list_zhong_private[2]
            list_zhong[3] = list_zhong_private[3]
            list_zhong[4] = list_zhong_private[4]
            # print("中墩牌：",end = "")
            # print(list_zhong)
            # print("score_max_zhong:%d" %score_max_private)
            list_qian[0] = list_2_backup[0]
            list_qian[1] = list_2_backup[1]
            list_qian[2] = list_2_backup[2]
            # print("前墩牌：",end = "")
            # print(list_qian)
            # print("lastscore:%d" %score)
            # print("_______________________")
        score = score_max_private


def get_score_max(list_1):
    global list_2
    global list_qian
    global list_zhong
    global list_hou
    global list_output
    global score
    score_max = 0
    list_2 = list(itertools.combinations(list_1, 5))
    for index_hou in range(len(list_2)):
        # print("looping again")
        # print(list_2[index])
        list_2 = list(itertools.combinations(list_1, 5))
        score = 0
        get_score(index_hou)
        # print("score:%d" %score)
        # print("score_max:%d" %score_max)
        if (score > score_max):
            score_max = score
            ##print("score_max:%d" %score_max) #这个可以优先取消注释
            list_output[0] = list_qian[0]
            list_output[1] = list_qian[1]
            list_output[2] = list_qian[2]
            list_output[3] = list_zhong[0]
            list_output[4] = list_zhong[1]
            list_output[5] = list_zhong[2]
            list_output[6] = list_zhong[3]
            list_output[7] = list_zhong[4]
            list_output[8] = list_hou[0]
            list_output[9] = list_hou[1]
            list_output[10] = list_hou[2]
            list_output[11] = list_hou[3]
            list_output[12] = list_hou[4]
            ##print(list_output) #这个也不错，其他的输出用来定位具体错误
            # print("looping end")


def sort(list1):
    global list_input
    list_input = list1
    list_input.sort(key=func_1)
    # print(list_input)
    get_score_max(list_input)
    # print(list_qian)
    # print(list_zhong)
    # print(list_hou)
    # print(list_output)

    return list_output
