# string='Sharique'
# print(list(reversed(string))) # simple reversing
class Vowels: # reversing through custom object
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)
v = Vowels() #custom object

# reverse a custom object v
print(list(reversed(v)))

