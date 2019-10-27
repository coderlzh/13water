#!/usr/bin/python
# -*- coding: utf-8 -*-
from api import *
from sort import *

p1=Player('xiAoC','123456', '031702623', 'caijiayi5819.')

p1.login()
p1.show()
for i in range(100):
    print(p1.get_rank())
    for j in range(10):
        list1=p1.getCard()
        print(list1)
        list2=sort(list1)
        string1 = list2[0] + " " + list2[1] + " " + list2[2]
        string2 = list2[3] + " " + list2[4] + " " + list2[5] + " " + list2[6] + " " + list2[7]
        string3 = list2[8] + " " + list2[9] + " " + list2[10] + " " + list2[11] + " " + list2[12]
        list3 = []
        list3.append(string1)
        list3.append(string2)
        list3.append(string3)
        print(list3)
        p1.submitCard(list3)


