#!/usr/bin/env python3

import socket, time, sys

ip = "192.168.1.9"
port = 9999
timeout = 5
string ="A" * 100
username ="0xdigimon"

conn=True
while conn:
  try:
    with socket.socket(socket.AF_INET,socket. SOCK_STREAM) as d:
      d.settimeout(timeout)
      d.connect((ip,port))
      d.recv(1024)
      d.send(bytes(username, "latin-1"))
      d.recv(1024)
      print("Fuzzing with {} bytes".format(len(string)))
      d.send(bytes(string, "latin-1"))
      d.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(string)))
    sys.exit(0)
  d.close()
  string += 100 * "A"
  time.sleep(1)

