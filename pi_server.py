import TvMountStepper
from socket import *
from time import ctime
import RPi.GPIO as GPIO
from flask import Flask, redirect, url_for, request
pi_server = Flask(__name__)

# TvMountStepper.setup()



@pi_server.route('/')
def android():
        ctrCmd = ['Clockwise','CounterClockwise']
        HOST = ''
        PORT = 21567
        BUFSIZE = 1024
        ADDR = (HOST,PORT)
        tcpSerSock = socket(AF_INET, SOCK_STREAM)
        tcpSerSock.bind(ADDR)
        tcpSerSock.listen(5)
        try:
                tcpCliSock,addr = tcpSerSock.accept()
                print '...connected from :', addr
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                break
                        if data == ctrCmd[0]:
                                TvMountStepper.rotateClockwise()
                                print 'Rotated Clockwise'
                        if data == ctrCmd[1]:
                                TvMountStepper.rotateCounterClockwise()
                                print 'Rotated Counter Clockwise'
        except KeyboardInterrupt:
               # Servomotor.sclose()
               GPIO.cleanup()
               tcpSerSock.close();

@pi_server.route('/counterclockwise')
def counterclockwise():
        #print 'Waiting for connection'
        #tcpCliSock,addr = tcpSerSock.accept()
        #print '...connected from :', addr
        try:
                TvMountStepper.rotateCounterClockwise()
                print 'Rotated Counter Clockwise'
        except KeyboardInterrupt:
                GPIO.cleanup()
                #tcpSerSock.close();
               
@pi_server.route('/clockwise')
def clockwise():
#        while True:
#                print 'Waiting for connection'
#                tcpCliSock,addr = tcpSerSock.accept()
#                print '...connected from :', addr
        try:
                TvMountStepper.rotateClockwise()
                print 'Rotated Clockwise'        
        except KeyboardInterrupt:
               # Servomotor.close()
               GPIO.cleanup()
               #tcpSerSock.close();

if __name__ == '__main__':
        pi_server.run(debug=True, host='0.0.0.0', port=int("21478"))
