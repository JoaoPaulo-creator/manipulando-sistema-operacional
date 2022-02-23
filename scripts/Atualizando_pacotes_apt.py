#!/usr/bin/python3
from time import sleep
import os

_MANJARO = 'sudo pacman -Syu --noconfirm'
_POP_OS = 'sudo apt update && sudo apt upgrade -y'

distro_list = ['ubuntu', 'POP!_OS', 'fedora', '_manjaro']
dict_ = {'manjaro': _MANJARO}


def update_packages():
	try:
		if _id in dict_:
			os.system(dict_.get(_id))
		else:
			print('Not found')

	except e:
		return 'Not found'

def upgrade_packages():
	upgrade_packages = os.system('sudo apt upgrade -y')
	return upgrade_packages


def main():
	update_packages()
	upgrade_packages()
	
	
if __name__ == '__main__':
	main()

