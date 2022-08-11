import os
from twilio.rest import Client
#Add your twilio SID and TOKEN in a .env file 

SID = os.environ['SID']
TOKEN = os.environ['TOKEN']
def main():
    client = Client(SID, TOKEN)
    message = "Test"
    while message != "":
        recipient = input("Enter recipient number: ")
        message = input("Enter message: ")
        if message != "":
            client.messages.create(
                to= f"+1{recipient}",
                from_="+19496702384",
                body=message)
            print("Message sent!")
        else:
            print("Message not sent!")
            break

if __name__ == "__main__":
    main()