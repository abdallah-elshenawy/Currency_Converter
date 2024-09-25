import os
import time

def display_currencies():
   print("""
      
||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\  ||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||
||\\$//        ~         '------========--------'                \\$//  ||
||<< /        /$\              // ____ \\\\                         \ >>||
||>>|  12    //L\\\\            // ///..) \\\\         L38036133B   12 |<<||
||<<|        \\\\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\\\  |\_/  //* series                 |>>||
||>>|  12                     *\\\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\ ||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//  ||
||====================================================================||
      
""") 
   print("---------------------------------------------------------------------\n")
   print("USD: 1.0")
   print("EUR: 0.85")
   print("EGP: 30.9")
   print("RMP: 6.5\n")


currencies_info = {
   "usd": 1.0,
   "eur": 0.85,
   "egp": 30.9,
   "rmp": 6.5
}

def clear_screen():
   os.system("cls" if (os.name == "nt") else "clear")

def currency_converter():
   clear_screen()
   display_currencies()
   old_currency = input("Choose a currency to convert from: ").lower()
   while True:
      amount = float(input("Enter the amount: "))
      choice = input(f"\nYou entered {amount} {old_currency.upper()}. Confirm? (Y/N): ").lower()
      if choice == "y":
         break

   clear_screen()
   display_currencies()

   new_currency = input("Choose a currency to convert to: ").lower()
   print("Analyzing your request ... Please wait.")
   time.sleep(2)
   print(f"Checking for {new_currency.upper()}'s best rates available .... Please wait")
   time.sleep(2)
   print(f"Getting a discount price for {old_currency.upper()} .... Please wait")
   time.sleep(2)

   if ((old_currency in currencies_info) and (new_currency in currencies_info)):

      clear_screen()
      new_rate = currencies_info[new_currency] / currencies_info[old_currency]

      print(f"Preparing the deal from {old_currency.upper()} to {new_currency.upper()} .... Please wait\n")
      time.sleep(2)
      print(f"Exchange Rate: 1 {old_currency.upper()} = {new_rate} {new_currency.upper()}\n\n")
      time.sleep(2)

      print(f"{amount} {old_currency.upper()} is equal to {round(amount * new_rate, 2)} {new_currency.upper()}\n")
      time.sleep(2)
      if (input("Do you accept this transaction? (Y/N): ")).lower() == "y":
         print("\nTransaction Completed.")
         time.sleep(2)
      else:
         print("\nTransaction Canceled.")
         time.sleep(2)
      
      if (input("Do you want to perform another conversion? (Y/N): ")).lower() == "y":
         currency_converter()
      else:
         print("Thanks for using the currency converter.")
   else:
      print("\nInvalid Currency. Conversion canceled.")
      time.sleep(3)
      currency_converter()
      

currency_converter()