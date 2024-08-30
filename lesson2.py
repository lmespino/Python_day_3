# create a print function that prints
# out the string "Hello, World!"
# print("Hello World!")
# ask the user for the day of the week
# day_of_week = input("What day of the week is it? ")
# print("Today is"+ day_of_week)
# concatenations is when you add two strings together
# using a plus sign (+)
# movies_this_week = input("What movies are you watching this week? ")
# print("I am watching "+ movies_this_week + " this week")
# mood = input("How are you feeling today? ")
# print("I am feeling"+ mood + "today")

# data types for variables in python
# strings - text
#name = "John" # This is a string data type
# Whenever it is wrapped in quotes it is a string
#year = "2024"
# integers - whole numbers
#year = 2024 # this is an integer data type
# does not need to be wrapped in quotes
#yearFourFromNow = 2028
#subtract = yearFourFromNow - year
#print(subtract)
# floats - decimal numbers
#priceBigMac = 3.99 # this is a float data type
#priceDoublePounder = 4.99
#totalPrice = priceBigMac + priceDoublePounder
#print(totalPrice)
# booleans - True or False
#isRaining = False # this is a boolean data type
#print(isRaining)
# lists - a collection of items 
#groceries = ["apples", "bananas", "carrots"]
#print(groceries)

#challenge #1
#you and your family are going to see a movie and
# dinner. You need a list of movies to choose from
list_of_movies = ["Despicable Me 4", "Inside Out 2", "Deadpool & Wolverine", "Aliens: Romulus", "The Crow"]
# the place of the restaurant
restaurantAddress = "1234 Street"
# the time of the movie
movieTime = "7:00 PM"
# the time of the dinner
dinnerTime = "4:00 PM"
# the name of the movie
movieName = "Inside Out 2" 
# the price of the movie
moviePrice = "15:50"
# the price of the dinner
dinnerPrice = "35.25"
# check to see if the movie is playing in the evening
inEvening = True
# how many people are going
peopleGoing = input("How many people are going? ")
# print the entire output 
print("We are going to see"+ movieName +
      "at"+ movieTime +
       "and then eat dinner at"+ 
        restaurantAddress + "at"+ 
         dinnerTime)
