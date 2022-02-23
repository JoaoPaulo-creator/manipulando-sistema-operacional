import platform
import distro

'''
Script criado para verificar qual é o nome da distro linux e sua versão do kernel
'''


_system = platform.system()

#versão do kernel
_kernel_version = platform.release()
#id da distro
_id = distro.id()
#nome da distro
_name = distro.name()
#versão da distro
_version = distro.version()

primeiros_caracteres_kernel_version = list(_kernel_version)
juntar = ''.join(primeiros_caracteres_kernel_version[0:4])

print(f'Systen: {_system}')
print(f'Kernel version: {juntar}')
print(f'Distro ID: {_id}')
print(f'Distro name: {_name}')
print(f'Distro version: {_version}')
