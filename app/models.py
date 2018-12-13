#!/usr/bin/env python
# -*-coding:utf-8 -*-
import serial
import struct


class BT809():
  #从809读数
  def get(self,x):
    with serial.Serial('/dev/ttyUSB0',4800,timeout=0.5) as ser:
      ser.write(bytes.fromhex(x))
      fd = ser.readline()
      if len(fd) == 8:
        r =list(struct.unpack('hhbbh',fd))
      return r


if __name__=="__main__":

  print(BT809().get('8181521B'))



