start_ip = 10
end_ip = 100
subnet_mask = "255.255.254.0"
gateway = "172.40.40.1"
dns_servers = ["8.8.8.8", "1.1.1.1"]

for ip_suffix in range(start_ip, end_ip+1):
    ip_address = f"172.40.40.{ip_suffix}"

    # Create the content for the CMD file
    cmd_content = f"""\
@echo off
echo Setting static IP configuration for {ip_address}
netsh interface ip set address "Local Area Connection" static {ip_address} {subnet_mask} {gateway} 1
netsh interface ip set dns "Local Area Connection" static {','.join(dns_servers)}
@echo off
ipconfig /all | findstr "IPv4 Physical Host" | clip
echo Static IP configuration applied.
echo Please Past Data
pause

"""

    # Generate the CMD file
    file_name = f"set_static_ip_{ip_suffix}.cmd"
    with open(file_name, "w") as cmd_file:
        cmd_file.write(cmd_content)

    print(f"Generated {file_name}")
