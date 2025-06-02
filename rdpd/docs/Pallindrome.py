class Pallindrome:
    def __init__(self, string):
        self.string = string

    def is_pallindrome(self):
        return self.string == self.string[::-1]

    def get_pallindrome(self):
        return self.string[::-1]

    def get_non_pallindrome(self):
        return self.string[::-1]


if __name__ == "__main__":
    pallindrome = Pallindrome("racecar")
    print(pallindrome.is_pallindrome())
    print(pallindrome.get_pallindrome())
    print(pallindrome.get_non_pallindrome())


