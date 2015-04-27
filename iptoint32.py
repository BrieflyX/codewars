'''
Convert an ip address to a 32-bit int.
'''
def ip_to_int32(ip):
  # your code here
  return reduce(lambda x,y: (x << 8) + y, map(int, ip.split('.')))

if __name__ == '__main__':
    print ip_to_int32('128.114.17.104')