class String:
    def __init__(self, value = "abcxyz"):
        self.value = value

    def input_string(self):
        self.value = input("Enter a string: ")

    def display_string(self):
        return(self.value)

    def length(self):
        return len(self.value)

    def concatenate(self, other_string):
        self.value += other_string

    def reverse(self):
        self.value = self.value[::-1]
  

string = String()
string.input_string()
print('string:',string.display_string())
print('chiều dài string:', string.length())
string.reverse()
print('đảo ngược string:', string.display_string())
