import smbus
bus = smbus.SMBus(1)
address = 0x48
temp1 = bus.read_byte_data(address,0x00)
print temp1*9/5+32