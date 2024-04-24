"""
Project information.

Create a class called Person which will have a name, when they were born and when (and if) they died.
Allow the user to create these Person classes and put them into a family tree structure. 
Print out the tree to the screen.
"""

import pandas as pd



class Person():
    """
    The Person class acts as a template for the user to create instances,
    which are then passed into a dataframe and plotted into a tree.
    Every instance acts as a single row in the dataframe. 
    """
    def __init__(self):
        self.name = input('Name: ')
        self.gender = input('Gender: ')
        self.birth_date = int(input('Year of birth: '))   # passed in as integer
        self.alive = input('Have they passed away? ')
        if self.alive.lower()[0] == 'y':
            self.death_date = input('Year of death: ')
        else:
            self.death_date = ' '
        
        

def Take_Info():
    """
    Function that greets user & creates as many instances of the Person class as the user wants.
    Returns a tuple of 5 variables. 
    Each variable is a list containing the same kind of attribute from different instances.
    """
    print('Welcome to Family Tree Creator!')
    fam_members = int(input('How many people do you want to be in this family tree? Enter a number: '))
    fam_names = []
    fam_genders = []
    fam_birth_dates = []
    fam_alive = []
    fam_death_dates = []

    # 1. The user enters their information -- USE THEM AS AN INITIAL NODE TO DETERMINE RELATIONS AND PATHS FOR TREE.
    print('Please enter your information: ')
    user_info = Person()
    fam_names.append(user_info.name)
    fam_genders.append(user_info.gender)
    fam_birth_dates.append(user_info.birth_date)
    fam_alive.append(user_info.alive)
    fam_death_dates.append(user_info.death_date)

    # 2. The user enters their family's information 
    for num in range(fam_members-1):
        print(f'Please provide the following information for the next person.')
        person = Person()
        fam_names.append(person.name)
        fam_genders.append(person.gender)
        fam_birth_dates.append(person.birth_date)
        fam_alive.append(person.alive)
        fam_death_dates.append(person.death_date)

    return fam_names, fam_genders, fam_birth_dates, fam_alive, fam_death_dates # GOING TO RETURN A TUPLE OF LISTS!


def Create_df():
    """
    1. Tuple unpacking for the variables returned by the Take_Info function.
       a = fam_names
       b = fam_genders
       c = fam_birth_dates
       d = fam_alive
       e = fam_death_dates
    2. Assign each variable (list) as a value to a key in a dictionary.
    3. Create dataframe from created dictionary.
    Returns a dataframe object.
    """
    a, b, c, d, e = Take_Info()
    family_data = {'Name': a, 'Gender': b, 'Date of birth': c, 'Alive': d, 'Date of death': e}

    df= pd.DataFrame(family_data)
    return df

df = Create_df()
print(df)
