import re
from datetime import time

'''
ttl原文本处理
'''

def ttl_dotToUndercore(path,path2):
    '''

    :param path: 输入文件
    :param path2: 输出文案
    :return:
    '''

    time_start = time.time()

   #读取文件和处理
    file1 = open(path, 'rt', encoding='utf-8')
    lines = file1.readlines()
    i = 0
    for line in lines:
        row = line.split(" ")
        init_l = re.findall('(?<=\/)[^\/]*?(?=>)', row[1])
        init_s = init_l[0]
        replace_s = init_s.replace('.', '_')
        line = line.replace(init_s, replace_s)
        if row[2].startswith('<') and row[2].endswith('>'):
            init_l = re.findall('(?<=\/)[^\/]*?(?=>)', row[2])
            init_s = init_l[0]
            replace_s = init_s.replace('.', '_')
            line = line.replace(init_s, replace_s)
        print(line)
        lines[i] = line
        i += 1
    file1.close()

    #写文件
    file2 = open(path2, 'wt', encoding='utf-8')
    file2.writelines(lines)
    file2.close()
    time_end = time.time()
    print('totally cost', time_end - time_start)
if __name__ == '__main__':


    path = "D:\WeiyunTongbuPan\Micro\DataSet\geo\data\geo@@23f75c2c-f6fb-4741-9cf8-1a79e829ee52@@geo_1@@carina-noEnglishComma.ttl"

