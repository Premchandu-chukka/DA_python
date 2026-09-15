prem_details_sbi = {
    "Name" : 'Prem',
    'adress':'sln123456789',
    'pan':'PCSPC987456',
    'atmpin':'1004',
    'Balance': 10000,
    'MiniStatement': []
    }
all_attempts = 3
while all_attempts >0:
    atm_pin = input("Enter your atm pin:") 
    if atm_pin in prem_details_sbi['atmpin'] and len(atm_pin) == 4 :
        print(f"welcome  to sbi Mr.{prem_details_sbi['Name']}")
        choice_ = int(input('enter \n1.Withdraw \n2.Deposit \n3.checkbalance \n4.Pinchange \n5.MiniStatement:'))

        if choice_ == 1:
            withdraw_money = int(input("Enter amount to withdraw:"))
            if withdraw_money<= prem_details_sbi['Balance'] and withdraw_money%100 == 0:
                prem_details_sbi["Balance"] -= withdraw_money
                print(f'Take your cash and the remaining balance is {prem_details_sbi["Balance"]}')
                prem_details_sbi['MiniStatement'].append(f" Withdraw: {withdraw_money}")
                choose_ = int(input("enter \n1.Home \n2.exit:"))
                if choose_==1:
                    print(f'Taking you to home page')
                    continue
                else:
                    print(f'Thanks for visiting our ATM')
                    break

            else:
                print(f'insuffcient balance or this atm cannot withdraw change')
                
        elif choice_==2:
            deposit_money = int(input('Enter amount you want to deposit:'))
            if deposit_money%100 == 0:
                prem_details_sbi['Balance']+= deposit_money
                print(f'rupees {deposit_money} added sucessfully to your account and total available balance is {prem_details_sbi['Balance']}')
                prem_details_sbi['MiniStatement'].append(f" Deposit: {deposit_money}")
                choose_ = int(input("enter \n1.Home \n2.exit:"))
                if choose_==1:
                    print(f'Taking you to home page')
                    continue
                else:
                    print(f'Thanks for visiting our ATM')
                    break
            else:
                print(f'the atm only accepts notes')
                
        elif choice_==3:
            print(f'your current balance is{prem_details_sbi["Balance"]}')
            choose_ = int(input("enter \n1.Home \n2.exit:"))
            if choose_==1:
                print(f'Taking you to home page')
                continue
            else:
                print(f'Thanks for visiting our ATM')
                break
            
        elif choice_== 4:
            oldpin = input("enter your oldpin:")
            if oldpin == prem_details_sbi["atmpin"]:
                new_atmpin=int(input("enter your new atmp in:"))
                prem_details_sbi["atmpin"]= new_atmpin
                if prem_details_sbi["atmpin"]==new_atmpin:
                    print("new atm pin updated sucessfully")
                else:
                    print("Pin update failed")
                choose_ = int(input("enter \n1.Home \n2.exit:"))
                if choose_==1:
                    print(f'Taking you to home page')
                    continue
                else:
                    print(f'Thanks for visiting our ATM')
                    break
                
        elif choice_==5:
            print(f'{prem_details_sbi['MiniStatement']} and your current balance is {prem_details_sbi['Balance']}')
            choose_ = int(input("enter \n1.Home \n2.exit:"))
            if choose_==1:
                print(f'Taking you to home page')
                continue
            else:
                print(f'Thanks for visiting our ATM')
                break
    else:
        all_attempts-=1
        if all_attempts>0:
            print(f"incorrect pin entered and you have {all_attempts} attempts left")
        else:
            print("your card hasbeen blocked")
    

    
