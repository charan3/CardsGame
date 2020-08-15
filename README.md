# CardsGame


1.startGame() POST api
http://127.0.0.1:5000/startGame

Input: 
{
   "players":[
      {
         "name":"reddy"
      },
      {
         "name":"charan"
      }
   ]
}

Output:
All the Players have joined. charan should start the game


2. whoseTurn GET api
http://127.0.0.1:5000/whoseTurn

Output: reddy

3. pickCard POST api
http://127.0.0.1:5000/pickCard

3.1 pickCard(general)

Output: Ace of Diamonds

3.2 pickCard(based on color)

Input:
{
    "color" : "RED"
}

Output:
Eight of Clubs


3.3 pickCard(based on suit)

Input:
{
    "suit" : "Hearts"
}

Output:
Seven of Hearts

4. getCardGameDetails GET api

http://127.0.0.1:5000/getGameDetails

Output: 
Game id:2534197774
Player1: reddy with picked cards:[Ace of Diamonds,Three of Diamonds,Eight of Clubs,].
Player2: charan with picked cards:[Eight of Diamonds,Seven of Hearts,].
Current Player Turn: reddy
Won:None
