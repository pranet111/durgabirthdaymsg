const express = require('express');
const twilio = require('twilio');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const accountSid = 'YOUR_TWILIO_ACCOUNT_SID'; // Your Account SID from www.twilio.com/console
const authToken = 'YOUR_TWILIO_AUTH_TOKEN'; // Your Auth Token from www.twilio.com/console
const client = new twilio(accountSid, authToken);

app.post('/send-sms', (req, res) => {
    const { phoneNumber, message } = req.body;

    client.messages.create({
        body: message,
        to: phoneNumber, // Text this number
        from: 'YOUR_TWILIO_PHONE_NUMBER' // From a valid Twilio number
    })
    .then((message) => res.status(200).send(`Message sent: ${message.sid}`))
    .catch((error) => res.status(500).send(error));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
