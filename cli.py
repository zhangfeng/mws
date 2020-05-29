import cmd

class Cli(cmd.Cmd):

    prompt = 'MWS> '

    def do_play(self, arg):
        "Play the song"
        pass

    def do_EOF(self, arg):
        return True

    def do_q(self, arg):
        "Exit"
        return True
