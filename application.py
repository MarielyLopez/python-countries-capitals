#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import getpass
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time
countries_capitals = {}
list_mails = []

def insert_country():
    """Here is for that user enter a country for after save a list or dictionary"""
    country = raw_input("Insert a country, please: ")
    #print country
    return country

def verific_country_and_capital(country):
    validname = True
    if country.isdigit() == False:
        pass
    else:
        validname = False
    return validname

def insert_capital():
    #Here is for that user enter a country for after save a list or dictionary
    capital = raw_input("Insert a capital, please: ")
    #print country
    #verific_capital(capital)
    return capital

def ingresa():
    CheckAnswer = False
    while CheckAnswer == False: 
        answer = raw_input("do you want insert more countries an capitals? y - n: ")
        answer = answer.lower()
        Verific = check(answer)
        if Verific == True:
            CheckAnswer = False
            break
        elif Verific == False:
            Chek = True
            CheckAnswer = True
        else:
            print "no valido"
    return Verific

def check(answer): #there teh program will ask if user want enter a new countrie
    if answer == "y" or answer == "yes":
        return False
    elif answer == "n" or answer == "no":
        return True
    else:
        pass

def function():
    Chek = False
    while Chek == False:
        country_and_capital()
        Chek = ingresa()

def country_and_capital():
    verific = False
#    verific_Capital = False
    while verific == False:
        country = insert_country()
        if len(country) == 0:
            return country
            print "Try again."
        else:
            verific_Capital = False
            Word = verific_country_and_capital(country)
            if Word == True:
                verific = True
                while verific_Capital == False:
                    capital = insert_capital()
                    if len(capital) == 0:
                        print "Try again."
                    else:
                        capi = verific_country_and_capital(capital)
                        if capi == True:
                            countries_capitals[country.capitalize()]= capital.capitalize()
                            verific = True
                            verific_Capital = True
                            return True

def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
        return True
    elif os.name == ("nt"):
        os.system("cls")

#-***---***---***---***
def list_of_mails():
    finishmails = False
    while(finishmails == False):
        newmail = raw_input("Enter a recipient: ")
        list_mails.append(newmail)
        insertmail = False
        while (insertmail == False):
            more_mails = raw_input("Do you want enter more emails? y - n: ")
            more_mails = more_mails.lower()
            if more_mails == "yes" or more_mails == "y":
                finishmails = False
                insertmail = True
            elif more_mails == "n" or more_mails == "no":
                finishmails = True
                insertmail = True
            else:
                print "Your answer is incorrect. Try again."

def create_mail():
    list_of_mails()
    user = raw_input("Transmitter: ")
    password = getpass.getpass("Enter password: ")

    message = "Country\t-\tCapital\n"
    for capit_ in countries_capitals:
        message = message + str(capit_) +"\t-\t"+ str(countries_capitals[capit_]) + "\n"
    mail = SendMail(list_mails, user, password, message)
    time.sleep(3)

def SendMail(recipient, user, password, message):
    recipient = recipient
    user = user
    password = password
    message = message

#       def enviar(self):
    for unknownmail in list_mails:
        try: #intentar mandar el correo
            to_adds  = unknownmail
            msg = MIMEMultipart()
            msg['From'] = user
            msg['To'] = to_adds
            msg['Subject'] = "Countries and capitals by Maria"
            msg.attach(MIMEText(message, 'plain'))
                   # from_add = user
            #username = user
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(user, password)
            text = msg.as_string()
            server.sendmail(user, to_adds, text)
            server.quit()
            print "Mail sent successfully to",unknownmail,"!"
        except (smtplib.SMTPAuthenticationError): #mostrar error si se fallo validacion de usuario/password
            print "Your User Name and Password are invalid."

def show_counries():
    coun = 0
    for unknownmail in countries_capitals:
        print unknownmail
        coun += 1
    if coun == 0:
        print "No country was found!"
    time.sleep(2)

def show_capitals():
    coun = 0
    for unknownmail in countries_capitals:
        print countries_capitals[unknownmail]
        coun += 1
    if coun == 0:
        print "No capital was found!"
    time.sleep(2)

def show_Alls():
    coun = 0
    for unknownmail in countries_capitals:
        print "Country:", str(unknownmail)+". Capital:", countries_capitals[unknownmail]
        coun += 1
    if coun == 0:
        print "you have not entered anything to show!"
    time.sleep(2)
    
def order():
    longitud = len(countries_capitals.values())
    coun = 0
    order_cap = sorted(countries_capitals.values())
    order_coun = sorted(countries_capitals.keys())
    while (coun < longitud):
        print "Capital: "+str(order_cap[coun])+ ". Country:", order_coun[coun]
        coun += 1
    time.sleep(2)

def option_user():
    clear()
    print "Please, enter a option, you can enter a number or the name option: "
    print "1. Enter country and capital."
    print "2. To show countries."
    print "3. To show capitals."
    print "4. To Show all."
    print "5. To show all ordered."
    print "6. Send mail."
    print "7. Exit."
    option = raw_input("Inser a option of 1 to 7: ")
    return option

"""here is for check te answer number for the option its her/he
for example option one option two option three"""

def Menu():
    option_menu = False 
    while(option_menu == False):
        option = option_user()
        option = option.lower()
        if option == "1" or option == "Enter country and capital.":
            clear()
            function()
        elif option == "2" or option == "To show countries":
            clear()
            show_counries()
        elif option == "3" or option == "To show capitals.":
            clear()
            show_capitals()
        elif option == "4" or option == "To Show all.":
            clear()
            show_Alls()
        elif option == "5" or option == "To show all ordered." :
            clear()
            order()
        elif option == "6" or option == "Send mail.":
            clear()
            create_mail()
        elif option == "7" or option == "Exit.":
            clear()
            print "... Good bye "
            option_menu = True
            sys.exit(1)
        else:
            print "Unrecognized option.Try again."
            

if __name__ == '__main__':
    Menu()