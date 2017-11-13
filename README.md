# FolderIconTool README

A little tool for Windows folder icon.

## How to use it

1. Put one icon in every folder, like this.

```
D:\
|- Common Documents
|-|- Tools
|-|-|- Tools.ico
|-|- Pages
|-|-|- Pages.ico
|-|- Games
|-|-|- Game Center.ico
|-|- Movies
|-|-|- Movie.ico
```

2. Put FolderIconTool in the "Common Documents".

3. FolderIconTool will replace the every folders' icon.

Enjoy it !

## WARNING

1. FolderIconTool is secure, it only modifies the `.ini` configuration file. But on the safe side, you'd better try in the empty folder first before use it in the important folder.

2. If there are multiple `.ico` files in the same folder, FolderIconTool will automatically select the last icon as the folder icon.

3. If you refresh the icon cache in the last step and the icon is not changed, just restart the system.


# FolderIconTool 中文说明

一个批量修改 Windows 文件夹图标的小工具。

## 使用方法

1. 你只需要把喜欢的图标放进各个文件夹中，就像这样——

```
D:\
|- 常用文件
|-|- 工具库
|-|-|- Tools.ico
|-|- 文档库
|-|-|- Pages.ico
|-|- 游戏库
|-|-|- Game Center.ico
|-|- 视频库
|-|-|- Movie.ico
```

2. 然后将 FolderIconTool 放在「常用文件」这个文件夹中。

3. 运行 FolderIconTool，就可以自动将该目录下的所有文件夹添加图标。

## 注意事项

1. 尽管 FolderIconTool 很安全，只会修改 `.ini` 配置文件，但在对重要文件夹设置图标之前。最好先在空文件夹中尝试一下，以免与预期不符。

2. 如果同一文件夹中有多个 `.ico` 文件，自动选取最后的图标作为文件夹图标。

3. 如果在最后一步刷新了图标缓存，图标依然没有更换，只需要重启系统即可。

4. 我生成了一个测试版的 `.exe`，但是目前很不稳定，如果电脑上有 python 3.5，建议使用 .py 直接运行。

# Update log

## Nov 13, 2017 - Update FolderIconTool 0.0.5

Renamed as FolderIconTool.

Add FolderIconTool.exe releases.

## Nov 13, 2017 - Update FolderIconTool 0.0.4

Forced refresh function is added.

Add more description.

Fix some bug about System permission.

## Nov 9, 2017 - Update IconTool 0.0.3

A version that can be used normally.

Put `.ico` file in every folder, then start the IconTool.py.

## Nov 9, 2017 - Update IconTool 0.0.2

Rebuild the IconTool.

## Oct 30, 2017 - Update IconTool 0.0.1

The new project IconTool.
