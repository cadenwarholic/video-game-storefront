class Game:
    """
    This class represents the game itself and the characteristic that correspond
    """
    def __init__(self, title, price, stock):
        self.title = title
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Title: {self.title}\nPrice: {self.price}\nStock: {self.stock}"

class Inventory:
    """
    This class represents the inventory itself and different methods that follow
    """
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game) # Append the game to the games list

    def list_games(self):
        for game in self.games: # For loop the printing of the different games
            print(game)

    
