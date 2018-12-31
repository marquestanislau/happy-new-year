# 1. criar ambiente virtual, virtualenv <nome_do_ambiente> -p python3
# 2. instalar os modulos (colorama, termcolor, pyfiglet) pip3 install -r requirement.txt
# 3. correr o codigo com o comando python3 happy.py

import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

# init(strip=not sys.stdout.isatty())

cprint(figlet_format('Feliz 2019!\n from Python Community Maputo', font='starwars'),
	'yellow', 'on_red', attrs=['bold'])