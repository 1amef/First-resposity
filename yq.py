import pandas as pd

f1 = pd.read_table('yq_in.txt', header=None,encoding='gbk')
f2 = open('D:\pythonProject\py_exp1\yq_out2.txt', 'a')
array = f1.values
for i in range(len(f1)):
    if array[i][0] == array[i-1][0]:
        f2.write('%s\t' % array[i][1])
        f2.write('%d\n' % array[i][2])
    else:
        f2.write('%s\n' % array[i][0])
        f2.write('%s\t' % array[i][1])
        f2.write('%d\n' % array[i][2])