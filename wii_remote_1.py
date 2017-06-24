#!/usr/bin/python
# -----------------------
# -----------------------
import cwiid
import commands
import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM)
import time
import funcion
import wiiclose
# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
#***************************************
GPIO.cleanup()
GPIO.setup(04,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.output(04,0)
GPIO.output(17,0)

p = GPIO.PWM(17,50)
p.start(0)
button_delay = 0.1

#*******************************************

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line):
  # Send string to display
 
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
#*************************************************************************
#def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
 
  # Initialise display
  #lcd_init()
  #i=1
  #while i:
 
    # Send some test
   # lcd_string("Boton A",LCD_LINE_1)
    #lcd_string("Presionado",LCD_LINE_2)
 
    #time.sleep(3) # 3 second delay
 
    #time.sleep(3)#
    #i=0
    #break
#********************************************
print 'Presiona 1 + 2 para iniciar.'
time.sleep(1)

# Conecta el wiimote
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error de conexion"
  quit()

print 'Wiimote conectado...\n'
print 'Presiona Home para salir.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']

  # Interrupcion
  if (buttons - cwiid.BTN_HOME == 0):  
    print '\n Conexion terminada ...'
    
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    execfile("wiiclose.py") # redirecciona a archivo que muestra en pantalla lcd fin de la conexion
    wiiclose()
    exit(wii)  
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Izquierda'
    GPIO.output(04,1)

    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
    print 'Derecha'
    GPIO.output(04,0)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):
    print 'Arriba'        
    GPIO.output(17,01)  
    time.sleep(button_delay)          
    
  if (buttons & cwiid.BTN_DOWN):
    print 'Abajo'   
    GPIO.output(17,0)   
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    print 'Boton 1'
    def funcion():
        print 'Hizo la funcion'
    funcion()    
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print 'Boton 2'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    print 'Boton A'
#---------------------------------LCD------------------------------------
  #  main()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS
    GPIO.setup(LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(LCD_D7, GPIO.OUT) # DB7
    lcd_init()

    lcd_string("Boton A",LCD_LINE_1)
    lcd_string("Presionado",LCD_LINE_2)
    time.sleep(3) # 3 second delay
    lcd_string("",LCD_LINE_1)
    lcd_string("",LCD_LINE_2)
    GPIO.cleanup()
     
#--------------------------------FIN LCD--------------------------------- 
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_B):
    print 'Boton B'
    time.sleep(button_delay)                 
    
  if (buttons & cwiid.BTN_MINUS):
    print 'Boton -'
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print 'Boton +'
    time.sleep(button_delay)