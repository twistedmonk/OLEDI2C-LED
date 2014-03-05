#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import commands


def rpisysinfo_system():
##    print "###[ SYSTEM       ]#############################################################"
##    hostname       = commands.getoutput( 'uname -n' )
##    print "Hostname ............ : " + hostname
##    procfile       = open( "/proc/cpuinfo" )
##    cpuinfo        = procfile.read().splitlines()
##    procfile.close()
##    cputype        = cpuinfo[1]
##    print "CPU ................. : " + cputype[13:]
##    procfile       = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor" )
##    governor       = procfile.read().replace( '\n', '' )
##    procfile.close()
##    print "Scaling Governor .... : " + governor
##    procfile       = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq" )
##    curcpuclk      = procfile.read().replace( '\n', '' )
##    procfile.close()
##    print  "Current Frequency ... : "  + str( float(curcpuclk) / 1000 ) + "MHz"
##    procfile       = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq" )
##    mincpuclk      = procfile.read().replace( '\n', '' )
##    procfile.close()
##    print "Minimum Frequency ... : " + str( float(mincpuclk) / 1000 ) + "MHz"
##    procfile       = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq" )
##    maxcpuclk      = procfile.read().replace( '\n', '' )
##    procfile.close()
##    print "Maximum Frequency ... : " + str( float(maxcpuclk) / 1000 ) + "MHz"
##    cpufeatures    = cpuinfo[3]
##    print "Features ............ : "+ cpufeatures[11:]
##    bogomips       = cpuinfo[2]
##    print "BogoMIPS ............ : "+ bogomips[11:]
##    hardware       = cpuinfo[10]
##    revision       = cpuinfo[11]
##    if revision[11:].startswith('1'):
##            print "Hardware ............ : " + hardware[11:] + " Revision " + revision[11:] + color["red"] + " (WARRANTY VOID)" + color["nocolor"]
##    else:
##            print "Hardware ............ : " + hardware[11:] + " Revision " + revision[11:]
##    serialnumber   = cpuinfo[12]
##    print "Serialnumber ........ : "+ serialnumber[10:]
##    distro         = commands.getoutput( 'lsb_release -d' )
##    print "Distribution ........ : "+ str( distro[13:] )
##    kernel         = commands.getoutput( 'uname -s' ) + " " + commands.getoutput( 'uname -r' ) + " " + commands.getoutput( 'uname -m' )
##    print "Kernel .............. : " + kernel
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
            uptime     += str( days ) + ' ' + ( days == 1 and 'Day' or 'Days' ) + ' '
    if len ( uptime ) > 0 or hours > 0:
            uptime     += str( hours ) + ' ' + ( hours == 1 and 'Hour' or 'Hours' ) + ' '
    if len ( uptime ) > 0 or minutes > 0:
            uptime     += str( minutes ) + ' ' + ( minutes == 1 and 'Minute' or 'Minutes' ) + ' '
    uptime         += str( seconds ) + ' ' + ( seconds == 1 and 'Second' or 'Seconds' )
    print "Uptime .............. : " + uptime
    memory         = commands.getoutput( 'free -o | grep "Mem:" | cut -d: -f2' ).lstrip().split()
    #swap           = commands.getoutput( 'free -o | grep "Swap:" | cut -d: -f2' ).lstrip().split()
    print "Memory .............. : " + "Total  : " + memory[0] + "KB"
    print "\t\t\tUsed   : " + memory[1] + "KB"
    #print "\t\t\tFree   : " + memory[2] + "KB"
    #print "\t\t\tShared : " + memory[3] + "KB"
    #print "\t\t\tBuffers: " + memory[4] + "KB"
    #print "\t\t\tCached : " + memory[5] + "KB"
    #print "Swap ................ : "+ "Total  : " + swap[0] + "KB"
    #print "\t\t\tUsed   : " + swap[1] + "KB"
    #print "\t\t\tFree   : " + swap[2] + "KB"
    return
rpisysinfo_system()
