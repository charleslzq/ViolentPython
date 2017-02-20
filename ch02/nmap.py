import optparse
from nmap import PortScanner


def nmap_scan(tgt_host, tgt_port):
    nm_scan = PortScanner()
    nm_scan.scan(tgt_host, tgt_port)
    state = nm_scan[tgt_host]['tcp'][int(tgt_port)]['state']
    print(" [*] " + tgt_host + " tcp/" + tgt_port + " " + state)

if __name__ == '__main__':
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    tgt_host = options.tgtHost
    tgt_port = options.tgtPort
    tgt_ports = str(tgt_port).split(',')
    if (tgt_host is None) | (tgt_port is None):
        print(parser.usage)
        exit(0)
    nmap_scan(tgt_host, tgt_ports)