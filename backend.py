from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio import twiml
import csv
import random

app = Flask(__name__)

pun_list = ["1 or 2? We got you.", "Lets get you out of this shitty situation.", "Places to poo near you.", "Need to pee for free?", " You’re the shit or you’re about to shit?", "You’re looking flushed.", "Not all banks accept deposits, but we got you.", "Unlocking the stall with a dookey.", "Bathroom fairy Stinkerbell is here to help!", "Time to B.S. (For Real).", "People who tell you that they’re constipated are full of crap.", "Is it just me or does it smell funny in here?", "You don’t need to pay a fee to pee.", "A pee-line to your closest toilet.", "Urine on the pee club.", "Coding your next stall with P++", "Peeing in Europe? European."]

def valid_restrooms (zip_code):
    with open('Bathrooms_-_Sheet1_2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        restrooms = []
        count = 0
        for row in csv_reader:
            count += 1
            if count > 0:
                if row[2].find(str(zip_code)) > -1:
                    restrooms.append(row)
        return restrooms

def generate_message(row_array):
    str_out = random.choice(pun_list) + "\n"
    print(str_out)
    str_out += "Lucky for you we have found " + str(len(row_array)) + " restrooms! \n"
    count = 1
    for row in row_array:
        str_out += (f'[{count}] {row[4]} \n')
        str_out += (f'Address: {row[2]} \n')
        if row[3].find("-") < 0:
            str_out += (f'Code: {row[3]} \n')
        count += 1

    my_playlist = ["https://open.spotify.com/track/3AJwUDP919kvQ9QcozQPxg?si=e5511f6e930c4bda", 
    "https://open.spotify.com/track/6Slt6WiWnriaqCb8xXb2ZT?si=2a6f1e4ee5dc4971", 
    "https://open.spotify.com/track/629TRAVD61y1ZVNl9EOfEE?si=a10c29f64a194056",
    "https://open.spotify.com/track/6zpxioiW2NpqCCC3T7SoRN?si=fcffb7c46bfc4568",
    "https://open.spotify.com/track/6PZNj9qWs6oguSyN9J5H7X?si=d2955bd5e6d64f1f",
    "https://open.spotify.com/track/0440JCJyIAmINA8KcYgFb5?si=a9b8667aefb348cb",
    "https://open.spotify.com/track/1otG6j1WHNvl9WgXLWkHTo?si=c023211c3de64e65",
    "https://open.spotify.com/track/1otG6j1WHNvl9WgXLWkHTo?si=c023211c3de64e65",
    "https://open.spotify.com/track/5SkRLpaGtvYPhw02vZhQQ9?si=b01927b7e658410c",
    "https://open.spotify.com/track/4KFY4EEv9CN6ivrzD6vEvg?si=4b963cb4a7574149",
    "https://open.spotify.com/track/5QvBXUm5MglLJ3iBfTX2Wo?si=ca91cec8461e487c",
    "https://open.spotify.com/track/5ghIJDpPoe3CfHMGu71E6T?si=8df6c53fba954f67",
    "https://open.spotify.com/track/2ctvdKmETyOzPb2GiJJT53?si=d92c87d09cdb4cdc",
    "https://open.spotify.com/track/1qOU8KzFifXE9YrgjVwYvc?si=01bf00a8fbcc4247",
    "https://open.spotify.com/track/430qNtapCS3Ue1yoSql1oV?si=f54a1e961a024621",
    "https://open.spotify.com/track/3XOalgusokruzA5ZBA2Qcb?si=95b95e34e29f4bc5",
    "https://open.spotify.com/track/4v5kAh2wWyCSuKuhMJK8u6?si=fe1acf072d124320",
    "https://open.spotify.com/track/2iJuuzV8P9Yz0VSurttIV5?si=8f7335cec227413c",
    "https://open.spotify.com/track/6naxalmIoLFWR0siv8dnQQ?si=5d3f57d21a43498b",
    "https://open.spotify.com/track/2cZrrQMjB63c0iIugYH9zS?si=9ecb172416b84b5b",
    "https://open.spotify.com/track/3KyKxJ4P3pVCgaZwaq2rUC?si=447456270d304b24"]

    song = random.choice(my_playlist)
    str_out += "\nA tune for your tinkle: " + song
    return str_out


#row = valid_restrooms("11211")
#generate_message(row)


#######################################################################################################

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start oxur TwiML response
    resp = MessagingResponse()
    zip = request.values.get('Body', None)
    
    row = valid_restrooms(zip)
    ret = generate_message(row)
    print("hi")

    # Add a message
    resp.message(ret)

    return str(resp)


if __name__ == "__main__":
    app.run(port="5004")
