# mynotePython
# My code note for Python study.
#
# Enviroment building
一、For Linux
  一般自带python；
  1.检查Python版本
    $ python
  或
    $ python3

  2.安装文本编辑器Geany
    $ sudo apt-get install geany

  3.运行Hello World程序
    启动Geany
    创建工作文件夹python_work
    选择菜单 File>Save As, 将当前的空文件保存到python_work, 并将其命名为 hello.py 
    保存后，在其中输入代码：
      printf("Hello Python world!")
    当有多个版本时，可选择菜单 Build > Set Build Commands (设置生成命令)，修改Compile（编译）和Execute（执行）后的命令为需要的；
    至此，可选择菜单 单击执行 或 按 F5 执行；