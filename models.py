from mongoengine import *

connect(
    db="web13",
    host="mongodb+srv://web13user:MXiZgtXDqEC5hN8U@cluster0.kgddv8w.mongodb.net/",
)


class Contact(Document):
    full_name = StringField(required=True)
    email = EmailField(required=True)
    email_sent = BooleanField(default=False)
    # Add other fields as needed
    meta = {"collection": 'contacts'}
