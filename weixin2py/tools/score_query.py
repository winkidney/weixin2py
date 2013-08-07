#!usr/bin/python
# coding:utf-8

import urllib
import urllib2
import re


#post数据处理和接收的页面
posturl = 'http://61.136.204.41:8080/edu/login!checkLogin.action'   #外网
#posturl = 'http://211.67.32.144/edu/login!checkLogin.action'    #内网
#成绩查询地址
score_query_url = 'http://61.136.204.41:8080/edu/gradeEnteringStudent!getAllGradeEnter.action'  #外网
#score_query_url = 'http://211.67.32.144/edu/gradeEnteringStudent!getAllGradeEnter.action'    #内网
def score_query(user_name,password,year='',term=''):
    """返回一个成绩查询页面的html文本字符串对象"""

    #构造header,一般header至少包含以下两项
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0',
               }

    #构造post数据，通过抓包分析的数据
    postdata = {'user.account':user_name,
                'user.password':password,
                'user.roleId':'2'}
    #给post编码
    encoded_data = urllib.urlencode(postdata)

    #通过urllib2提供的request方法向指定url发送我们构造的数据并完成登录过程

    request = urllib2.Request(posturl,encoded_data,headers)
    try:  
        response = urllib2.urlopen(request,timeout=2)
    except urllib2.URLError:
        return False
    #获得cookie并加入新的request头中
    cookie = response.headers['Set-Cookie'].split(r' ')[0][0:-1]
    score_query_request = urllib2.Request(score_query_url)
    score_query_request.add_header('Cookie',
                                   cookie
                                   )

    #如果指定了年份，则查询指定年份的成绩，添加一个post
    if year != '':
        score_post = {'Submit':'查询',
                      'configData.openTerm':str(term),
                      'configData.openYear':str(year)
                      }
        encoded_scorepost = urllib.urlencode(score_post)
        score_query_request.add_data(encoded_scorepost)
        
    try :
        score_response = urllib2.urlopen(score_query_request)
    except urllib2.URLError:
        return False
    result_html = score_response.read()
    str_result = clean_text(result_html)
    return str_result

def clean_text(src_html):
    '''利用源获得的源网页数据生成一个字符串对象，科目：成绩'''
    regexp = re.compile(r'<td>(.+?)</td>')
    result = re.findall(regexp,src_html)
    length = len(result)
    clean_data = {}
    count = 0
    while 1:
        clean_data[result[3+count*9]] = result[3+count*9+1] #不进行解码，保持原始的ascii字节流
        #clean_data[result[3+count*9].decode('utf-8')] = result[3+count*9+1].decode('utf-8')    #解码为utf-8
        count = count+1
        if count*9+3 > length:
            break
    #生成列表
    results = []
    for key in clean_data:
        results.append(key+'：'+clean_data[key])
    #生成字符串
    str_data = '\n'.join(results)
    return str_data

def main(user_name,passwd,year='',term=''):
    '''根据输入的学号密码返回一个字符串列表，每一行的内容为“科目：成绩”'''
    str_data = score_query(user_name,passwd,year,term)
    #print str_data#.decode('utf-8')
    return str_data
if __name__ == '__main__':
    main('031140816','19921226')
    