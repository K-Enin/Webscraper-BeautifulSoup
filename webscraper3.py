#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:26:41 2020

@author: katharinaenin
"""

import requests
#import re
import numpy as np
from bs4 import BeautifulSoup

url = 'https://www.ama.org/marketing-news/traditionally-creative-marketers-play-a-big-role-in-data-driven-customer-experience/'
page = requests.get(url).text


soup = BeautifulSoup(page)
headline = soup.find('h1').get_text()
headline = headline + ". "
p_tags = soup.find_all('p');
p_tags_text = [tag.get_text().strip() for tag in p_tags] 
#p_tags_text = [headline, p_tags_text]

#remove first 2 elements, because they are useless, like author name, date
#p_tags_text ist eine Liste
p_tags_text = p_tags_text[2:-2]

#np.concatenate

#p_tags_text=','.join(p_tags_text) #jetzt ist es ein string

#remove bad characters from script
#bad_chars = ['\u200b','\xa0I','\xa0'];
#p_tags_text=re.sub("|".join(bad_chars),"",p_tags_text)
file = open("Output.txt","w");
#p_tags_text_headline=headline+'. '+p_tags_text;
file.writelines(headline);
file.writelines(p_tags_text);
#file.writelines('MeinNameistCathy');
file.close();

#file = open("Output.rtf","r+")
#print file.read() 

#print(f'Headline:{headline} \n')
#merge headline and text


