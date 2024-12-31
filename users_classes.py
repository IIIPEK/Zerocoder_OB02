
class Privileges:
    def __init__(self, can_change_name=False, can_change_email=False, can_change_password=False, can_add_user=False, can_delete_user=False):
        self.__privileges = self.privileges_to_mask(
            [can_change_name, can_change_email, can_change_password, can_add_user, can_delete_user])

    @staticmethod
    def privileges_to_mask(privileges_list: list):
        mask = 0
        for i, val in enumerate(privileges_list):
            if val:
                mask |= (1 << i)
        return mask

    def show_privileges(self):
        privileges_dict = {
            1: 'can change name',
            2: 'can change email',
            4: 'can change password',
            8: 'can add user',
            16: 'can delete user',
        }
        for key, description in privileges_dict.items():
            status = "granted" if self.__privileges & key else "not granted"
            print(f'{description}: {status}')

    def get_privileges(self):
        return self.__privileges

    def set_privileges(self, privileges):
        self.__privileges = privileges


class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__privileges = Privileges()

    def get_privileges(self):
        return self.__privileges

    def set_privileges(self, privileges):
        self.__privileges.set_privileges(privileges)

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def check_password(self,password):
        return self.__password == password

    def change_password(self, password):
        self.__password = password


    def change_name(self, name):
        self.__name = name

    def change_email(self, email):
        self.__email = email

    def get_info(self):
        print('User info:')
        print(f'Name: {self.__name}\nEmail: {self.__email}')
        print('Privileges:')
        self.__privileges.show_privileges()

class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.set_privileges(Privileges.privileges_to_mask([True, True, True, True, True]))

    def add_user(self, users:[User]):
        user_list = []
        for user in users:
            print(f'User {user.get_name()} added.')
            user_list.append(user)
        return user_list

    def delete_user(self, username, users:[User]):
        for index, user in enumerate(users):
            if user.get_name() == username:
                print(f'User {user.get_name()} deleted.')
                users.pop(index)

    def get_privileges(self):
        return self.__privileges

