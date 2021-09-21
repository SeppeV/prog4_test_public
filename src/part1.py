def volume_kubus(x):
    """Return the volume of a cube

    Raise a RuntimeError exception with message "negatieve lengte" if x < 0.
    """

    if x < 0:
        print("negatieve lengte")
        raise RuntimeError

    else:
        volume = x**3
        return volume


def minutes_in_day(x):

    """Return the number of minutes in x days

    Raise a custom NegativeDuration exception if x < 0.
    """

    if x < 0:
        print("NegativeDuration")

    else:
        days = x * 60 * 24
        return days


def minutes_in_week(x):

    """Return the number of minutes in x weeks"""

    weeks = x * 60 * 24 * 7

    return weeks


def list_of_squares(n):

    """Return a list of the first n squares

    >>> list_of_squares(3)
    [0, 1, 4]
    """

    for i in n:
        range(n)
        result = (i ** 2)
    return result



def product_of_list(l):

    """Return the product of all numbers in the list

    >>> product_of_list([2,3,4])
    24
    """

    for i in l:
        result = i * l
        return result



def price_search(articles, name):

    """Return the price of the article in list articles

    >>> articles = [
        ["Doom", 25],
        ["Among Us", 5],
    ]
    >>> price_search("Doom")
    25
    """
