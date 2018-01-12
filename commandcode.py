while True:    #setup
    from time import sleep
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(26, GPIO.IN) 
    
    def forwards(x):
      print("forwards")
      GPIO.output(24, GPIO.HIGH)
      GPIO.output(27, GPIO.HIGH)
      sleep(x)
      GPIO.output(27, GPIO.LOW)
      GPIO.output(24, GPIO.LOW)
      GPIO.cleanup()
    
    def left(x):
      print("left")
      GPIO.output(27, GPIO.HIGH)
      sleep(x)
      GPIO.output(27, GPIO.LOW)
      GPIO.cleanup()
    
    def right(x):
      print("right")
      GPIO.output(24, GPIO.HIGH)
      sleep(x)
      GPIO.output(24, GPIO.LOW)
      GPIO.cleanup()
    
    def backwards(x):
      print("backwards")
      GPIO.output(23, GPIO.HIGH)
      GPIO.output(17, GPIO.HIGH)
      sleep(x)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(23, GPIO.LOW)
      GPIO.cleanup()
    
    #program
    
    choice=input("f, l, r, b, exit :")
    x=int(input("How long do you want to go for?: "))
    
    print(choice)
    
    if choice=="f":
      forwards(x)
    
    elif choice=="l":
      left(x)
    
    elif choice=="r":
      right(x)
    
    elif choice=="b":
   `  backwards(x)
    
    elif choice=="exit":
      break
    
    else:
      print("this is not a choice")
      GPIO.cleanup()
    
    GPIO.cleanup()
