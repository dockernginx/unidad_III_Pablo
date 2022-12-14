from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type= 'cisco_ios', 
    host= '10.10.20.48', 
    port= 22,
    username= 'developer',
    password= 'C1sco12345'
    )
#output = sshCli.send_command("sh ip int br")
#print("{}\n".format(output))

config_commands = [
    'int loopback 1', 
    'ip address 192.168.20.105 255.255.255.0', 
    'description LAb 2.2'
] 

output = sshCli.send_config_set(config_commands)
output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))
