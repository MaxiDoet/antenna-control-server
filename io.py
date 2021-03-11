import serial

# Commands are defined here
COMMAND_SET_OUTPUT=0x01
COMMAND_SET_INPUT=0x02
COMMAND_SWITCH=0x03

def io_connect(device):
  try:
    return serial.Serial(device)
  except:
    print("Couldn't connect to device (%s)!" % device)
    return False

def io_write(device, data):
  try:
    device.write(data)
    return True
  except:
    print("Couldn't write data to %s", device.name)
    return False  

  