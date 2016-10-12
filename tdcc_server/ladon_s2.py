# -*- coding: utf-8 -*-
from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType
from ladon.compat import PORTABLE_STRING
from albumdata import albums

class Band(LadonType):
  name = PORTABLE_STRING
  album_titles = [ PORTABLE_STRING ]

class Album(LadonType):
  band = Band
  title = PORTABLE_STRING
  songs = [ PORTABLE_STRING ]


class AlbumService(object):
  """
  Search through albums and bands.
  """
 
  @ladonize(PORTABLE_STRING,rtype=[ Album ])
  def listAlbums(self,search_frase=PORTABLE_STRING('')):
    """
    Fetch a list of albums matching search_frase
    """
    album_list = []
    for band_name,albums_dict in albums.items():
      b = Band()
      b.name = band_name
      b.album_titles = []
      for album_title,songs in albums_dict.items():
        b.album_titles += [ album_title ]
        if len(search_frase)==0 or album_title.find(search_frase)>-1:
          a = Album()
          a.band = b
          a.title = album_title
          a.songs = [ ]
          for idx,song_title in songs:
            a.songs += [song_title]
          album_list += [a]
    return album_list

  @ladonize(PORTABLE_STRING,rtype=[ Band ])
  def listBands(self,search_frase=PORTABLE_STRING('')):
    """
    Fetch a list of albums matching search_frase
    """
    bands = []
    for band_name,albums_dict in albums.items():
      if len(search_frase)==0 or band_name.find(search_frase)>-1:
        b = Band()
        b.name = band_name
        b.album_titles = []
        for album_title,songs in albums_dict.items():
          b.album_titles += [ album_title ]
        bands += [b]
    return bands
