list = [('老师:北宋有个人和你一样，他姓武！', '\n<p>\n\u3000\u3000老师:&ldquo;小明，你的梦想是什么？&rdquo;小明沉思'
                              '片刻道:&ldquo;有房有铺，自己当老板，<br />\n妻子貌美如花，还有当官的兄弟&rdquo; '
                              '老师:北宋有个人和你一样，他姓武&hellip;！</p>\n')]
import re
content = []
for i in list:
    j = re.sub(r'\n|<p>|\u3000|<br />|</p>|','',list[0][1])
    j = j.replace('&ldquo;','"').replace('&rdquo','"').replace('&hellip;','...')
    content.append([i[0],j])
    print(content)