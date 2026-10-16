from random import choice
"""
Authors: Alex and Nicole
Date:10-15-2026
Description: Contains all headline events and a function to return one to be used for the day
"""
#TODO: create events for headlines, each stock should have two positive and two negative, and these should cause drastic changes to the stock's trading value
#Format: [(str) event description, (tuple) ((float) amount to change negative growth by, (float) amount to change positive growth by)]
headlines={
    "Sliced Bread":[
        [],
        [],
        [],
        []
    ],
    "Math":[
        [],
        [],
        [],
        []
    ],
    "Boiled Chicken":[
        [],
        [],
        [],
        []
    ],
    "Cheerios":[
        [],
        [],
        [],
        []
    ],
    "Library":[
        [],
        [],
        [],
        []
    ],
    "World Clock":[
        [],
        [],
        [],
        []
    ],
    "Coffee":[
        [],
        [],
        [],
        []
    ],
    "Forks":[
        [],
        [],
        [],
        []
    ],
    "Pencils":[
        [],
        [],
        [],
        []
    ],
    "The Circle of Life":[
        [],
        [],
        [],
        []
    ],
    "Popular Music":[
        [],
        [],
        [],
        []
    ],
    "The Law":[
        
        [],
        [],
        [],
        []
    ],
    "Weather":[
        [],
        [],
        [],
        []
    ],
    "Apples":[
        [],
        [],
        [],
        []
    ],
    "Science":[
        [],
        [],
        [],
        []
    ],
    "Social Media Platforms":[
        [],
        [],
        [],
        []
    ],
    "Language":[
        [],
        [],
        [],
        []
    ],
    "Evolution":[
        [],
        [],
        [],
        []
    ],
    "Technology":[
        [],
        [],
        [],
        []
    ],
    "Pizza":[
        [],
        [],
        [],
        []
    ],
    "Movie Musicals":[
        [],
        [],
        [],
        []
    ],
    "Mutations":[
        [],
        [],
        [],
        []
    ],
    "Superhero Movies":[
        [],
        [],
        [],
        []
    ],
    "Indie Games":[
        [],
        [],
        [],
        []
    ],
    "Halloween Candy":[
        [],
        [],
        [],
        []
    ],
    "Blind Box":[
        [],
        [],
        [],
        []
    ],
    "Trends":[
        [],
        [],
        [],
        []
    ],
    "Art":[
        [],
        [],
        [],
        []
    ],
    "Genetics":[
        [],
        [],
        [],
        []
    ],
    "Taste Buds":[
        [],
        [],
        [],
        []
    ]
}
def get_headline(stocks):
    """
    Description: Determines headline event for day, removes stock used from stocks so that the same stock won't be selected for an event twice in a day,
    and removes event used so it won't be seen again in the playthrough

    Parameters: (list) stocks: a list of all stocks the player is trading

    Returns: (list) event: a list containing all of the information of one event, (list) stocks: a list containing all stocks the user is trading except for the one
    used in this function
    """
    removed=[]
    for stock in stocks:
        if not headlines[stock[0]]:
            removed.append(stocks.pop(stocks.index(stock)))
    stock=choice(stocks)
    stocks.remove(stock)
    event=choice(headlines[stock[0]])

    #the event needs to be deleted this way because remove() wont function on a dictionary value
    stockeventscopy=headlines[stock[0]][:]
    stockeventscopy.remove(event)
    headlines[stock[0]]=stockeventscopy

    stocks.extend(removed)

    return event, stocks