
# import ntplib
# from time import ctime

# import argparse
# import time
# import sys
# import struct
# import socket
# from binascii import hexlify


# def print_machine_info():
#     host_name = socket.gethostname()
#     ip_address = socket.gethostbyname(host_name)
#     print(f"Host name : {host_name}")
#     print(f"Ip address : {ip_address}")


# if __name__ == '__main__':
#     print_machine_info()


# def convert_ip4_address():
#     for ip_addr in ['127.0.0.1', '192.168.0.1']:
#         packed_ip_addr = socket.inet_aton(ip_addr)
#         unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
#         print(f"IP ADDRESS : {ip_addr} => "
#               f"packed : {hexlify(packed_ip_addr)}, "
#               f"Unpacked : {unpacked_ip_addr}")


# if __name__ == '__main__':
#     convert_ip4_address()


# def find_service_name():
#     protocol_name = 'tcp'
#     for port in [80, 25]:
#         try:
#             service_name = socket.getservbyport(port, protocol_name)
#             print(f"Port : {port} => Service name : {service_name}")
#         except OSError:
#             print(f"Port : {port} => Service name not found")

#     try:
#         udp_port = 53
#         udp_service_name = socket.getservbyport(udp_port, 'udp')
#         print(f"Port : {udp_port} => Service name : {udp_service_name}")
#     except OSError:
#         print(f"Port : {udp_port} => Service name not found")


# if __name__ == '__main__':
#     find_service_name()

# NTP_SERVER = "0.uk.pool.ntp.org"
# TIME1970 = 2208988800


# def sntp_client():
#     client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     data = '\x1b' + 47 * '\0'
#     client.sendto(data.encode(), (NTP_SERVER, 123))
#     data, address = client.recvfrom(1024)
#     if data:
#         print(f"Response received from : {address}")
#         t = struct.unpack('!12I', data)[10]
#         t -= TIME1970
#         print(f'\tTime={time.ctime(t)}')


# if __name__ == "__main__":
#     sntp_client()

import ntplib
from time import ctime


def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print(
        f"Response received from : pool.ntp.org, Time={ctime(response.tx_time)}")


if __name__ == "__main__":
    print_time()
