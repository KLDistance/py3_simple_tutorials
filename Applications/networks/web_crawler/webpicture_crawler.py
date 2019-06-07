import requests
from bs4 import BeautifulSoup
import os

def Get_image_url(url):
    Res = requests.get(url)
    Soup = BeautifulSoup(Res.text,'lxml')
    
    Name = Soup.select('h1')[0].string
    Tag = 'img[title=\"' + Name + '\"]'
    Image = Soup.select(Tag)
    
    return Image, Name

def Download_Image(Image_url):
    Image = requests.get(Image_url,stream=True)
    name = Image_url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(Image.content)

def Crawl(url):
    [Image, Name] = Get_image_url(url)
    # store dir
    path = os.getcwd()
    store_path = './crawled_pics/'
    # make dir
    os.chdir(store_path)
    for I in Image:
        Download_Image(I['src'])
    # retrieve to previous directory
    os.chdir(path)

if __name__ == '__main__':
    Crawl('http://www.win4000.com/wallpaper_detail_159024.html')
    Crawl('http://www.win4000.com/wallpaper_detail_159007.html')