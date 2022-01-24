
from linkedlist import LinkedList
from flower_data import *
from flower_title import title
from string import capwords

def flowerlinkedlist(lst):
    ll = LinkedList()
    for el in lst:
        ll.insert_beginning(el)
    return ll

typell = flowerlinkedlist(flower_types)
datall = flowerlinkedlist(flower_data)

def get_ll_values(ll, value_to_get):
    result = []
    current_node = ll.get_head_node()
    while current_node.get_value() != None:
        if current_node.get_value()[0] == value_to_get:
            result.append(current_node.get_value())
        elif current_node.get_value()[0][0] == value_to_get:
            result.append(current_node.get_value()[0])
        current_node = current_node.get_next_node()
    return result

def get_flower_data(ll, value_to_get, userChoice1=None, userChoice2=None, userChoice3=None, userChoice4=None):
    result = []
    current_node = ll.get_head_node()
    while current_node.get_value() != None:

        if current_node.get_value()[0] == value_to_get:
            return current_node.get_value()

        elif value_to_get in current_node.get_value()[1]:
            if userChoice2 != None and userChoice3 != None and userChoice4 != None:
                if userChoice2 in current_node.get_value()[2] and userChoice3 in current_node.get_value()[3] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice2 != None and userChoice3 != None:
                if userChoice2 in current_node.get_value()[2] and userChoice3 in current_node.get_value()[3]:
                    result.append(current_node.get_value())
            elif userChoice2 != None and userChoice4 != None:
                if userChoice2 in current_node.get_value()[2] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice3 != None and userChoice4 != None:
                if userChoice3 in current_node.get_value()[3] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice2 != None:
                if userChoice2 in current_node.get_value()[2]:
                    result.append(current_node.get_value())
            elif userChoice3 != None:
                if userChoice3 in current_node.get_value()[3]:
                    result.append(current_node.get_value())
            elif userChoice4 != None:
                if len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice4 == None:
                result.append(current_node.get_value())

        elif value_to_get in current_node.get_value()[2]:
            if userChoice1 != None and userChoice3 != None and userChoice4 != None:
                if userChoice1 in current_node.get_value()[1] and userChoice3 in current_node.get_value()[3] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice1 != None and userChoice3 != None:
                if userChoice1 in current_node.get_value()[1] and userChoice3 in current_node.get_value()[3]:
                    result.append(current_node.get_value())
            elif userChoice1 != None and userChoice4 != None:
                if userChoice1 in current_node.get_value()[1] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice3 != None and userChoice4 != None:
                if userChoice3 in current_node.get_value()[3] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice1 != None:
                if userChoice1 in current_node.get_value()[1]:
                    result.append(current_node.get_value())
            elif userChoice3 != None:
                if userChoice3 in current_node.get_value()[3]:
                    result.append(current_node.get_value())
            elif userChoice4 != None:
                if len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice4 == None:
                result.append(current_node.get_value())   

        elif value_to_get in current_node.get_value()[3]:
            if userChoice1 != None and userChoice2 != None and userChoice4 != None:
                if userChoice1 in current_node.get_value()[1] and userChoice2 in current_node.get_value()[2] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice1 != None and userChoice2 != None:
                if userChoice1 in current_node.get_value()[1] and userChoice2 in current_node.get_value()[2]:
                    result.append(current_node.get_value())
            elif userChoice1 != None and userChoice4 != None:
                if userChoice1 in current_node.get_value()[1] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice2 != None and userChoice4 != None:
                if userChoice2 in current_node.get_value()[2] and len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice1 != None:
                if userChoice1 in current_node.get_value()[1]:
                    result.append(current_node.get_value())
            elif userChoice2 != None:
                if userChoice2 in current_node.get_value()[2]:
                    result.append(current_node.get_value())
            elif userChoice4 != None:
                if len(current_node.get_value()) == 5:
                    result.append(current_node.get_value())
            elif userChoice4 == None:
                result.append(current_node.get_value()) 

        elif value_to_get == "safe" and len(current_node.get_value()) == 5:
            if userChoice1 != None and userChoice2 != None and userChoice3 != None:
                if userChoice1 in current_node.get_value()[1] and userChoice2 in current_node.get_value()[2] and userChoice3 in current_node.get_value()[3]:
                    result.append(current_node.get_value())
            elif userChoice1 != None and userChoice2 != None:
                if userChoice1 in current_node.get_value()[1] and userChoice2 in current_node.get_value()[2]:
                    result.append(current_node.get_value())
            elif userChoice1 != None and userChoice3 != None:
                if userChoice1 in current_node.get_value()[1] and userChoice3 in current_node.get_value()[3]:
                    result.append(current_node.get_value())
            elif userChoice2 != None and userChoice3 != None:
                if userChoice2 in current_node.get_value()[2] and userChoice3 in current_node.get_value()[3]:
                    result.append(current_node.get_value())
            elif userChoice1 != None:
                if userChoice1 in current_node.get_value()[1]:
                    result.append(current_node.get_value())
            elif userChoice2 != None:
                if userChoice2 in current_node.get_value()[2]:
                    result.append(current_node.get_value())
            elif userChoice3 != None:
                if userChoice3 in current_node.get_value()[3]:
                    result.append(current_node.get_value())
            elif userChoice4 == None:
                result.append(current_node.get_value()) 

        current_node = current_node.get_next_node()
    return result

