groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

list = []
total = 0

while True:
    item = input("What do you want to buy?\n").lower()
    
    if item == "done":
        break
    elif item not in groceries:
        print("Sorry, we don't have that item.")
    else:
        list.append(item)
        total += groceries[item]
        

print("\nYou bought:", list)
print(f"Your total is: ${total}")
if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")
    