# coding=utf-8
'''
说明：传入长度，生成字符串
'''
str=''
chars='x'
for i in range(100):
    str+=chars
print(len(str))
print('{{{0}}}'.format(str))


str=''
for i in range(50):
    str+=chars
print(len(str))
print('{{{0}}}'.format(str))

s = '：超重；尿酸、肌酐偏高；脂肪肝，请注意清淡饮食，多运动。详细内容请看报告，报告由单位统一领取。'
print(len(s))