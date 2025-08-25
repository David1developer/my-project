from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

# Your Gmail details
EMAIL_ADDRESS = "crownjude33@gmail.com"   # your Gmail
EMAIL_PASSWORD = "whqqwtivhruuruqw"  # the 16-digit app password

@app.route("/")
def home():
    return render_template("index.html")  # Your website’s HTML file

@app.route("/send_message", methods=["POST"])
def send_message():
    first_name = request.form["firstName"]
    last_name = request.form["lastName"]
    sender_email = request.form["email"]
    message_content = request.form["message"]

    # -------------------------
    # 1. SEND MESSAGE TO YOU
    # -------------------------
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = f"New Contact Form Message from {first_name} {last_name}"

    body = f"""
    You got a new message from your portfolio website:

    Name: {first_name} {last_name}
    Email: {sender_email}
    Message:
    {message_content}
    """
    msg.attach(MIMEText(body, "plain"))

    auto_reply = MIMEMultipart()
    auto_reply["From"] = EMAIL_ADDRESS
    auto_reply["To"] = sender_email
    auto_reply["Subject"] = "Thanks for contacting me!"

    auto_reply_body = f"""
    Hi {first_name},

    Thanks for reaching out! I’ve received your message and will get back to you soon.

    Best regards,  
    David
    """
    auto_reply.attach(MIMEText(auto_reply_body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        
            server.send_message(msg)

            
            server.send_message(auto_reply)

        flash("✅ Your message has been sent, and an auto-reply was delivered!")
    except Exception as e:
        print("❌ Error:", e)
        flash("⚠️ Something went wrong. Please try again later.")

    return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)
