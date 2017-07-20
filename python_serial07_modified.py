#this is very python serial
#it should work but i need fix this path

import serial
from time import sleep
from os import getlogin

import csv
import os
import random
	
def find_ports():
    #get from stackoverflow
    ports = ("COM%s" % (i+1) for i in range(256))
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
	
def make_connection():
    baudRate = 9600
    port = 0
    while (not port):
        try:
            ports = find_ports()		
            port = ports[0]
        except:
            print("Please connect module to USB")
            sleep(0.5)
    print("\nConnection completed on port %s\n" % port)
    serialData = serial.Serial(port, baudRate)
    sleep(1);	#wait for arduino initialization
    # return serialData, port
    return serialData
	

def communicate(connection, debug = [False]):
    # text = input('Podaj tekst do wyswietlenia: ')
    runcsv = False	#jednorazowo
	#debug			#stale
    text = input('@stranger_console>>> ')
    words = text.split()
	
	#sekcja debuggingu
	#uzyj if (debug): print(something)
	#w dowolnym miejscu tej funkcji
	#badz funkcji make_command()
    if (not words):
        words = ["none"]
	
    if (words[0] == 'debug') and (len(words)>1):
        if (words[1] == 'on'):
            debug[0] = True
        elif (words[1] == 'off'):
            debug[0] = False
        else:
            pass
    
    if (words[0] == "help"):
        if (len(words)>1):
            help_mode(words[1])
        else:
            help_mode()
	
    if (words[0] == "whoami"):
        print(getlogin())
	
    if (words[0] == "runcsv"):
        fileName = "thing.csv"
        timeout = 1 # t[s]
        runcsv = True
        try:
            fileName = words[1]
        except:
            pass
        try:
            timeout = int(words[2])
        except:
            pass
        execute_command(connection, "thing.csv", timeout)
        # run_csv(fileName="thing.csv")
    #it just show what you said
    debug_mode("words", words, debug[0])
	
    # print(words)
    #makes command from words
    output_command = make_command(words,debug[0])
    text_out = output_command[1]
    strcom = output_command[0]
    if (strcom):
        #iteration for many items
        for item in strcom:
            connection.write(item.encode('utf-8'))
            sleep(0.05)
        return True, runcsv

    if (text_out):
        connection.write(text_out.encode('utf-8'))
        return True, runcsv
    else:
        debug_mode("output_command", output_command, debug)
        return False, runcsv


def execute_command(connection, fileName, timeout):
    # fileName = "thing.csv"
    data = csv_reader(fileName, column=True)
    for row in data:
        for words in row:
            words = words.split()
            # print("words:", words)			
            csv_command = make_command(words, [True])
            text_out = csv_command[1]
            strcom = csv_command[0] 
            # print("strcom: ", strcom)
            if (strcom):
                #iteration for many items
                # print("WE ARE HERE")
                for item in strcom:
                    connection.write(item.encode('utf-8'))
                    # connection.write(item)
                    # print('something wrong')
                    # sleep(0.05)
                    sleep(timeout);
            if (text_out):
                # connection.write(text_out.encode('utf-8'))
                pass				
    return True

def get_path(fileName):
    # soup = "this is sample \n of the text"
    # fileName = "indexfile.html"
    try:
	    os.chdir(os.path.dirname(__file__))
    except:
	    os.path.dirname(os.path.abspath(__file__))
    pathAbs = os.getcwd()
    path = os.path.join(pathAbs, fileName)
    # file = open(path, "w")
    return path	
	
def csv_reader(fileName, column=False):
    path = get_path(fileName)
    data = []
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if (column):
                for item in row:
                    print(item)
                    data.append(item)
            else:
                print(" ".join(row))
    return [data]		
		
