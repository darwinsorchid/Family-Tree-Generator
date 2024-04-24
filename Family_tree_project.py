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
    Returns a tuple of 6 variables. 
    Each variable is a list containing the same kind of attribute from different instances.
    """
    print('Welcome to Family Tree Creator! \nPlease enter information about the members of the tree starting from the earliest ancestor.')
    node_labels = []
    fam_names = []
    fam_genders = []
    fam_birth_dates = []
    fam_alive = []
    fam_death_dates = []
    
    #print('Please enter information about the members of the tree starting from the earliest ancestor.')
    num = 0 
    child_num = 0

    add_person = input('Do you want to add a person to this tree?')

    while add_person.lower()[0] == 'y':
        num +=1 
        # A1 = Earliest ancestor
        a1 = Person()
        fam_names.append(a1.name)
        fam_genders.append(a1.gender)
        fam_birth_dates.append(a1.birth_date)
        fam_alive.append(a1.alive)
        fam_death_dates.append(a1.death_date)
        node_labels.append(f'Person{num}')
        
        
        spouse = input('Does this person have a spouse?') # Earliest ancestor's spouse = S1
        if spouse.lower()[0] == 'y':
            sp = Person()
            fam_names.append(sp.name)
            fam_genders.append(sp.gender)
            fam_birth_dates.append(sp.birth_date)
            fam_alive.append(sp.alive)
            fam_death_dates.append(sp.death_date)
            node_labels.append(f'Spouse{num}')
        else:
            break

        
        child = input('Do they have a child?') # First gen children 
        while child.lower()[0] == 'y':
            child_num +=1 
            ch = Person()
            fam_names.append(ch.name)
            fam_genders.append(ch.gender)
            fam_birth_dates.append(ch.birth_date)
            fam_alive.append(ch.alive)
            fam_death_dates.append(ch.death_date)
            node_labels.append(f'Child{child_num}')
            break 

        add_person = input('Do you want to add another person to this tree?')
    return node_labels, fam_names, fam_genders, fam_birth_dates, fam_alive, fam_death_dates # GOING TO RETURN A TUPLE OF LISTS!


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
    a, b, c, d, e, f = Take_Info()
    family_data = {'Relations': a ,'Name': b, 'Gender': c, 'Date of birth': d, 'Alive': e, 'Date of death': f}

    df= pd.DataFrame(family_data)
    return df

df = Create_df()


