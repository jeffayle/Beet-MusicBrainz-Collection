from beets.plugins import BeetsPlugin
from beets.ui import Subcommand

update_mb_collection = Subcommand('mbupdate',
        help='Update MusicBrainz collection')
def updateCollection(lib, config, opts, args):
    username = beets.ui.config_val(config, 'musicbrainz', 'user', '')
    password = beets.ui.config_val(config, 'musicbrainz', 'pass', '')

update_mb_collection.func = updateCollection

class MusicbrainzCollection(BeetsPlugin):
    def commands(self):
            return [update_mb_collection]
