from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sched, time, timeit
import random
import getpass
import keyboard
import json
from pprint import pprint
import os
import hashlib

#LICENSE

try:
        licenseFile = open('license.txt','r')

        hashLicense = licenseFile.read(80) 

        userEmail = input("Please enter your user email.\n")

        hashUser = userEmail + '+qricaqricaweed'
        hashUser =  hashlib.md5(hashUser.encode("utf")).hexdigest()
        
        if(hashLicense == hashUser):
        
                while True:
                        userPass = getpass.getpass("Please enter password.\n")
                        userQuantity = input("Please enter how many users you wish to send.\n")
                        userQuantity = int(userQuantity)
                        userTimeInterval = input("Please enter time (seconds) between each message. \n")
                        userTimeInterval = int(userTimeInterval)
                        userMessageType = "single"#input("Please enter message type ['single' or 'multiple', without quotes]. \n")
                        if userMessageType == 'single':
                                userMessageQuantity = 1
                                userMessage = input("Please enter the message you wish to send. \n")
                                userMessages = [userMessage]
                                operation = True
                        elif userMessageType == 'multiple':
                                userMessageQuantity = input("How many distinct messages will you have?\n")
                                userMessages = []
                                for i in range(1, userMessageQuantity + 1):
                                        thisMessage = raw_input("Please enter message " + str(i) + " of " + str(userMessageQuantity) + ".\n")
                                        userMessages.append(thisMessage)
                                operation = True
                        else:
                                print("Invalid input.")
                                operation = False
                                input("Press ENTER to restart the program.\n")


                        if operation:
                                for i in range(userMessageQuantity):
                                        print ("    " + str(i + 1) + " " + userMessages[i] + "\n")
                                proceed = input("Proceed? y/n\n")
                                if proceed == 'y':
                                        operation = True
                                        break;
                                else:
                                        print ("Operation aborted.\n")
                                        input("Press ENTER to restart the program.\n")
                                        operation = False




                if operation:

                        #getting friends from fb json
                        print("reading friend list")
                        with open('friendsin.json','rb') as f:
                                data = json.load(f)
                        print ("Friends readed,Initializing Bot . . .")
                        
                        #webdriver
                        options = webdriver.ChromeOptions()
                        prefs = {"profile.default_content_setting_values.notifications" : 2}
                        options.add_experimental_option("prefs", prefs)
                        options.add_argument("start-maximized")
                        browser = webdriver.Chrome("C:/webdrivers/chromedriver.exe",chrome_options=options)
                        browser.maximize_window()

                        print ("Operation in progress. . .")

                        browser.get('http://www.facebook.com')
                        emailElem = browser.find_element_by_id("email")
                        emailElem.send_keys(userEmail)
                        passElem = browser.find_element_by_id("pass")
                        passElem.send_keys(userPass)
                        passElem.send_keys(Keys.RETURN)
                        #checking facebook login
                        userTargetUrl = "http://www.facebook.com/messages/t/"
                        browser.get(userTargetUrl)
                        #iterate users
                        for i in range(userQuantity):
                                #thisMessage = random.choice(userMessages)
                                inputsaso = browser.find_element_by_xpath("//input[contains(@placeholder,'Buscar en Messenger')]")
                                time.sleep(1)
                                inputsaso.send_keys(data["friends"][i]["name"])
                                time.sleep(1)
                                keyboard.send('enter')
                                time.sleep(2)
                                keyboard.write(userMessage)
                                time.sleep(1)
                                keyboard.send('enter')
                                time.sleep(userTimeInterval)
                        print ("Operation successful.")
        else :
                print("This license isnt valid for this account")


except IOError:

        print("License doesnt exist,creating license by email account fb")
