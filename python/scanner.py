import socket
from datetime import datetime


def display_port(open_ports):
    for port in open_ports:
        try :
            service = socket.getservbyport(port)
        except:
            service = "unknown"
        print(f"port:{port} >> {service}")



    
def scan_port(target,port):
    s = socket.socket()
    s.settimeout(0.4)
    result = s.connect_ex((target, port))
    s.close()
    return result == 0



def scan_target(target , start_port,end_port):
    print("-"*50)
    print(f"target : {target}")
    try : 
        ip = socket.gethostbyname(target)
        print(f"tracking IP : {ip}")
    except socket.gaierror:
        print("Hostname couldn't resolved ")
        return 
    print(f"scanning ports from {start_port} to {end_port}")
    print(f"port scanning started")
    start_time = datetime.now()
    print("-"*50)

    open_ports =[]

    for port in range(start_port,end_port+1):
        if scan_port(target,port):
            open_ports.append(port)

    stop_time = datetime.now()
    print("-"*50)
    print(f"scan completed in {stop_time - start_time}\n {len(open_ports)} open ports found")
    display_port(open_ports)

target = input("enter the target:")
start_port = int(input("enter the start_port:"))
end_port = int(input("enter the end_port:"))

scan_target(target, start_port, end_port)
