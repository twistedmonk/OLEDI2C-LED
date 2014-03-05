	
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rpisysinfo.py Version 1.0.2
# Copyright (c) Jochen Blacha <jochen.blacha@gmail.com>
# This script is published under the terms of the GNU General Public License v2
# See http://www.gnu.org/licenses/gpl-2.0.html

def format_clk( clock ):
    while len( clock ) < 8:
            clock = ' ' + str( clock )

    return clock

def rpisysinfo_logo():
    print ""
    print color["green"] + "   .~~.   .~~.   " + color["nocolor"]
    print color["green"] + "  '. \ ' ' / .'  " + color["nocolor"]
    print color["red"]   + "   .~ .~~~..~.   " + color["lred"]    + "                  _                          _ " + color["nocolor"]
    print color["red"]   + "  : .~.'~'.~. :  " + color["lred"]    + "  ___ ___ ___ ___| |_ ___ ___ ___ _ _    ___|_|" + color["nocolor"]
    print color["red"]   + " ~ (   ) (   ) ~ " + color["lred"]    + " |  _| .'|_ -| . | . | -_|  _|  _| | |  | . | |" + color["nocolor"]
    print color["red"]   + "( : '~'.~.'~' : )" + color["lred"]    + " |_| |__,|___|  _|___|___|_| |_| |_  |  |  _|_|" + color["nocolor"]
    print color["red"]   + " ~ .~ (   ) ~. ~ " + color["lred"]    + "             |_|                 |___|  |_|    " + color["nocolor"]
    print color["red"]   + "  (  : '~' :  )  " + color["lred"]    + "\t\t\t\t       System Information v1.0.2" + color["nocolor"]
    print color["red"]   + "   '~ .~~~. ~'   " + color["lred"]    + "\t\t\t\t     Copyright (c) Jochen Blacha" + color["nocolor"]
    print color["red"]   + "       '~'       " + color["lred"]    + "\t\t      ASCII Logo (c) by b3n @ Raspberry Pi Forum" + color["nocolor"]
    print ""
    return

