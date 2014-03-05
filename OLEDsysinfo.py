# OLEDip.py

# Meant for use with the Raspberry Pi and an Adafruit monochrome OLED display!

# This program interfaces with the OLED display in order to print your current IP address to it. The program trys
# several methods in order to accquire an IP address. For example if you are using a WiFi dongle your IP will be 
# different to when you are using a Ethernet cable. This program tests for both and if it can not detect one prints:
# 'NO INTERNET!' to the display. This code is perfect to run on boot when you want to find your Pi's IP address for
# SSH or VNC.

# This was coded by The Raspberry Pi Guy!
# -*- coding: utf-8 -*-
# Imports all of the necessary modules
import gaugette.ssd1306
import time
import sys
import socket
import fcntl
import struct
import commands
import smbus
from time import sleep

# This function allows us to grab any of our IP addresses
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
#poll and display system memory
def rpisysinfo_mem():
    memory         = commands.getoutput( 'free -o | grep "Mem:" | cut -d: -f2' ).lstrip().split()
    led.clear_display()
    intro = 'Status'
    txt = 'Free Memory:'
    TEXT = memory[1]
    led.draw_text2(0,25,TEXT,1)
    led.draw_text2(0,0,intro,2)
    led.draw_text2(0,16, txt, 1)
    led.display()
    sleep(10)
    return
#poll and display system uptime
def rpisysinfo_uptime():
    procfile       = open( "/proc/uptime" )
    contents       = procfile.read().split()
    procfile.close()
    unixtime       = float( contents[0] )
    minute         = 60
    hour           = minute * 60
    day            = hour * 24
    days           = int( unixtime / day )
    hours          = int( ( unixtime % day ) / hour )
    minutes        = int( ( unixtime % hour ) / minute )
    seconds        = int( unixtime % minute )
    uptime         = ''
    if days > 0:
            uptime     += str( days ) + ' ' + ( days == 1 and 'D' or 'D' ) + ' '
    if len ( uptime ) > 0 or hours > 0:
            uptime     += str( hours ) + ' ' + ( hours == 1 and 'H' or 'H' ) + ' '
    if len ( uptime ) > 0 or minutes > 0:
            uptime     += str( minutes ) + ' ' + ( minutes == 1 and 'M' or 'M' ) + ' '
    uptime         += str( seconds ) + ' ' + ( seconds == 1 and 'S' or 'S' )
    TEXT = uptime
    led.clear_display()
    intro = 'Status'
    txt = 'Uptime:'
    led.draw_text2(0,25,TEXT,1)
    led.draw_text2(0,0,intro,2)
    led.draw_text2(0,16, txt, 1)
    led.display()
    sleep(10)
    return
def rpisysinfo_cpu_temp():
    tempSrc_cpu    = open( "/sys/class/thermal/thermal_zone0/temp" )
    tripSrc_cpu    = open( "/sys/class/thermal/thermal_zone0/trip_point_0_temp" )
    temp_cpu       = tempSrc_cpu.read()
    trip_cpu       = tripSrc_cpu.read()
    tempSrc_cpu.close()
    tripSrc_cpu.close()
    temp_cpu_c     = float( temp_cpu ) / 1000
    temp_cpu_f     = ( 1.8 * temp_cpu_c ) + 32
    trip_cpu_c     = float( trip_cpu ) / 1000
    trip_cpu_f     = ( 1.8 * trip_cpu_c ) + 32
    TEXT = str(temp_cpu_f)
    led.clear_display()
    intro = 'Status'
    txt = 'CPU Temp F:'
    led.draw_text2(0,25,TEXT,1)
    led.draw_text2(0,0,intro,2)
    led.draw_text2(0,16, txt, 1)
    led.display()
    sleep(10)

    return
#Poll external TEMP102 sensor via I2C
def rpisysinfo_ext_temp():
    bus = smbus.SMBus(1)
    address = 0x48
    temp1 = bus.read_byte_data(address,0x00)
    TEXT = str(temp1*9/5+32)
    led.clear_display()
    intro = 'Status'
    txt = 'Ext Temp F:'
    led.draw_text2(0,25,TEXT,1)
    led.draw_text2(0,0,intro,2)
    led.draw_text2(0,16, txt, 1)
    led.display()
    sleep(10)
# Sets our variables to be used later
RESET_PIN = 15
DC_PIN    = 16
TEXT = ''

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()
while True:
# This sets TEXT equal to whatever your IP address is, or isn't
    try:
        TEXT = get_ip_address('wlan0') # WiFi address of WiFi adapter. NOT ETHERNET
    except IOError:
        try:
            TEXT = get_ip_address('eth0') # WiFi address of Ethernet cable. NOT ADAPTER
        except IOError:
            TEXT = ('NO INTERNET!')

    # Display system IP
    led.clear_display()
    intro = 'Status'
    txt = 'Your IP Address is:'
    led.draw_text2(0,25,TEXT,1)
    led.draw_text2(0,0,intro,2)
    led.draw_text2(0,16, txt, 1)
    led.display()
    sleep(10)
    rpisysinfo_uptime()
    rpisysinfo_mem()
    rpisysinfo_cpu_temp()
    rpisysinfo_ext_temp()

