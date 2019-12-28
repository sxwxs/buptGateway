# BUPT Gateway Login

用于登录北京邮电大学校园网的命令行程序。跨平台，但仅支持 Python 3。

可以从文件读取用户名和密码自动登录，或者通过参数指定用户名密码，也可以交互式输入用户名密码。

## 安装

`pip install buptgw`

建议使用[清华大学 pip 源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)，速度快，且支持 IPv6（校园网电脑无需登录网络即可通过 IPv6 访问）

`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple buptgw`

如果你没有 root 权限，可以添加 `--user` 参数即

`pip install buptgw --user` 或
`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple buptgw --user`

## 使用

登录 `buptgw -i` 

退出 `buptgw -o`

保存用户名密码到文件（下次登录无需手动输入） `buptgw -w`  

### 全部参数

```
Usage: buptgw -i|-o|-w  [-c <config_file>] [-u <username>] [-p <password>]
    -i                login
    -o                logout
    -w                write username and password to config file
    -c <config_path>  config file path, optional, defualt is ~/.buptgw
    -u <username>
    -p <password>
```

参数 `-i` 代表登录 `-o` 代表退出，`-w` 把用户名和密码写入配置文件，这三个只能选择一个

`-c` 指定配置文件路径（存储用户名和密码），对 `-i` 和 `-w` 有效。如果不指定配置文件，默认为 ~/.buptgw。

`-u` 指定用户名，如果不指定，会从配置文件读取，如果读取失败则要求输入

`-p` 指定密码，如果不指定，则要求输入（如果用户名也没输入则一并从配置文件读取）

### 在 python 中调用

```python
import buptgw

buptgw.login('2018xxxxxx', 'passwd') # 登录，xxx 处替换为正确的学号和密码
buptgw.logout() # 退出
```

### 实现开机自动登录

#### window

windows 下编写 bat 文件（xxx 处替换为正确的学号和密码），例如保存为 network.bat （**注意，不能**保存为 buptgw.bat 这样会导致这个文件自己调用自己）

```bat
buptgw -i -u 2018xxxxxx -p xxxxx
```

然后把这个文件放到系统的启动目录下，一般来说，通过运行（快捷键是 win + R），输入 `shell:startup ` 可以快速打开启动目录。

#### Linux

把登录命令写入 ~/.profile 中





作者博客 ：https://codeplot.top