import requests
import sys
import time
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
def menu():
    print("Please choose an option:")
    print("1: Live counter")
    print("2: One time check")
    print("3: Convert")
    print("4: exit")
def dollars():
    x = int(input("Please enter how many seconds you want between each price check: ")) # There is a maximum on the API, make sure it's about 6 ish per minute 
    while True:
        print("Current price of btc is: $" + r.json()["bpi"]["USD"]["rate"] + " - Updated at: " + r.json()["time"]["updated"]) #Change 'updateduk' to 'updated' for UTC time not GMT - Change USD to EUR or GBP for euros or pounds
        time.sleep(x)
def once():
    print("Current price of btc is: $" + r.json()["bpi"]["USD"]["rate"] + " - Updated at: " + r.json()["time"]["updated"]) #Change 'updateduk' to 'updated' for UTC time not GMT - Change USD to EUR or GBP for euros or pounds
    ask_exit()
def convert():
    print("Please choose an option:")
    print("a: BTC to USD")
    print("b: USD to BTC")
    option = input("a or b?").lower()
    if option == "a":
        bitcoin_amount = float(input("Please enter the amount of bitcoin: "))
        bitcoin_price = float(r.json()["bpi"]["USD"]["rate"].replace(",", "")) # Change USD to EUR or GBP for euros or pounds
        print (f"That is ${round(bitcoin_amount * bitcoin_price ,2)} worth of BTC")
        time.sleep(3)
    if option == "b":
        USD_value = float(input("Please enter the amount of USD: "))
        bitcoin_price = float(r.json()["bpi"]["USD"]["rate"].replace(",", ""))# Change USD to EUR or GBP for euros or pounds
        print(round(USD_value / bitcoin_price, 8))
        print(f"That is {round(USD_value / bitcoin_price, 8)} BTC.")
        time.sleep(3)
    ask_exit()
def ask_exit():
    cont = input("Do you want to exit?: yes or no? ").lower()
    if cont == "yes":
        exit() 
def exit():
    sys.exit(0)
options = {
    1: dollars,
    2: once,
    3: convert,
    4: exit,
}
def getOption():
    optionRaw = input("Option #: ")
    if(optionRaw.isdigit() and 0 < int(optionRaw) <= len(options)): 
        return int(optionRaw)
    print("Invalid option, please try again.")
    return getOption()

while True:
    menu()
    options[getOption()]()

