import RPi.GPIO as GPIO
import serial
import time
import os
import datetime

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)

# Set up serial port for GSM module
ser = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Function to send an SMS message
def send_sms(phone_number, message):
    # Prepare AT command to send SMS
    cmd = 'AT+CMGF=1\r\n'
    ser.write(cmd.encode())
    time.sleep(1)

    # Enter the phone number to send SMS to
    cmd = 'AT+CMGS="{}"\r\n'.format(phone_number)
    ser.write(cmd.encode())
    time.sleep(1)

    # Enter the message body
    ser.write(message.encode())
    time.sleep(1)

    # Send the message
    ser.write(bytes([26]))
    time.sleep(1)

    # Save the phone number, date/time, and message to a file
    today = datetime.date.today()
    filename = "sms/{}.txt".format(today)
    if not os.path.exists("sms"):
        os.makedirs("sms")
    with open(filename, "a") as f:
        f.write("{}\t{}\t{}\n".format(phone_number, datetime.datetime.now(), message))

# Function to make a call
def make_call(phone_number):
    # Prepare AT command to make a call
    cmd = 'ATD{};\r\n'.format(phone_number)
    ser.write(cmd.encode())
    start_time = datetime.datetime.now()
    time.sleep(30)

    # Hang up the call
    cmd = 'ATH\r\n'
    ser.write(cmd.encode())
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    time.sleep(1)

    # Save the phone number, duration, and date/time to a file
    today = datetime.date.today()
    filename = "calls/{}.txt".format(today)
    if not os.path.exists("calls"):
        os.makedirs("calls")
    with open(filename, "a") as f:
        f.write("{}\t{}\t{}\n".format(phone_number, duration, start_time))

# Example usage
if __name__ == "__main__":
    phone_number = "+256XXXXXXXXX" # Replace with the phone number you want to call or text
    message = "Hello, this is a test message!" # Replace with the message you want to send

    send_sms(phone_number, message)
    make_call(phone_number)
