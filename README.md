#The three-S-devs 

A Python console application for managing user registrations, email validation, and user search operations. It features an interactive menu system with input validation and a mock database.

Features: 
 - Add users with validated names, emails, and phone numbers.
 - View all registered users in a formatted table.
 - Find users by email (supports partial matches).
 - Ensures correct formatting for emails, names, and phone numbers using regular expressions.


Installation: 
 clone the github repository: https://github.com/sgc-11/Three-S-devs.git
 Install dependencies: pip install -r dependencies.txt

Usage: 
 Run the application: python main.py 

Menu Options:
 - Register a new user: Enter name, email, and phone number (validated via regex).
 - List all users: Displays all registered users in a table.
 - Search by email: Finds users with matching/partial email addresses.
 - Exit: Closes the application.

Dependencies:
 - typer (for CLI interactions)
 - pyfiglet (for ASCII art headers)
 - rich (for formatted tables)
 - cowsaw (for fun exit messages)

Code structure:
 - main.py: Entry point
 - menus.py: Handles the main menu logic and user flows
 - base_datos.py: Mock database with user storage and retrieval methods
 - checker.py: Regular expressions based validation for emails, names and phone numbers
 - cleanTerminal.py: Utility for clearing the terminal
 - user.py: To stablish the attributes required for each user

Validation rules:
 - Emails: Must end with @utv.edu.co or @estudiante.utv.edu.co
 - Names: Only letters and spaces allowed
 - Phone Numbers: Supports international format 

Members:
 - Santiago Yepes
 - Simon Gomez 
 - Sofia Aristizabal


