---

### 🐍 `ip_calculator.py`

```python
import ipaddress

def get_ip_info(cidr_input):
    try:
        network = ipaddress.IPv4Network(cidr_input, strict=False)
        ip = ipaddress.IPv4Interface(cidr_input).ip

        print("\n📡 IP Address Info")
        print(f"IP Address      : {ip}")
        print(f"CIDR Notation   : {network.with_prefixlen}")
        print(f"Subnet Mask     : {network.netmask}")
        print(f"Network Address : {network.network_address}")
        print(f"Broadcast Addr  : {network.broadcast_address}")

        hosts = list(network.hosts())
        if hosts:
            print(f"First Usable IP : {hosts[0]}")
            print(f"Last Usable IP  : {hosts[-1]}")
            print(f"Usable Hosts    : {len(hosts)}")
        else:
            print("No usable hosts (subnet too small).")

        print(f"IP Class        : {get_ip_class(ip)}")

    except ValueError as e:
        print(f"❌ Error: {e}")

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
    else:
        return "Unknown"

if __name__ == "__main__":
    cidr_input = input("Enter IP address with CIDR (e.g. 192.168.1.10/24): ")
    get_ip_info(cidr_input)
