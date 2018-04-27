import uuid
from psutil import net_if_addrs

def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

def get_mac_address_s():
    for k,v in net_if_addrs().items():
        for item in v:
            print(item)
            address = item[1]
            print(address)
            if '-' in address and len(address) ==17:
                print(address)


if __name__ == '__main__':
    mac = get_mac_address_s()
    print(mac)
    print(net_if_addrs().items())