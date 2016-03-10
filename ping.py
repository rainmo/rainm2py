#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'rainmo'

import os
import time

start_Time = int(time.time())	#记录开始时间
def ping_Test():
	ips = open('iplist.txt', 'r')
	ip_True = open('ip_True.txt', 'w+')
	ip_False = open('ip_False.txt', 'w+')
	count_True, count_False = 0, 0

	for ip in ips.readlines():
		ip = ip.replace('\n', '')
		return1 = os.system('ping -n 1 -w 1 %s' %ip)
		if return1:
			print('ping %s is fail' %ip)
			ip_False.write(ip + '\n')
			count_False += 1
		else:
			print('ping %s is ok' %ip)
			ip_True.write(ip + '\n')
			count_True += 1

	ip_True.close()
	ip_False.close()
	ips.close()
	end_Time = int(time.time())
#	print("time", end_Time - start_Time, "s")
	print("ping success：", count_True, " ping fail：", count_False)
ping_Test()
