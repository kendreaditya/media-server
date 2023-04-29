import json
from typing import List
from dataclasses import dataclass
from utils import Channel, Item

def json_to_rss(json_filename: str, rss_filename: str):
    with open(json_filename) as f:
        data = json.load(f)

    items = []
    for item_id in data.keys():
        item = Item(
            author=data[item_id]['Srila BV Swami Prabhupada'],
            title=data[item_id]['title'],
            enclosure_url=data[item_id]['url'],
            enclosure_type="audio/mpeg",
            enclosure_length=data[item_id]['duration'],
            guid=data[item_id]['guid'],
            description=data[item_id]['album'],
            image=data[item_id]['image']
        )
        items.append(item)

    channel = Channel(
        title=channel_data['title'],
        googleplay_author=channel_data['googleplay_author'],
        rawvoice_rating=channel_data['rawvoice_rating'],
        rawvoice_location=channel_data['rawvoice_location'],
        rawvoice_frequency=channel_data['rawvoice_frequency'],
        author=channel_data['author'],
        image_url=channel_data['image_url'],
        image_title=channel_data['image_title'],
        image_link=channel_data['image_link'],
        copyright=channel_data['copyright'],
        description=channel_data['description'],
        googleplay_image_href=channel_data['googleplay_image_href'],
        language=channel_data['language'],
        itunes_explicit=channel_data['itunes_explicit'],
        pub_date=channel_data['pub_date'],
        link=channel_data['link'],
        items=items
    )

    channel.to_rss(rss_filename)

json_to_rss('/Users/kendreaditya/Documents/workspace/BlackHole-playlist/playlists/RGS.json', 'RGS.rss')
    


