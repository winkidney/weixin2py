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
    
class UserMsg(object):
    '''输入一个xml文本字符串对象，生成一个object并返回'''
    def get_text_msg(self,root):
        '''文本消息'''
        self.to_user_name = root[0].text
        self.from_user_name = root[1].text
        self.create_time = root[2].text
        self.msg_type = root[3].text
        self.content = root[4].text
        self.msg_id = root[5].text
        
    def get_img_msg(self,root):
        '''图片消息'''
        self.to_user_name = root[0].text
        self.from_user_name = root[1].text
        self.create_time = root[2].text
        self.msg_type = root[3].text
        self.pic_url = root[4].text
        self.msg_id = root[5].text
    def get_location_msg(self,root):
        '''地理位置消息'''
        self.to_user_name = root[0].text
        self.from_user_name = root[1].text
        self.create_time = root[2].text
        self.msg_type = root[3].text
        self.location_x = root[4].text
        self.location_y = root[5].text
        self.scale = root[6].text
        self.label = root[7].text
        self.msg_id = root[8].text
    def get_link_msg(self,root):
        '''链接消息推送'''
        self.to_user_name = root[0].text
        self.from_user_name = root[1].text
        self.create_time = root[2].text
        self.msg_type = root[3].text
        self.title = root[4].text
        self.description = root[5].text
        self.url = root[6].text
        self.msg_id = root[7].text
    def get_event_msg(self,root):
        '''事件推送'''
        self.to_user_name = root[0].text
        self.from_user_name = root[1].text
        self.create_time = root[2].text
        self.msg_type = root[3].text
        self.event = root[4].text
        self.event_key = root[5].text
        
    def __init__(self,xml_strs):
        '''传入一个xml字符串来初始化类，自动生成一个文档树，
        并调用get_object函数获得一个包含消息各个属性的对象'''
        xml_file = StringIO.StringIO(xml_strs)
        xml_tree = ET.ElementTree(file=xml_file)
        root = xml_tree.getroot()
        msgtype = xml_tree.find('MsgType').text
        if msgtype == 'text':
            self.get_text_msg(root)
        elif msgtype == 'image':
            self.get_img_msg(root)
        elif msgtype == 'location':
            self.get_location_msg(root)
        elif msgtype == 'link':
            self.get_link_msg(root)
        elif msgtype == 'event':
            self.get_event_msg(root)
            
#main函数仅供测试使用，模块直接导入即可使用，直接运行则输出有测试数据        
def main():
    xml_data=[]
    xml_data.append('''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName> 
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[这就是所谓的消息]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>
''')
    xml_data.append('''
 <xml>
 <ToUserName><![CDATA[toUser]]></ToUserName>
 <FromUserName><![CDATA[fromUser]]></FromUserName>
 <CreateTime>1348831860</CreateTime>
 <MsgType><![CDATA[image]]></MsgType>
 <PicUrl><![CDATA[this is a url]]></PicUrl>
 <MsgId>1234567890123456</MsgId>
 </xml>''')
    xml_data.append('''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1351776360</CreateTime>
<MsgType><![CDATA[location]]></MsgType>
<Location_X>23.134521</Location_X>
<Location_Y>113.358803</Location_Y>
<Scale>20</Scale>
<Label><![CDATA[位置信息]]></Label>
<MsgId>1234567890123456</MsgId>
</xml> ''')
    xml_data.append('''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1351776360</CreateTime>
<MsgType><![CDATA[link]]></MsgType>
<Title><![CDATA[公众平台官网链接]]></Title>
<Description><![CDATA[公众平台官网链接]]></Description>
<Url><![CDATA[url]]></Url>
<MsgId>1234567890123456</MsgId>
</xml> ''')
    xml_data.append('''
<xml><ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[FromUser]]></FromUserName>
<CreateTime>123456789</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[EVENT]]></Event>
<EventKey><![CDATA[EVENTKEY]]></EventKey>
</xml>''')
    for data in xml_data:
        user_msg = UserMsg(data)
        print user_msg.msg_type
if __name__ == '__main__':
    main()
 