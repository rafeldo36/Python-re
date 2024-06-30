import random
import string

def encode_message(message):
    if len(message) >= 3:
        # Rotate the string by moving the first character to the end
        message = message[1:] + message[0]
        # Append random letters at the beginning and end
        random_start = ''.join(random.sample(string.ascii_letters, 3))
        random_end = ''.join(random.sample(string.ascii_letters, 3))
        message = random_start + message + random_end
    else:
        # Simply reverse the string if it has less than 3 characters
        message = message[::-1]
    return message

def decode_message(message):
    if len(message) < 3:
        # Reverse the string if it has less than 3 characters
        message = message[::-1]
    else:
        # Remove the first and last three random characters
        message = message[3:-3]
        # Move the last character to the beginning
        message = message[-1] + message[:-1]
    return message

# Ask the user whether to encode or decode
question = int(input("What do you want to do? 1. Encode 2. Decode: "))

if question == 1:
    message = input("Enter the message: ")
    coded_message = encode_message(message)
    print("Encoded message:", coded_message)
elif question == 2:
    message = input("Enter the message: ")
    decoded_message = decode_message(message)
    print("Decoded message:", decoded_message)
else:
    print("Invalid option. Please enter 1 to encode or 2 to decode.")