def make_command(words,debug):
    strcom = []
    command = ""
    text_out = ""
    if (len(words)):
        order = words[0]
    else:
        order = "none"
    debug_mode("order", order, debug)
    exit_words = ['exit', 'koniec', 'finito', 'close']
    if (order == 'led'):
        try:
            pins = words[1].split(',')
            debug_mode("pins", pins, debug)
            values = words[2].split(',')
            debug_mode("values", values, debug)
            command = []
            for key,value in enumerate(pins):
                if (int(pins[key]) < 10):
                    pin = "0" + str(pins[key])
                else:
                    pin = str(pins[key])
                value = str(values[key])
                strcom.append("led" + pin + value)
                command.append(["led",pins[key],values[key]])
        except:
            strcom = []	#empty means False
            command = "wrong command"
            text_out = "wrong: led"
        #simply turn on the led
        #with the proper number
    elif (order == 'pwm'):
        text_out = "command: pwm"
        #this is for pwm write
    elif (order == 'mov'):
        #this is for making some movement
        text_out = "command: move"
    elif (order == 'none'):
        text_out = "just do nothing"
    elif (order in exit_words):
        text_out = False
    else:
        #which means this is default action
        text_out = " ".join(words)
    debug_mode("strcom", strcom, debug)
    debug_mode("----------------------", "", debug)
    return strcom, text_out
	
def close_connection(connection):
    connection.write("exit".encode('utf-8'))
    sleep(0.5)
    connection.close();
    print("zakonczono.")
    return 0

def debug_mode(name, variable, debug):
    #use it while debugging
    #just put it somewhere
    if (debug):
        print('\t', name,': ', variable)
		
def help_mode(argument="all"):
    actual_text = ""
    some_text = '''\n
    Aby wyswietlic pomoc dla komendy wpisz: help [komenda]
    Lista dostepnych komend:
	
	> debug
	> exit
	> help 
	> led 
	> pwm 
	> runcsv 
	\n'''
    debug_text = '''\n
    Wlacza i wylacza tryb debugowania.
    -aby uzyc wpisz komende
	    debug [on/off]
    -wyswietla stan zmiennych
    w trakcie wykonywania programu\n'''
    led_text = '''\n
    Pozwala na sterowanie pojedynczymi liniami portu.
    W domysle dotyczy diod led. Przykladowe uzycie:
        led [1,2,3,4] [1,0,1,0]
    -ledy na pinach 1234 ze stanami odp 1010\n'''
    pwm_text = '''\n
    Aktualnie w fazie rozwoju.
    Dzialanie bedzie analogiczne do instrukcji <>led<>
	\n'''	
    csv_text = '''\n
    Mozesz uzywac instrukcji zapisanych w plikach csv.
    Aby to zrobic, wystarczy wpisac polecenie:
        runcsv [plik.csv]
    gdzie plik.csv to plik z rozkazami zlokalizowany
    w katalogu naszego skryptu
    \n'''
    exit_text = '''\n
    Aby zakonczyc komunikacje z arduino
    i wyjsc z programu wpisz komende:
        exit\n'''	
	
	
    if (argument == "all"): actual_text = some_text
    elif (argument == "debug"): actual_text = debug_text
    elif (argument == "led"): actual_text = led_text
    elif (argument == "pwm"): actual_text = pwm_text
    elif (argument == "exit"): actual_text = exit_text
    elif (argument in ("runcsv", "csv")): actual_text = csv_text
    else: actual_text = some_text
	
    print(actual_text)

		
# data = ""
def get_line(serialData):
	# "|" - moj osobisty znak konca linii
    data = ""
    letter = ""
    # for x in range(13):
        # data += str(serialData.read(), 'utf-8')
    while (letter != '|'):
        try:
            letter = str(serialData.read(), 'utf-8')
            data += letter
        except:
            data = "\nConnection out\n"
            sleep(0.5)
            return data
    return data[:-1]
    # return data
	
	
def run_console():
    #czesc wykonawcza
    # connection = make_connection(find_ports())
    connection = make_connection()
    condition = communicate(connection)
    while condition[0]:
        condition = communicate(connection)
        # if (condition[1]):
            # execute_command(connection)
    close_connection(connection)	#zamykanie polaczenia	

	

#uruchomienie konsoli	
#run_console()



#just to find connected devices
results = find_ports()
print(results)
	
	
input('\nenter aby zakonczyc...')

