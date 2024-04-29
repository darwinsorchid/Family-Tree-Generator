"""
Project information.

Create a class called Person which will have a name, when they were born and when (and if) they died.
Allow the user to create these Person classes and put them into a family tree structure. 
Print out the tree to the screen.
"""

import pandas as pd 
import graphviz


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
        alive = input('Have they passed away? ')
        if alive.lower()[0] == 'y':
            self.death_date = input('Year of death: ')
        else:
            self.death_date = '-'
        self.children = ''

        spouse = input('Do they have a spouse? ')
        if spouse.lower()[0] == 'y':
            self.spouse = input("Please enter spouse's name: ")
            children = int(input('How many children do they have? Please enter a number. '))
            if children != 0:
                for i in range(children):
                    self.children += input(f"Please enter child{i+1} name: ") + ' ' # Each person's children = space separated string
            else:
                self.children = '-'
        else:
            self.spouse = '-'
            self.children = '-'
        
        

def Take_Info():
    """
    Function that greets user & creates as many instances of the Person class as the user wants.
    Returns a tuple of 6 variables. 
    Each variable is a list containing the same kind of attribute from different instances.
    """
    print('Welcome to Family Tree Creator! \nPlease enter information about the members of the tree starting from the earliest ancestor.')
    print('NOTE: Every family member that will be represented in the tree must be submitted as a different person.')
    names = []
    genders = []
    birth_dates = []
    death_dates = []
    spouses = []
    children = [] # list of space separated strings of each person's children
    

    choice = int(input('How many people in total do you want this tree to have? Please enter a number. '))
    for i in range(choice):
        print(f'Person number {i+1}')
        person = Person()
        names.append(person.name)
        genders.append(person.gender)
        birth_dates.append(person.birth_date)
        death_dates.append(person.death_date)
        spouses.append(person.spouse)
        children.append(person.children)
    
    return  names, genders, birth_dates, death_dates, spouses, children # GOING TO RETURN A TUPLE OF LISTS!


def Create_df():
    """
    1. Tuple unpacking for the variables returned by the Take_Info function.
    a = names
    b = genders
    c = birth_dates
    d = death_dates
    e = spouses
    f = children

    2. Assign each variable (list) as a value to a key in a dictionary.
    3. Create dataframe from created dictionary.
    Returns a dataframe object.
    """
    a, b, c, d, e, f= Take_Info()
    family_data = {'Name': a, 'Gender': b, 'Birth': c, 'Death': d,'Spouse': e, 'Children': f}

    df= pd.DataFrame(family_data)
    return df


def Create_Tree(df):
    """
    Function that takes in dataframe created by Create_df function as argument.
    Creates nodes and edges checking for double edges.
    Returns rendered tree graph.
    """

    print(df)

    tree_graph = graphviz.Digraph(format = 'pdf')
    children = set() # To eliminate double children edges 
    spouses= []      # To eliminate double spouse edges

    for i in range(len(df['Name'])):
        # Create nodes
        tree_graph.node(str(df['Name'][i]), 
                        shape = 'box' if df['Gender'][i].lower()[0] == 'm' else 'ellipse', 
                        style = 'filled' if df['Death'][i] != '-' else '', color = 'grey')
        
        if df['Spouse'][i] != '-' and (str(df['Spouse'][i]), str(df['Name'][i])) not in spouses:
            tree_graph.edge(str(df['Name'][i]), str(df['Spouse'][i]),
                            arrowhead = 'none', color='black:invis:black', constraint = 'false')
            spouses.append((str(df['Name'][i]), str(df['Spouse'][i])))

        if df['Children'][i] != '-' and df['Children'][i] not in children:
            children_list = df['Children'][i].split()
            for child in children_list:
                tree_graph.edge(str(df['Name'][i]), child, arrowhead = 'none')
                children.add(df['Children'][i])

    tree_graph.source
    tree_graph.render('C:/Users/alexa/OneDrive/Έγγραφα/Family Tree Creator/Family_Tree_Graph', view = True)



df = Create_df()
Create_Tree(df)


