file=open("/home/devasc/labs/devnet-src/python/devices.txt","r")
devices = []


for item in file:
    item=item.strip()
    devices.append(item)

file.close()

devices[0]="solaris123"

print(devices)
