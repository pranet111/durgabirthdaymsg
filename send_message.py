import os
from twilio.rest import Client

# Get credentials from environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone = os.environ['TWILIO_PHONE']

# Create a Twilio client
client = Client(account_sid, auth_token)

def send_message(to, body):
    message = client.messages.create(
        body=body,
        from_=twilio_phone,
        to=to
    )
    print(f"Message sent with SID: {message.sid}")

if __name__ == "__main__":
    # recipient phone number and message content
    recipient_phone = '+19083976483'  # replace with the actual recipient's number
    message_text = 'happy 16th birthday, durga. i hope this day is everything you want it to be. even though we’ve drifted apart, i can’t help but think about all the memories we used to share, especially on days like this. i miss you, more than i probably should admit. but i genuinely hope your birthday is filled with happiness and love, because you deserve nothing less. i wish things were different between us, but even from a distance, i’ll always wish the best for you. enjoy your day.'
    
    send_message(recipient_phone, message_text)
