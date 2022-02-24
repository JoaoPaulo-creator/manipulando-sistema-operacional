from os import makedirs as mk
from os import removedirs as rd
from os import system
from os import chdir as cd
from time import sleep


def criando_diretorio():
    try:
        _mk = mk(f'/home/$USER/TESTE')
        return mk    
    except FileExistsError:
        removendo_diretorio()


def removendo_diretorio():
    try:
        _rd = rd(f'/home/$USER/TESTE')
        system('cd ..')
        return _rd
    except OSError:
        return system('rm -r TESTE')


def mudando_de_diretorio():
    _cd = cd('/home/$USER/TESTE')
    return _cd


def retornando_dir_antigo():
    _cd = cd('/home/$USER')
    return _cd


def verificando_onde_estou():
    s = system('pwd')
    return s


def criando_arquivo():
    with open('teste.txt', 'w') as f:
        f.write('Se estou lendo isso '
        'é porque deu certo\n')
    
    system('cat teste.txt')
    return


def _ls():
    return system('ls')


def main():
    criando_diretorio()  
    sleep(0.5)  
    _ls()
    mudando_de_diretorio()        
    verificando_onde_estou()
    criando_arquivo()
    _ls()
    sleep(2)
    retornando_dir_antigo()
    removendo_diretorio()
    _ls()


if __name__=='__main__':
    main()    
