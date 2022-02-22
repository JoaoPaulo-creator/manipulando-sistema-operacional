import platform
import distro

'''
Script criado para verificar qual é o nome da distro linux e sua versão do kernel
'''

_system = platform.system()
_kernel_version = platform.release()

primeiros_caracteres_kernel_version = list(_kernel_version)
juntar = ''.join(primeiros_caracteres_kernel_version[0:4])

print(f'Systen: {_system}')
print(f'Kernel version: {juntar}')

t = distro.linux_distribution()
print(t[0])

