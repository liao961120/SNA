"""
106_1_inschool.txt
"Id" "id2" 共計 男 女 男 女 男 女 男 女 男 女 男 女 男 女 男 女 男 女

100-106_suspend.txt
系別代碼 系別 上學期 下學期 上學期 下學期 上學期 下學期 上學期 下學期 上學期 下學期 上學期 下學期 上學期 下學期
"""

# Clean 100-106_suspend.txt
with open('100-106_suspend.txt', 'r') as f:
    x = f.readlines()
for i, line in enumerate(x):
    x_lst = line.split(' ')
    dept = x_lst[1]
    drop = x_lst[-2]
    x[i] = [dept, drop]
with open('1061_suspend.csv', 'w') as f:
    f.write('Id,drop\n')
    for line in x:
        out = ','.join(line) + '\n'
        f.write(out)

# Clean 106_1_inschool.txt
with open('106_1_inschool.txt', 'r') as f:
    x = f.readlines()

for i, line in enumerate(x):
    x_lst = line.split(' ')
    dept = x_lst[0]
    total = x_lst[2]
    x[i] = [dept, total]

with open('1061_inschool.csv', 'w') as f:
    f.write('Id,inSchool\n')
    for line in x:
        out = ','.join(line) + '\n'
        f.write(out)


"""
    with open('106_1_inschool.csv', 'a') as f:
        f.write(dept + ',' + total + '\n')
    # read next line
    x = input()
"""