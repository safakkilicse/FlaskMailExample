from flask import Flask, render_template
from Flask_Mail import Mail, Message
from config import Config

app = Flask(__name__)
mail = Mail(app)


def create_app():
    create_admin(app)
    app.config.from_object(Config)
    return app


def create_admin(app):
    from flask import render_template

    @app.route("/", methods=["GET"])
    def home():
        return "<h1>Go to '/mail' </h1>"

    @app.route("/mail", methods=["GET"])
    def mail():
        return render_template("menu.html")

    @app.route("/mail/mail_sender", methods=["GET"])
    def mail_sender():
        return render_template("mail_sender.html")

    @app.route("/mail/mail_done", methods=["POST"])
    def mail_done():
        rendered_template = render_template(
            'mail_template.html',
            button_url='The variable in to the mail_template.html you can bind what you need.'
        )
        send_html_email(
            subject='Mail Success',
            html=rendered_template,
            recipients="your_recipient@gmail.com")
        print("Mail sended.")
        return "Mail sended."


def send_html_email(subject, html, recipients, sender='flaskmail@deneme.com'):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html
    mail.send(msg)
