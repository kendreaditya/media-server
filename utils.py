import xml.etree.ElementTree as ET
from typing import List
from dataclasses import dataclass

@dataclass
class Item:
    title: str
    author: str
    pubDate: str
    enclosure_url: str
    enclosure_type: str
    enclosure_length: str
    description: str

@dataclass
class Channel:
    title: str
    author: str
    image_url: str
    image_title: str
    image_link: str
    copyright: str
    description: str
    googleplay_image_href: str
    language: str
    itunes_explicit: str
    pub_date: str
    link: str
    items: List[Item]


    def to_rss(self, filename: str):
        channel_elem = ET.Element('channel')

        title_elem = ET.SubElement(channel_elem, 'title')
        title_elem.text = self.title

        googleplay_author_elem = ET.SubElement(channel_elem, 'googleplay:author')
        googleplay_author_elem.text = self.googleplay_author
        googleplay_author_elem.set('xmlns:googleplay', 'http://www.google.com/schemas/play-podcasts/1.0')

        # ... add remaining channel elements ...

        for item in self.items:
            item_elem = ET.SubElement(channel_elem, 'item')
            for key, value in item.items():
                item_child_elem = ET.SubElement(item_elem, key)
                item_child_elem.text = value

        rss_elem = ET.Element('rss')
        rss_elem.set('xmlns:googleplay', 'http://www.google.com/schemas/play-podcasts/1.0')
        rss_elem.set('xmlns:itunes', 'http://www.itunes.com/dtds/podcast-1.0.dtd')
        rss_elem.set('xmlns:atom', 'http://www.w3.org/2005/Atom')
        rss_elem.set('xmlns:rawvoice', 'http://www.rawvoice.com/rawvoiceRssModule/')
        rss_elem.set('xmlns:content', 'http://purl.org/rss/1.0/modules/content/')
        rss_elem.set('version', '2.0')

        rss_elem.append(channel_elem)

        ET.ElementTree(rss_elem).write(filename, encoding='UTF-8', xml_declaration=True)
