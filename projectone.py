import random



# from secrets import choice

# def run_day_trip_generator():
# def list_of_options():
#     destination_one  = "Destination:"
#     restaurant_one = "Restaurant:"
#     entertainment_one = "Entertainment:"
#     transportation_one = "Transportation:"
#     return()


# list_of_options = ["Destination:", "Restaurant:", "Entertainment:", "Transportation:"]

# for word in list_of_options:
#     print(word)


# def print_full_trip(list_of_options, list_generator):
#     full_trip = list_of_options + list_generator
#     return full_trip


destination_list = ["Nashville", "Indianapolis", "New York City", "Philadelphia"]
restaurant_list = ["El Rodeo", "Pacos Tacos", "La Margarita", "Don Tequilas"]
entertainment_list = ["Musical", "Movie Theater", "Music Festival", "Football Game"]
transportation_list = ["Uber", "Lime Scooter", "Tandem Bike", "Walking"]

def destination_str():
    select_destination = random.randint(0,len(destination_list)-1)
    return destination_list

def restaurant_str():
    select_restaurant = random.randint(0,len(restaurant_list)-1)
    return restaurant_list

def entertainment_str():
    select_entertainment = random.randint(0,len(entertainment_list)-1)
    return entertainment_list

def transportation_str():
    select_transportation = random.randint(0,len(transportation_list)-1)
    return transportation_list

def list_generator():
    select_destination = random.randint(0,len(destination_list)-1)
    select_restaurant = random.randint(0,len(restaurant_list)-1)
    select_entertainment = random.randint(0,len(entertainment_list)-1)
    select_transportation = random.randint(0,len(transportation_list)-1)
    return destination_list[select_destination], restaurant_list[select_restaurant], entertainment_list[select_entertainment], transportation_list[select_transportation]


def print_full_trip(destination, restaurant, entertainment,transportation):
    print("Destination:", destination)
    print("Restaurant:", restaurant)
    print("Entertainment:", entertainment)
    print("Transportation:", transportation)
    return 0



destination, restaurant, entertainment, transportation = list_generator()
print_full_trip(destination, restaurant, entertainment, transportation)

# user_input = "Y"

# while True:

#     user_input = input('Are you satisfied with your trip? Y or N ')

#     if user_input == 'Y':
#         print("")
#         print("Destination:", destination)
#         print("Restaurant:", restaurant)
#         print("Entertainment:", entertainment)
#         print("Transportation:", transportation)
#         print("")
#         print("Have a nice trip!")
#         break
#     else:
#         break

while True:

    user_input = input('Are you satisfied with your trip? Y or N ')
    
    if user_input == 'Y':
        print("Final Trip:")
        print("Destination:", destination)
        print("Restaurant:", restaurant)
        print("Entertainment:", entertainment)
        print("Transportation:", transportation)
        print("Have a nice trip!")
        break
    else:
        user_input = input("Which category would you like to change? Destination, Restaurant, Entertainment, Transportation ")
        break


    

while True: 

    # user_input = input("Which category would you like to change? Destination, Restaurant, Entertainment, Transportation ")

    
    if user_input == 'Destination':
        print("")
        print("Destination:", random.choice(destination_list))
        print("Restaurant:", restaurant)
        print("Entertainment:", entertainment)
        print("Transportation:", transportation)
        print("")
        user_input = input("Are you satisfied with your trip? Y or N ")
        if user_input == "Y":
            continue
    elif user_input == 'Restaurant':
        print("Destination:", destination)
        print("Restaurant:", random.choice(restaurant_list))
        print("Entertainment:", entertainment)
        print("Transportation:", transportation)
        user_input = input("Are you satsified with your trip? Y or N ")
        if user_input == "Y":
            continue
    elif user_input == 'Entertainment':
        print("Destination:", destination)
        print("Restaurant:", restaurant)
        print("Entertainment:", random.choice(entertainment_list))
        print("Transportation:", transportation)
        user_input = input("Are you satisfied with your trip? Y or N ")
        if user_input == "Y":
            continue
        else:
            continue
    elif user_input == 'Transportation':
        print("Destination:", destination)
        print("Restaurant:", restaurant)
        print("Entertainment:", entertainment)
        print("Transportation:", random.choice(transportation_list))
        user_input = input("Are you satisfied with your trip? Y or N ")
        if user_input == "Y":
            continue
    else:
        print("Final Trip:")
        print("Destination:", destination)
        print("Restaurant:", restaurant)
        print("Entertainment:", entertainment)
        print("Transportation:", transportation)
        print("Have a nice trip!")
        break

# def final_trip():
#     final = print_full_trip 
#     final = user_input
#     print(final)

# final_trip()

# def final_trip(current_trip):
#     current_trip = (("Destination:", destination)
#     ("Restaurant:", restaurant)
#     ("Entertainment:", entertainment)
#     ("Transportation:", transportation))
#     return current_trip

# final_trip = "current_trip"


   







    




