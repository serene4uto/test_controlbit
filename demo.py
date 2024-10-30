import serial

def read_serial_data(port, baudrate=921600):
    try:
        buffer = ""

        # Open serial port
        ser = serial.Serial(port, baudrate)
        print(f"Connected to {port} at {baudrate} baud.")
        
        while True:
            data = ser.read(100)
            if data:
                buffer += data.decode('utf-8')

                # Split the buffer based on the delimiter
                chunks = buffer.split('t,')

                # Process each complete chunk (all except the last one)
                for chunk in chunks[:-1]:
                    print(f"Received chunk: {chunk}")
                    # Here you can process each chunk as needed

                # The last part is either empty or an incomplete chunk, keep it in the buffer
                buffer = chunks[-1]

    
    except serial.SerialException as e:
        print(f"Serial exception: {e}")
    except KeyboardInterrupt:
        print("Serial reading interrupted by user.")
    finally:
        if ser.is_open:
            ser.close()
            print("Serial port closed.")


def main():
    read_serial_data('/dev/ttyUSB0', 921600)


if __name__ == '__main__':
    main()