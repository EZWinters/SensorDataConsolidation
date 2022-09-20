class Menu:
    def display_main_menu(self):
        print('******Welcome to sensor data consolidation*******')
        print('1. IMU Data')
        print('2. OMoCap data')
        print('3. Exit')
        try:
            user_choice = int(input('Enter...'))
        except ValueError as ve:
            print("Invalid Choice....Please try again ! ! !")
            self.display_main_menu()
        except Exception as e:
            print("Something went wrong....Please try again ! ! !")
            self.display_main_menu()
        if user_choice in [1, 2, 3]:
            return user_choice
        else:
            print(print("Invalid Choice....Please try again ! ! !"))
            self.display_main_menu()

    def display_IMU_menu(self):
        print('******Choose from below options*******')
        print('1. S07')
        print('2. S08')
        print('3. S09')
        print('4. S10')
        try:
            choice = int(input('Enter...'))
        except ValueError as ve:
            print("Invalid Choice....Please try again ! ! !")
            self.display_IMU_menu()
        except Exception as e:
            print("Something went wrong....Please try again ! ! !")
            self.display_IMU_menu()
        if choice in [1, 2, 3, 4]:
            return choice
        else:
            print(print("Invalid Choice....Please try again ! ! !"))
            self.display_IMU_menu()

    def display_OMoCap_menu(self):
        print('******Choose from below options*******')
        print('1. S11')
        print('2. S12')
        print('3. S13')
        print('4. S14')
        try:
            choice = int(input('Enter...'))
        except ValueError as ve:
            print("Invalid Choice....Please try again ! ! !")
            self.display_OMoCap_menu()
        except Exception as e:
            print("Something went wrong....Please try again ! ! !")
            self.display_OMoCap_menu()
        if choice in [1, 2, 3, 4]:
            return choice
        else:
            print(print("Invalid Choice....Please try again ! ! !"))
            self.display_OMoCap_menu()
