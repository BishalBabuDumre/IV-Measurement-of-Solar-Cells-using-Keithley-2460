import pyvisa

# Initialize the resource manager
rm = pyvisa.ResourceManager('@py')

# Open a connection to the instrument using its IP address
ip_address = 'XXX.XXX.XXX.XXX'  # Replace with your instrument's IP address
instrument = rm.open_resource(f'TCPIP0::{ip_address}::INSTR')
instrument.timeout = 10000

data = instrument.query(':TRAC:DATA? 1, 101, "defbuffer1", SOUR, READ')#This extracts data in the format of Source, Read(Measured Value). So, in our case, it will be a voltage value, current value starting from point 1 to 101.

# Save the data to a file
with open('bufferForward.csv', 'w') as f:
    f.write(data)

print("Data Extraction Complete for Forward Sweep")

# Close the connection
instrument.close()
