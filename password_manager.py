import secrets
import sqlite3
import os, os.path as path

connection = sqlite3.connect(":memory:")
conn = connection.cursor()
connection.execute('''CREATE TABLE services(
                    name varchar,
                    password varchar
                    )''')

islamic
enter_key = input("Enter master Key: ")



class PasswordManager:

    services_name_ls, services_pass_ls = [], []

    # The dawn of creation.
    def __init__(self):
        # Begin the application by authenticating master key
        if enter_key == 'islamic':
            while True:
                print('''
                    Press 'Q' to quit
                    Press 'A' to add a service
                    Press 'D' to delete a service
                    Press 'G' to get service details  
                    Press 'U' to update a service's info
                    Press 'L' to list all registered services''')
                option = str(input('>: '))

                if option == 'Q' or option == 'q':
                    exit()

                elif option == 'A' or option == 'a':
                    self.add_new_service()

                elif option == 'D' or option == 'd':
                    self.delete_a_service()

                elif option == 'G' or option == 'g':
                    self.get_service_details()

                elif option == 'L' or option == 'l':
                    self.list_all_services()

                elif option == 'U' or option == 'u':
                    self.update_a_service()
                else:
                    print("Please choose and option from the list above to continue.")

    # Allow a user create password for a new service.
    def add_new_service(self):
        # Adding a new service
        new_service_name = input("Enter Name of new service:").upper()

        # Auto generate password
        password_options = input(f"Auto generate new password for {new_service_name}? (y/n): ")
        if password_options == 'y':
            new_service_password = str(secrets.token_hex(16))
        else:
            new_service_password = str(input(f'Enter {new_service_name} password: '))
        self.services_name_ls.append(new_service_name)
        self.services_pass_ls.append(new_service_password)
        # Saving new service to Database
        connection.execute("INSERT INTO services VALUES (:name, :password)",
                           {'name': new_service_name, 'password': new_service_password})
        print('')
        print(f"The new password for {new_service_name}, is '{new_service_password}'")
        print("##############################################################")
        return 0

    def get_service_details(self):
        if len(self.services_name_ls) == 0:
            print('There is nothing to get, please input at least one service.')
        else:
            get_service = str(input('Enter the name of the service you want: ').upper())

            if get_service in self.services_name_ls:
                get_service_pos = int(self.services_name_ls.index(get_service))
                password_pos = self.services_pass_ls[get_service_pos]

                print(f'''
                    Service: {get_service}
                    Password: {password_pos}
                    ''')
            else:
                print('Service does not exist')

            print("##############################################################")
        return 0

    # Allow a user to update his account password.
    def update_a_service(self):
        if len(self.services_name_ls) == 0:
            print('There is nothing to get, please input at least one service.')
        else:
            get_service = str(input('Enter the name of the service you want: ').upper())
            # getting index of service and its password
            if get_service in self.services_name_ls:
                get_service_pos = int(self.services_name_ls.index(get_service))
                # The index of the service = index of password.
                password_pos = get_service_pos

                # Updating the service
                self.services_name_ls[get_service_pos] = str(input('Enter The new name of the service: '))
                password_options = input(f"Auto generate new password for {get_service}? (y/n): ").upper()
                if password_options == 'Y':
                    new_service_password = str(secrets.token_hex(16))
                else:
                    self.services_pass_ls[password_pos] = str(input(f'Enter {get_service} password: '))

                # Show new service name and new password
                print(f'''
                    Service: {self.services_name_ls[get_service_pos]}
                    Password: {self.services_pass_ls[password_pos]}
                    ''')

            else:
                print('Service does not exist')
            print("##############################################################")

        return 0

    # Allow a user to delete a service and its password.
    def delete_a_service(self):
        if len(self.services_name_ls) == 0:
            print('There is nothing to delete, please input at least one service.')
        else:
            # Get user requested service.
            get_service = str(input('Enter the name of the service to delete: ').upper())

            if get_service in self.services_name_ls:
                # Get service index and use it to get password of the service.
                password_pos = self.services_pass_ls[int(self.services_name_ls.index(get_service))]
                self.services_name_ls.remove(get_service)
                self.services_pass_ls.remove(password_pos)
                print(f'{get_service} has successfully been deleted.')
            else:
                print('Service does not exist')
            print("##############################################################")
        return 0

    # List all registered services.
    def list_all_services(self):
        if len(self.services_name_ls) == 0:
            print('There is nothing to list, please input at least one service.')
        else:
            for service, password in zip(self.services_name_ls, self.services_pass_ls):
                print(f'''
                    Service: {service}
                    Password: {password}
                    ''')
        print("##############################################################")
        return 0


PasswordManager()
