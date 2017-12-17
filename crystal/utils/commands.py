class Commander(object):
    def __init__(self, commands):
        self.commands = commands

    def run(self):
        while True:
            print "\nPick one:"
            for idx, command in enumerate(self.commands):
                print str(idx + 1) + ": " + command.title
            selection = int(input("Enter choice: "))
            if 1 <= selection <= len(self.commands):
                try:
                    self.commands[selection-1].run()
                except Exception as e:
                    print 'ERROR: ' + str(e)


class Command(object):
    def __init__(self, title, action):
        self.title = title
        self.action = action

    def run(self):
        self.action()
