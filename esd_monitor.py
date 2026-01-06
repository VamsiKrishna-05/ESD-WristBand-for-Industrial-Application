import spidev
import time
import RPi.GPIO as GPIO

# Pin assignments
BUZZER_PIN = 2    # Buzzer on GPIO2 (pin 3)
IR_SENSOR_PIN = 18 # IR sensor on GPIO18 (pin 12)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

# SPI setup for MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def read_channel(channel):
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    result = ((adc[1] & 3) << 8) + adc[2]
    return result

def convert_to_voltage(adc_value, v_ref=3.3):
    return (adc_value / 1023.0) * v_ref

def set_buzzer(state):
    GPIO.output(BUZZER_PIN, GPIO.HIGH if state else GPIO.LOW)

def is_wristband_connected(v):
    return v < 3.0

def is_box_off(v):
    return 1.3 < v < 1.80

try:
    while True:
        ir_detected = GPIO.input(IR_SENSOR_PIN)
        adc_value = read_channel(0)
        voltage = convert_to_voltage(adc_value)
        
        print(f"ADC Value: {adc_value}, Voltage: {voltage:.2f}V, IR Detected: {ir_detected}")
        
        wristband_connected = is_wristband_connected(voltage)
        box_off = is_box_off(voltage)
        
        # Buzzer logic as described in your requirements
        if not ir_detected:
            set_buzzer(False)
            print("No object detected by IR")
        elif box_off:
            set_buzzer(True)
            print("Object detected, box off pls power on")
        elif not wristband_connected:
            set_buzzer(True)
            print("Object detected, wristband not connected")
        else:
            set_buzzer(False)
            print("Object detected, wristband connected")
            
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    spi.close()
    GPIO.cleanup()
import spidev
import time
import RPi.GPIO as GPIO

# Pin assignments
BUZZER_PIN = 2    # Buzzer on GPIO2 (pin 3)
IR_SENSOR_PIN = 18 # IR sensor on GPIO18 (pin 12)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

# SPI setup for MCP3008
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def read_channel(channel):
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    result = ((adc[1] & 3) << 8) + adc[2]
    return result

def convert_to_voltage(adc_value, v_ref=3.3):
    return (adc_value / 1023.0) * v_ref

def set_buzzer(state):
    GPIO.output(BUZZER_PIN, GPIO.HIGH if state else GPIO.LOW)

def is_wristband_connected(v):
    return v < 2.0

def is_box_off(v):
    return 1.3 < v < 1.80

try:
    while True:
        ir_detected = GPIO.input(IR_SENSOR_PIN)
        adc_value = read_channel(0)
        voltage = convert_to_voltage(adc_value)
        
        print(f"ADC Value: {adc_value}, Voltage: {voltage:.2f}V, IR Detected: {ir_detected}")
        
        wristband_connected = is_wristband_connected(voltage)
        box_off = is_box_off(voltage)
        
        # Buzzer logic as described in your requirements
        if not ir_detected:
            set_buzzer(False)
            print("No object detected by IR, buzzer OFF")
        elif box_off:
            set_buzzer(True)
            print("Object detected, box off voltage, buzzer ON")
        elif not wristband_connected:
            set_buzzer(True)
            print("Object detected, wristband not connected, buzzer ON")
        else:
            set_buzzer(False)
            print("Object detected, wristband connected, buzzer OFF")
            
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    spi.close()
    GPIO.cleanup()
