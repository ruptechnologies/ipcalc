import ipaddress

def calculate_ip_info(cidr_input):
    try:
        network = ipaddress.IPv4Network(cidr_input, strict=False)
        ip = ipaddress.IPv4Interface(cidr_input).ip
        hosts = list(network.hosts())

        return {
            "IP Address": str(ip),
            "CIDR Notation": network.with_prefixlen,
            "Subnet Mask": str(network.netmask),
            "Network Address": str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
            "First Usable IP": str(hosts[0]) if hosts else "N/A",
            "Last Usable IP": str(hosts[-1]) if hosts else "N/A",
            "Usable Hosts": str(len(hosts)),
            "IP Class": get_ip_class(ip),
        }
    except ValueError as e:
        return { "error": str(e) }

def get_ip_class(ip):
    first_octet = int(str(ip).split('.')[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    return "Unknown"
