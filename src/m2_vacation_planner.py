# ask for type of destination
#   prints out a packing list for that vacation type

###############################################################################
# done: 1. (5 pts)
#
#   For this module, we are going to create a vacation planner that will help
#   the user plan what they need to bring on vacation.
#
#   For this _TODO_, write a function called starter_list() that takes 1
#   parameter:
#       - type      <-- str
#
#   This function should use a match case statement that checks for a matching
#   vacation type and returns a list of items that the user should probably
#   bring on that type of vacation.
#
#   So, for example, if the function is given the type "beach", the function
#   would return a list like this:
#
#      ["swimsuit", "towel", "sunscreen"]
#
#   For your function, make sure you have at least 3 vacation types and each
#   type should return a list of at least 3 items.
#
#   If the user types in an invalid vacation type, the function should return
#   an empty list.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def starter_list(vacation_type):
    
    match vacation_type.lower():
        case "beach":
            return ["swimsuit", "towel", "sunscreen"]
        case "mountain":
            return ["hiking boots", "warm jacket", "water bottle"]
        case "city":
            return ["comfortable shoes", "map", "camera"]
        case _:
            return []

print(starter_list("beach"))
print(starter_list("mountain"))
print(starter_list("city"))
print(starter_list("jungle"))  

###############################################################################
# done: 2. (4 pts)
#
#   Now, perhaps the user would like to bring some of their own stuff that they
#   specify.
#
#   For this _TODO_, write a function called gather_items() that will
#   continually ask the user for an item to add to their list.
#
#   The function should meet these criteria:
#
#       1. Prompt the user like so:
#               "Please enter an item: "
#       2. It should keep track of all of the items in a list as it goes.
#       3. If the user types "end", it should stop asking for more items
#       4. Once it is done, it should return the list of items.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def gather_items():
    items = []
    while True:
        item = input("Please enter an item: ")
        if item.lower() == "end":
            break
        items.append(item)
    return items

print(gather_items())

###############################################################################
# done: 3. (6 pts)
#
#   For this _TODO_, write a function called main() that will start things off.
#
#   Your function should meet these criteria:
#
#       1. It should first greet the user in a friendly way.
#       2. It should then prompt the user for a vacation type and allow them to
#          enter a vacation type.
#       3. It should then show them what item are already in their list based
#          on the type entered. There should be one item per line.
#       3. Next, it should start asking them for particular items and keep track
#          of them as the user enters more.
#       4. Once the user is done entering items, instead of printing the list of
#          items that they entered, it should print their entire list that
#          includes the starter list from the beginning and all the items that
#          they entered. You should do this by combining the lists and looping
#          through it printing each item. Do NOT just loop through the two lists
#          separately.
#       5. At the very end, it should say goodbye to the user in some friendly
#          way.
#
#   Make sure you call the function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
    print("Welcome to Vacation Planner!")
    vacation_type = input("What type of vacation are you planning (beach, mountain, city)?: ")
    print("Here's a list of items you might want to bring:")
    for item in starter_list(vacation_type):
        print(item)
    
    print("\nNow, let's gather some specific items you'd like to bring:")
    user_items = gather_items()
    
    print("\nHere's your complete packing list:")
    packing_list = starter_list(vacation_type) + user_items
    for item in packing_list:
        print(item)
    
    print("\nEnjoy your vacation!")
    
if __name__ == "__main__":
    main()