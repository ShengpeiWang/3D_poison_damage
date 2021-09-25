import numpy.random as npr

def make_drink(list1 = None, list2 = None, list3 = None, lucky_number = None):
    '''Makes a random drink with one choice from each list, with an optional lucky number.
    
    Args:
        list1, list2, list3 (list): The lists of ingredients.
        lucky_number (int): Random seed for a deterministic drink.

    Returns:
        A list of three ingredients for your drink.
    '''
    # The default ingredients lists:
    if list1 is None:
        list1 = ["double", "Rum", "Whiskey", "Wine", "Vodka", "your choice"]
    if list2 is None:
        list2 = ["Coke", "Club soda", "nothing to dilute it", "milk", "heavy cream", "Pineapple juice"]
    if list3 is None:
        list3 =["a dollop of honey", "salted rim", "a splash of lime juice", "some hot sauce", 
                "a dash of Venilla", "whatever evil the person to your right decides"]

    # Generate the mix
    if lucky_number is None:
        out = [npr.choice(i) for i in [list1, list2, list3]]
    else:
        rng = npr.default_rng(lucky_number)
        out = [rng.choice(i) for i in [list1, list2, list3]]
    
    # process list1 choice:
    if out[0] == "double":
        new_list = list1.copy()
        new_list.remove("double")
        new_item = npr.choice(new_list)
        out[0] = f"a double shot of {new_item}"
    else:
        out[0] = "a shot of " + out[0] 
    # process list2 choice:
    if out[1] != "nothing to dilute it":
        out[1] = "some " + out[1]
    
    return out

def bar_tend(*args, **kwargs):
    '''Processes the output from make_drink
    
    Args:
        *list1, *list2, *list3 (list): The lists of ingredients.
        *lucky_number (int): Random seed for a deterministic drink.
        ...
        **list1, **list2, **list3 (list): The lists of ingredients.
        **lucky_number (int): Random seed for a deterministic drink.
        ...
        
    Returns:
        A string of mixing instruction from your randomized bar tender.
    '''
    drink = make_drink(*args, **kwargs)
    message = f"You are mixing {drink[0]} with {drink[1]}, with {drink[2]}"
    return message