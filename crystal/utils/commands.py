import logging

from crystal.utils.console import clear_screen


class Commander(object):
    def __init__(self, header_command, commands):
        self.commands = commands
        self.header_command = header_command

    def run(self):
        while True:
            clear_screen()
            self.header_command.action()

            print "\nPick one:"
            for idx, command in enumerate(self.commands):
                print str(idx + 1) + ": " + command.title
            selection = self._try_parse_int(raw_input("Enter choice: "))
            if 1 <= selection <= len(self.commands):
                try:
                    self.commands[selection - 1].run()
                except Exception as e:
                    logging.exception('ERROR: ' + str(e))

    @staticmethod
    def _try_parse_int(str):
        try:
            return int(str)
        except:
            return 0


class Command(object):
    def __init__(self, title, action):
        self.title = title
        self.action = action

    def run(self):
        self.action()
