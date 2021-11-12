#%%
from netmiko import ConnectHandler
csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.245',
    'username': 'username',
    'password': 'password',
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}

ssh = ConnectHandler(**csr)
ssh.enable 
cmd_list = [
    'show version',
    'show ip int brief',
    'show arp',
    'show cdp neighbors'
]

for cmd in cmd_list:
    command = ssh.send_command(cmd)
    print(f'#####> {cmd} <#####')
    print(command)
    print('-'*80)



ssh.exit_enable_mode
# %%
