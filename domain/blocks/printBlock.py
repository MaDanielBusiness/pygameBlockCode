from domain.blockInterfaces.commandBlockInterface import CommandBlock


class printBlock(CommandBlock):
    string: str

    def __init__(self, string='default'):
        """ Receive a string to print """
        self.string = string

    def run(self):
        """ Perform the print statement """
        print(self.string)

    def setString(self, string):
        self.string = string

    def getString(self):
        return self.string
