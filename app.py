from flask import Flask, request
from models import Deck, Game
import random, string, time, math

app = Flask(__name__)

letters = string.digits
game_id = ''.join(random.choice(letters) for i in range(10))
game = Game(game_id)
deck = Deck()
n = 4

def checkWinningCondition(cardList: list):
    length = len(cardList)
    if length>=n:
        return cardList[length-n].getCardValue() < cardList[length-n+1].getCardValue() < cardList[length-n+2].getCardValue() \
           < cardList[length-n+3].getCardValue()
    else:
        return False

def isGameCompleted():
    isGameCompleted = False
    if len(game.player1cards)>=n and checkWinningCondition(game.player1cards):
        game.won = game.player1
        isGameCompleted = True
    elif len(game.player2cards)>=n and checkWinningCondition(game.player2cards):
        game.won = game.player2
        isGameCompleted = True
    elif deck.size() == 0:
        game.won = "Draw"
        isGameCompleted = True
    return isGameCompleted

@app.route('/startGame', methods=['POST'])
def start_Game():
    input = request.json
    players = input['players']

    game.player1 = players[0]['name']
    game.player2 = players[1]['name']

    print("All the players have joined \n")
    print("Randomly choosing player for the first turn \n")

    currentPlayerTurn = random.choice([game.player1, game.player2])

    game.turn = currentPlayerTurn
    game.lastPlayedTime = time.time()

    return "All the Players have joined. " + currentPlayerTurn + " should start the game"


@app.route('/whoseTurn', methods=['GET'])
def whoseTurn():
    print(math.floor((time.time() - game.lastPlayedTime)/30)%2)
    if math.floor((time.time() - game.lastPlayedTime)/30)%2 == 1:
        print("Timeout has occurred for player:"+ game.turn)
        if game.player1 == game.turn:
            return game.player2
        else:
            return game.player1
    return game.turn


@app.route('/pickCard', methods=['POST'])
def pickCard():
    input = request.json
    if not isGameCompleted():
        deck.shuffle()
        if input is not None and ('color' in input or 'suit' in input):
            if 'color' in input:
                color = input['color']
                card = deck.pickColor(color)
            elif 'suit' in input:
                suit = input['suit']
                card = deck.pickSuite(suit)
        else:
            card = deck.pick()
        if card:
            game.turn = whoseTurn()
            game.lastPlayedTime = time.time()
            if game.player1 == game.turn:
                game.player1cards.append(card)
                game.turn = game.player2
            else:
                game.player2cards.append(card)
                game.turn = game.player1
            if isGameCompleted():
                if game.won == "Draw":
                    return str(card) + "\n Game is drawn"
                else:
                    return str(card) + "\n Game over and " + game.won + " has won the game"
            else:
                return str(card)
        else:
            return "No card found with specific requirement"
    else:
        return "Game was completed"


@app.route('/getGameDetails', methods=['GET'])
def getCardGameDetails():
    return str(game)

if __name__ == '__main__':
    app.run()
