#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask_socketio import SocketIO, emit
import time
import serial
import struct

#从809读数
class BT809():
  def get(self,x):
      with serial.Serial('/dev/ttyUSB0',4800,timeout=1) as ser:
          ser.write(bytes.fromhex(x))
          return ser.readline()

  #向809中写入数据
  def set(self,x):
      with serial.Serial('/dev/ttyUSB0',4800,timeout=1) as ser:
          ser.write(bytes.fromhex(x))
          return ser.readline()
  #解包
  def upk(self,x):
    return struct.unpack('hhbbh',x)


  #返回真实值列表
  def feed(self,ord):
        bt = BT809()
        fd = bt.get(ord)
        if len(fd) == 8:
          r = list(bt.upk(fd))
        else:
          fd = bt.get(ord)
        return r


if __name__=="__main__":

  print(BT809().feed('8181521B'))



