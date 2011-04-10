#Copyright (c) 2011, Jeffrey Aylesworth <jeffrey@aylesworth.ca>
#
#Permission to use, copy, modify, and/or distribute this software for any
#purpose with or without fee is hereby granted, provided that the above
#copyright notice and this permission notice appear in all copies.
#
#THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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
