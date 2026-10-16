from random import choice
"""
Authors: Alex and Nicole
Date:10-16-2026
Description: Contains all breaking_news events and a function to return one to be used for the day
"""
#TODO: create events for breaking_news, each stock should have two positive and two negative, and these should cause drastic changes to the stock's trading value
#Format: [(str) event description, (tuple) ((float) amount to change negative growth by, (float) amount to change positive growth by)]
breaking_news={
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
def get_breaking_news(stocks):
    """
    Description: Determines breaking news event for day, removes stock used from stocks so that the same stock won't be selected for an event twice in a day,
    and removes event used so it won't be seen again in the playthrough

    Parameters: (list) stocks: a list of all stocks the player is trading

    Returns: (list) event: a list containing all of the information of one event
    """
    stock=choice(stocks)
    event=choice(breaking_news[stock[0]])

    #the event needs to be deleted this way because remove() wont function on a dictionary value
    stockeventscopy=breaking_news[stock[0]][:]
    stockeventscopy.remove(event)
    breaking_news[stock[0]]=stockeventscopy

    return event