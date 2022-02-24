# Codecademy - CS102: Data Structures and Algorithms - Final Project
# Flower recommendation/data search program based on types of flowers

# Imports flower data binary search tree, flower types and data lists, and title image
from flower_data_bst import BST
from flower_data import *
from flower_title import title

# Gets flower types the user can search for from type or data lists
def get_list_values(lst, value_to_get):
    result = []
    if value_to_get != "":
        for val in lst:
            if val[:len(value_to_get)] == value_to_get:
                result.append(val)
            elif val[0][:len(value_to_get)] == value_to_get:
                result.append(val[0])
    return result

# Sorts the flower types retrieved from the type or data lists
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]
    left_sort = merge_sort(left)
    right_sort = merge_sort(right)
    return merge(left_sort, right_sort)
 
def merge(left, right):
    result = []
    while (left and right):
        for i in range(1,len(left[0])):
            if left[0][i] < right[0][i] or right[0][:len(left[0])] == left[0]: 
                result.append(left[0])
                left.pop(0)
                break
            elif left[0][i] > right[0][i] or left[0][:len(right[0])] == right[0]:
                result.append(right[0])
                right.pop(0)
                break
    if left:
        result += left
    if right:
        result += right
    return result

# Gets user input to filter search
def user_choice(userData, q1, q2, q3):
    print("\nTo filter your results...")
    if q1 == 1:
        userChoice1 = input(f"\nWould you like to search for {userData} flowers for a specific season? (y/n): ")
        if userChoice1 == "y":
            userSeason = input("\nEnter a flower season: ").lower()
            while userSeason not in ['winter', 'spring', 'summer', 'fall']:
                userSeason = input("\nEnter winter, spring, summer, or fall: ").lower()
        else:
            userSeason = None

    if q1 == 2 or q2 == 2:
        userChoice2 = input(f"\nWould you like to search for {userData} flowers with a specific life cycle? (y/n): ")
        if userChoice2 == "y":
            userLifeCycle = input("\nEnter a flower life cycle: ").lower()
            while userLifeCycle not in ['perennial', 'annual', 'biennial']:
                userLifeCycle = input("\nEnter perennial, annual, or biennial: ").lower()
        else:
            userLifeCycle = None

    if q2 == 3 or q3 == 3:
        userChoice3 = input(f"\nWould you like to search for {userData} flowers of a specific color? (y/n): ")
        if userChoice3 == "y":
            userColor = input("\nEnter a flower color: ").lower()
            while userColor not in ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black']:
                userColor = input("\nEnter red, orange, yellow, green, blue, purple, pink, white, or black: "). lower()
        else:
            userColor = None
            
    if q3 == 4:
        userChoice4 = input(f"\nWould you like to search for pet safe {userData} flowers (y/n): ")
        if userChoice4 == "y":
            userPetSafe = "safe"
        else:
            userPetSafe = None
        
    if q1 == 2:
        return userLifeCycle, userColor, userPetSafe
    elif q2 == 3:
        return userSeason, userColor, userPetSafe
    elif q3 == 4:
        return userSeason, userLifeCycle, userPetSafe
    else:
        return userSeason, userLifeCycle, userColor

