import json
import xml.etree.ElementTree as ET

with open('/Users/kendreaditya/Documents/workspace/BlackHole-playlist/playlists/GGM.json') as f:
    data = json.load(f)

rss = ET.Element('rss', version='2.0')
channel = ET.SubElement(rss, 'channel')
title = ET.SubElement(channel, 'title')
title.text = 'Music List'

for key, value in data.items():
    item = ET.SubElement(channel, 'item')
    url = ET.SubElement(item, 'url')
    url.text = value['url']
    perma_url = ET.SubElement(item, 'perma_url')
    perma_url.text = value['perma_url']
    title = ET.SubElement(item, 'title')
    title.text = value['title']
    album = ET.SubElement(item, 'album')
    album.text = value['album']
    artist = ET.SubElement(item, 'artist')
    artist.text = value['artist']
    duration = ET.SubElement(item, 'duration')
    duration.text = value['duration']
    image = ET.SubElement(item, 'image')
    image.text = value['image']
    subtitle = ET.SubElement(item, 'subtitle')
    subtitle.text = value['subtitle']
    expire_at = ET.SubElement(item, 'expire_at')
    expire_at.text = value['expire_at']
    release_date = ET.SubElement(item, 'release_date')
    release_date.text = str(value['release_date'])
    genre = ET.SubElement(item, 'genre')
    genre.text = value['genre']
    has_lyrics = ET.SubElement(item, 'has_lyrics')
    has_lyrics.text = value['has_lyrics']
    language = ET.SubElement(item, 'language')
    language.text = value['language']
    dataAdded = ET.SubElement(item, 'dataAdded')
    dataAdded.text = value['dataAdded']
    item_id = ET.SubElement(item, 'id')
    item_id.text = key
    album_id = ET.SubElement(item, 'album_id')
    album_id.text = value['album_id']

xml_data = ET.tostring(rss)
with open('music.xml', 'wb') as f:
    f.write(xml_data)
