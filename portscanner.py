import socket
import termcolor


def scan(target, ports):
	print('\n' + ' Começando a escanear: ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Porta Aberta: " + str(port))
		sock.close()
	except:
		pass


targets = input("[*] Insira alvos a serem escaneados(separe por vírgula): ")
ports = int(input("[*] Insira a quantidade de portas a serem escaneadas: "))
if ',' in targets:
	print(termcolor.colored(("[*] Escaneando múltiplos alvos"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)