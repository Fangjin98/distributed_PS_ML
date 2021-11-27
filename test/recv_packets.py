import argparse
import socket
import sys

import torch

from header_config import *
from utils.NGAPacket import *

sys.path.append("..")

from utils.comm_utils import *

ETH_P_ALL = 0x3

parser = argparse.ArgumentParser(description='Packet Sender')
parser.add_argument('--ip', type=str, default='172.16.160.3')

args = parser.parse_args()

if __name__ == "__main__":
    listen_ip = args.ip
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, NGA_TYPE)
    s.bind((listen_ip, 0))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024*1024*1024)
    print("Recv buff: {}".format(s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)))
    print("Get data from {}...".format(listen_ip))
    count = 0
    while True:

        raw_data = s.recvfrom(HEADER_BYTE + DATA_BYTE)[0]
        count += 1
        # nga_header = NGAHeader(raw_data[:HEADER_BYTE])
        # print("Workerid and sequenceid: {} {}".format(nga_header.workermap, nga_header.sequenceid))
        # if nga_header.sequenceid == -1:
        #     break
        # nga_payload = NGAPayload(raw_data[HEADER_BYTE:])

        # print("Protocol: {} {}->{}".format(nga_header.protocol, nga_header.src_address, nga_header.dst_address))
        # tensor = torch.Tensor(nga_payload.data)
        # print(tensor)