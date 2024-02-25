def main():
    # Prompt the user for input
    name = input("Please, enter your name: ")
    age = input("Please, enter your age: ")
    location = input("Please, enter your location: ")

    # Store user data in a dictionary
    user_data = {
        "name": name,
        "age": age,
        "location": location
    }

    # Print personalized message
    print_personalized_message(user_data)


def print_personalized_message(user_data):
    # Extract user data from the dictionary
    name = user_data["name"]           #Retrieve user's name from the dictionary
    age = user_data["age"]
    location = user_data["location"]

    # Print personalized message
    print(f"Hello {name}, you are {age} years old and live in {location}.") #embeded variables


if __name__ == "__main__":
    main()
