import optparse

from ch02.scanner import port_scan


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
    port_scan(tgt_host, tgt_ports)


