[TOC]

## 前言

[![build status](https://secure.travis-ci.org/maxcountryman/flask-login.png?branch=master)](https://travis-ci.org/#!/maxcountryman/flask-login)

用Flask框架，`SQLalchemy`,`SQlite` ,` Bootstrap` ,`Pyserial`搭建一个温度监控系统。

结构示意图：
![](https://img2018.cnblogs.com/blog/720033/201812/720033-20181210182519634-1172375356.png)


### 项目前提 ：

- 温度传感器pt100获取温度模拟信号AS
- 信号AS通过温控仪表BT809转换为数字信号DS
- 要求：对数字信号DS加工,实现Web操控

### 控制流程：

上位机每向通道发一条指令，仪表送回一次数据

- 上位机：Raspberry Pi(树莓派)
- 下位机：BT809
- 通信协议：BTBUS_BT800、RS485

### 技术栈

- 数据库：SQLite
- 数据库ORM：SQLAlchemy
- 路由框架：Flask
- CSS框架：Bootstrap
- 前后同步：SocketIO
- 通信接口：Pyserial
- 通信解包：Struct