def rpisysinfo_clocks():
    print color["purple"] + "###[ CLOCKS       ]#############################################################" + color["nocolor"]
    clkSrc_arm     = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock arm | cut -d= -f2' )
    clk_arm        = float( clkSrc_arm ) / 1000000
    clk_arm        = "%.3f" % clk_arm
    clk_arm        = format_clk( clk_arm )
    clkSrc_core    = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock core | cut -d= -f2' )
    clk_core       = float( clkSrc_core ) / 1000000
    clk_core       = "%.3f" % clk_core
    clk_core       = format_clk( clk_core )
    print color["lpurple"] + "CPU ................. : " + color["nocolor"] + clk_arm + "MHz\t" + color["lpurple"] + "GPU Core ............ : " + color["nocolor"] + clk_core + "MHz"
    clkSrc_h264    = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock h264 | cut -d= -f2' )
    clk_h264       = float( clkSrc_h264 ) / 1000000
    clk_h264       = "%.3f" % clk_h264
    clk_h264       = format_clk( clk_h264 )
    clkSrc_isp     = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock isp | cut -d= -f2' )
    clk_isp        = float( clkSrc_isp ) / 1000000
    clk_isp        = "%.3f" % clk_isp
    clk_isp        = format_clk( clk_isp )
    print color["lpurple"] + "H.264 Decoder ....... : " + color["nocolor"] + clk_h264 + "MHz\t" + color["lpurple"] + "Image Sensor Pipeline : " + color["nocolor"] + clk_isp + "MHz"
    clkSrc_v3d     = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock v3d | cut -d= -f2' )
    clk_v3d        = float( clkSrc_v3d ) / 1000000
    clk_v3d        = "%.3f" % clk_v3d
    clk_v3d        = format_clk( clk_v3d )
    clkSrc_uart    = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock uart | cut -d= -f2' )
    clk_uart       = float( clkSrc_uart ) / 1000000
    clk_uart       = "%.3f" % clk_uart
    clk_uart       = format_clk( clk_uart )
    print color["lpurple"] + "3D Video ............ : " + color["nocolor"] + clk_v3d + "MHz\t" + color["lpurple"] + "UART ................ : " + color["nocolor"] + clk_uart + "MHz"
    clkSrc_pwm     = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock pwm | cut -d= -f2' )
    clk_pwm        = float( clkSrc_pwm ) / 1000000
    clk_pwm        = "%.3f" % clk_pwm
    clk_pwm        = format_clk( clk_pwm )
    clkSrc_emmc    = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock emmc | cut -d= -f2' )
    clk_emmc       = float( clkSrc_emmc ) / 1000000
    clk_emmc       = "%.3f" % clk_emmc
    clk_emmc       = format_clk( clk_emmc )
    print color["lpurple"] + "PWM ................. : " + color["nocolor"] + clk_pwm + "MHz\t" + color["lpurple"] + "EMMC ................ : " + color["nocolor"] + clk_emmc + "MHz"
    clkSrc_pixel   = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock pixel | cut -d= -f2' )
    clk_pixel      = float( clkSrc_pixel ) / 1000000
    clk_pixel      = "%.3f" % clk_pixel
    clk_pixel      = format_clk( clk_pixel )
    clkSrc_vec     = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock vec | cut -d= -f2' )
    clk_vec        = float( clkSrc_vec ) / 1000000
    clk_vec        = "%.3f" % clk_vec
    clk_vec        = format_clk( clk_vec )
    print color["lpurple"] + "PIXEL ............... : " + color["nocolor"] + clk_pixel + "MHz\t" + color["lpurple"] + "VEC ................. : " + color["nocolor"] + clk_vec + "MHz"
    clkSrc_hdmi    = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock hdmi | cut -d= -f2' )
    clk_hdmi       = float( clkSrc_hdmi ) / 1000000
    clk_hdmi       = "%.3f" % clk_hdmi
    clk_hdmi       = format_clk( clk_hdmi )
    clkSrc_dpi     = commands.getoutput( '/opt/vc/bin/vcgencmd measure_clock dpi | cut -d= -f2' )
    clk_dpi        = float( clkSrc_dpi ) / 1000000
    clk_dpi        = "%.3f" % clk_dpi
    clk_dpi        = format_clk( clk_dpi )
    print color["lpurple"] + "HDMI ................ : " + color["nocolor"] + clk_hdmi + "MHz\t" + color["lpurple"] + "DPI ................. : " + color["nocolor"] + clk_dpi + "MHz"
    return

def rpisysinfo_display():
    print color["purple"] + "###[ DISPLAY      ]#############################################################" + color["nocolor"]
    dispSrc_res    = open( "/sys/class/graphics/fb0/modes" )
    dispSrc_bpp    = open( "/sys/class/graphics/fb0/bits_per_pixel" )
    display_res    = dispSrc_res.read()
    display_bpp    = dispSrc_bpp.read()
    dispSrc_res.close()
    dispSrc_bpp.close()
    print color["lpurple"] + "Framebuffer ......... : " + color["nocolor"] + display_res.replace( 'U:', '' ).replace( '-0', '' ).replace( '\n', '' ) + " @ " + display_bpp.replace( '\n', '' ) + " Bits/pixel"
    return

def rpisysinfo_codecs():
    print color["purple"] + "###[ CODECS       ]#############################################################" + color["nocolor"]
    codec_h264     = commands.getoutput( '/opt/vc/bin/vcgencmd codec_enabled H264 | cut -d= -f2' )
    codec_mpg2     = commands.getoutput( '/opt/vc/bin/vcgencmd codec_enabled MPG2 | cut -d= -f2' )
    codec_wvc1     = commands.getoutput( '/opt/vc/bin/vcgencmd codec_enabled WVC1 | cut -d= -f2' )
    if codec_h264 == "enabled":
            h264_accel = "\t\t(Hardware accelerated)"
    else:
            h264_accel = "\t(Not hardware accelerated)"
    print color["lpurple"] + "H.264 Codec ......... : " + color["nocolor"] + codec_h264 + h264_accel
    if codec_mpg2 == "enabled":
            mpg2_accel = "\t\t(Hardware accelerated)"
    else:
            mpg2_accel = "\t(Not hardware accelerated)"
    print color["lpurple"] + "MPEG-2 Codec ........ : " + color["nocolor"] + codec_mpg2 + mpg2_accel
    if codec_wvc1 == "enabled":
            wvc1_accel = "\t\t(Hardware accelerated)"
    else:
            wvc1_accel = "\t(Not hardware accelerated)"
    print color["lpurple"] + "WMV VC-1 Codec ...... : " + color["nocolor"] + codec_wvc1 + wvc1_accel
    return

