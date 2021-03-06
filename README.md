# LC_Python
### 人生苦短，我用python；Python就是一个'万金油';在python里面一切接对象；
 - Python官网：https://www.python.org/
 - Python 标准库：https://docs.python.org/zh-cn/3/library/index.html
 - 标准库以外还存在成千上万并且不断增加的其他组件(从单独的程序、模块、软件包直到完整的应用开发框架)，访问Python包管理工具pip即可获取这些第三方包：https://pypi.org/
 - 三方库：所谓三方库，是指非公司内部开发和使用的，也不是来自于官方标准库的Python模块，这些模块通常由其他公司、组织或个人开发，所以被称为三方库。虽然Python语言的标准库虽然已经提供了诸多模块来方便我们的开发，但是对于一个强大的语言来说，它的生态圈一定也是非常繁荣的。
 - Python入门文档：https://docs.pythontab.com/

### 优点：
 - 解释性语言
 - 交互式语言(方便测试 比如：ipython...)
 - 面向对象语言
 - 跨平台语言
 - 开发效率高学习成本低
 - 可移植/可扩展/可嵌入式
 - 提供丰富的库

### 缺点：
 - 运行速度慢-》相对，可以通过cpython解决。
 - 代码不能加密-》python主要用于研究，实现功能。
 - 慢和不能加密问题：python核心逻辑-》封装成C语言，可以提升效率和实现加密。


### Python应用领域和职业发展分析

简单的说，Python是一个“优雅”、“明确”、“简单”的编程语言。

 - 学习曲线低，非专业人士也能上手
 - 开源系统，拥有强大的生态圈
 - 解释型语言，完美的平台可移植性
 - 动态类型语言，支持面向对象和函数式编程
 - 代码规范程度高，可读性强

Python在以下领域都有用武之地。

 - 后端开发 - Python / Java / Go / PHP
 - DevOps - Python / Shell / Ruby
 - 数据采集 - Python / C++ / Java
 - 量化交易 - Python / C++ / R
 - 数据科学 - Python / R / Julia / Matlab
 - 机器学习 - Python / R / C++ / Julia
 - 自动化测试 - Python / Shell

作为一名Python开发者，根据个人的喜好和职业规划，可以选择的就业领域也非常多。

- Python后端开发工程师（服务器、云平台、数据接口）
- Python运维工程师（自动化运维、SRE、DevOps）
- Python数据分析师（数据分析、商业智能、数字化运营）
- Python数据挖掘工程师（机器学习、深度学习、算法专家）
- Python爬虫工程师
- Python测试工程师（自动化测试、测试开发）

> **说明**：目前，**数据分析和数据挖掘是非常热门的方向**，因为不管是互联网行业还是传统行业都已经积累了大量的数据，各行各业都需要数据分析师从已有的数据中发现更多的商业价值，从而为企业的决策提供数据的支撑，这就是所谓的数据驱动决策。

给初学者的几个建议：

- Make English as your working language. （让英语成为你的工作语言）
- Practice makes perfect. （熟能生巧）
- All experience comes from mistakes. （所有的经验都源于你犯过的错误）
- Don't be one of the leeches. （不要当伸手党）
- Either outstanding or out. （要么出众，要么出局）

### Day01~15 - [Python语言基础](./Day01-15)

#### Day01 - [初识Python](./Day01-15/01.初识Python.md)

- Python简介 - Python的历史 / Python的优缺点 / Python的应用领域
- 搭建编程环境 - Windows环境 / Linux环境 / MacOS环境
- 从终端运行Python程序 - Hello, world / `print`函数 / 运行程序
- 使用IDLE - 交互式环境(REPL) / 编写多行代码 / 运行程序 / 退出IDLE
- 注释 - 注释的作用 / 单行注释 / 多行注释

#### Day02 - [语言元素](./Day01-15/02.语言元素.md)

- 程序和进制 - 指令和程序 / 冯诺依曼机 / 二进制和十进制 / 八进制和十六进制
- 变量和类型 - 变量的命名 / 变量的使用 / `input`函数 / 检查变量类型 / 类型转换
- 数字和字符串 - 整数 / 浮点数 / 复数 / 字符串 / 字符串基本操作 / 字符编码
- 运算符 - 数学运算符 / 赋值运算符 / 比较运算符 / 逻辑运算符 / 身份运算符 / 运算符的优先级
- 应用案例 - 华氏温度转换成摄氏温度 / 输入圆的半径计算周长和面积 / 输入年份判断是否是闰年

