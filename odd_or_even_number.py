def odd_or_even_number():
    name = input("Welcome, what is your name? ")
    print(f"welcome {name}")

    def user_number():
        global number
        try:
            number = int(input("please input a number between 1 and 1000 and I would tell you if it is an odd or even number: "))   
        except ValueError:
            print("please input numbers only, no special characters, no numbers, no punctuation marks, thank you!!")
            user_number()
        else:
            pass

        if number not in range(1, 1001):
            print(f"{number} exceeds the alloted range, Please enter a number within the range")
            user_number() 
        
        else:    
            result = number % 2    
            if result == 0:
                print(f"the remainder of {number} divided by 2 is {result}, therefore {number} is an even number thank you")
            
            elif result != 0:
                print(f"the remainder of {number} divided by 2 is {result}, therefore {number} is an odd number thank you")
        exit1()
        
    def exit1():
        a = input("please enter 'yes' to have another go or select 'no' to end ")
        if a == "yes":
            user_number()
        elif a == "no":
            print("thank you have have a great day!!")
        elif a.lower() != "yes" or a.lower() != "no":
            print("please enter only either 'yes' or 'no' ")
            exit1()    
        else:
            pass
    
        
        
    user_number()

            
        

odd_or_even_number()




