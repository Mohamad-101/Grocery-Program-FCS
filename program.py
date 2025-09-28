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
        
    