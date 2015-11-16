from twilio.rest import TwilioRestClient

ACCOUNT_SID = ""
AUTH_TOKEN = ""

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

f_sl = open("song_list.txt", "a")

messages = client.messages.list()
stack = []

for message in messages:
    if message.status == "received": 
        print message.body
        print message.sid
        stack.append(message.body)
        client.messages.delete(message.sid)

while len(stack) > 0:
    f_sl.write(stack.pop())
    f_sl.write("\n")

f_sl.close()
