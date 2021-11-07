import smtplib, ssl
from os import urandom

def sendEmail(userID, receiver_email):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "pixeltoapp.uta@gmail.com"
    password = "erb513uta"
#    receiver_email = "soumik.mohian@gmail.com"
# Create a secure SSL context
    context = ssl.create_default_context()
    new_password = urandom(16).hex()
#    message = "Your UserID for pixel2app Draw is: " + userID + "and New Password is:"+ new_password
    message = """From: From pixeltoapp <"pixeltoapp.uta@gmail.com">
To: To %s <%s>
Subject: Forgot Password PixeltoApp

Your User ID for pixel2app Draw is %s  and New Password is %s.
"""%(userID,receiver_email,userID,new_password)

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here
    except Exception as e:
    # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
    return new_password


