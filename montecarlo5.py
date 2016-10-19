import random
import matplotlib
import matplotlib.pyplot 
def cal_dice_roll():
    outcome=random.randint(1,100)
    if 50<=outcome<=99:
     
        return True
    elif outcome==100:
       
        return False
    elif outcome<50:
        
        return False
count=1
def odds(tot_amt,wager):
    amount=tot_amt
    xCor=[]
    yCor=[]
    original_wager=wager
    previous_outcome='Won'
    for count in range(1,101):
        
        if previous_outcome=='Won':
            #amount=amount+wager
            print "Won"
            if cal_dice_roll():
                print "True"
                amount=amount+wager
                wager=original_wager
                print amount
                xCor.append(count)
                yCor.append(amount)
                #previous_outcome='Won'
                # print amount
            else:
                print "False"
                amount=amount-wager
                wager=original_wager
                print amount
                previous_outcome='Lost'
                xCor.append(count)
                yCor.append(amount)
                if amount <=0:
                    break
        elif previous_outcome=='Lost':
             print "Lost"
             
             if cal_dice_roll():
                 print "True"
                 amount=amount+wager
                 print amount
                 xCor.append(count)
                 yCor.append(amount)
                 previous_outcome='Won'
                 wager=original_wager
             else:
                 
                 print "False"
                 amount=amount-wager
                 print amount
                 xCor.append(count)
                 yCor.append(amount)
                 #previous_outcome='Lost'
                 if amount<=0:
                     break
    matplotlib.pyplot.plot(xCor,yCor)      

#for i in range(1,100):
odds(10000,100)        
matplotlib.pyplot.show()   
