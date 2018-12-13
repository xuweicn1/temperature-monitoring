# -*- coding:utf-8 -*-
'''
BT809-and-PT100_Monitor
思路：后端后台线程一旦产生数据，即刻推送至前端。
好处：不需要前端ajax定时查询，节省服务器资源。
'''

import psutil
from threading import Lock
from flask import render_template, session, request
from flask_socketio import SocketIO, emit
import time
import glob
from app.models import BT809
from app import app

async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

# 后台线程 产生数据，即刻推送至前端
def background_thread():
    count = 0
    while True:
        socketio.sleep(10)
        r = BT809().feed('8181521B')
        r[0],r[1] = r[0]/10,r[1]/10
        t = time.strftime('%H:%M:%S', time.localtime()) # 获取系统时间
        socketio.emit('server_response',{'data': [t] + r, 'count': count},namespace='/test')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/h1', methods=['GET', 'POST'])
def h1():
    return render_template('h1.html')

@app.route('/h3', methods=['GET', 'POST'])
def h3():
    return render_template('h3.html')

@app.route('/sock')
def sock():
    return render_template('sock.html', async_mode=socketio.async_mode)

# 与前端建立 socket 连接后，启动后台线程
@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    # socketio.run(app)