def rpisysinfo_voltages():
    print color["purple"] + "###[ VOLTAGES     ]#############################################################" + color["nocolor"]
    volt_core      = commands.getoutput( '/opt/vc/bin/vcgencmd measure_volts core | cut -d= -f2' )
    volt_sdram_c   = commands.getoutput( '/opt/vc/bin/vcgencmd measure_volts sdram_c | cut -d= -f2' )
    volt_sdram_i   = commands.getoutput( '/opt/vc/bin/vcgencmd measure_volts sdram_i | cut -d= -f2' )
    volt_sdram_p   = commands.getoutput( '/opt/vc/bin/vcgencmd measure_volts sdram_p | cut -d= -f2' )
    print color["lpurple"] + "CPU/GPU Core ........ : " + color["nocolor"] + volt_core + color["lpurple"] + "\t\tSDRAM Controller .... : " + color["nocolor"] + volt_sdram_c
    print color["lpurple"] + "SDRAM I/O ........... : " + color["nocolor"] + volt_sdram_i + color["lpurple"] + "\t\tSDRAM PHY ........... : " + color["nocolor"] + volt_sdram_p
    return

def rpisysinfo_temps():
    print color["purple"] + "###[ TEMPERATURES ]#############################################################" + color["nocolor"]
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
    print color["lpurple"] + "CPU ................. : " + color["nocolor"] + "%.1f°C / %.1f°C\t[ %.2f°F / %.2f°F ]" % (temp_cpu_c,trip_cpu_c,temp_cpu_f,trip_cpu_f)
    tempSrc_gpu    = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    temp_gpu_c     = float( tempSrc_gpu )
    temp_gpu_f     = ( 1.8 * temp_gpu_c ) + 32
    print color["lpurple"] + "GPU ................. : " + color["nocolor"] + "%.1f°C\t\t[ %.2f°F ]" % ( temp_gpu_c, temp_gpu_f )
    return

def rpisysinfo_firmware():
    print color["purple"] + "###[ FIRMWARE     ]#############################################################" + color["nocolor"]
    firmware_ver   = commands.getoutput( '/opt/vc/bin/vcgencmd version' ).splitlines()
    print color["lpurple"] + "Version ............. : " + color["nocolor"] + firmware_ver[2].replace( 'version ', '' )
    print "\t\t\t" + firmware_ver[0] + firmware_ver[1]
    return

