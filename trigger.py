import pyvisa
import time

# Initialize the resource manager
rm = pyvisa.ResourceManager('@py')

# Open a connection to the instrument using its IP address
ip_address = 'XXX.XXX.XXX.XXX'  # Replace with your instrument's IP address
instrument = rm.open_resource(f'TCPIP0::{ip_address}::INSTR')
instrument.timeout = 10000

commands3 = [
    ':INIT'
]
# Send each command in the list
for command in commands3:
    instrument.write(command)

