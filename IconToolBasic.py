# -*- coding: UTF-8 -*-

import os

##总体思路：
##1. 检测当前目录下是否有 .ico 文件。
##2. 获取 .ico 文件的文件名。
##3. 新建一个 desktop.ini 文件，设为隐藏。
##4. 将文件夹设置为只读。


Const_Image_Format = [".ico"] ## 设置需要寻找的文件格式为 .ico

def main():

        ## 1. 检测当前目录下是否有 .ico 文件。

        ## 遍历当前目录下的文件
        print ('1. 检测当前目录下是否有 .ico 文件')
        DirPath = os.getcwd()  ## 搜索当前路径
        print ( "当前路径为：" + DirPath)
        counter = 0
        for root, dirs, files in os.walk(DirPath, topdown=False):
                for file in files:
                        if file.endswith(".ico"):
                                print (os.path.join(root, file))
                                os.rename(root +"/"+ file, root +"/"+"foldericon.ico")
                                counter += 1

        print ('检测完毕！\n')

        ## 2. 获取 .ico 文件的文件名。

        print ('2. 正在获取 .ico 文件的文件名')

        print ("发现图标数量为：" + str(counter))
                
        print ("已将上述图标重命名为 foldericon.ico")

        print ('获取完毕！\n')



        ## 3. 新建一个 desktop.ini 文件，设为隐藏。

        print ('3. 正在新建 desktop.ini 文件')

        ## 将文件夹图标设置为同文件夹下的 iconfile.ico 图标（覆盖原内容）

        ## 配置信息
        iniline1 = "[.ShellClassInfo]"
        iniline2 = "IconResource=foldericon.ico,0"
        iniline = iniline1 + "\n"+ iniline2

        
        for root, dirs, files in os.walk(DirPath, topdown=False):
                for file in files:
                        if file.endswith(".ico"):
                                ## 为 desktop.ini 写入配置
                                inifile = open(root +"/"+ 'desktop.ini','w')
                                inifile.write(iniline)
                                inifile.close()
                                print ('正在为 ' + os.path.join(root, file) + ' 添加配置信息')
                                cmd = 'attrib +h "foldericon.ico"'
                                os.system(cmd)
                                
        for root, dirs, files in os.walk(DirPath, topdown=False):
                for file in files:
                        if file.endswith(".ini"):
                                cmd = 'attrib +h "desktop.ini"'
                                os.system(cmd) ## 将 desktop.ini 设为隐藏
                                print(cmd)
        print ('新建完毕！\n')


        ## 4. 将文件夹设置为只读。

        print ('4. 正在将文件夹设置为只读')

        ## 设置父文件夹只读
        print (root)
        os.system('attrib +r //d ' + root)
        
        print ('设置完成！\n')



## 开始执行

main()

## 结束任务

