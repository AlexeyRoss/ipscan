import socket
import sys
host = input('Vvedite IP ')
ports_q = input('Vse porti? Y/N')
if ports_q == 'Y' or ports_q == 'y':
    ports = range(1,65535)
elif ports_q == 'N' or ports_q == 'n' :
    ports = [20,21,22,23,25,42,43,53,67,69,80,110,115,123,137,138,139,143,161,179,443,445,514,515,993,1433,3389,5432]
else:
    ports = map(int, input('Togda vvedite porti cherez probel: ').split(' '))

for port in ports:
  s = socket.socket()
  s.settimeout(1)
  try:
    s.connect((host,port))
  except socket.error:
    pass
  else:
    s.close
    print(host + ':' + str(port)+ ' --active')
