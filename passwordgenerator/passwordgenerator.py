import random 
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
password_list = []
password = ""


def login_(password):
#Asks the user to login with their newly generated password.
    print("Try logging in with your new password!")
    login = input("Password: ")

    if login == password:
        print("""
        
             **                                                     ********                              **                ** **
    ****                                                   **//////**                            /**               /**/**
   **//**    *****   *****   *****   ******  ******       **      //  ******  ******   *******  ******  *****      /**/**
  **  //**  **///** **///** **///** **////  **////       /**         //**//* //////** //**///**///**/  **///**  ******/**
 **********/**  // /**  // /*******//***** //*****       /**    ***** /** /   *******  /**  /**  /**  /******* **///**/**
/**//////**/**   **/**   **/**////  /////** /////**      //**  ////** /**    **////**  /**  /**  /**  /**//// /**  /**// 
/**     /**//***** //***** //****** ******  ******        //******** /***   //******** ***  /**  //** //******//****** **
//      //  /////   /////   ////// //////  //////          ////////  ///     //////// ///   //    //   //////  ////// // 
        
        """)
        
    else:
        print("""
        
                                   (                            ____ 
   (                       )\ )                   (    |   / 
   )\            (        (()/(    (      (    (  )\ ) |  /  
((((_)(  (  (   ))\(  (    /(_))  ))\ (   )\  ))\(()/( | /   
 )\ _ )\ )\ )\ /((_)\ )\  (_))_  /((_))\ |(_)/((_)((_))|/    
 (_)_\(_|(_|(_|_))((_|(_)  |   \(_)) _(_/((_|_))  _| |(      
  / _ \/ _/ _|/ -_|_-<_-<  | |) / -_) ' \)) / -_) _` |)\     
 /_/ \_\__\__|\___/__/__/  |___/\___|_||_||_\___\__,_((_)    
                                                             
        
        """)


def complex():
#Generates and displays a random password consisting of letters, numbers and symbols.
#Asks the user how many letters, numbers and symbols they would like in their password.
#The characters from each respective category are truly randomized and not grouped together.
#We will refer to the result of this function as a complex password.

    letter_count = int(input("How many letters would you like in your password:\n"))
    number_count = int(input("How many numbers would you like in your password:\n"))
    symbol_count = int(input("How many symbols would you like in your password:\n"))
    
    for letter in range(letter_count):
        password_list.append(random.choice(letters))
    for number in range(number_count):
        password_list.append(random.choice(numbers))
    for symbol in range(symbol_count):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    password = "".join(password_list)

    print(password)
    login_(password)

    
def simple():
#Generates and displays a random password consisting of letters, numbers and symbols.
#Asks the user how many letters, numbers and symbols they would like in their password.
#The characters from each respective category are not truly randomized and will be grouped together.
#We will refer to the result of this function as a simple password.

    letter_count = int(input("How many letters would you like in your password:\n"))
    number_count = int(input("How many numbers would you like in your password:\n"))
    symbol_count = int(input("How many symbols would you like in your password:\n"))
    
    for letter in range(letter_count):
        password_list.append(random.choice(letters))
    for number in range(number_count):
        password_list.append(random.choice(numbers))
    for symbol in range(symbol_count):
        password_list.append(random.choice(symbols))

    password = "".join(password_list)

    print(password)
    login_(password)


print("""

 ,---.    .--.     .---.   .---. .-.  .-. .---.  ,---.   ,'|"\      ,--,   ,---.  .-. .-.,---.  ,---.    .--.  _______  .---.  ,---.    
 | .-.\  / /\ \   ( .-._) ( .-._)| |/\| |/ .-. ) | .-.\  | |\ \   .' .'    | .-'  |  \| || .-'  | .-.\  / /\ \|__   __|/ .-. ) | .-.\   
 | |-' )/ /__\ \ (_) \   (_) \   | /  \ || | |(_)| `-'/  | | \ \  |  |  __ | `-.  |   | || `-.  | `-'/ / /__\ \ )| |   | | |(_)| `-'/   
 | |--' |  __  | _  \ \  _  \ \  |  /\  || | | | |   (   | |  \ \ \  \ ( _)| .-'  | |\  || .-'  |   (  |  __  |(_) |   | | | | |   (    
 | |    | |  |)|( `-'  )( `-'  ) |(/  \ |\ `-' / | |\ \  /(|`-' /  \  `-) )|  `--.| | |)||  `--.| |\ \ | |  |)|  | |   \ `-' / | |\ \   
 /(     |_|  (_) `----'  `----'  (_)   \| )---'  |_| \)\(__)`--'   )\____/ /( __.'/(  (_)/( __.'|_| \)\|_|  (_)  `-'    )---'  |_| \)\  
(__)                                     (_)         (__)         (__)    (__)   (__)   (__)        (__)               (_)         (__) 

""")

password_diff = int(input("Enter 1 for a simple password. \nEnter 2 for a complex password.\n"))

if password_diff == 1:
    simple()
elif password_diff == 2:
    complex()
else:
    print("We'll get there soon!!!")
