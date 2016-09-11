from lcddriver import lcd
from time import time
from time import sleep
import psutil
import socket
import fcntl
import struct

# Get the IP address of the PI
def get_ip_address(ifname):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  return socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8915,  # SIOCGIFADDR
    struct.pack('256s', ifname[:15])
  )[20:24])

lcd = lcd()

while True:
  # Display system stats
  temp = round(int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3,2)
  lcd.display_string("CPU  : "+str(psutil.cpu_percent()) + '% - ' + str(temp) + 'C',1)

  # Display memory stats  
  memory = psutil.virtual_memory()
  # Divide from Bytes -> KB -> MB
  available = round(memory.available/1024.0/1024.0,1)
  total = round(memory.total/1024.0/1024.0,1)
  lcd.display_string("Mem  : " + str(total) + 'MB/' + str(memory.percent) + '%',2)

  # Display Disk stats
  disk = psutil.disk_usage('/')
  # Divide from Bytes -> KB -> MB -> GB
  free = round(disk.free/1024.0/1024.0/1024.0,1)
  total = round(disk.total/1024.0/1024.0/1024.0,1)
  lcd.display_string("Disk : "+str(total) + 'GB/' + str(disk.percent) + '% ',3)

  # Display Network info
  #lcd_string("wlan : " + get_ip_address('eth0'),LCD_LINE_4)
  lcd.display_string("wlan : " + get_ip_address('wlan0'),4)

  sleep(30)
