class Snake:
    def __init__(self, type):
        self.a = type

    def __str__(self):
        return "Snake, type = " + self.a

# Create Snake instance.
# ... Print its repr.
s = Snake("Anaconda")
print(s)


# #Get repr of Snake.
# value = repr(s)
# print(value)

