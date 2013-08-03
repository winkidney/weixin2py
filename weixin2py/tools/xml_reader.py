#coding:utf-8
#in folder 'tools'
#read xml text and return a xml object
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
try:
    import cStringIO as StringIO
except:
    import StringIO
    
class userMsg(object):
    def get_object(self,msg_tree):
        root = msg_tree.getroot()
        self.to_user_name = root[0].text
        self.from_user = root[1].text
        self.create_time = root[2].text
        self.msg_type = root[3].text
        self.content = root[4].text
        self.msg_id = root[5].text
        del self.msg_tree,root
    def __init__(self,xml_strs):
        '''传入一个xml字符串来初始化类，自动生成一个文档树，
        并调用get_object函数获得一个包含消息各个属性的对象'''
        xml_file = StringIO.StringIO(xml_strs)
        self.msg_tree = ET.ElementTree(file=xml_file)
        self.get_object(self.msg_tree)
    
def main():
    xml_data = '''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName> 
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[this is a test]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>
'''  
    xml_eg = userMsg(xml_data)
    print 'user name is '+xml_eg.to_user_name
if __name__ == '__main__':
    main()
 