#Importing necessary libraries
import pyshorteners
import os
import time
import requests
import validators
import pyttsx3
import speech_recognition as sr
from itertools import chain, repeat
import re
from string import ascii_letters, digits
from tabulate import tabulate

#Clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#Using pttsx3 for voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)       #1 for female voice and 0 for male voice

#Speak function
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

#Function to check if the given url is valid or not
def check():
    print("\t\t\t*URL CHECKER*", flush = False)
    
    #Commands for url check
    commands = ["Hello, I am the virtual URL checker.", "I will check whether the given url is valid or not.",
                	"If the given Url is valid only then You can proceed to further process",
            		"Else You won't be able to proceed further.", "Let's begin"]
    
    time.sleep(1)
    print("\n\t*NOTE*\nIf you enter anything else a URL, the program will end and you will to start again.\n")
    time.sleep(3)
    for i in chain.from_iterable(repeat(commands, 1)):
    	time.sleep(0.5)
    	speak(i)
    
check()		#Calling the url check function

#Function for url check
def shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

#Function to take the user to main menu
def commands():
    
    #Again calling the clear function to clear the terminal
    clear()
    
    #Main menu commands
    print("\t\t\t*MAIN MENU*", flush=False)
    operations = ["Welcome to the main menu", "There are two opeartions which you can perform:", "And they are:", 
                    "1st. Shorten a URL", "2nd. Unshorten a URL"]
    
    for i in chain.from_iterable(repeat(operations, 1)):
        time.sleep(0.5)
        speak(i)
        time.sleep(0.5)
        
    print("1. Shorten a URL")
    time.sleep(0.5)
    print("2. Unshorten a URL")

#Function for user to decide if he/she wants to shorten the url or unshorten the url
def get(shorten):
    
    #While loop to repeat the commands
    while True:
        
        time.sleep(1)
        
	#Checking which operation the user want to perform
        speak("Enter the operation you want to perform.")
        try:
            c = int(input("\nEnter the operation you want to perform: "))
            
        except ValueError:
            speak("Invalid operation. Please try again.")
            continue
        
	#First command for shorten the url
        if c == 1:
            
            clear()
            
            print("\t\t\t*URL SHORTNER*", flush = False)
            time.sleep(0.5)
            speak("Enter your URL again to shorten.")
            url = input("\nEnter your URL again to shorten: ")
            time.sleep(0.5)
            speak("The shorten form of the given URL is.")
            print("\nThe shorten form of the given URL is: ",shorten(url))
            time.sleep(1)
                
            speak("I have made a tabular representaion of the input and output data.")
            print("\nTabular representation of input and output data:\n")
            time.sleep(1)
            table = [["Given url:", [url]],["Shorten form:", [shorten(url)]]]
            print(tabulate(table))
         
	#Second command for unshorten the url
        elif c == 2:
            
            clear()
            
            print("\t\t\t*URL UNSHORTNER*", flush = False)
            time.sleep(0.5)
            speak("Please enter your URL again to unshorten.")
            url = input("\nEnter your URL again to Unshorten: ")
            site = requests.get(url)
            time.sleep(0.5)
            speak("The unshorten form of the given url is.")
            print("\nThe unshorten form of the given URL is: ",site.url)
            time.sleep(1)
            
            speak("I have made a tabular representaion of the input and output data.")
            print("\nTabular representation of input and output data:\n")
            time.sleep(1)
            table = [["Given url:", [url]],["Shorten form:", [site.url]]]
            print(tabulate(table))
        
	#If user inputs a value other then 1 or 2
        else:
            speak("Invalid Operation. Please try again.")
            continue
        
        time.sleep(1)
        
	#To perform again.
        speak("To perform again, please enter yes else enter no.")
        again = input("\nTo perform again, Please enter 'yes' else enter 'no': ")
        
	#If user inputs yes then loops starts again
        if again == "yes":
            time.sleep(0.5)
            continue
        
	#If user inputs no then the loop breaks and program ends
        elif again == "no":
            speak("Thank you for your time.")
            print("\nThank You.")
            exit()
        
	#If user enter a value other then yes or no then this statement becomes true
        else:
            speak("Invalid Input.\nPlease choose again.")
            again = input("To perform again, Please enter 'yes' else enter 'no': ")

#Using regex to check if the input url is valid or not
def isValidURL(str):

	# Regex to check valid URL 
	regex = ("((http|https)://)(www.)?" +
			"[a-zA-Z0-9@:%._\\+~#?&//=]" +
			"{2,256}\\.[a-z]" +
			"{2,6}\\b([-a-zA-Z0-9@:%" +
			"._\\+~#?&//=]*)")
	
	p = re.compile(regex)

	if (str == None):
		return False

	if(re.search(p, str)):
		return True
	else:
		return False

#Entering the url
speak("Please enter your URL for verification.")
url = input("Enter the url: ")

#If user inputs an integer value
if url.isnumeric() == True:
    speak("You have entered an integer value. The program will end for now. Please restart again.")
    time.sleep(0.5)
    print("You have entered an integer value.\nPlease restart again.")
    time.sleep(1)
    exit()
 
if url.isdigit() == False:
    #If user inputs a floating value
    if(url.isdigit() == True) and "." in url:
        speak("You have entered a float value. The program will end  for now. Please try again.")
        time.sleep(0.5)
        print("You have entered a float value.\nPlease restart again.")
        time.sleep(1)
        exit()
    
    #If user inputs a url which contains "https://" and ".com"
    elif "https://" and ".com" in url:
        pass
    
    #If user enters special characters
    elif set(url).difference(ascii_letters + digits):
        speak('You have entered special characters. The program will end for now. Please restart again.')
        time.sleep(0.5)
        print("You have entered special characters.\nPlease restart again.")
        time.sleep(1)
        exit()
    
    #else if user inputs a string value
    else:
        speak("You have entered a string value. The program will end for now. Please restart again.")
        time.sleep(0.5)
        print("You have entered a string value.\nPlease restart again.")
        time.sleep(1)
        exit()

#And if the url is valid then you will be taken to the main menu
if(isValidURL(url) == True):
    
    speak("This a valid URL. You can use it.")
    time.sleep(0.5)
    speak("Taking you to menu section. Please wait for a moment.")
    time.sleep(1)
    
    commands()
    get(shorten)
