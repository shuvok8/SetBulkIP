def generate_cmd_file(ip_address, subnet_mask, gateway, dns_servers):
    cmd_content = f'@echo off\n'
    cmd_content += f'echo Setting static IP configuration...\n'
    cmd_content += f'netsh interface ip set address name="Local Area Connection" static {ip_address} {subnet_mask} {gateway} 1\n'
    cmd_content += f'netsh interface ip set dns name="Local Area Connection" static {dns_servers[0]}\n'
    cmd_content += f'netsh interface ip add dns name="Local Area Connection" addr={dns_servers[1]} index=2\n'
    cmd_content += f'echo Static IP configuration applied.\n'
    cmd_content += f'pause\n'

    with open('set_static_ip.cmd', 'w') as cmd_file:
        cmd_file.write(cmd_content)

ip_address = '172.40.40.10'
subnet_mask = '255.255.254.0'
gateway = '172.40.40.1'
dns_servers = ['8.8.8.8', '1.1.1.1']

generate_cmd_file(ip_address, subnet_mask, gateway, dns_servers)
