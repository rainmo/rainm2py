#!/usr/bin/env python3

import os
import time
import xml.etree.ElementTree as ET
from subprocess import (
  check_output, CalledProcessError,
  Popen, PIPE,
)

import requests

def github_contributed():
	user = os.environ['USER']
	today = time.strftime('%Y-%m-%d')
	url = "https://github.com/users/%s/contributions" % user
	data = requests.get(url, timeout = 30).text
	svg = ET.fromstring(data)
	rect = svg.find('.//rect[@data-date="%s"]' % today)
	if rect is None:
		return False
	return int(rect.get('data-count')) > 0

def get_display():
	if 'DISPLAY' in os.environ:
		return True

	cmd = ['pgrep', '-U%d' % os.getuid(), '-x', 'awesome']
	try:
		pid = check_output(cmd).strip().decode('ascii')
	except CalledProcessError as e:
		if e.returncode == 1:
			# Awesome not running
			return False
		raise

	with open('/proc/%s/environ' % pid) as f:
		display = [x.split('=', 1)[1] for x in f.read().split('\0') if x.startswith('DISPLAY=')]
	if not display:
		print("can't get DISPLAY of awesome (pid %s)" % pid, file=sys.stderr)
		return False
	display = display[0]

	os.environ['DISPLAY'] = display
	return True


def main():
 	ok = get_display()
  	if not ok:
    return False

  	s = str(github_contributed()).lower()
  	s = 'update_github(%s)' % s

  	client = Popen(['awesome-client'], stdin=PIPE)
  	client.communicate(s.encode('ascii'))

if __name__ == '__main__':
	main()

	