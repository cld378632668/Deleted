import csv
import re
import time
import os

def travelCurrentDir(file_dir):
    '''
    遍历当前目录进行操作
    :param file_dir:
    :return:
    '''
    for root, dirs, files in os.walk(file_dir):
         print(root) #当前目录路径
         print(dirs) #当前路径下所有子目录
         print(files) #当前路径下所有非目录子文件 a string_list
    print("All files in current dir are:")
    for file in files:
        print(root+"\\"+file)
        path = root+"\\"+file
        #请替换下面的处理函数来处理你的每个文件
        moveCsvCol(path,"type_object_name:string[]",0)

def moveCsvCol(path,header,final_position=0):
    '''
    将path文件中header为header的一列，插入到index=final的位置，然后删除原来那一列
    #输出文件覆盖原来的文件
    :param path:
    :param header:
    :param final_position:
    :return:
    '''
    time_start = time.time()

    f = open(path,encoding='utf-8')
    rows = csv.reader(f,delimiter=',')
    lines_in = list(rows) # list<list>
    f.close()

    #获取header对应的index：i
    headers:list = lines_in[0]
    i = 0
    for i in range(2, headers.__len__()):
        if headers[i] == header:
            break
    lines = [[]] #最后输出的结果
    lines.append(headers)

    #移动column
    for row in lines_in:
        row.insert(final_position,row[i])
        row.pop(i + 1)


    #覆盖写入原来的csv
    write_f = open(path, 'w',
              encoding='utf-8')
    f_csv = csv.writer(write_f, delimiter=',')
    f_csv.writerows(lines_in)
    write_f.close()
    time_end = time.time()
    print('totally cost', time_end - time_start)

if __name__ == '__main__':
    travelCurrentDir(r'D:\GeoData')
    path = r'D:\GeoData\node_travel_tourist_attraction.csv'
    # csv1('D:\WeiyunTongbuPan\Micro\DataSet\geo\data\geo@@23f75c2c-f6fb-4741-9cf8-1a79e829ee52@@geo_1@@carina-noEnglishComma.ttl')
   # ? csv2(path, "type_object_name:string[]")
