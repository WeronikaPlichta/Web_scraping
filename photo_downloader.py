# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:52:37 2022

@author: weron
"""
import requests
from bs4 import BeautifulSoup
import os
import lxml

'''
Function takes an url from Unsplsh (website with open source pictures) and downloads 
20 pictures (one page) matching the keyword given in the url.
'''
def photo_downloader(url, photo_name):
    
    directory = f'./pictures/'
    
    if not os.path.exists(directory):
         os.makedirs(directory)
    
    
    request = requests.get(url,allow_redirects = True)
    data = BeautifulSoup(request.text,'lxml')
    all_image=data.find_all('figure',itemprop="image") #url of pictures are separated by <figure>, so we use it as marker
    count =0
    os.chdir('./pictures')
    for i in all_image:
        url=i.find('a',rel="nofollow")
        if url != None:
            i_url = url['href'] #go through saved urls and download pictures they represent
            photo_bytes = requests.get(i_url,allow_redirects=True)
            with open(f'{count}{photo_name}.jpg','wb') as photo:
                photo.write(photo_bytes.content)
                count +=1

    print("Done")


if __name__ == "__main__":
    keyword1 = "cats" #output of "sentiment_analysis" function
    keyword2 = "dogs"
    photo_downloader(f'https://unsplash.com/s/photos/{keyword1}-{keyword2}',"cats&dogs")