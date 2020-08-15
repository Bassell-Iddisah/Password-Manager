import secrets
import sqlite3
import os


# Creating sqlite connection and cursor
connection = sqlite3.connect("Database")
conn = connection.cursor()
# connection.execute('''CREATE TABLE services(
#                     name VARCHAR UNIQUE,
#                     password VARCHAR
#                     )''')


class PasswordManager:
    enter_key = input("Enter master Key: ")
    # The dawn of creation.
    def __init__i(self):
        # Begin the application by authenticating master key
        			# The app isnt working because i tried setting the master key to env variable so correct it and it's done.	
        if self.enter_key == os.environ.get('master_key'):
            while True:
                print('''
                #############################################
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
        else:
            pass
#             counter = 1
#             while counter < 3:
#                 counter += 1
#                 PasswordManager()
#             print('''
#                 You have entered the wrong key three consecutive times.
#                 The program will now exit...
# ''')

    # Allow a user create password for a new service.
    def add_new_service(self):
        # Adding a new service
        new_service_name = input("Enter Name of new service:").upper()
        all_services = list(conn.execute("SELECT name FROM SERVICES"))
        # Testing if new_service_name already exists

        if new_service_name in all_services:

            print("The service already exists, please update or enter a new service.")

        else:
            # Auto generate password
            password_options = input(f"Auto generate new password for {new_service_name}? (y/n): ")

            if password_options == 'y':

                new_service_password = str(secrets.token_hex(16))

            else:

                new_service_password = str(input(f'Enter {new_service_name} password: '))



            #     Entering data into the database.

            conn.execute("INSERT INTO services VALUES (:name, :password)", {'name': new_service_name,
                                                                                  'password': new_service_password})
            print("")
            print(f"The new password for {new_service_name}, is '{new_service_password}'")
        return 0

    def get_service_details(self):
        get_service = str(input('Enter the name of the service you want: ').upper())
        conn.execute('SELECT * FROM services WHERE name=?', (get_service, ))
        for service, password in conn.fetchall():
            print(f'''Service: {service}
Password: {password}''')
        return 0

    # Allow a user to update his account password.
    def update_a_service(self):
        # Updating the service name
        get_service = str(input('Enter the name of the service you to update: ').upper())
        new_name = str(input('Enter new name: ').upper())
        option = str(input('Would you like to update password?: ').lower())
        if option == 'y' or option == 'yes':
            auto_generate = input("Auto generate password?: ").lower()
            if auto_generate == 'y' or auto_generate == 'yes':
                new_password = secrets.token_hex(16)
            else:
                new_password = str(input('Enter new password: '))
            conn.execute('UPDATE services SET password=? WHERE name=?', (new_password, get_service, ))
            print('Password Updated')
        else:
            pass
        conn.execute('UPDATE services SET name=? WHERE name=?', (new_name, get_service, ))
        print('Service Updated')

        conn.execute('SELECT * FROM services WHERE name=:name', {'name': new_name})
        print(conn.fetchone())
        # getting index of service and its password
        # if get_service in self.services_name_ls:
        #     get_service_pos = int(self.services_name_ls.index(get_service))
        #     # The index of the service = index of password.
        #     password_pos = get_service_pos
        #
        #     # Updating the service
        #     self.services_name_ls[get_service_pos] = str(input('Enter The new name of the service: '))
        #     password_options = input(f"Auto generate new password for {get_service}? (y/n): ").upper()
        #     if password_options == 'Y':
        #         new_service_password = str(secrets.token_hex(16))
        #     else:
        #         self.services_pass_ls[password_pos] = str(input(f'Enter {get_service} password: '))
        #
        #     # Show new service name and new password
        #     print(f'''
        #         Service: {self.services_name_ls[get_service_pos]}
        #         Password: {self.services_pass_ls[password_pos]}
        #         ''')
        return 0

    # Allow a user to delete a service and its password.
    def delete_a_service(self):
        # Get user requested service.
        get_service = str(input('Enter the name of the service to delete: ').upper())
        conn.execute('SELECT name FROM services')
        # Get all service names in a list
        lists = []
        for i in conn.fetchall():
            lists += i
        #     If service exists, delete and if not, try adding it
        if get_service in lists:
            option = str(input('Do you confirm to delete this service?: ').lower())
            if option == 'y' or option == 'yes':
                conn.execute('DELETE FROM services WHERE name=?', (get_service, ))
                print('Service successfully deleted.')
                return 0
            else:
                pass
        else:
            add_option = input(f'{get_service} does not exist, would you like to add it?:').lower()
            if add_option == 'y' or add_option == 'yes':
                self.add_new_service()
        return 0

    # List all registered services.
    def list_all_services(self):
        conn.execute('SELECT name, password FROM services')
        for service, password in conn.fetchall():
            print(f'''
                Service: {service}
                Password: {password}
''')
        return 0


    def trying_to_insertandget(self):
        new_connection = sqlite3.connect("Database_test")
        new_conn = new_connection.cursor()
        # new_conn.execute('''CREATE TABLE new_services(
        #                     name VARCHAR UNIQUE,
        #                     password VARCHAR
        #                     )''')

        # new_conn.execute("INSERT INTO new_services(name, password) VALUES('Bassell', 'it should be done')")
        # new_conn.execute("INSERT INTO new_services(name, password) VALUES('Edith', 'it is done')")
        # new_conn.execute("INSERT INTO new_services(name, password) VALUES('Sharon', 'it will be done')")
        # new_conn.execute("INSERT INTO new_services(name, password) VALUES('Hajara', 'it has done')")
        new_conn.execute("SELECT * FROM new_services")

        for i in list(new_conn.fetchall()):
            print(i)
            print("")
        return 0


PasswordManager().trying_to_insertandget()
connection.close()
