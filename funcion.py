def funcion():
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    
    p = GPIO.PWM(17, 50)  # channel=12 frequency=50Hz
    p.start(0)
    i=1
    try:
        while i:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)   
            i=0
    except KeyboardInterrupt:
        pass
    p.stop()
    GPIO.cleanup()