#### Day03 - [分支结构](./Day01-15/03.分支结构.md)

- 分支结构的应用场景 - 条件 / 缩进 / 代码块 / 流程图
- if语句 - 简单的`if` / `if`-`else`结构 / `if`-`elif`-`else`结构 / 嵌套的`if`
- 应用案例 - 用户身份验证 / 英制单位与公制单位互换 / 掷骰子决定做什么 / 百分制成绩转等级制 / 分段函数求值 / 输入三条边的长度如果能构成三角形就计算周长和面积

#### Day04 - [循环结构](./Day01-15/04.循环结构.md)

- 循环结构的应用场景 - 条件 / 缩进 / 代码块 / 流程图
- while循环 - 基本结构 / `break`语句 / `continue`语句
- for循环 - 基本结构 / `range`类型 / 循环中的分支结构 / 嵌套的循环 / 提前结束程序 
- 应用案例 - 1~100求和 / 判断素数 / 猜数字游戏 / 打印九九表 / 打印三角形图案 / 猴子吃桃 / 百钱百鸡

#### Day05 - [构造程序逻辑](./Day01-15/05.构造程序逻辑.md)

- 经典案例：水仙花数 / 百钱百鸡 / Craps赌博游戏
- 练习题目：斐波那契数列 / 完美数 / 素数

#### Day06 - [函数和模块的使用](./Day01-15/06.函数和模块的使用.md)

- 函数的作用 - 代码的坏味道 / 用函数封装功能模块
- 定义函数 - `def`关键字 / 函数名 / 参数列表 / `return`语句 / 调用自定义函数
- 调用函数 - Python内置函数 /  导入模块和函数
- 函数的参数 - 默认参数 / 可变参数 / 关键字参数 / 命名关键字参数
- 函数的返回值 - 没有返回值  / 返回单个值 / 返回多个值
- 作用域问题 - 局部作用域 / 嵌套作用域 / 全局作用域 / 内置作用域 / 和作用域相关的关键字
- 用模块管理函数 - 模块的概念 / 用自定义模块管理函数 / 命名冲突的时候会怎样（同一个模块和不同的模块）

#### Day07 - [字符串和常用数据结构](./Day01-15/07.字符串和常用数据结构.md)

- 字符串的使用 - 计算长度 / 下标运算 / 切片 / 常用方法
- 列表基本用法 - 定义列表 / 用下表访问元素 / 下标越界 / 添加元素 / 删除元素 / 修改元素 / 切片 / 循环遍历
- 列表常用操作 - 连接 / 复制(复制元素和复制数组) / 长度 / 排序 / 倒转 / 查找
- 生成列表 - 使用`range`创建数字列表 / 生成表达式 / 生成器
- 元组的使用 - 定义元组 / 使用元组中的值 / 修改元组变量 / 元组和列表转换
- 集合基本用法 - 集合和列表的区别 /  创建集合 / 添加元素 / 删除元素 /  清空
- 集合常用操作 - 交集 / 并集 / 差集 / 对称差 / 子集 / 超集
- 字典的基本用法 - 字典的特点 / 创建字典 / 添加元素 / 删除元素 / 取值 / 清空
- 字典常用操作 - `keys`方法 / `values`方法 / `items`方法 / `setdefault`方法
- 基础练习 - 跑马灯效果 / 列表找最大元素 / 统计考试成绩的平均分 / Fibonacci数列 / 杨辉三角
- 综合案例 - 双色球选号 / 井字棋

#### Day08 - [面向对象编程基础](./Day01-15/08.面向对象编程基础.md)

- 类和对象 - 什么是类 / 什么是对象 / 面向对象其他相关概念
- 定义类 - 基本结构 / 属性和方法 / 构造器 / 析构器 / `__str__`方法
- 使用对象 - 创建对象 / 给对象发消息
- 面向对象的四大支柱 - 抽象 / 封装 / 继承 / 多态
- 基础练习 - 定义学生类 / 定义时钟类 / 定义图形类 / 定义汽车类

#### Day09 - [面向对象进阶](./Day01-15/09.面向对象进阶.md)

