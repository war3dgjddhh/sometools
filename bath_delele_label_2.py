import os
# read all file form filePath, save all file  to filePath2
filePath = '/home/yly/evm/HardHar/test/labels/'
filePath2 = '/home/yly/evm/SafeHat/test/labels/'
# this for loop all files in filePath, k is filename, i is emmm, j is emmm
for i,j,k in os.walk(filePath):
    print("i",i)
    print("j",j)
    # print("k",k)
    for n in k :
        f1 = open(filePath+n,'r')               # 返回一个文件对象 read
        f2 = open(filePath2+n, 'w')             # return a file object write
        cache = ""
        line = f1.readline()              # 调用文件的 readline()方法 
        while line: 
            if (line[0] != '2') :               # yolov5 label files, the first number in line is the class id in classes name, if class id not equal 2, just not write to new file 
                cache += line
            line = f1.readline() 
        f2.write(cache) 
        f2.close()
        f1.close()
