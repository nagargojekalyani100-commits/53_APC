# Base class
class Notification:
    def send(self):
        print("Sending notification")


# Email Notification class
class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email")


# SMS Notification class
class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS")


# Push Notification class
class PushNotification(Notification):
    def send(self):
        print("Sending notification through Push Notification")


# Create objects
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

# Runtime polymorphism
notifications = [email, sms, push]

for notification in notifications:
    notification.send()