- 属性 - 类属性 / 实例属性 / 属性访问器 / 属性修改器 / 属性删除器 / 使用`__slots__`
- 类中的方法 - 实例方法 / 类方法 / 静态方法
- 运算符重载 - `__add__` / `__sub__` / `__or__` /`__getitem__` / `__setitem__` / `__len__` / `__repr__` / `__gt__` / `__lt__` / `__le__` / `__ge__` / `__eq__` / `__ne__` / `__contains__` 
- 类(的对象)之间的关系 - 关联 / 继承 / 依赖
- 继承和多态 - 什么是继承 / 继承的语法 / 调用父类方法 / 方法重写 / 类型判定 / 多重继承 / 菱形继承(钻石继承)和C3算法
- 综合案例 - 工资结算系统 / 图书自动折扣系统 / 自定义分数类

#### Day10 - [图形用户界面和游戏开发](./Day01-15/10.图形用户界面和游戏开发.md)

- 使用`tkinter`开发GUI程序
- 使用`pygame`三方库开发游戏应用
- “大球吃小球”游戏

#### Day11 - [文件和异常](./Day01-15/11.文件和异常.md)

- 读文件 - 读取整个文件 / 逐行读取 / 文件路径
- 写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件
- 异常处理 - 异常机制的重要性 / `try`-`except`代码块 / `else`代码块 / `finally`代码块 / 内置异常类型 / 异常栈 / `raise`语句
- 数据持久化 - CSV文件概述 / `csv`模块的应用 / JSON数据格式 / `json`模块的应用

#### Day12 - [字符串和正则表达式](./Day01-15/12.字符串和正则表达式.md)

- 字符串高级操作 - 转义字符 / 原始字符串 / 多行字符串 / `in`和`not in`运算符 / `is_xxx`方法 / `join`和`split`方法 / `strip`相关方法 / `pyperclip`模块 / 不变字符串和可变字符串 / `StringIO`的使用
- 正则表达式入门 - 正则表达式的作用 / 元字符 / 转义 / 量词 / 分组 / 零宽断言 /贪婪匹配与惰性匹配懒惰 / 使用`re`模块实现正则表达式操作（匹配、搜索、替换、捕获）
- 使用正则表达式 - `re`模块 / `compile`函数 / `group`和`groups`方法 / `match`方法 / `search`方法 / `findall`和`finditer`方法 / `sub`和`subn`方法 / `split`方法
- 应用案例 - 使用正则表达式验证输入的字符串

#### Day13 - [进程和线程](./Day01-15/13.进程和线程.md)

- 进程和线程的概念 - 什么是进程 / 什么是线程 / 多线程的应用场景
- 使用进程 - `fork`函数 / `multiprocessing`模块 / 进程池 / 进程间通信
- 使用线程 -  `threading`模块 / `Thread`类 / `RLock`类 / `Condition`类 / 线程池

#### Day14 - [网络编程入门和网络应用开发](./Day01-15/14.网络编程入门和网络应用开发.md)

- 计算机网络基础 - 计算机网络发展史 / “TCP-IP”模型 / IP地址 / 端口 / 协议 / 其他相关概念
- 网络应用模式 - “客户端-服务器”模式 / “浏览器-服务器”模式
- 基于HTTP协议访问网络资源 - 网络API概述 / 访问URL / `requests`三方库 / 解析JSON格式数据
- Python网络编程 - 套接字的概念 / `socket`模块 /  `socket`函数 / 创建TCP服务器 / 创建TCP客户端 / 创建UDP服务器 / 创建UDP客户端
- 电子邮件 - SMTP协议 / POP3协议 / IMAP协议 / `smtplib`模块 / `poplib`模块 / `imaplib`模块
- 短信服务 - 调用短信服务网关

#### Day15 - [图像和文档处理](./Day01-15/15.图像和办公文档处理.md)

- 用Pillow处理图片 - 图片读写 / 图片合成 / 几何变换 / 色彩转换 / 滤镜效果
- 读写Word文档 - 文本内容的处理 / 段落 / 页眉和页脚 / 样式的处理
- 读写Excel文件 - `xlrd` / `xlwt` / `openpyxl`

### Day16~Day20 - [Python语言进阶 ](./Day16-20/16-20.Python语言进阶.md)

- 常用数据结构
- 函数的高级用法 - “一等公民” / 高阶函数 / Lambda函数 / 作用域和闭包 / 装饰器
- 面向对象高级知识 - “三大支柱” / 类与类之间的关系 / 垃圾回收 / 魔术属性和方法 / 混入 / 元类 / 面向对象设计原则 / GoF设计模式
- 迭代器和生成器 - 相关魔术方法 / 创建生成器的两种方式 / 
- 并发和异步编程 - 多线程 / 多进程 / 异步IO / `async`和`await`