def flower_data_search():
    flowerdatasearch = True
    while flowerdatasearch:
        searchResult = []
        userSearch1 = input("\nEnter the beginning of a flower name, color, life cycle, or season: ").lower()

        typeResult = get_ll_values(typell, userSearch1)
        dataResult = get_ll_values(datall, userSearch1)
        typeResult += dataResult
        searchResult += typeResult
        
        if len(searchResult) == 0:
            print(f"\nThere were no flower types that start with '{userSearch1}'")
            continue
        print(f"\nFlower types that start with '{userSearch1}' include: {searchResult}")
        userSearch2 = input("\nWould you like to search for one of these? (y/n) ")
        
        while userSearch2 == "y":
            userData = input("\nEnter the flower type you would like to search for: ").lower()
            if userData in dataResult:
                flowerData = get_flower_data(datall, userData)
                if len(flowerData) == 5:
                    print(f"\n{capwords(str(flowerData[0]))}\nSeason: {flowerData[1]}\nLife cycle: {flowerData[2]}\nColors: {flowerData[3]}\nChild & pet safe\n")
                else:
                    print(f"\n{capwords(str(flowerData[0]))}\nSeason: {flowerData[1]}\nLife cycle: {flowerData[2]}\nColors: {flowerData[3]}\n")

            elif userData in typeResult:
                if userData in ['winter', 'spring', 'summer', 'fall']:
                    userChoice2 = input(f"\nWould you like to search for {userData} flowers with a specific life cycle? (y/n) ")
                    if userChoice2 == "y":
                        userLifeCycle = input("\nEnter a flower life cycle (perennial, annual, biennial): ").lower()
                    else:
                        userLifeCycle = None

                    userChoice3 = input(f"\nWould you like to search for {userData} flowers of a specific color? (y/n) ")
                    if userChoice3 == "y":
                        userColor = input("\nEnter a flower color: ").lower()
                    else:
                        userColor = None
                        
                    userChoiceSafe = input(f"\nWould you like to search for child and pet safe {userData} flowers? (y/n) ")
                    if userChoiceSafe == "y":
                        flowerData = get_flower_data(datall, userData, userChoice2=userLifeCycle, userChoice3=userColor, userChoice4=userChoiceSafe)
                        for flower in flowerData:
                            print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\nChild & pet safe\n")

                    elif userChoiceSafe == "n":
                        flowerData = get_flower_data(datall, userData, userChoice2=userLifeCycle, userChoice3=userColor)
                        for flower in flowerData:
                            if len(flower) == 5:
                                print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\nChild & pet safe\n")
                            else:
                                print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\n")          

                elif userData in ['perennial', 'annual', 'biennial']:
                    userChoice1 = input(f"\nWould you like to search for {userData} flowers for a specific season? (y/n) ")
                    if userChoice1 == "y":
                        userSeason = input("\nEnter a flower season: ").lower()
                    else:
                        userSeason = None

                    userChoice3 = input(f"\nWould you like to search for {userData} flowers of a specific color? (y/n) ")
                    if userChoice3 == "y":
                        userColor = input("\nEnter a flower color: ").lower()
                    else:
                        userColor = None

                    userChoiceSafe = input(f"\nWould you like to search for child and pet safe {userData} flowers? (y/n) ")
                    if userChoiceSafe == "y":
                        flowerData = get_flower_data(datall, userData, userChoice1=userSeason, userChoice3=userColor, userChoice4=userChoiceSafe)
                        for flower in flowerData:
                            print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\nChild & pet safe\n")

                    elif userChoiceSafe == "n":
                        flowerData = get_flower_data(datall, userData, userChoice1=userSeason, userChoice3=userColor)
                        for flower in flowerData:
                            if len(flower) == 5:
                                print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\nChild & pet safe\n")
                            else:
                                print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\n")              

                elif userData in ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black']:
                    userChoice1 = input(f"\nWould you like to search for {userData} flowers for a specific season? (y/n) ")
                    if userChoice1 == "y":
                        userSeason = input("\nEnter a flower season: ").lower()
                    else:
                        userSeason = None

                    userChoice2 = input(f"\nWould you like to search for {userData} flowers with a specific life cycle? (y/n) ")
                    if userChoice2 == "y":
                        userLifeCycle = input("\nEnter a flower life cycle (perennial, annual, biennial): ").lower()
                    else:
                        userLifeCycle = None

                    userChoiceSafe = input(f"\nWould you like to search for child and pet safe {userData} flowers? (y/n) ")
                    if userChoiceSafe == "y":
                        flowerData = get_flower_data(datall, userData, userChoice1=userSeason, userChoice2=userLifeCycle, userChoice4=userChoiceSafe)
                        for flower in flowerData:
                            print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\nChild & pet safe\n")

                    elif userChoiceSafe == "n":
                        flowerData = get_flower_data(datall, userData, userChoice1=userSeason, userChoice2=userLifeCycle)
                        for flower in flowerData:
                            if len(flower) == 5:
                                print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\nChild & pet safe\n")
                            else:
                                print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\n")                  

                elif userData == "safe":
                    userChoice1 = input(f"\nWould you like to search for {userData} flowers for a specific season? (y/n) ")
                    if userChoice1 == "y":
                        userSeason = input("\nEnter a flower season: ").lower()
                    else: 
                        userSeason = None

                    userChoice2 = input(f"\nWould you like to search for {userData} flowers with a specific life cycle? (y/n) ")
                    if userChoice2 == "y":
                        userLifeCycle = input("\nEnter a flower life cycle (perennial, annual, biennial): ").lower()
                    else:
                        userLifeCycle = None

                    userChoice3 = input(f"\nWould you like to search for {userData} flowers of a specific color? (y/n) ")
                    if userChoice3 == "y":
                        userColor = input("\nEnter a flower color: ").lower()
                    else:
                        userColor = None

                    flowerData = get_flower_data(datall, userData, userChoice1=userSeason, userChoice2=userLifeCycle, userChoice3=userColor)
                    for flower in flowerData:
                        print(f"\n{capwords(str(flower[0]))}\nSeason: {flower[1]}\nLife cycle: {flower[2]}\nColors: {flower[3]}\nChild & pet safe\n")  
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

title()
flower_data_search()                                                                        