#chap15
##习题
1. Unix 纪元是编程中经常参考的时间：1970 年1 月1 日0 点，即协调世界时（UTC）。
2. 函数time.time()
3. time.sleep(5)
4. 取整之后的数
5. datetime是一个日期格式，timedelta是两个日期之间的差值
6. threading.Thread(target=spam)
7. 全局变量与局部变量命名分开
8. subprocess.Popen('C:\\Windows\\System32\\calc.exe')

## 实践项目

```python
#! python3
# stopwatch.py - A simple stopwatch program.
import time
import pyperclip
# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.\
Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum=1
# Start tracking the lap times.
copytext=''
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        copytext+=('Lap #%s: %s (%s)\n' % (str(lapNum).ljust(2), str(totalTime).rjust(5), str(lapTime).rjust(5)))
        print('Lap #%s: %s (%s)' % (str(lapNum).ljust(2), str(totalTime).rjust(5), str(lapTime).rjust(5)), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    pyperclip.copy(copytext)
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

```

#chap16
## 习题
1. 发送协议smtp，接收协议imap
2. 需要函数如下
```python
import smtplib
smtpObj = smtplib.SMTP()
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login()
```

                
3. 需要函数如下

        imapObj = imapclient.IMAPClient()
        imapObj.login()
    
4. 传递给mapObj.search()什么样的参数？
    传入搜索关键词字符串，例如日期，主题，正文内容，发件人，收件人等

5. 如果发生这种情况，必须断开并重连 IMAP 服务器，然后再试。
可以通过执行代码,将限制从 10000 字节改为 10000000 字节.

    ```python
    import imaplib
    imaplib._MAXLINE = 10000000
    ```                    
6. pyzmail
模块解析这些原始消息，将它们作为 PyzMessage 对象返回，使邮件的主题、正文、“收
件人”字段、“发件人”字段和其他部分能用 Python 代码轻松访问。

7. accountSID、authToken、myTwilioNumber 和 myCellPhone 
           
## 实践项目
```python
#coding:utf-8
import imapclient
import pyzmail
import webbrowser
from bs4 import BeautifulSoup
import string
import re
def unsub(html):
    soup = BeautifulSoup(html, 'lxml')
    unsub = soup.findAll('a', text='unsubscribe')
    if unsub !=None:
        try:
            unsub_link = unsub.attrs['href']
            return unsub_link
        except:
            print('cannot find link')
            return None
    else:
        print('cannot find unsubscribe')
        return None

imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
imapObj.login('zikepeng@outlook.com', '3014159micro')
select_info=imapObj.select_folder('INBOX', readonly=True)

print('%d messages in INBOX' % select_info[b'EXISTS'])
UIDs = imapObj.search(['SINCE','05-Jul-2011'])
for uid in UIDs:
    rawMessages = imapObj.fetch(uid,['BODY[]','FLAGS'])

    message = pyzmail.PyzMessage.factory(rawMessages[uid]['BODY[]'])
    esubject=message.get_subject()
    try:
        efrom=message.get_addresses('from')
        eto=message.get_addresses('to')
        etext=message.text_part.get_payload().decode(message.text_part.charset)
        ehtml=message.html_part.get_payload().decode(message.html_part.charset)
        for i in string.punctuation:
            esubject = esubject.replace(i, '')
        link=unsub(ehtml)
        webbrowser.open(link)
    except:
        continue
```

imapObj.logout()
#chap17
1. 什么是RGBA值？
RGBA 值是一组数字，指定顔色中的红、绿、蓝和alpha（透明度）的值。这些值是从0（根本没有）到255（最高）的整数。

2. 如何利用 Pillow 模块得到'CornflowerBlue'的 RGBA 值？
ImageColor.getcolor('CornflowerBlue', 'RGBA')

3. 什么是矩形元组
矩形元组是4 个整数的元组：分别是左边的x 坐标，顶边的y 坐标，宽度和高度。

4. Image.open（'zophie.png'）

5. imageObj.size 是两个整数的元组，宽度和高度。

6. imageObj.crop((0, 50, 50, 50))。请注意，传入crop() 的是一个矩形元组，不是4 个独立的整数参数。

7. 调用Image 对象的imageObj.save（'new_filename.png'）方法。

8. ImageDraw 模块包含在图像上绘画的代码。

9. ImageDraw 对象有一些绘制形状的方法，例如point() 、line() 或rectangle()。这些对象是将Image 对象传入ImageDraw.Draw() 函数后返回的。

## 实践项目
```python
#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
logoIm = logoIm.resize((int(logoWidth/10), int(logoHeight/10)))
print(logoIm.size)
logoWidth, logoHeight = logoIm.size

print(logoWidth,logoHeight)

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    filename=filename.lower()
    if not (filename.endswith('.png') or filename.endswith('.jpg')or filename.endswith('.gif')or filename.endswith('.bmp')) \
       or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size
    if width<(2*logoWidth) or height<(2*logoHeight):
        continue
    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
            print(height,width)
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
            print(height,width)

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))

```

##chap18 
1. 将鼠标移到屏幕的左上角，即坐标（0，0）。
2. pyautogui.size() 返回2 个整数的元组，表示屏幕的宽和高。
3. pyautogui.position() 返回2 个整数的元组，表示鼠标的x 和y 坐标。
4. moveTo() 函数将鼠标移到屏幕的绝对坐标处，而moveRel() 函数相对于鼠
标的当前位置来移动鼠标。
5. pyautogui.dragTo() 和pyautogui.dragRel()。
6. pyautogui.typewrite('Hello world!')
7. 要么向pyautogui.typewrite() 输入键盘键字符串的列表（例如'left'），要么向
pyautogui.press() 输入单个键盘键字符串。
8. pyautogui.screenshot('screenshot.png')
9. pyautogui.PAUSE = 2

##实践项目
```python
#! python3
import pyautogui
import time
import random

try:
    while True:
        x=random.randint(-1,1)
        y=random.randint(-1,1)
        print(x,y)
        pyautogui.moveRel(x, y, duration=0.2)
        time.sleep(10)
except KeyboardInterrupt:
    print('done')
```









