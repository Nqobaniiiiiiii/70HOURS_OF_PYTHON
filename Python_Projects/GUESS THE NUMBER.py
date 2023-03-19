import random


#CONDITIONS OF LOOP 
comp_guess = random.randint(1, 100)                                                                                                                                              
nummber_of_attempts = 3
count_attempt = nummber_of_attempts + 1


# this loop   breaks whEN THE 2 CONDITIONS ABOVE ARE TRUE   
while nummber_of_attempts >= count_attempt :  # WE MYT CHANGE THIS TRUE TO A CONDITION 
    try:
        user_guess = int(input("Please gusess number"))
        
        if comp_guess == user_guess :
            nummber_of_attempts = nummber_of_attempts 
            print(f'You won in {nummber_of_attempts} attemPTS.')
            break
        
        elif user_guess < comp_guess :
            print("too low")
            nummber_of_attempts = nummber_of_attempts + 1
            count_attempt
            
        else :
            print(" too high")
            nummber_of_attempts = nummber_of_attempts + 1 
            count_attempt
            
              
            
    except :
        print("CHOOSE NUM,BER BTWN 1 TO 100")