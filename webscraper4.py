#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:22:47 2020
@author: katharinaenin
"""

#Webscraper for AMA

import requests
import numpy as np
from bs4 import BeautifulSoup

#starting page or root page
root_url='https://www.ama.org/marketing-news-archive/'
page = requests.get(root_url).text

soup = BeautifulSoup(page, features="lxml")

link_list = np.array([]);

file = open("OutputAMA.txt","w");

number_article = 0;

#get all the links to monthly archive pages
for a in soup.select('.wp-block-column h3 a'):
    link_list = np.append(link_list,a.get('href')); #alle Monatslinks
    
    
#extract content    
for month_link in link_list:  
    
    #Load More Button entgehen
    url1 = month_link;
    url2 = month_link+'?paged=2';
    url3 = month_link+'?paged=3';
    month_links = [url1,url2,url3];
    
    for month_link_page in month_links: 
        new_url = month_link_page;
        page = requests.get(new_url).text
        soup = BeautifulSoup(page, features="lxml")
        
        for link in soup.findAll('a',{"class": "content-card-url"}):
            url = link.get('href');
            page = requests.get(url).text
            soup = BeautifulSoup(page)
            
            headline = soup.find('h1').get_text()
            sub_headline = soup.find('h2').get_text()
            p_tags = soup.find_all('p');
            p_tags_text = [tag.get_text().strip() for tag in p_tags] 
        
            p_tags_text = p_tags_text[3:-2]
            file.writelines(headline);
            file.writelines("\n");
            file.writelines(sub_headline);
            file.writelines("\n");
            file.writelines(p_tags_text);
            file.writelines("\n \n"); 
            number_article = number_article + 1;
            
file.close();            
        
        
    
    
        
     
    

