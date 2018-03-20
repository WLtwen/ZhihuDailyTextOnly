import re
import requests
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
urls = "http://daily.zhihu.com"

contents = requests.get(urls,headers=headers)
content = contents.text
story = '<div class="box"><a href="([\d\D]*?)" class="link-button">'
title = 'class="title">([\d\D]*?)</span></a></div>'

result = {}
result1 = re.findall(story,content)
result2 = re.findall(title,content)

result =dict(zip(result1,result2))
for num in result:
    print(str(num) +" : " +str(result[num] ))

select = input('输入要打开的故事号码：')

# import requests
# import re
def openstory(num):
    url = urls+"/story/"+num
    # headers={
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    # }
    response = requests.get(url,headers= headers)
    # print(response.text)
    resource = response.text
    title = '<title>(.*?)</title>'
    title = re.findall(title,resource)
    print("标题： ",title)
    author = '<span class="author">(.*?)</span>'
    author = re.findall(author,resource)
    # print(author)
    answer = '<div class="content">(.*?)?</div>'
    answer = re.findall(answer,resource,re.S)
    subpattern = '<[^>]*>'
    if(len(author)>=2):
        for x in range(0,len(author)):
            print("作者： ",author[x])
            answerg = re.sub(subpattern,"",answer[x])
            print(answerg)
    else:
        print("作者： ",author)
        for x in range(0,len(answer)):
            answerg = re.sub(subpattern,"",answer[x])
            print(answerg)

openstory(select)
