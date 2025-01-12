import requests
import os

# Function to clear the screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print a separator for clarity in output
def print_separator():
    print("\n" + "-" * 50 + "\n")

# Function to display the menu
def display_menu():
    clear_screen()
    print("""
 ██ ▄█▀ ██▓ ██▓▄▄▄█████▓ ▄▄▄       ███▄    █      █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
 ██▄█▒ ▓██▒▓██▒▓  ██▒ ▓▒▒████▄     ██ ▀█   █    ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▓███▄░ ▒██▒▒██▒▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒   ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
▓██ █▄ ░██░░██░░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒   ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
▒██▒ █▄░██░░██░  ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
▒ ▒▒ ▓▒░▓  ░▓    ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒     ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒ ▒░ ▒ ░ ▒ ░    ░      ▒   ▒▒ ░░ ░░   ░ ▒░    ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
░ ░░ ░  ▒ ░ ▒ ░  ░        ░   ▒      ░   ░ ░     ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
░  ░    ░   ░                 ░  ░         ░            ░           ░    ░       ░  ░   ░     
                                                                       ░                      

    """)
    print("=======================================")
    print("           STUDENT DATA SEARCH        ")
    print("=======================================")
    print("1. Single Input Search")
    print("2. Range of Number Search")
    print("3. Custom Search (from input.txt)")
    print("4. Exit")
    print("=======================================")

# Function to search for a single roll number
def single_input_search():
    roll_number = input("Enter the roll number (e.g., 22054354): ").strip()
    try:
        url = f"https://ddos.erucix.workers.dev/?roll={roll_number}"
        response = requests.get(url)
        
        if response.status_code == 200:
            json_data = response.json()
            name = json_data.get('name', 'N/A')
            email = json_data.get('email', 'N/A')
            phone = json_data.get('phone', 'N/A')  # Get phone number
            
            # Display the result
            print_separator()
            print(f"Roll Number: {roll_number}")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Phone: {phone}")  # Display phone number
            print_separator()
            
            # Save to file
            save_to_file(roll_number, name, email, phone)
        else:
            print("Error: Could not fetch data. Please check the roll number.")
    except Exception as e:
        print(f"Error: {e}")
    
    input("Press Enter to return to the menu...")  # Wait for user to press enter
    clear_screen()  # Clear the screen

# Function to save the result to an output file in a single line with aligned columns
def save_to_file(roll_number, name, email, phone):
    # Define maximum widths for each column
    max_name_length = 20
    max_email_length = 30
    max_phone_length = 15

    # Pad the values with spaces to ensure proper alignment
    name = name.ljust(max_name_length)
    email = email.ljust(max_email_length)
    phone = phone.ljust(max_phone_length)

    with open("output.txt", "a") as file:
        file.write(f"Roll Number: {roll_number} | Name: {name} | Email: {email} | Phone: {phone}\n")


# Function to search for a range of roll numbers
def range_search():
    try:
        start_roll = int(input("Enter the start roll number: ").strip())
        end_roll = int(input("Enter the end roll number: ").strip())
        
        # Loop through the specified range
        print_separator()
        for roll_number in range(start_roll, end_roll + 1):
            url = f"https://ddos.erucix.workers.dev/?roll={roll_number}"
            response = requests.get(url)
            
            if response.status_code == 200:
                json_data = response.json()
                name = json_data.get('name', 'N/A')
                email = json_data.get('email', 'N/A')
                phone = json_data.get('phone', 'N/A')  # Get phone number
                
                # Display the result
                print(f"Roll Number: {roll_number} - Name: {name}, Email: {email}, Phone: {phone}")
                save_to_file(roll_number, name, email, phone)
            else:
                print(f"Error fetching data for Roll Number: {roll_number}")
        print_separator()
    except Exception as e:
        print(f"Error: {e}")
    
    input("Press Enter to return to the menu...")  # Wait for user to press enter
    clear_screen()  # Clear the screen

# Function to search for roll numbers from input.txt
def custom_search():
    try:
        # Read roll numbers from input.txt
        with open("input.txt", "r") as file:
            roll_numbers = file.readlines()
        
        print_separator()
        for roll_number in roll_numbers:
            roll_number = roll_number.strip()
            url = f"https://ddos.erucix.workers.dev/?roll={roll_number}"
            response = requests.get(url)
            
            if response.status_code == 200:
                json_data = response.json()
                name = json_data.get('name', 'N/A')
                email = json_data.get('email', 'N/A')
                phone = json_data.get('phone', 'N/A')  # Get phone number
                
                # Display the result
                print(f"Roll Number: {roll_number} - Name: {name}, Email: {email}, Phone: {phone}")
                save_to_file(roll_number, name, email, phone)
            else:
                print(f"Error fetching data for Roll Number: {roll_number}")
        print_separator()
    except Exception as e:
        print(f"Error: {e}")
    
    input("Press Enter to return to the menu...")  # Wait for user to press enter
    clear_screen()  # Clear the screen

# Main menu function
def main_menu():
    while True:
        display_menu()  # Show the main menu
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            single_input_search()
        elif choice == "2":
            range_search()
        elif choice == "3":
            custom_search()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to return to the menu...")  # Wait for user to press enter

# Starting the program
if __name__ == "__main__":
    print("Welcome to the Student Data Search Program!")
    input("Press Enter to begin...")  # Wait for user to press enter to start
    main_menu()  # Start the program by showing the main menu
