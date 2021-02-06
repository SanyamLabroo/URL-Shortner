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

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)       #1 for female voice and 0 for male voice

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def check():
    print("\t\t\t*URL CHECKER*", flush = False)
    
    commands = ["Hello, I am the virtual URL checker.", "I will check whether the given url is valid or not.",
                	"If the given Url is valid only then You can proceed to further process",
            		"Else You won't be able to proceed further.", "Let's begin"]
    
    time.sleep(1)
    print("\n\t*NOTE*\nIf you enter anything else a URL, the program will end and you will to start again.\n")
    time.sleep(3)
    for i in chain.from_iterable(repeat(commands, 1)):
    	time.sleep(0.5)
    	speak(i)
    
check()

def shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

def commands():
    
    clear()
    
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
    
def get(shorten):
    
    while True:
        
        time.sleep(1)
        
        speak("Enter the operation you want to perform.")
        try:
            c = int(input("\nEnter the operation you want to perform: "))
            
        except ValueError:
            speak("Invalid operation. Please try again.")
            continue
        
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
            
        else:
            speak("Invalid Operation. Please try again.")
            continue
        
        time.sleep(1)
        
        speak("To perform again, please enter yes else enter no.")
        again = input("\nTo perform again, Please enter 'yes' else enter 'no': ")
        
        if again == "yes":
            time.sleep(0.5)
            continue
        
        elif again == "no":
            speak("Thank you for your time.")
            print("\nThank You.")
            exit()
            
        else:
            speak("Invalid Input.\nPlease choose again.")
            again = input("To perform again, Please enter 'yes' else enter 'no': ")

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

speak("Please enter your URL for verification.")
url = input("Enter the url: ")

if url.isnumeric() == True:
    speak("You have entered an integer value. The program will end for now. Please restart again.")
    time.sleep(0.5)
    print("You have entered an integer value.\nPlease restart again.")
    time.sleep(1)
    exit()
    
if url.isdigit() == False:
    if(url.isdigit() == True) and "." in url:
        speak("You have entered a float value. The program will end  for now. Please try again.")
        time.sleep(0.5)
        print("You have entered a float value.\nPlease restart again.")
        time.sleep(1)
        exit()
        
    elif "https://" and ".com" in url:
        pass
    
    elif set(url).difference(ascii_letters + digits):
        speak('You have entered special characters. The program will end for now. Please restart again.')
        time.sleep(0.5)
        print("You have entered special characters.\nPlease restart again.")
        time.sleep(1)
        exit()
    
    else:
        speak("You have entered a string value. The program will end for now. Please restart again.")
        time.sleep(0.5)
        print("You have entered a string value.\nPlease restart again.")
        time.sleep(1)
        exit()


if(isValidURL(url) == True):
    
    speak("This a valid URL. You can use it.")
    time.sleep(0.5)
    speak("Taking you to menu section. Please wait for a moment.")
    time.sleep(1)
    
    commands()
    get(shorten)
