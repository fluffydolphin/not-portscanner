import socket
import argparse
import time
import sys


parser = argparse.ArgumentParser(
    description="not-portscanner, is a simple port scanner"
)

parser.add_argument("host", nargs="?", help="Address of the Server")


parser.add_argument(
    "-p", "--port", default=1000, help="the range of ports that will be scanned", type=int
)


args = parser.parse_args()

if not args.host:
    print("Host required! \n")
    parser.print_help()
    sys.exit(1)


print("""
              _                        _                                       
             | |                      | |                                      
  _ __   ___ | |_     _ __   ___  _ __| |_ ___  ___ __ _ _ __  _ __   ___ _ __ 
 | '_ \ / _ \| __|   | '_ \ / _ \| '__| __/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
 | | | | (_) | |_    | |_) | (_) | |  | |_\__ \ (_| (_| | | | | | | |  __/ |   
 |_| |_|\___/ \__|   | .__/ \___/|_|   \__|___/\___\__,_|_| |_|_| |_|\___|_|   
                     | |                                                       
                     |_|                                                                                                            
                 not portscanner v 1.0 | fluffydolphin
""")


startTime = time.time()
open_ports = 0

for i in range(0, args.port):
    host = args.host
    port = i
    timeout_seconds = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout_seconds)
    result = sock.connect_ex((host,int(port)))
    if result == 0:
        print("Host: {}, Port: {}".format(host, port))
    else:
        continue
    sock.close()
    open_ports += 1
print("\nOpen ports: " + str(open_ports))
executionTime = (time.time() - startTime)
executionTime = int(executionTime)
print('Execution time in seconds: ' + str(executionTime) + "\n")