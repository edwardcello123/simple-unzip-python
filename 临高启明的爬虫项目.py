#!/usr/bin/env python
# coding: utf-8

# In[198]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[199]:


html = urlopen('https://www.fpzw.com/xiaoshuo/0/63/8570814.html')
bsObj = BeautifulSoup(html)
content = bsObj.findAll('p',{'class':'Text'})
text = '\n'.join([i for i in list(content[0].children) if str(i)[0]!='<'])


# In[277]:


homepage = 'https://www.fpzw.com/xiaoshuo/0/63/'
html = urlopen(homepage)
soup = BeautifulSoup(html)
banner = soup.dl.findAll('a')[4:]
title = [i.text for i in banner]

title[893] = '第四十四节 总督德-卡蓬蒂尔'
title[1526] = title[1526].replace('**','腐败')


# In[203]:


story = []
j = 0
for i in banner:
    url = homepage + i['href']
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    content = bsObj.findAll('p',{'class':'Text'})
    text = '\n'.join([i for i in list(content[0].children) if str(i)[0]!='<'])
    
    story.append(text)
    print(j)
    j=j+1
    
story[1526] = story[1526].replace('**','腐败')


# In[294]:


n=1
for i in range(len(story)):
    if "第一节" in banner[i].text:
        if n == 1:
            os.mkdir(str(n))
            n = n+1
            os.chdir(str(n-1))
        else:
            os.chdir('..')
            os.mkdir(str(n))
            n = n+1
            os.chdir(str(n-1))
        
    with open(title[i]+'.txt','w',encoding='utf-8') as f:
        f.write(story[i])
    

