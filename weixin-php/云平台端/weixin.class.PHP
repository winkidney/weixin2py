<?php
/**
 *  微信 公众平台消息接口改进型 SDK DEMO
 *  @author zuohome admin@zuohome.com/QQ:305612992
 *  修改自  xhxu xh_xu@qq.com/QQ:7844577 1.0.20130103 版本
 *  @version 2.0.20130305
 */
class Weixin {
	public $token = '';
	public $debug = false;
	public $pictures = false;
	public $flag = false;
	public $msgtype = 'text'; // ('text','image','location','voice')
	public $msg = array ();
	private $logPath = '';
	public function __construct($token, $debug, $log = './', $pictures) {
		$this->token = $token;
		$this->debug = $debug;
		$this->logPath = $log;
		$this->pictures = $pictures;
	}
  public function song($name) {
		$content2 = file_get_contents ( "http://shopcgi.qqmusic.qq.com/fcgi-bin/shopsearch.fcg?value=" . $name );
		$str2 = substr ( $content2, 15 );
		$str2 = substr ( $str2, 0, - 2 );
		$tempstrs = explode ( ",", $str2 );
		$endstr = array ();
		$i = 0;
		
		foreach ( $tempstrs as $tempstr ) {
			$endstr [$i] = str_replace ( ":", '":', $tempstr );
			if ($i != 0) {
				$endstr [$i] = '"' . $endstr [$i];
			}
			$i ++;
		}
		$endstr [0] = str_replace ( '{', '{"', $endstr [0] );
		$endstr [5] = str_replace ( '[{', '[{"', $endstr [5] );
		$str2 = implode ( ",", $endstr );
		$str2 = str_replace ( "[", "", $str2 );
		$str2 = str_replace ( "]", "", $str2 );
		$str2 = str_replace ( "\"{", "{\"", $str2 );
		$tempstrs = explode ( ",", $str2 );
		$tempstrs [5] = '"songlist1":{"idx":"1"';
		$i = 0;
		$x = 2;
		foreach ( $tempstrs as $json ) {
			$jsons [$i] = iconv ( 'gb2312', 'utf-8//IGNORE', $json );
			if (substr ( $json, 0, 8 ) == '{"idx":"') {
				$a = $i - 1;
				$jsons [$i] = iconv ( 'gb2312', 'utf-8//IGNORE', '"songlist' . $x . '":{"idx":"' . $x . '"' );
				$x ++;
			}
			$i ++;
		}
		$str = implode ( ",", $jsons );
		$result = json_decode ( $str, true );
		return $result;
	}
	public function getMsg() {
		$postStr = $GLOBALS ["HTTP_RAW_POST_DATA"];//相当于$_post[],但是这个函数所能接受的数据类型比$_post[]要多
		if ($this->debug) {//验证是否要调试
			if (! file_exists ( $this->logPath )) {//检查文件是否存在
				mkdir ( $this->logPath, 0777 );//条件为假则新建文件夹并规定访问权限
			}
			file_put_contents ( $this->logPath . 'log.txt', date ( 'c' ) . "\n" . $postStr . "\n", FILE_APPEND );//无论条件是否为真都要向文件中写入数据
		}
		if (! empty ( $postStr )) {//判断接收的值是否为空，真
			$this->msg = ( array ) simplexml_load_string ( $postStr, 'SimpleXMLElement', LIBXML_NOCDATA );//将接收到的xml数据强制转换成数组
			$this->msgtype = strtolower ( $this->msg ['MsgType'] );//将微信服务器传送过来的消息类型转换成小写并赋给成员属性
		}
		if ($this->msg ['MsgType'] === 'image') {
			if ($this->pictures) {
				$this->msg ['PicUrl'] = self::getImg ( $this->msg ['PicUrl'] );//调用本类中的getImg函数
			}
		}
	}
	function getImg($url) {//如果用户发送的是图片则处理用户发送的图片图片消息
		$header = file_get_contents ( $url, 0, NULL, 0, 5 );//将$url读入一个字符串中
		// return $header;
		if ($header {0} . $header {1} == "\x89\x50") {//判断图片的后缀名
			$ext = '.png';
			$imgtype = 'png';
		} else if ($header {0} . $header {1} == "\xff\xd8") {
			$ext = '.jpg';
			$imgtype = 'jpeg';
		} else if ($header {0} . $header {1} . $header {2} == "\x47\x49\x46") {
			
			if ($header {4} == "\x37") {
				$ext = '.gif';
				$imgtype = 'gif87';
			} else if ($header {4} == "\x39") {
				$ext = '.gif';
				$imgtype = 'gif89';
			}
		} else {
			return $url; // 不是图片不处理
		}
		$category = 'user/';
		if (! file_exists ( $category )) {
			mkdir ( $category, 0777 );
		}
		$category .= date ( "Ym" );//格式化时间年月
		if (! file_exists ( $category )) {
			mkdir ( $category, 0777 );
		}
		$filename = $category . '/' . date ( "dgis" ) . $ext;//要重命名的文件的名字，以时间命名
		$hander = curl_init ();
		$fp = fopen ( $filename, 'wb' );
		curl_setopt ( $hander, CURLOPT_URL, $url );//图片发往的地址
		curl_setopt ( $hander, CURLOPT_FILE, $fp );//发送的文件
		curl_setopt ( $hander, CURLOPT_HEADER, 0 );
		curl_setopt ( $hander, CURLOPT_FOLLOWLOCATION, 1 );
		// curl_setopt($hander,CURLOPT_RETURNTRANSFER,false);//以数据流的方式返回数据,当为false是直接显示出来
		curl_setopt ( $hander, CURLOPT_TIMEOUT, 60 );
		curl_exec ( $hander );
		curl_close ( $hander );
		fclose ( $fp );
		$domain = 'http://' . $_SERVER ['HTTP_HOST'];//主机地址
		$filenames = ( string ) end ( explode ( '/', $_SERVER ['SCRIPT_NAME'] ) );//从域名中剥离出文件名
		$strURL = $domain . str_replace ( $filenames, '', $_SERVER ['SCRIPT_NAME'] );//取出文件名后格式化域名
		return $strURL . $filename;
	}
	public function makeEter($paraEeter = array()) {
		$CreateTime = time ();
		if ($paraEeter ['type']) {//判断参数类型
			$type = $paraEeter ['type'];
		} else {
			$type = 'text';
		}
		$flag = $paraEeter ['flag'] ? 1 : 0;
		if (is_array ( $paraEeter )) {//检测$paraEeter是否为数组
			if ($type === 'text') {
				$Content = "<Content><![CDATA[{$paraEeter['Content']}]]></Content>";
			} else if ($type === 'music') {
				$Content = "<Music>
				<Title><![CDATA[{$paraEeter['title']}]]></Title>
				<Description><![CDATA[{$paraEeter['description']}]]></Description>
				<MusicUrl><![CDATA[{$paraEeter['musicurl']}]]></MusicUrl>
				<HQMusicUrl><![CDATA[{$paraEeter['hqmusicurl']}]]></HQMusicUrl>
				</Music>";
			} else if ($type === 'news') {//图文消息
				$itemsCount = count ( $paraEeter ['items'] );//消息的条数
				$itemsCount = $itemsCount < 10 ? $itemsCount : 10;//限制消息在十条以内
				$newTplHeader = "<ArticleCount>{$itemsCount}</ArticleCount>
		<Articles>";
				$newTplItem = "<item>
			<Title><![CDATA[%s]]></Title>
			<Description><![CDATA[%s]]></Description>
			<PicUrl><![CDATA[%s]]></PicUrl>
			<Url><![CDATA[%s]]></Url>
			</item>";
				$newTplFoot = "</Articles>";
				$Content = '';
				if ($itemsCount) {
					foreach ( $paraEeter ['items'] as $key => $item ) {
						if ($key <= 9) {
							$Content .= sprintf ( $newTplItem, $item ['title'], $item ['description'], $item ['picurl'], $item ['url'] );
						}
					}
				}
				$Content = $newTplHeader . $Content . $newTplFoot;
			}
		} else {
			$type = 'text';
			$Content = "<Content><![CDATA[$paraEeter]]></Content>";
		}
		$header = "<xml>
<ToUserName><![CDATA[{$this->msg['FromUserName']}]]></ToUserName>
<FromUserName><![CDATA[{$this->msg['ToUserName']}]]></FromUserName>
<CreateTime>{$CreateTime}</CreateTime>
<MsgType><![CDATA[{$type}]]></MsgType>
";
		$footer =" 
<FuncFlag>{$flag}</FuncFlag>
	</xml>";
		return $header . $Content . $footer;
	}
	public function reply($data) {
		if ($this->debug) {
			file_put_contents ( $this->logPath . 'reply.txt', date ( 'c' ) . "\n" . $data . "\n", FILE_APPEND );
		}
		echo $data;
	}
	public function valid() {
		if ($this->checkSignature ()) {//验证签名
			if ($_SERVER ['REQUEST_METHOD'] == 'GET') {
				echo $_GET ['echostr'];
				exit ();
			}
		}//签名非空
		 else {
			file_put_contents ( $this->logPath . 'log.txt', date ( 'c' ) . '非法数据请求 ip:' . $_SERVER ["REMOTE_ADDR"] . "\n", FILE_APPEND );
			// echo '非法请求';
			header ( $_SERVER ['SERVER_PROTOCOL'] . ' 403 Forbidden' );
			exit ();
		}//签名为空
	}
	private function checkSignature() {
		$signature = $_GET ["signature"];
		$timestamp = $_GET ["timestamp"];
		$nonce = $_GET ["nonce"];
		
		$tmpArr = array (
				$this->token,
				$timestamp,
				$nonce 
		);
		sort ( $tmpArr );
		$tmpStr = implode ( $tmpArr );
		$tmpStr = sha1 ( $tmpStr );
		
		if ($tmpStr == $signature) {
			return true;
		} else {
			return false;
		}
	}
}
?>