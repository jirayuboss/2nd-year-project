from flask import Flask
from flask import jsonify

import requests
import urllib, json
import itertools, random

app = Flask(__name__)

playerhands = {}
show_deck={}
cards = []
iden1 = []
iden2 =	[]
iden3 =	[]
iden4 =	[]
draw_P1 = []
draw_P2 = []
draw_P3 = []
draw_P4 = []
checktime = []
MID = []

hands = {}
updatehands = {}

deck = list(itertools.product(range(10,14), ['H','H','S','S','D','D']))
deck.append(("0","JK"))
for i in range(len(deck)):
    cards.append(str(deck[i][0]) + deck[i][1])

random.shuffle(cards)

@app.route('/picking', methods=['GET',"POST"])
def picking(pos):
    draw_P1.append(draw_P2.pop(pos))
    return redirect(url_for('update'))
    

@app.route('/pick', methods=['GET',"POST"])
def pick():
    if request.method == 'POST':
      user = request.form['pos']
      return redirect(url_for('picking',pos = pos))

@app.route('/update', methods=["GET"])
def update():
    temp1 = []
    for i in range(len(draw_P1)):
        char1 = draw_P1.pop(0)
        if char1 in draw_P1:
            temp1.append(char1)
            MID.append(char1)
        elif char1 in temp1:
            temp1.append(char1)
            MID.append(char1)
        else:
            draw_P1.append(char1)
    temp2 = []
    for i in range(len(draw_P2)):
        char2 = draw_P2.pop(0)
        if char2 in draw_P2:
            temp2.append(char2)
            MID.append(char2)
        elif char2 in temp2:
            temp2.append(char2)
            MID.append(char2)
        else:
            draw_P2.append(char2)
    temp3 = []
    for i in range(len(draw_P3)):
        char3 = draw_P3.pop(0)
        if char3 in draw_P3:
            temp3.append(char3)
            MID.append(char3)
        elif char3 in temp3:
            temp3.append(char3)
            MID.append(char3)
        else:
            draw_P3.append(char3)
    temp4 = []
    for i in range(len(draw_P4)):
        char4 = draw_P4.pop(0)
        if char4 in draw_P4:
            temp4.append(char4)
            MID.append(char4)
        elif char4 in temp4:
            temp4.append(char4)
            MID.append(char4)
        else:
            draw_P4.append(char4)

        updatehands["P1"] = draw_P1
        updatehands["P2"] = draw_P2
        updatehands["P3"] = draw_P3 
        updatehands["P4"] = draw_P4 
        updatehands["MID"] = MID
    return jsonify(updatehands)

@app.route('/playercards', methods=["GET"])
def playercards():
    return jsonify(hands)

@app.route("/draw", methods=["GET"])
def bdraw():
    pos = 0
    if len(draw_P1) == 0:
        for i in range(6):
            draw_P1.append(cards[pos])
            pos += 1

        for i in range(6):
            draw_P2.append(cards[pos])
            pos += 1

        for i in range(6):
            draw_P3.append(cards[pos])
            pos += 1

        for i in range(7):
            draw_P4.append(cards[pos])
            pos += 1
          
    hands["P1"] = draw_P1
    hands["P2"] = draw_P2
    hands["P3"] = draw_P3
    hands["P4"] = draw_P4
    hands["MID"] = MID   
    return jsonify(hands) 

@app.route('/check', methods=["GET", "POST"])
def check():
    return "Reply back"

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000,ssl_context=('cert.pem', 'key.pem'))
