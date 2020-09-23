class Text:
    def get_String(self):
        self.string = input('String:')
    def print_String(self):
        print(self.string.upper())
newobj = Text()
newobj.get_String()
newobj.print_String()
