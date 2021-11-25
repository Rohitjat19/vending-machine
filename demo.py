
def ven():

    a={'item':'coke', 'price': 15}
    b={'item':'pepsi','price': 20}
    c={'item':'coffee','price': 10}
    item=[a,b,c]
    for i in item:
        print(i)

    print('welcome to vending machine')
    print("1. coke")
    print("2. pepsi")
    print("3. coffee")

    def show():
        while(True):
            try:
                n = int(input("Enter your select number 1,2,3: "))        
                if n ==1 :
                    print("please select coke")
                    print("only 1,5,10 or 25 are accepted")
                    coin = int(input("please enter your coin\n "))
                    if coin == 1 or coin == 5 or coin ==10 or coin==25 :
                        coins_count = int(input('how many coins '))
                        total_input_coins = coins_count*coin
                        print ("your order is ready remaning amount", coin-15)
                        print("Total inserted coins is ",  total_input_coins)
                        if total_input_coins >= 15:
                                if total_input_coins != 15:
                                    remaining_amount = total_input_coins-15
                                    print('Your Coke is ready \n Your Remaning Amount Is : ', remaining_amount)
                                    print('Your Coke is ready')
                                    print('THANK YOU')
                        else:
                            print("We need {} more coins".format(15-total_input_coins))
                    else:
                        print("sorry please inserted a valid Coin")
                
                elif n==2:
                    print("please select pepsi")
                    print("only 1,5,10 or 25 are accepted")
                    coin = int(input("please enter your coin\n "))
                    if coin == 1 or coin == 5 or coin ==10 or coin==25 :
                        coins_count = int(input('how many coins '))
                        total_input_coins = coins_count*coin
                        print ("your order is ready remaning amount", coin-20)
                        print("Total inserted coins is ",  total_input_coins)
                        if total_input_coins >= 20:
                                if total_input_coins != 20:
                                    remaining_amount = total_input_coins-20
                                    print('Your pepsi is ready \n Your Remaning Amount Is : ', remaining_amount)
                                    print('Your pepsi is ready')
                                    print('THANK YOU')
                        else:
                            print("We need {} more coins".format(20-total_input_coins))
                    else:
                        print('sorry please inserted a valid Coin')
                    
                elif n==3:
                    print("please select coffee")
                    print("only 1,5,10 or 25 are accepted")
                    coin = int(input("please enter your coin\n "))
                    if coin == 1 or coin == 5 or coin ==10 or coin==25 :
                        coins_count = int(input('how many coins '))
                        total_input_coins = coins_count*coin
                        print ("your order is ready remaning amount", coin-10)
                        print("Total inserted coins is ",  total_input_coins)
                        if total_input_coins >= 10:
                                if total_input_coins != 10:
                                    remaining_amount = total_input_coins-10
                                    print('Your Coffee is ready \n Your Remaning Amount Is : ', remaining_amount)
                                    print('Your Coffee is ready')
                                    print('THANK YOU')
                        else:
                            print("We need {} more coins".format(10-total_input_coins))
                    else:
                        print('You are not inserted a valid Coin')
                
                else:
                    print("this is not available please choose correct number")
            except:
                print("Please type valid choice, String value is not valid")
            
        
    show()
ven()
            





    

