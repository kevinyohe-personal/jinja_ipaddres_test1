import jinja2
import os
import ipaddress

loader = jinja2.FileSystemLoader(os.getcwd())

jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True )


template = jenv.get_template('port_vlan.j2')
#test1 = ipaddress.IPv4Address('192.168.0.1')+2
test2 = ipaddress.IPv4Address('10.10.10.1')+1

my_ports = ['gig0/1', 'gig0/5','gig0/6','gig0/6','gig0/9',]
print (template.render(iface_list=my_ports,vlan_name=10 ))



print (test2)

