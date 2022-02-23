#!/usr/bin/python3

from constants import PACMAN_PACKAGE_MANAGER, APT_PACKAGE_MANAGER, DNF_PACKAGE_MANAGER
import distro
import os


#distro based
UBUNTU_BASED = {'zorin': _POP_OS, 'pop': _POP_OS, 'mint': _POP_OS}
ARCH_BASED = {'manjaro': PACMAN_PACKAGE_MANAGER, 'reborn': PACMAN_PACKAGE_MANAGER}


dict_ = {
	'manjaro': PACMAN_PACKAGE_MANAGER,
	'fedora': _FEDORA}

_id = distro.id()


def update_upgrade_packages():
	try:
		if _id in dict_:
			os.system(dict_.get(_id))
		else:
			print(f'{_id} not found in dictionary')

	except Exception:
		return 'Some error message here'


def main():
	update_upgrade_packages()
	
	
if __name__ == '__main__':
	main()

