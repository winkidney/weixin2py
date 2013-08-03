#coding:utf-8
#in folder 'tools'
#read xml text and return a xml object
import xml.dom.minidom
class msgFromUser(object):
    def __init__(xml_strs):
        self.msg = xml.dom.minidom.parse(xml_strs)
        self.to_user_name = msg.getElementsByTagName('ToUserName')
        self.from_user = msg.getElementsByTagName('FromUserName')
        self.create_time = msg.getElementsByTagName('CreateTime')
        self.msg_type = msg.getElementsByTagName('MsgTpye')
        self.content = msg.getElementsByTagName('Content')
        self.msg_id = msg.getElementsByTagName('MsgId')
def main():
    xml_data = '''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName> 
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[this is a test]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>'''  
    xml_eg = msgFromUser(xml_data)
    print xml_eg
if __name__ == '__main__':
    main()
 