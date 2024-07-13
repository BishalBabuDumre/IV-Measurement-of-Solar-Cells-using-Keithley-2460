import pyvisa

# Initialize the resource manager
rm = pyvisa.ResourceManager('@py')

# Open a connection to the instrument using its IP address
ip_address = 'XXX.XXX.XXX.XXX'  # Replace with your instrument's IP address
instrument = rm.open_resource(f'TCPIP0::{ip_address}::INSTR')
instrument.timeout = 10000

# List of SCPI commands to send
commands1 = [
    '*RST', #Resets the Keithley for new measurement.
    'SENS:FUNC "CURR"', #The mode is sense current.
    'SENS:CURR:RANG:AUTO ON', #It makes sensing current range to be auto.
    'SENS:CURR:RSEN ON', #This turns on 4-wire measurement sense.
    'SOUR:FUNC VOLT', #This means source will be voltage.
    'SOUR:VOLT:RANG 5', #This means that the max volt we will be using is 2V.
    'SOUR:VOLT:ILIM 1', #The output current after sending voltage should not exceed 1A because current more than this may damage device.
    'SOUR:SWE:VOLT:LIN 0, 5, 101, 0.01, 1, BEST, ON, OFF, "defbuffer1"', #This will be explained in detail in README.
    ':INIT' #Initialize
]

# Send each command in the list
for command in commands1:
    instrument.write(command)

print("Forward Sweep Complete")

# Close the connection
instrument.close()
