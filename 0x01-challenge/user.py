#!/usr/bin/python3
"""
User class
"""


class User:
    """ 
    User class represents a user with an email address.
    """

    def __init__(self):
        """ 
        Initialize User with an email address.
        """
        self.__email = None

    @property
    def email(self):
        """ 
        Getter method for email address.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """ 
        Setter method for email address.
        """
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self.__email = value


if __name__ == "__main__":
    """ 
    Main function to demonstrate usage of the User class.
    """
    u = User()
    u.email = "john@snow.com"
    print(u.email)
