from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow frontend requests

# Configure Flask-Mail with Gmail SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'myworld03071003@gmail.com'  # Your Gmail
app.config['MAIL_PASSWORD'] = 'hpip gydg gnwt rzyn'  # App Password (Not Gmail password)
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

mail = Mail(app)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    email = data.get('email')
    message = data.get('message')

    if not email or not message:
        return jsonify({'error': 'Email and message are required'}), 400

    try:
        # Send email
        msg = Message("New Contact Form Submission",
                      recipients=["your-email@gmail.com"])  # Change to your Gmail
        msg.body = f"Received Email: {email}\nMessage: {message}"
        mail.send(msg)

        return jsonify({'message': 'Message sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
