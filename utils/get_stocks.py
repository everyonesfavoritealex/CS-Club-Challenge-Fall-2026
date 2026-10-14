from random import choice
"""
Author: Alex
Date:10-14-2026
Description: Contains get_stocks()
"""
def get_stocks(num):
    """
    Description: Contains lists of all potential stocks at different variance levelsand returns random ones to be used, if num==3: return one from each category, 
    if num==2: return one from only med and high
    """
    #low/med/high[a]==[(str) stock name, (str) stock description, (float) stock starting price ($), (float) stock variaton: percentages]
    low=[
        ["Sliced Bread","You know it, you love it. As safe as safe gets.",100.00,.01],
        ["Math", "The laws of math stay consistent", 314.15,.03],
        ["Boiled Chicken", "The most boring food possible, shouldn't change much", 50.0,.01],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    med=[
        ["Halloween Candy", "Size may vary, but candy is candy",1000.0,.07],
        ["The Law", "Interpretations may be different, but should follow the framework",3000.0,.08],
        ["Weather", "Variable, but with predictable patterns", 500,.12],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    high=[
        ["Movie Musicals", "Either the best or worst thing ever, no inbetween", 3000.00,.2],
        ["Mutation", "Who knows what'll happen", 500.0,.33],
        ["Superhero Movies", "You'll either love it or hate it", 5000.0,.2],
        ["Indie Games", "Could be game of the year, or could be trash, who knows", 100.0,.23],
        [],
        [],
        [],
        [],
        [],
        []
    ]

    if num==3:
        return[choice(low), choice(med), choice(high)]
    if num==2:
        return[choice(med), choice(high)]