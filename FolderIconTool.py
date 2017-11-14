# -*- coding: UTF-8 -*-

import os
import stat

## 总体思路：
## 1. 检测当前目录下是否有 .ico 文件。
## 2. 将文件夹设置为只读。
## 3. 在每个有图标的目录中新建 desktop.ini 文件，设为隐藏。

def main():

	## -----说明文字-----
	print ("=======================================")
	print ("- 欢迎使用 FolderIconTool")
	print ("- Design by fengyunkkx")
	print ("=======================================\n")

	print ("============================== 使用方法 ==============================")
	print (" ")
	print ("- 1. 首先将图标文件手动放进每个文件夹中。")
	print ("- 2. 将 FolderIconTool 放置在希望批量替换文件夹图标的目录下。")
	print ("- 3. 运行本程序。")
	print (" ")
	print ("======================================================================\n")

	a = str(input('- 输入 1 开始设置图标：\n'))
	if (a == "1"):
		print("\n- 开始执行，请勿对文件进行操作。\n")
		start()
	else:
		b = str(input('按下回车键退出本程序\n'))
		exit()

def start():

	## -----1. 检测当前目录下是否有 .ico 文件。-----

	iconame = []
	print ("=======================================")
	print ("- 1. 检测当前目录下是否有 .ico 文件")
	print ("=======================================\n")
	DirPath = os.getcwd()                                           ## DirPath：当前路径

	print ( "- 当前路径为：\n"+ DirPath)
	counter = 0                                                     ## counter：计数

	print ( "- 该路径下的图标有：")
	for root, dirs, files in os.walk(DirPath, topdown=False):       ## 遍历当前目录下的图标文件
		for file in files:
			if file.endswith(".ico"):
				print (os.path.join(root, file))
				iconame.append(file)
				## os.rename(root +"\\"+ file, root +"/"+"foldericon.ico")
				## 早期做法：统一命名为 foldericon.ico
				counter += 1
	print ("\n- 检测完毕！")
	print ("- 该目录下共有 " + str(counter) + " 个图标文件。\n")


	## 确认操作
	print ("=======================================")
	print ("- 是否开始将上述图标设为文件夹图标？")
	print ("=======================================")
	print ("（如果同一文件夹下有多个图标，将选取最后一个图标作为文件夹图标。）\n")
	a = str(input('- 输入 1 继续：\n'))

	if (a == "1"):

		print("\n- 开始批量设置，请勿对文件进行操作。\n")



		## -----2. 将文件夹设置为只读。-----
		print ("=======================================")
		print ("- 2. 正在将文件夹设置为只读")
		print ("=======================================\n")
		## 设置父文件夹只读
		for root, dirs, files in os.walk(DirPath, topdown=False):
			for file in files:
				if file.endswith(".ico"):
					os.chmod(root, stat.S_IREAD)    ## 将带有 .ico 图标文件的目录设为只读。

					## os.system("cd " + root + "&& attrib +r /d")
					## 另一种设置方法，需要管理员权限。

		print ("- 已将「" + root + "」目录下所有子文件夹设置为只读（不包括文件）。")
		## os.system("cd " + root + "&& attrib -r IconToolsBasic.py")

		print ("- 设置完成！\n")



		## -----3. 新建一个 desktop.ini 文件，设为隐藏。-----
		print ("=======================================")
		print ("- 3. 正在新建 desktop.ini 文件")                        ## 将文件夹图标设置为同文件夹下的 iconfile.ico 图标（覆盖原内容）
		print ("=======================================\n")
		print ("- 正在获取 .ico 文件的文件名")
		print ("- 图标名称为：" + str(iconame))
		print ("- 获取完毕！\n")

		## 配置信息
		print ("- 正在生成 .ini 配置文件\n")
		iniline1 = "[.ShellClassInfo]"
		i = 0
		try:
			for root, dirs, files in os.walk(DirPath, topdown=False):
				for file in files:
					if file.endswith(".ico"):
						## 为 desktop.ini 写入配置
						iniline2 = "IconResource=" + iconame[i] + ",0"
						i += 1
						iniline = iniline1 + "\n"+ iniline2

						try:
							os.system("cd " + root + "&& attrib -h -s desktop.ini")
						except FileNotFoundError:
							print ("正在为 " + file + " 新建配置信息。")
						except PersmissionError:
							print ("- 你没有对 " + file + " 进行配置的权限，请用管理员身份打开 FolderIconTool。")
						inifile = open(root + "\\" + "desktop.ini","w+")
						inifile.write(iniline)
						print ("正在为 " + file + " 更新配置信息。")
						inifile.close()
						os.system("cd " + root + "&& attrib +h desktop.ini")
						## 将 desktop.ini 设为隐藏
		except:
			print('权限不足，请用管理员身份重新运行 IconTools')
		finally:
			print ("- 执行完毕！配置文件已隐藏。\n")
			print ("=======================================")
			print ("- 请检查图标是否已经替换成功，请按下回车键退出。")
			print ("- 如果尚未替换成功请输入 1 继续。")
			print ("=======================================\n")
			a = str(input("- 输入 1 继续，回车键退出：\n"))
			if (a == "1"):
				print ("=======================================")
				print ("- 是否强制刷新图标缓存？")
				print ("=======================================")
				print ("- 警告：该操作会关闭所有文件夹窗口，仅在图标未更新时使用！\n")
				a = str(input("- 输入 2 继续，回车键退出：\n"))
				if (a == "2"):
					print("\n- 正在关闭 Windows 外壳程序 Explorer")
					os.system("taskkill /f /im explorer.exe")
					print("- 正在清理「系统图标缓存数据库」")
					try:
						os.system("attrib -h -s -r \"%userprofile%\AppData\Local\IconCache.db\"")
						os.system("del /f \"%userprofile%\AppData\Local\IconCache.db\"")
						os.system("attrib /s /d -h -s -r \"%userprofile%\AppData\Local\Microsoft\Windows\Explorer\*\"")
						os.system("del /f \"%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_32.db\"")
						os.system("del /f \"%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_96.db\"")
						os.system("del /f \"%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_102.db\"")
						os.system("del /f \"%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_256.db\"")
						os.system("del /f \"%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_1024.db\"")
						os.system("del /f \"%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_idx.db\"")
						os.system("del /f \"%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_sr.db\"")
					except PersmissionError:
						print ("你没有足够的权限，请用管理员身份打开 FolderIconTool。")
					except WindowsError:
						print ("一部分缓存文件不存在，但这并不影响程序执行。")
					finally:
						print("- 正在清理「系统托盘记忆的图标」")
						try:
							os.system("echo y|reg delete \"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\TrayNotify\" /v IconStreams")
							os.system("echo y|reg delete \"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\TrayNotify\" /v PastIconsStream")
						except PersmissionError:
							print ("你没有足够的权限，请用管理员身份打开 FolderIconTool。")
						except WindowsError:
							print ("没有找到对应注册表，但这并不影响程序执行。")
						print("- 正在重启 Windows 外壳程序 Explorer")
						os.system("start explorer")
						print ("- 在 CMD 中运行可能会出现找不到文件的报错，但不影响正常刷新。")
						print ("（如果图标仍未刷新，请重启电脑。）\n")
						print ("- 执行完毕！")

				b = str(input('按下回车键退出本程序\n'))
				exit()

	else:
		b = str(input('按下回车键退出本程序\n'))
		exit()

## 开始执行

main()

## 结束任务
