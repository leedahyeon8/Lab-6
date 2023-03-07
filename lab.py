# Day 3/7/23 worked with Ryan

def encode(password):
    encoded = ""
    for i in password:
        encoded += str(int(i) + 3)
    return encoded
