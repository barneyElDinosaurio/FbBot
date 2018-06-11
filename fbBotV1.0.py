from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sched, time, timeit
import random
import getpass
import os
import keyboard

while True:
	userEmail = "marioalzatelopez@gmail.com"#input("Please enter email.\n")
	userPass ="Mario4406859"#getpass.getpass("Please enter password.\n")
	userTarget = "jairocardonaea"#input("Please enter Facebook username of the user you wish to target.\n")
	userQuantity = 2#input("Please enter how many messages you wish to send.\n")
	userTimeInterval = 2#input("Please enter time (seconds) between each message. \n")
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
	print ("Initializing...")
	options = webdriver.ChromeOptions()
	prefs = {"profile.default_content_setting_values.notifications" : 2}
	options.add_experimental_option("prefs", prefs)
	options.add_argument("start-maximized")
	browser = webdriver.Chrome("C:/webdrivers/chromedriver.exe",chrome_options=options)
	browser.maximize_window()

	print ("Operation in progress.")

	browser.get('http://www.facebook.com')
	emailElem = browser.find_element_by_id("email")
	emailElem.send_keys(userEmail)
	passElem = browser.find_element_by_id("pass")
	passElem.send_keys(userPass)
	passElem.send_keys(Keys.RETURN)
	userTargetUrl = "http://www.facebook.com/messages/t/" + userTarget
	browser.get(userTargetUrl)
	data = open('script.txt', 'r').read()
        #textAreaElem = browser.find_element_by_css_selector("div textarea.uiTextareaNoResize")
	for i in range(userQuantity):
		thisMessage = random.choice(userMessages)
		keyboard.write(data)
		keyboard.send('enter')
		#os.system("C:/Users/mario/Documents/FbBot/kyes.ahk")
		#textAreaElem.send_keys(thisMessage)
		#textAreaElem.send_keys(Keys.RETURN)
		time.sleep(userTimeInterval)
	print ("Operation successful.")
