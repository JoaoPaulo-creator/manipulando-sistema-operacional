#!/usr/bin/python3
from time import sleep
import os


def update_packages():
	update_packages = os.system('sudo apt update')
	return update_packages


def upgrade_packages():
	upgrade_packages = os.system('sudo apt upgrade -y')
	return upgrade_packages


def main():
	update_packages()
	upgrade_packages()
	
	
if __name__ == '__main__':
	main()

