from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets import library
import beets
import urllib
import urllib2

def sendAlbums(username, password, albumIds):
    url = 'http://musicbrainz.org/ws/1/collection/' #Where to send them
    data = urllib.urlencode({ 'add': ",".join(albumIds) })
    #Post it
    pm = urllib2.HTTPPasswordMgrWithDefaultRealm()
    pm.add_password(None, url, username, password)
    urllib2.install_opener(urllib2.build_opener(
            urllib2.HTTPDigestAuthHandler(pm)))
    resp = urllib2.urlopen(url, data).read()
    return resp

update_mb_collection = Subcommand('mbupdate',
        help='Update MusicBrainz collection')
def updateCollection(lib, config, opts, args):
    username = beets.ui.config_val(config, 'musicbrainz', 'user', '')
    password = beets.ui.config_val(config, 'musicbrainz', 'pass', '')
    #Get a list of all the albums
    albums =  map(lambda a: a.mb_albumid, lib.albums())
    print 'Updating MusicBrainz collection...'
    sendAlbums(username, password, albums)
    print '...MusicBrainz collection updated'

update_mb_collection.func = updateCollection

class MusicbrainzCollection(BeetsPlugin):
    def commands(self):
            return [update_mb_collection]
