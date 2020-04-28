from asterisk.ami import AMIClient, AutoReconnect
import time
import socket
import json
import sys
import logging


logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s\n')


def event_listener(event, **kwargs):
    logging.info('ami client -> '+str(event))


ami_ip = "192.168.5.73"
ami_port = 5038
ami_user = 'bear' 
ami_secret='GJKBvth22'


client = AMIClient(address=ami_ip, port=ami_port)

AutoReconnect(client)

try:
    future = client.login(username=ami_user, secret=ami_secret)
except:
    raise Exception('ami client login failed')

time.sleep(0.5)

if future.response.is_error():
    raise Exception(str(future.response))

client.add_event_listener(event_listener)

