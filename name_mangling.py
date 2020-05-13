class SecretString:

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrpt(self, pass_phrase):
        if pass_phrase == self.__plain_string:
            return self.__plain_string
        else:
            return ""
