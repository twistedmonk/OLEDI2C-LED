#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import commands


def rpisysinfo_voltages():
    print "###[ VOLTAGES     ]#############################################################" 
    volt_core      = commands.getoutput( '/opt/vc/bin/vcgencmd measure_volts core | cut -d= -f2' )
    volt_sdram_c   = commands.getoutput( '/opt/vc/bin/vcgencmd measure_volts sdram_c | cut -d= -f2' )
    volt_sdram_i   = commands.getoutput( '/opt/vc/bin/vcgencmd measure_volts sdram_i | cut -d= -f2' )
    volt_sdram_p   = commands.getoutput( '/opt/vc/bin/vcgencmd measure_volts sdram_p | cut -d= -f2' )
    print "CPU/GPU Core ........ : " + volt_core + "\t\tSDRAM Controller .... : " + volt_sdram_c
    print "SDRAM I/O ........... : " + volt_sdram_i + "\t\tSDRAM PHY ........... : " + volt_sdram_p
    return

rpisysinfo_voltages()