# Prints flower data from a user search for a type of flower
def flower_data_search():
    flowerdatasearch = True
    print("\nWelcome to Flowers to Grow, where you can search for flowers to add to your garden!")
    while flowerdatasearch:
        searchResult = []
        userSearch1 = input("\nEnter the beginning of a flower name, color, life cycle, or season: ").lower()

        typeResult = merge_sort(get_list_values(flower_colors, userSearch1) + get_list_values(flower_cycles, userSearch1) + get_list_values(flower_seasons, userSearch1) + get_list_values(flower_safe, userSearch1))
        dataResult = merge_sort(get_list_values(flower_data, userSearch1))
        searchResult = typeResult + dataResult

        if len(searchResult) == 0:
            print(f"\nThere were no flower types that start with '{userSearch1}'")
            continue
        if len(searchResult) == 1:
            print(f"\nThere was only one flower type that starts with '{userSearch1}': {''.join(searchResult)}")
            userSearch2 = input(f"\nWould you like to search for {''.join(searchResult)}? (y/n) ")
            if userSearch2 == "y":
                userData = ''.join(searchResult)
        else:
            print(f"\nFlower types that start with '{userSearch1}' include:  {',  '.join(searchResult)}")
            userSearch2 = input("\nWould you like to search for one of these types of flowers? (y/n) ")
            userData = None
        
        while userSearch2 == "y":
            if userData not in (typeResult or dataResult):
                userData = input("\nEnter the flower type you would like to search for: ").lower()
            if userData in dataResult:
                BST.get(userData)

            elif userData in typeResult:
                if userData in flower_seasons:
                    userLifeCycle, userColor, userPetSafe = user_choice(userData, 2, 3, 4)
                    if userPetSafe == "safe":
                        if userColor != None and userLifeCycle != None:
                            BST.get(userColor+userLifeCycle+userData+userPetSafe)
                        elif userColor != None:
                            BST.get(userColor+userData+userPetSafe)
                        elif userLifeCycle != None:
                            BST.get(userLifeCycle+userData+userPetSafe)
                        else:
                            BST.get(userData+userPetSafe)
                    else:
                        if userColor != None and userLifeCycle != None:
                            BST.get(userColor+userLifeCycle+userData)
                        elif userColor != None:
                            BST.get(userColor+userData)
                        elif userLifeCycle != None:
                            BST.get(userLifeCycle+userData)
                        else:
                            BST.get(userData)       

                elif userData in flower_cycles:
                    userSeason, userColor, userPetSafe = user_choice(userData, 1, 3, 4)
                    if userPetSafe == "safe":
                        if userColor != None and userSeason != None:
                            BST.get(userColor+userData+userSeason+userPetSafe)
                        elif userColor != None:
                            BST.get(userColor+userData+userPetSafe)
                        elif userSeason != None:
                            BST.get(userData+userSeason+userPetSafe)
                        else:
                            BST.get(userData+userPetSafe)
                    else:
                        if userColor != None and userSeason != None:
                            BST.get(userColor+userData+userSeason)
                        elif userColor != None:
                            BST.get(userColor+userData)
                        elif userSeason != None:
                            BST.get(userData+userSeason)
                        else:
                            BST.get(userData)           

                elif userData in flower_colors:
                    userSeason, userLifeCycle, userPetSafe = user_choice(userData, 1, 2, 4)
                    if userPetSafe == "safe":
                        if userLifeCycle != None and userSeason != None:
                            BST.get(userData+userLifeCycle+userSeason+userPetSafe)
                        elif userLifeCycle != None:
                            BST.get(userData+userLifeCycle+userPetSafe)
                        elif userSeason != None:
                            BST.get(userData+userSeason+userPetSafe)
                        else:
                            BST.get(userData+userPetSafe)
                    else:
                        if userLifeCycle != None and userSeason != None:
                            BST.get(userData+userLifeCycle+userSeason)
                        elif userLifeCycle != None:
                            BST.get(userData+userLifeCycle)
                        elif userSeason != None:
                            BST.get(userData+userSeason)
                        else:
                            BST.get(userData)              

                elif userData in flower_safe:
                    userSeason, userLifeCycle, userColor = user_choice(userData, 1, 2, 3)
                    userData = "safe"
                    if userColor != None and userLifeCycle != None and userSeason != None:
                        BST.get(userColor+userLifeCycle+userSeason+userData)
                    elif userColor != None and userLifeCycle != None:
                        BST.get(userColor+userLifeCycle+userData)
                    elif userColor != None and userSeason != None:
                        BST.get(userColor+userSeason+userData)
                    elif userLifeCycle != None and userSeason != None:
                        BST.get(userLifeCycle+userSeason+userData)
                    elif userColor != None:
                        BST.get(userColor+userData)
                    elif userLifeCycle != None:
                        BST.get(userLifeCycle+userData)
                    elif userSeason != None:
                        BST.get(userSeason+userData)
                    else:
                        BST.get(userData)

            else:
                print(f"\n'{userData}' is not in the list of flower types that start with '{userSearch1}'")
                continue
            
            searchAgain = input("Would you like to search again? (y/n) ")
            if searchAgain == "n":
                flowerdatasearch = False
                break 
            else:
                break

        if userSearch2 == "n":
            exitSearch = input("\nWould you like to exit? (y/n) ")
            if exitSearch == "y":
                flowerdatasearch = False

    print("\nThanks for searching at Flowers to Grow!")            

# Calls the title image and data search functions
title()
flower_data_search()                                                                      