def rpisysinfo_system():
    print color["purple"] + "###[ SYSTEM       ]#############################################################" + color["nocolor"]
    hostname       = commands.getoutput( 'uname -n' )
    print color["lpurple"] + "Hostname ............ : " + color["nocolor"] + hostname
    procfile       = open( "/proc/cpuinfo" )
    cpuinfo        = procfile.read().splitlines()
    procfile.close()
    cputype        = cpuinfo[1]
    print color["lpurple"] + "CPU ................. : " + color["nocolor"] + cputype[13:]
    procfile       = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor" )
    governor       = procfile.read().replace( '\n', '' )
    procfile.close()
    print color["lpurple"] + "Scaling Governor .... : " + color["nocolor"] + governor
    procfile       = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq" )
    curcpuclk      = procfile.read().replace( '\n', '' )
    procfile.close()
    print color["lpurple"] + "Current Frequency ... : " + color["nocolor"] + str( float(curcpuclk) / 1000 ) + "MHz"
    procfile       = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq" )
    mincpuclk      = procfile.read().replace( '\n', '' )
    procfile.close()
    print color["lpurple"] + "Minimum Frequency ... : " + color["nocolor"] + str( float(mincpuclk) / 1000 ) + "MHz"
    procfile       = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq" )
    maxcpuclk      = procfile.read().replace( '\n', '' )
    procfile.close()
    print color["lpurple"] + "Maximum Frequency ... : " + color["nocolor"] + str( float(maxcpuclk) / 1000 ) + "MHz"
    cpufeatures    = cpuinfo[3]
    print color["lpurple"] + "Features ............ : " + color["nocolor"] + cpufeatures[11:]
    bogomips       = cpuinfo[2]
    print color["lpurple"] + "BogoMIPS ............ : " + color["nocolor"] + bogomips[11:]
    hardware       = cpuinfo[10]
    revision       = cpuinfo[11]
    if revision[11:].startswith('1'):
            print color["lpurple"] + "Hardware ............ : " + color["nocolor"] + hardware[11:] + " Revision " + revision[11:] + color["red"] + " (WARRANTY VOID)" + color["nocolor"]
    else:
            print color["lpurple"] + "Hardware ............ : " + color["nocolor"] + hardware[11:] + " Revision " + revision[11:]
    serialnumber   = cpuinfo[12]
    print color["lpurple"] + "Serialnumber ........ : " + color["nocolor"] + serialnumber[10:]
    distro         = commands.getoutput( 'lsb_release -d' )
    print color["lpurple"] + "Distribution ........ : " + color["nocolor"] + str( distro[13:] )
    kernel         = commands.getoutput( 'uname -s' ) + " " + commands.getoutput( 'uname -r' ) + " " + commands.getoutput( 'uname -m' )
    print color["lpurple"] + "Kernel .............. : " + color["nocolor"] + kernel
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
    print color["lpurple"] + "Uptime .............. : " + color["nocolor"] + uptime
    memory         = commands.getoutput( 'free -o | grep "Mem:" | cut -d: -f2' ).lstrip().split()
    swap           = commands.getoutput( 'free -o | grep "Swap:" | cut -d: -f2' ).lstrip().split()
    print color["lpurple"] + "Memory .............. : " + color["nocolor"] + "Total  : " + memory[0] + "KB"
    print "\t\t\tUsed   : " + memory[1] + "KB"
    print "\t\t\tFree   : " + memory[2] + "KB"
    print "\t\t\tShared : " + memory[3] + "KB"
    print "\t\t\tBuffers: " + memory[4] + "KB"
    print "\t\t\tCached : " + memory[5] + "KB"
    print color["lpurple"] + "Swap ................ : " + color["nocolor"] + "Total  : " + swap[0] + "KB"
    print "\t\t\tUsed   : " + swap[1] + "KB"
    print "\t\t\tFree   : " + swap[2] + "KB"
    return

def rpisysinfo_network():
    print color["purple"] + "###[ NETWORK      ]#############################################################" + color["nocolor"]
    chkIsNetworked = commands.getoutput( 'ls /sys/class/net' )
    if 'eth0' in chkIsNetworked:
            print color["lpurple"] + "Interface ........... : " + color["nocolor"] + "eth0"
            sysfile    = open( '/sys/class/net/eth0/device/uevent' )
            eth0hw     = sysfile.read().splitlines()
            sysfile.close()
            etherhw    = eth0hw[1]
            print color["lpurple"] + "Hardware ............ : " + color["nocolor"] + etherhw[7:]
            sysfile    = open( "/sys/class/net/eth0/address" )
            eth0Mac    = sysfile.read().replace( '\n', '' )
            sysfile.close()
            print color["lpurple"] + "MAC Address ......... : " + color["nocolor"] + eth0Mac
            sysfile    = open( "/sys/class/net/eth0/carrier" )
            eth0Link   = sysfile.read().replace( '\n', '' )
            sysfile.close()
            if eth0Link == '0':
                    eth0Link = 'Disconnected'
            elif eth0Link == '1':
                    eth0Link = 'Connected'
            print color["lpurple"] + "Cable ............... : " + color["nocolor"] + eth0Link
            sysfile    = open( "/sys/class/net/eth0/speed" )
            eth0Line   = sysfile.read().replace( '\n', '' )
            sysfile.close()
            sysfile    = open( "/sys/class/net/eth0/duplex" )
            eth0duplex = sysfile.read().replace( '\n', '' )
            sysfile.close()
            print color["lpurple"] + "Link Speed .......... : " + color["nocolor"] + eth0Line + "Mbps " + eth0duplex + " duplex"
    else:
            print "No wired Network Adapter(s) found."

    # To be done - No WiFi adapter here
    #if 'wlan0' in chkIsNetworked:
    #	pass
    #else:
    #	print 'No wireless Network Adapter(s) found.'
    return

