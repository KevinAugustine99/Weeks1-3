MARS_BONUS = 3
MERCURY_BONUS = 5
MOON_BONUS = 2
VENUS_BONUS = 4

def display_elements(planet, cerium, yttrium, scandium, space_rocks):
    """
    Display the elements gathered from a particular planet.
    :param planet: the planet name
    :param cerium: amount of cerium
    :param yttrium: amount of yttrium
    :param scandium: amount of scandium
    :param space_rocks: amount of space rocks
    """
    print(planet, 'yielded',
          cerium, 'cerium,',
          yttrium, 'yttrium',
          scandium, 'scandium and',
          space_rocks, 'space rocks')

def visit_mercury(drills):
    """
    Visit mercury and gather cerium.
    :param drills: number of drills sent
    :return: total amount of cerium gathered
    """
    if drills > 10:
        cerium = drills + 5 + MERCURY_BONUS
    else:
        cerium = drills + 2 + MERCURY_BONUS

    display_elements("Mercury", cerium, 0, 0, 0)

    return cerium

def visit_venus(drills, shovels):
    """
    Visit venus and gather yttrium.
    :param drills: number drills sent
    :param shovels: number of shovels sent
    :return: total amount of yttrium gathered
    """
    if shovels <= 6:
        yttrium = drills * 5 + shovels + VENUS_BONUS
    else:
        yttrium = (shovels + 1) // (drills // 2) + VENUS_BONUS

    display_elements("Venus", 0, yttrium, 0, 0)

    return yttrium

def visit_mars(drills, dozers):
    """
    Visit mars and gather scandium.
    :param drills: number of drills sent
    :param dozers: number of dozers sent
    :return: total amount of scandium gathered
    """
    if drills + dozers < 5:
        scandium = (drills + dozers) // 2 + MARS_BONUS
    elif drills + dozers >= 5 and drills + dozers < 20:
        scandium = drills * 3 // dozers + MARS_BONUS
    else:
        scandium = drills * 2 + 3 * dozers + MARS_BONUS

    display_elements("Mars", 0, 0, scandium, 0)

    return scandium

def visit_from_moon(drills, shovels, dozers):
    """
    Visit the moon and gather space rocks.

    :param drills: number of drills sent
    :param shovels: number of shovels sent
    :param dozers: number of dozers sent
    :return: total amount of space rocks gathered
    """

    # visit mercury.  the amount of space rocks obtained
    # from the cerium is multiplied by 2 plus the
    # global MOON_BONUS
    space_rocks = (visit_mercury(drills) * 2 + MOON_BONUS) + (visit_venus(drills,shovels) + 3 + MOON_BONUS) + ((visit_mars(drills, dozers)/2) + MOON_BONUS)

    display_elements("Moon", 0, 0, 0, space_rocks)
    return space_rocks
    # visit venus.  the amount of space rocks obtained
    # from the yttrium is 3 plus the MOON_BONUS


    # visit mars.  the amount of space rocks obtained
    # is integer divided by 2 plus the MOON_BONUS


    # display the total yield from the moon


    # return the total space rocks

def visit_from_earth():
    """
    Visit earth and see how many elements are gathered by several
    mining missions.
    """

    # first pay individual visits to each other planet
    cerium = visit_mercury(4)
    yttrium = visit_venus(2, 6)
    scandium = visit_mars(5, 3)
    space_rocks = visit_from_moon(10,12,11)
    # now visit the moon and gather the space rocks

    # display the yield from the earth
    display_elements("Earth", cerium, yttrium, scandium, space_rocks)

if __name__ == '__main__':
    visit_from_earth()