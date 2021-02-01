my_f = open(u'D:\test.txt', 'r', encoding='utf-8')
with open('D:\test.txt') as myfile:
    count = sum(1 for line in myfile)
    print(count)
num = len('D:\test.txt')
print(num)


