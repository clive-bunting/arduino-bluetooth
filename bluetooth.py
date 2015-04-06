import serial

def findAvailableSerialPorts():
    """Lists serial ports.
       Basically a brute force approach trying to open a list of known ports to see if a connection can be made

    :returns:
        A list of available serial ports
    """
    ports = ['COM' + str(i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def openBluetoothConnection(port):
    """Opens a serial connection over bluetooth.

    :returns:
        An open connection ready for reading/writing
    """
    bluetoothSerial = serial.Serial(port, baudrate=9600, timeout=5)
    return bluetoothSerial

def closeBluetoothConnection(bluetoothSerial):
    """Close an open serial connection
    """
    try:
        bluetoothSerial.close()
    except:
        pass # Ignore errors when closing the connection

def blinkLED(bluetoothSerial):
    """Blink the LED on the Arduino UNO a user specified number of times.
       Requires that the appropriate sketch be installed on the Arduino.
    """
    blinks = None
    while True:
        try:
            blinks = int(raw_input('Please enter the number of times to blink the LED (enter 0 to end):'))
        except:
            pass    # Ignore any errors that may occur and try again
        if blinks == 0:
            break
        bluetoothSerial.write(str(blinks))
        print bluetoothSerial.readline()

if __name__ == '__main__':
    ports = findAvailableSerialPorts()
    print 'Available ports: ', ports
    port = raw_input( "Please enter the bluetooth port:")
    bluetoothSerial = openBluetoothConnection(port)
    try:
        blinkLED(bluetoothSerial)
    finally:
        closeBluetoothConnection(bluetoothSerial)
