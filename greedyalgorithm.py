""""
Write a program that uses the greedy algorithm, which gives back the fewest coins as possible
Coin count is number of coins (quarters, dimes, nickels, and pennies)
"""

Amount = float(raw_input("How much change is owed?\n"))
cent_amount = int(round(Amount*100))

while cent_amount < 0:
    Amount = float(raw_input("Retry. How much change is owed?\n"))
    cent_amount = int(round(Amount*100))   

quarter_count = 0
ten_count = 0
five_count = 0
one_count = 0
coin_count = 0


while cent_amount >= 25:
    quarter_count = quarter_count + 1
    cent_amount = cent_amount-25
    
coin_count = coin_count + quarter_count


      
while cent_amount >= 10:
    ten_count = ten_count + 1
    cent_amount = cent_amount-10
    
coin_count = coin_count + ten_count    

   

while cent_amount >= 5:
    five_count = five_count + 1
    cent_amount = cent_amount-5
    
coin_count = coin_count + five_count
   
    
while cent_amount >= 1:
    one_count = one_count + 1
    cent_amount = cent_amount-1

coin_count = coin_count + one_count

print (coin_count)


'''
test cases:

How much change is owed? 0.01    Customer is owed 1 cent in change.
1                                Return 1 coin--a penny (1 coin).

How much change is owed? 0.06     Customer is owed 6 cents in change.
2                                 Return 1-5cent and a penny (2 coins).

How much change is owed? .41      Customer is owed 41 cents in change.
4                                 Return a quarter,dime, nickel, and penny (4 coins).

How much change is owed? 9.93     Customer is owed 9.93 in change.
44                                Return 39 quarters, 1 dime, 1 nickel, 3 pennies (44 coins).

How much change is owed?
-7.75
Retry. How much change is owed?
-7.75
Retry. How much change is owed?
7.75
31

How much change is owed? 4.77
21

How much change is owed? 0
0
    
'''
