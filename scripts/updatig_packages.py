#!/usr/bin/python3

from constants import PACMAN_PACKAGE_MANAGER, APT_PACKAGE_MANAGER, DNF_PACKAGE_MANAGER
import distro
import os


#distro based
UBUNTU_BASED = ['ubuntu', 'zorin', 'pop', 'mint']
ARCH_BASED = ['manjaro', 'reborn']

dict_ = {
	'manjaro': PACMAN_PACKAGE_MANAGER,
	'fedora': DNF_PACKAGE_MANAGER
	}

_id = distro.id()


def adding_to_dict(distro_id, dictionary, dict_based_a, dict_based_b):
	try:
		if distro_id not in dictionary:
			if distro_id in dict_based_a:
				dictionary[distro_id] = APT_PACKAGE_MANAGER
			elif distro_id in dict_based_b:
				dictionary[distro_id] = PACMAN_PACKAGE_MANAGER

	except NameError:
		print('An error was returned while trying to add distro id to dictionary')



def upgrade(id_distro, dictionary):
	try:
		if id_distro in dictionary:
			os.system(dictionary.get(id_distro))
		else:
			print(f'{id_distro} no found in dictionary')
			adding_to_dict(id_distro, dictionary, UBUNTU_BASED, ARCH_BASED)
			upgrade(id_distro, dictionary)
			return f'Adding {id_distro} to {dictionary}'
	except Exception:
		print('An error was returned while trying to update packages')


def main():
	upgrade(_id, dict_)
	
	
if __name__ == '__main__':
	main()
