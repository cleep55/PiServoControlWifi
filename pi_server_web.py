import TvMountStepper
from socket import *
from time import ctime
import RPi.GPIO as GPIO

# TvMountStepper.setup()

ctrCmd = ['Clockwise','CounterClockwise']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

@pi_server_web.route('/')
def android():
        while True:
                print 'Waiting for connection'
                tcpCliSock,addr = tcpSerSock.accept()
                print '...connected from :', addr
                try:
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
                        # Servomotor.close()
                        GPIO.cleanup()
        tcpSerSock.close();
@pi_server_web.route('/counterclockwise')
def counterclockwise():
        while True:
                print 'Waiting for connection'
                tcpCliSock,addr = tcpSerSock.accept()
                print '...connected from :', addr
                try:
                        TvMountStepper.rotateCounterClockwise()
                        print 'Rotated Counter Clockwise'
                except KeyboardInterrupt:
                        # Servomotor.close()
                        GPIO.cleanup()
        tcpSerSock.close();
@pi_server_web.route('/clockwise')
def clockwise():
        while True:
                print 'Waiting for connection'
                tcpCliSock,addr = tcpSerSock.accept()
                print '...connected from :', addr
                try:
                        TvMountStepper.rotateClockwise()
                        print 'Rotated Clockwise'        
                except KeyboardInterrupt:
                        # Servomotor.close()
                        GPIO.cleanup()
        tcpSerSock.close();
