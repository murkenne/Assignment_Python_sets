'''
1. Python Sets Adventure
Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. 
Write a Python program to find out:

1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.

'''


def similar_routes(our_routes, competitor_routes):
    common_routes = our_routes.intersection(competitor_routes)
    if common_routes:
        print(f"These are the routes you share with your competition: {common_routes}")
    else:
        print("There are no common routes between the two airlines.")
   


def your_route(our_routes, competitor_routes):
    unique_routes = our_routes.difference(competitor_routes)
    if unique_routes:
        print(f"These are the flight routes unique to your team {unique_routes}.")
    else:
        print("No unique flight routes.")


def others_route(our_routes, competitor_routes):
    unique_routes = competitor_routes.difference(our_routes)
    if unique_routes:
        print(f"These are the routes only the competitor flies to: {unique_routes}")
    else:
        print("All competitor routes are also covered by your airline.")
   


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


while True:
    print("\n1. View similar routes: ")
    print("2. View Your routes: ")
    print("3. View Competitor routes")
    print("4. Exit: ")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        similar_routes(our_routes, competitor_routes)
    elif choice == '2':
        your_route(our_routes, competitor_routes)
    elif choice == '3':
        others_route(our_routes, competitor_routes)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