def rpisysinfo_footer():
    print color["purple"] + "################################################################################" + color["nocolor"]
    print ""
    return

def rpisysinfo_help():
    rpisysinfo_logo()
    print "Usage: rpisysinfo [switch]\n"
    print "       --help     | -h   Prints this help text."
    print "       --clocks   | -c   Displays an overview about all possible system clocks."
    print "       --display  | -d   Displays framebuffer resolution and bit-depth."
    print "       --codecs   | -c   Displays status of the video codecs."
    print "       --voltages | -v   Displays an overview about the voltages."
    print "       --temps    | -t   Displays system temperatures."
    print "       --firmware | -f   Displays firmware version."
    print "       --system   | -s   Displays system related information."
    print "       --network  | -n   Displays network related information.\n"
    print "Invoking rpisysinfo without any parameter will run all info modules."
    return

if __name__ == '__main__':
    import commands, sys

    def makedict(**kwargs):
            return kwargs

    color = makedict(black   = "\033[0;30m", dgrey   = "\033[1;30m", red     = "\033[0;31m",
                                     lred    = "\033[1;31m", green   = "\033[0;32m", lgreen  = "\033[1;32m",
                                     brown   = "\033[0;33m", yellow  = "\033[1;33m", blue    = "\033[0;34m",
                                     lblue   = "\033[1;34m", purple  = "\033[0;35m", lpurple = "\033[1;35m",
                                     cyan    = "\033[0;36m", lcyan   = "\033[1;36m", lgrey   = "\033[0;37m",
                                     white   = "\033[1;37m", nocolor = "\033[0m")

    if sys.argv[1:]:
            SysArgV = sys.argv[1]
    else:
            rpisysinfo_logo()
            rpisysinfo_clocks()
            rpisysinfo_display()
            rpisysinfo_codecs()
            rpisysinfo_voltages()
            rpisysinfo_temps()
            rpisysinfo_firmware()
            rpisysinfo_system()
            rpisysinfo_network()
            rpisysinfo_footer()
            sys.exit(0)

    if SysArgV == "--help" or SysArgV == "-h":
            rpisysinfo_help()
            sys.exit(0)
    elif SysArgV == "--clocks" or SysArgV == "-c":
            rpisysinfo_logo()
            rpisysinfo_clocks()
            rpisysinfo_footer()
            sys.exit(0)
    elif SysArgV == "--display" or SysArgV == "-d":
            rpisysinfo_logo()
            rpisysinfo_display()
            rpisysinfo_footer()
            sys.exit(0)
    elif SysArgV == "--codecs" or SysArgV == "-c":
            rpisysinfo_logo()
            rpisysinfo_codecs()
            rpisysinfo_footer()
            sys.exit(0)
    elif SysArgV == "--voltages" or SysArgV == "-v":
            rpisysinfo_logo()
            rpisysinfo_voltages()
            rpisysinfo_footer()
            sys.exit(0)
    elif SysArgV == "--temps" or SysArgV == "-t":
            rpisysinfo_logo()
            rpisysinfo_temps()
            rpisysinfo_footer()
            sys.exit(0)
    elif SysArgV == "--firmware" or SysArgV == "-f":
            rpisysinfo_logo()
            rpisysinfo_firmware()
            rpisysinfo_footer()
            sys.exit(0)
    elif SysArgV == "--system" or SysArgV == "-s":
            rpisysinfo_logo()
            rpisysinfo_system()
            rpisysinfo_footer()
            sys.exit(0)
    elif SysArgV == "--network" or SysArgV == "-n":
            rpisysinfo_logo()
            rpisysinfo_network()
            rpisysinfo_footer()
            sys.exit(0)
    else:
            print "Unrecognized switch."
            rpisysinfo_help()

    sys.exit(0)
