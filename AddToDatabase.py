#COnfiguration file test

#importing parser
from configparser import ConfigParser
#Getting current time and date modules
from datetime import datetime
#Importing socket to get host IP/name
import socket
#Blank out password library
from getpass import getpass
#Import base64 for encodign password
import base64

#Declaring config file.
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)


config = ConfigParser()
def createINI():
    #Getting teh current time.
    firstRunTime = datetime.now()
    #These are the default variables. they can be changed if user wants.
    config['DEFAULTS'] = {
        'Install Date & Time: ': firstRunTime,
        'Host Machine Name: ': host_name,
        'Host Machine IP: ' : host_ip,
        'Subject': '!!!! Public IP Changed !!!!',
        'Email Body': ("""
          Your Public IP has changed.\n
          Host Name: {}
          Host IP: {}
          API Host Used: {}
          OLD Public IP: {}
          NEW Public IP: {}\n 
          \nThank you For Using GetPubIP from K&M Inc.""")#.format(previousIP, currentPublicIP))

    }

    config['database'] = {}
    database = config['database']
    #Setting all the variables.
    print("\nThe next few questions will help you setup your emailing notification service.\nPressing \"Enter\" on some questions will result in default values: \n")
    database['Send Email To'] = input("Send email to this address: ") or 'BLANK_TO_EMAIL'
    database['Sending Email'] = input("SMTP Authentication Email: ") or 'BLANK_AUTH_EMAIL'
    #Getting input from user for SMTP Auth Pass - Secure entry and Base64 Encoding for storage.
    #Gets the password twice and makes sure they are the same string. If not loop repeats.
    while True:
        rawPass = getpass("SMTP Authentication Email Password (Entry will be blank while typing): ") or 'BLANK_AUTH_PASSWORD'
        rawPass2 = getpass("Re-Enter SMTP Auth Password: ") or 'BLANK_AUTH_PASSWORD'
        if rawPass == rawPass2:
            print("Passwords Match - Moving On\n")
            break
        else:
            print("\nPasswords do not match!\n")
            pass
    asciiPass = rawPass.encode('ascii')
    base64PassEnc = base64.b64encode(asciiPass)
    base64PassEncAsc = base64PassEnc.decode('ascii')
    database['Email Password'] = base64PassEncAsc
    #Done with Password

    database['SMTP Server'] = input("SMTP Server Address (Default: smtp.gmail.com): ") or 'smtp.gmail.com'
    database['SMTP Server Port'] = input("SMTP Port Number (Default: 465): ") or '465'
    database['From Email'] = input("Header FROM Address (Change this if needed): ") or database['Sending Email']
    database['To Email'] = input("Header TO Address (Change this if needed): ") or database['Send Email To']

    database['IPv4 API #1'] = input("Main API URL for Public IPv4 (Default: https://v4.ident.me/): ") or 'https://v4.ident.me/'
    database['IPv4 API #2'] = input("Second-Backup API URL for Public IPv4 (Default: https://icanhazip.com/): ") or 'https://icanhazip.com/'
    database['IPv4 API #3'] = input("Third-Backup API URL For Public IPv4 (Default: https://ifconfig.me/ip): ") or 'https://ifconfig.me/ip'
    print("\nThank You, You have succefully completed the Initial Configuration.\nYou may change anything you wish by either running this script again or directly changing the 'config.ini' file.")

    #Writing congiurations to file.
    with open('config.ini','w') as configfile:
        config.write(configfile)
print(__name__)
#Running Only this code if this file is so - That way user can re-run config program.
if __name__ == "__main__":
    #Running the function to test. Leave commenetd when packaging file.
    createINI()
    print(__name__)