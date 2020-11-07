import subprocess
import time
print('At Your Service Sir')
time.sleep(2)
print('''
====================================
|  Exploiting The System For You   |
====================================
''')
time.sleep(2)

# In Windows we use 'netsh wlan show profiles' to get the name of all wifi to which our device was connected
# now we will store the output of this command in variable 'data' by using subprocess module
# module which will run this command for us using 'check_output' method on subprocess.
# By default 'subprocess.check_output' gives output as Byte, So we need to convert it to string
# using 'decode' method to 'utf-8' format and then split at every new line,and convert it to list
# thats why split('\n')
data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

print('Name Of All Wifi Found\n')
time.sleep(2)

# now we will store the profilesby converting them to  list
profiles = [i.split(':')[1][1:-1] for i in data if 'All User Profile' in i]
print('Extracting Wifi Passwords\n')
time.sleep(2)

# using for loop we are checking and printing the wifi name
# passwords if they are present in 2nd command else empty string
for i in profiles:
	# running the 2nd command to check wifi passwords
	results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')

	# storing the password after converting them to list
	passwords = [b.split(":")[1][1:-1] for b in results if 'Key Content' in b]
	try:
		print('{:30}| {:}'.format(i,passwords[0]))
	except IndexError:
		print('{:30}| {:}'.format(i,''))
print('''
====================================
|      Task Completed              |
====================================
''')