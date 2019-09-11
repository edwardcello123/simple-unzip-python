#!/usr/bin/env python
# coding: utf-8

# In[2]:


### Entrepreneur Example ###
from selenium import webdriver
from PIL import Image 
from bs4 import BeautifulSoup

import requests
import os


# In[97]:


### global parameters need to adjust ###
search_query = input('which press:')
link = input('link:')
author = input('author:')
###########

###
headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
###

### check proper tags ###
html = requests.get(link,headers=headers).text
soup = BeautifulSoup(html)
body = soup.findAll('p')
detect = [i.parent for i in body]
count = [i.text for i in detect]
while len(count)==len(set(count)):
    detect = [i.parent for i in detect]
    count = [i.text for i in detect]
real_parent = max(detect, key=lambda item: len(item.text))
article = [i for i in body if i.text in real_parent.text and len(i.text)>2 ]


if author!='NA':
    author_tag = soup.findAll(text=author)[0].parent
    author_class = author_tag['class'][0]


# In[98]:


### screen shot of the logo ###
driver = webdriver.PhantomJS()
driver.maximize_window()

url_part1 = 'https://www.google.com/search?q='
url_part2 = '&source=lnms&tbm=isch'

driver.get(url_part1+search_query+url_part2)
driver.save_screenshot('capture.png')    

ele = driver.find_element_by_tag_name("img")
left = ele.location['x']
top = ele.location['y']
right = left + ele.size['width']
bottom = top + ele.size['height'] 
#crop the logo
im = Image.open('capture.png')
im = im.crop((left, top, right, bottom))    
im.save('logo.png')    

driver.quit()
###################################


# In[99]:


driver = webdriver.PhantomJS()
driver.maximize_window() 

#screen shot of the whole page#
### input the link of the news ###
driver.get(link)
driver.save_screenshot('capture.png')    


# In[100]:


#locate the header
header = driver.find_element_by_tag_name('h1')
left = header.location['x']
top = header.location['y']
right = left + header.size['width']
bottom = top + header.size['height']
#crop the header
im = Image.open('capture.png')
im = im.crop((left,top,right,bottom))
im.save('header.png')


# In[101]:


text = real_parent.get_text()
name = real_parent.name
attrs = list(real_parent.attrs.keys())[0]
if type(list(real_parent.attrs.values())[0])==type('fuck'):
    value = list(real_parent.attrs.values())[0]
else:
    values = ' '.join(list(real_parent.attrs.values())[0])
ele = driver.find_element_by_xpath("//{0}[@{1}='{2}']".format(name,attrs,values))
left = ele.location['x']
top = ele.location['y']
right = left + ele.size['width']
bottom = top + ele.size['height'] 
#crop the article
im = Image.open('capture.png')
im = im.crop((left, top, right, bottom))    
im.save('article.png')


# In[110]:


#locate the author
if author!='NA':
    author = driver.find_element_by_class_name(author_class)
    left = author.location['x']
    top = author.location['y']
    right = left + author.size['width']
    bottom = top + author.size['height']
    #crop the author
    im = Image.open('capture.png')
    im = im.crop((left,top,right,bottom))
    im.save('author.png')

    
#Done
driver.quit()


#Paste all the component
if author=='NA':
    ims = [Image.open(fn) for fn in ['logo.png','header.png','article.png']]
else:
    ims = [Image.open(fn) for fn in ['logo.png','header.png','author.png','article.png']]
width = ims[1].size[0]

for i in range(1,len(ims)):
    ims[i] = ims[i].resize((width,int(width/ims[i].size[0]*ims[i].size[1])))

height = sum([ims[i].size[1] for i in range(len(ims))])
result = Image.new(ims[0].mode,(width, height))

height = ims[0].size[1]
result.paste(ims[0],(int((width-ims[0].size[0])/2),0))
for im in ims[1:]:
    result.paste(im,(0,height))
    height += im.size[1]

result.save('result.png')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#locate article in the page
i = 1
for para in article:
    print(i)
    try:
        text = para.get_text()
        ele = driver.find_element_by_class
        left = ele.location['x']
        top = ele.location['y']
        right = left + ele.size['width']
        bottom = top + ele.size['height'] 
        #crop the article
        im = Image.open('capture.png')
        im = im.crop((left, top, right, bottom))    
        im.save('./img/para'+str(i)+'.png')
        i+=1
    except:
        continue
ims = [Image.open('img/'+fn) for fn in os.listdir('img')]
width = ims[1].size[0]
height = sum([ims[i].size[1] for i in range(len(ims))])
main = Image.new(ims[0].mode,(width, height))
height=0
for im in ims:
    main.paste(im,(0,height))
    height += im.size[1]
main.save('article.png')

