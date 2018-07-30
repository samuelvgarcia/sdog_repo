# Read / Write Serial for UMON
# Using Python 3 and Pyserial 3.x
# S.Garcia

import serial #for serial read/write
import time #for time delay

#==============================================
# Serial Port Parameters
# port = "com6"
port = "/dev/ptyp1"
ser = serial.Serial(port, baudrate=115200, parity='N', 
					bytesize=8, stopbits=1, timeout=1, xonxoff=0, rtscts=0)

##==============================================
# Functions
# def umon_write( my_command ):
# 	my_command = my_command + '\n'
# 	for k in range( len(my_command) ):
# 		ser.write(my_command[k].encode())
# 		# time.sleep(0.01) #need to add delay between writing characters		

def umon_write( my_command ):
	ser.write(my_command.encode())



def umon_read( ser_inst, echo=1 ):
	tmp = ser_inst.readline() #readline for serial instantiation
	tmp = str(tmp,'utf-8') #convert byte to utf-8
	tmp = tmp.replace('\n', '') #get rid of newline
	tmp = tmp.replace('\r', '') #and carriage return
	if echo ==1:		
		print(tmp)
	return tmp

##==============================================	
#Some flags/variables
fpga_version_check = "c0000000 w@ ."
start_ADC1 = "1 c00c0000 w!"
start_ADC2 = "1 c00c0000 w!"

check_ADC1_done = "c00d0000 w@ ."
check_ADC2_done = "c00d0000 w@ ."

#Set umon to interpret hex numbers/addresses

str  =     "Hello {0}             World {0}"
str2 = "\r\nThis  {0}             Sucks {0}" 
	
for k in range(20):	
	umon_write("\033[0;0H")
	umon_write(str.format(k))
	umon_write(str2.format(k))
	umon_write("\033[0;0H")
	time.sleep(0.5)

# for k in range(50):	
# 	ser.write("\033[0;0H".encode())
# 	ser.write(str.format(k).encode())
# 	ser.write(str2.format(k).encode())
# 	ser.write("\033[0;0H".encode())	
# 	time.sleep(.1)
	
# umon_read( ser, echo=1 ) #clear the read buffer, but don't echo
# for k in range(20):
# 	umon_write("\r\n")
umon_write("\033c")
# umon_write( chr(27) + "[2J" )

#DEBUG
#Check all umon commands
# umon_write("words")
# umon_read( ser )
# print() #print new line
##==============================================	

#Check FPGA version number
umon_write( fpga_version_check )
umon_read( ser, echo=0 ) #to not get command echo
print("FPGA version is:")
umon_read( ser ) #read FPGA versionback data
print() #print newline

#==============================================	
#Start ADC aquisition Ch1
print( "Starting ADC Aquisition Ch1")
umon_write( start_ADC1 )
umon_read( ser, echo = 0) #don't echo command

#Check that ADC1 aquisition done
umon_write( check_ADC1_done ), umon_read( ser, echo = 0)
flag = umon_read( ser, echo=0 )
flag = int(flag) #convert string to integer
if flag == 1:
	print( "Aquisition Finished\n")

#Check Channel 1
adc0_array = ['c00c0004','c00c0008','c00c000c','c00c0010','c00c0014','c00c0018','c00c001c','c00c0020']
adc_pin = 1
for k in adc0_array:
	umon_write( k + " w@ ."), umon_read( ser, echo=0 ) #send command to read adc
	tmp = umon_read( ser , echo = 0) #then read the value
	print( "Hex Value Ch1,{}: 0x{}".format(adc_pin, tmp) )
	adc_pin = adc_pin + 1
print()

#==============================================	
#Check Channel 2
#Start ADC aquisition Ch2
print( "Starting ADC Aquisition Ch2")
umon_write( start_ADC2 )
umon_read( ser, echo = 0) #don't echo command

#Check that ADC aquisition done
umon_write( check_ADC2_done ), umon_read( ser, echo = 0)
flag = umon_read( ser, echo=0 )
flag = int(flag) #convert string to integer
if flag == 1:
	print( "Aquisition Finished\n")

adc1_array = ['c00d0004','c00d0008','c00d000c','c00d0010','c00d0014','c00d0018','c00d001c','c00d0020']
adc_pin = 1
for k in adc1_array:
	umon_write( k + " w@ ."), umon_read( ser, echo=0 )
	tmp = umon_read( ser , echo = 0)
	print( "Hex Value Ch2,{}: 0x{}".format(adc_pin, tmp) )
	adc_pin = adc_pin + 1
print() #get new line


ser.close()