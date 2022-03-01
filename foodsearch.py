

def no_allergies():
    return exec_get_all("""SELECT name FROM FOOD""")

def filter_allergen(allergy):
    return exec_get_all(
        """SELECT name FROM FOOD
        WHERE %s = true
        """, (al_one,))

def filter_two_allergen(al_one, al_two):
    return exec_get_all(
        """SELECT name FROM FOOD
        WHERE %s = true AND %s = true
        """, (al_one, al_two,))

def filter_three_allergen(al_one, al_two, al_two):
    return exec_get_all(
        """SELECT name FROM FOOD
        WHERE %s = true AND %s = true AND %s = true
        """, (al_one, al_two, al_three))

def filter_except_allergen(al_one):
    return exec_get_all(
        """SELECT name FROM FOOD
        WHERE %s = false
        """, (al_one,))

def filter_except_two_allergen(al_one, al_two):
    return exec_get_all(
        """SELECT name FROM FOOD
        WHERE %s = false AND %s = false
        """, (al_one, al_two,))

def all_allergies():
    return exec_get_all("""SELECT name FROM FOOD""")