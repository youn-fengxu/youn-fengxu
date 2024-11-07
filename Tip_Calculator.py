#TIP CALCULATER
print("Welcome to the Tip Calculator~")
bill=eval(input("What was the total bill?"))
percent=eval(input("How much tip would you like to give? 10, 12 or 15"))
split=eval(input("How many people to split the bill?"))
print(f"So your total bills {bill}."f"\nAnd you would like to give {percent}, splitting between {split} people, right?")
answer=input()
percent=(percent/100)+1.0
tip=round(bill*percent/split,2)
print(f"Okay then, each person should pay {tip}""\nThank you so much!")