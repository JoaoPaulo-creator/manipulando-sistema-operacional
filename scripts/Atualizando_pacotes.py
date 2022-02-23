#!/usr/bin/python3

from constants import _MANJARO, _POP_OS, _FEDORA
import distro
import os

dict_ = {
	'manjaro': _MANJARO,
	'fedora': _FEDORA}

_id = distro.id()


def update_packages():
	try:
		if _id in dict_:
			os.system(dict_.get(_id))
		else:
			print(f'{_id} not found in dictionary')

	except Exception:
		return 'Some error message here'


def upgrade_packages():
	upgrade_packages = os.system('sudo apt upgrade -y')
	return upgrade_packages


def main():
	update_packages()
	upgrade_packages()
	
	
if __name__ == '__main__':
	main()

