import platform
import distro

_system = platform.system()
_kernel_version = platform.release()

primeiros_caracteres_kv = list(_kernel_version)
juntar = ''.join(primeiros_caracteres_kv[0:4])

print(f'Systen: {_system}')
print(f'Kernel version: {juntar}')

t = distro.linux_distribution()
print(t[0])

