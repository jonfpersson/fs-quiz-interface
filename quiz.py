import requests
import json
import random

def print_correct_answer(response):
    # Load the JSON response
    response_data = json.loads(response)

    # Get the correct answer
    correct_answer = None
    for answer in response_data["answers"]:
        if answer["is_correct"]:
            correct_answer = answer["answer_text"]
            break

    if correct_answer:
        print(f"Correct Answer: {correct_answer}")
    else:
        print("No correct answer found.")



def send_request(extension):
    # Define the URL with the API key
    url = f"https://api.fs-quiz.eu/1/s29RaBPy/{extension}"
    print(url)

    try:
        # Send the GET request
        headers = {'User-Agent': 'YourApp/1.0'}
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # If successful, print the response content
            return response.text
        else:
            print(f"Error: Status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def display_menu():
    print("")
    print("Welcome to the Start Menu")
    print("1. Get quiz answer")
    print("2. Get random question")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        
        id = input("Enter question id ")
        print_correct_answer(send_request("question/" + id))
        
    elif choice == '2':
        id = str(random.randint(1, 600))

        response = send_request("question/" + id + "/info")
        parsed = json.loads(response)
        print(parsed["text"])

    elif choice == '3':
        print("You selected Option 3")
        # Add code for Option 3 here
    elif choice == '4':
        print("You selected Option 4")
        # Add code for Option 4 here
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")

# Continue with the rest of your script after the menu
