from random import choice
"""
Authors: Alex and Nicole
Date:10-16-2026
Description: Contains all smaller_stories events and a function to return two to be used for the day
"""
#TODO: create events for smaller_stories, each stock should have two positive and two negative, and these should cause drastic changes to the stock's trading value
#Format: [(str) event description, (tuple) ((float) amount to change negative growth by, (float) amount to change positive growth by)]
smaller_stories={
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
def get_smaller_stories(stocks):
    """
    Description: Determines smaller_stories events for day, removes stocks used from stocks so that the same stock won't be selected for an event twice in a day,
    and removes event used so it won't be seen again in the playthrough

    Parameters: (list) stocks: a list of all stocks the player is trading except for the one used for the headline today

    Returns: (list) events[0]: a list containing all of the information of one event, (list) events[1]: a list containing all of the information of another event, 
    (list) stocks: a list containing all stocks the user is trading except for the one used in this function
    """
    events=[]
    removed=[]
    for stock in stocks:
        if not smaller_stories[stock[0]]:
            removed.append(stocks.pop(stocks.index(stock)))
    for a in range (2):
        stock=choice(stocks)
        stocks.remove(stock)
        events.append(choice(smaller_stories[stock[0]]))

        #the event needs to be deleted this way because remove() wont function on a dictionary value
        stockeventscopy=smaller_stories[stock[0]][:]
        stockeventscopy.remove(events[a])
        smaller_stories[stock[0]]=stockeventscopy

    #this needs to be done so events of other types for the file can be accessed this day
    stocks.extend(removed)

    return events[0],events[1], stocks