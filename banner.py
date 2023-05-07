import argparse
import requests
import socket
parser = argparse.ArgumentParser(description='Web Domain Scanner')
parser.add_argument('-t', '--target', help='Target domain name or IP address', required=True)
parser.add_argument('-p', '--ports', help='Port numbers to scan (comma separated)', default='80,443')
parser.add_argument('-ssl', '--ssl', help='Enable SSL/TLS', action='store_true')
parser.add_argument('-v', '--verbose', help='Enable verbose output', action='store_true')
args = parser.parse_args()
def scan_ports(target, ports, use_ssl):
    open_ports = []
    for port in ports.split(','):
        port = int(port.strip())
        try:
            if use_ssl:
                url = 'https://' + target + ':' + str(port)
                response = requests.get(url, verify=False, timeout=5)
                if response.status_code == 200:
                    open_ports.append(port)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
        except:
            pass
    return open_ports
if args.verbose:
    print('Scanning target:', args.target)

if args.ssl:
    use_ssl = True
else:
    use_ssl = False

open_ports = scan_ports(args.target, args.ports, use_ssl)

if open_ports:
    print('Open ports:', open_ports)
else:
    print('No open ports found.')
