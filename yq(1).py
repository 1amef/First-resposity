import numpy as np
import pandas as pd
import sys

num = []
for index, arg in enumerate(sys.argv):  # 获取命令行的参数
    num.append(arg)

# yq_in_03 = h[1]
# yq_out_03 = h[2]

fr = pd.read_table("yq_in_03.txt", header=None,encoding='gbk')
a = np.array(fr)
fw = open("yq_out_03.txt", 'w')
sum = 0
city = []
pro = []
for i in range(len(a)):
    if len(num) < 2:
        for l in range(3, len(num)):
            if num[l] == a[i][0]:
                city.append([a[i][1], a[i][2]])  # 将该省份的每一个市以及数据存入列表
                sum += a[i][2]
                if a[i][0] != a[(i + 1) % len(a)][0] and i != 0 or i == len(a) - 1:  # 确认省份是否变换
                    city.append([a[i - 1][0], sum])
                    for n in range(len(city)):  # 将上一列表中省份的数据排序
                        for k in range(0, len(city) - 1):
                            if city[k][1] < city[k + 1][1]:
                                city[k], city[k + 1] = city[k + 1], city[k]
                    sum = 0
                    pro.append(city)  # 将每个排序好的省份再放入一个列表
                    city = []
    else:
        city.append([a[i][1], a[i][2]])  # 将该省份的每一个市以及数据存入列表
        sum += a[i][2]
        if a[i][0] != a[(i + 1) % len(a)][0] and i != 0 or i == len(a) - 1:  # 确认省份是否变换
            city.append([a[i - 1][0], sum])
            for n in range(len(city)):  # 将上一列表中省份的数据排序
                for k in range(0, len(city) - 1):
                    if city[k][1] < city[k + 1][1]:
                        city[k], city[k + 1] = city[k + 1], city[k]
            sum = 0
            pro.append(city)  # 将每个排序好的省份再放入一个列表
            city = []
for j in range(len(pro)):  # 对每个省进行排序
    for o in range(0, len(pro) - 1):
        if pro[o][0][1] < pro[o + 1][0][1]:
            pro[o], pro[o + 1] = pro[o + 1], pro[o]
for num in range(len(pro)):  # 将最终结果写入文档
    for g in range(len(pro[num])):
        fw.writelines([str(pro[num][g][0]), '\t', str(pro[num][g][1]), '\n'])
    fw.writelines(['\n'])
#
# if len(num) < 3:   #如果输入的参数为3个，即带有省份，则根据输入指定省份输出该省份的城市
#     for k in range(len(pro)):
#         if pro[k][0] == num[3]:
#             fw.write('%s\n ' % pro[k][0])
#             fw.write('%s\t ' % pro[k][1])
#             fw.write('%s\n ' % pro[k][2])
fw.close()