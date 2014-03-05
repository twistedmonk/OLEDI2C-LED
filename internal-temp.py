#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import commands
def rpisysinfo_temps():
    print "###[ TEMPERATURES ]#############################################################" 
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
    print "CPU ................. : " + "%.1f°C / %.1f°C\t[ %.2f°F / %.2f°F ]" % (temp_cpu_c,trip_cpu_c,temp_cpu_f,trip_cpu_f)
    tempSrc_gpu    = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    temp_gpu_c     = float( tempSrc_gpu )
    temp_gpu_f     = ( 1.8 * temp_gpu_c ) + 32
    print "GPU ................. : "  + "%.1f°C\t\t[ %.2f°F ]" % ( temp_gpu_c, temp_gpu_f )
    return

rpisysinfo_temps()
