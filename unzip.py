#!/usr/bin/env python
# coding: utf-8

# In[34]:


import os
import zipfile
import tkinter
import tkinter.messagebox
import tkinter.filedialog


# In[35]:


root = tkinter.Tk()
root.title = 'myzip'
root.minsize=(600,800)


# In[36]:


filenames = []


# In[37]:


def addfiles():
    global filenames
    files = tkinterfiledialog.askopenfilenames()
    filenames += list(files)
    strs = '\n'.join(filenames)
    label['text'] = strs
    
    global num
    num = strs.count('\n') + 1
    if filenames == []:
        tkinter.messagebox.showinfo(title='提示信息', message='您好，您还未添加任何文件')
    else:
        tkinter.messagebox.showinfo(title='提示信息', message='您好，您共添加了{}个文件'.format(num))
        


# In[38]:


def zip_files():
    
    global path
    path = './myzip.zip'
 
    
    result = tkinter.messagebox.askokcancel(title='提示信息', message='是否需要对当前{}个文件进行压缩？'.format(num))
    
    if result == True:
        
        zp = zipfile.ZipFile(path, 'w')
        
        
        for file in filenames:
            global dir
            dir = os.path.basename(file)
            zp.write(file,dir)
        
        zp.close()
 
    
    if os.path.exists(path):
        tkinter.messagebox.showinfo(title = '提示信息',message = '压缩文件创建成功！！！\n目录为:'+ path)
    else:
        tkinter.messagebox.showerror(title = '错误信息',message = '压缩文件创建失败！！！')
 


# In[39]:


#解压文件的函数
def unzip_files():
 
    try:
        
        tkinter.messagebox.showinfo(title='提示信息', message='请选择选择解压文件！！！')
        unzipfile = tkinter.filedialog.askopenfilename()
        
        result = tkinter.messagebox.askokcancel(title='提示信息', message='是否需要对当文件进行解压？')
        if result == True:
        
            tkinter.messagebox.showinfo(title='提示信息', message='请选择选择解压路径！！！')
            unzippath = tkinter.filedialog.askdirectory()
        
            unzp = zipfile.ZipFile(unzipfile)
        
            unzp.extractall(unzippath)
        
            unzp.close()
            tkinter.messagebox.showinfo(title='提示信息', message='解压文件成功！！！')
        else:
            tkinter.messagebox.showinfo(title='提示信息', message='您已取消解压，\n解压文件失败！！！')
 
 
    
    except:
        tkinter.messagebox.showerror(title='错误信息', message='系统程序错误，\n解压文件失败！！！')
 
 
 
 
 
 
 
 


# In[ ]:


btn_add = tkinter.Button(root,text = '添加文件',command = addfiles)
btn_add.place(x = 10,y = 20 )
 
btn_zip = tkinter.Button(root,text = '压缩文件',command = zip_files)
btn_zip.place(x = 110,y = 20)
 
btn_unzip = tkinter.Button(root,text = '解压文件',command = unzip_files)
btn_unzip.place(x = 210,y = 20)
 

label = tkinter.Label(root,text = '暂时没有文件信息',bg = 'white',anchor = 'nw',justify = 'left')
label.place(x = 10,y = 70 ,width = 280,height = 300)
 
 
 
root.mainloop()


# In[ ]:





# In[ ]:




