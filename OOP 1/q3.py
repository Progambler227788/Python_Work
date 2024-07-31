# Question 3
''' In this question, there will be a message class having attributes sender, recipient and message that is sent by sender
and received by receiver. Get Sender return sender name, Get Recipient return Recipient name and append function 
adds give line of string to message body. toString() function is tro return string having sender name, receiver name
and message body'''
class Message:
    """
    The Message class having sender, recpient and message as its attributes.
    """
    def __init__(self, sender, recipient):
        """
        Initializes a Message object with sender, recipient, and an empty message body using Constructor.
        """
        self.sender       = sender
        self.recipient    = recipient
        self.message_body = ""

    def get_sender(self):
        """
        This function will return the sender's name.
        """
        return self.sender

    def get_recipient(self):
        """
        This function will return the recipient's name.
        """
        return self.recipient

    def append(self, line):
        """
        This function will append a line to message body.
        """
        self.message_body = self.message_body + line + "\n"

    def toString(self):
        """
        This function will return sender name, recipient name and message.
        """
        return f"From: {self.sender}\n\nTo: {self.recipient}\n\n{self.message_body}"

# Create a Message object having harry morgan as sender and rudolf reindeer as receiver
message = Message("Harry Morgan", "Rudolf Reindeer")

# Append lines to the message body
message.append("Hi Rudolf,")
message.append("I hope you're doing well!")
message.append("Are you available tomorrow for meeting?")
message.append("Best regards,")
message.append("Harry Morgan")

# Print the message 
print(message.toString())
