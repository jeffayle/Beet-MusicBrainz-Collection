from beets.plugins import BeetsPlugin
from beets.ui import Subcommand

my_super_command = Subcommand('super', help='do something super')
def say_hi(lib, config, opts, args):
    print "Hello everybody! I'm a plugin!"
my_super_command.func = say_hi

class MusicbrainzCollection(BeetsPlugin):
    def commands(self):
            return [my_super_command]
