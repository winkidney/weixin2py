<?php
error_reporting ( E_ALL & ~ E_NOTICE );
date_default_timezone_set ( "Asia/Shanghai" );

require_once 'weixin.class.php';

define ( 'TOKEN', '123456' ); // 微信公众平台自定义接口处设置的 Token
define ( 'DEBUG', false ); // 是否调试模式 true/false (开启调试将会把收发的信息写入文件)
define ( 'LOGPATH', './logPath/' ); // 日志目录
define ( 'PICTURES', false ); // 是否本地保存图片 true/false (开启将会本地保存用户发送图片)

$weixin = new weixin ( TOKEN, DEBUG, LOGPATH, PICTURES );
$weixin->valid ();
$weixin->getMsg ();
$type = $weixin->msgtype;
$weihu = 1;    //0为维护，1为开放
$domain = 'http://upupyoyoyo.net/COFFdD0xMzY4NzEzMTI3Jmk9MjE5LjEzOC4yMDkuNzEmdT1Tb25ncy92Mi9mYWludFFDLzVjLzMzLzUwMTE2MmVlODA5ZWM3ZDFmOWY3ZmE3MDlhZjQzMzVjLm1wMyZtPWE4ZDFlZjllZjI2YzdhZTEyYTRkZjBiZDBjZWY3MThiJnY9ZG93biZuPbjpx7Mmcz3W3L3cwtcmcD1z.mp3';
$filename = ( string ) end ( explode ( '/', $_SERVER ['SCRIPT_NAME'] ) );
$strURL = $domain . str_replace ( $filename, '', $_SERVER ['SCRIPT_NAME'] );
if($weihu == 0){
  //维护功能
  //$note = '服务器维护，请稍后查询,预计维护时间：00：00-11：00，如果无聊呢，可以去调戏一下小机器人 彼小岸，翻版小黄鸡，各种无压力！微信号：hbmzxymryp 
  //更多精彩，尽在彼岸！
  //.bi-anbbs.com';
  $note = '服务器TMD又发生故障了，正在维护,实在抱歉！对不起！ [委屈]';
}
  else
if($type === 'event'){
  $note = '欢迎关注彼岸社区微信公众平台，你可以选择一些服务:
        1.发送‘@学号@密码@年份@学期’可以查询成绩(1为上学期，0为下学期)例如：@011140101@111111@2013@0；
		2.发送‘@1@楼栋号@寝室号’可以查询所剩电量，例如：@1@1@101；
		3.发送‘@2@楼栋号@寝室号’可以查询缴费历史记录，例如：@2@1@101；
		--------
		回复help获取帮助；
		科院学号开头大写K，查询语句中请不要留空格；
		字符串中@号为输入英文状态下@号；
		因学校服务器经常抽风，导致功能时而不可用，请见谅！'
    	;
}
else if ($type === 'text') {
	if($weixin->msg ['Content']==='help'||$weixin->msg ['Content']==='HELP'){
  $note = '
		1.发送‘@学号@密码@年份@学期’可以查询成绩(1为上学期，0为下学期)（本学期为2013@0）；
		2.发送‘@1@楼栋号@寝室号’可以查询所剩电量；
		3.发送‘@2@楼栋号@寝室号’可以查询缴费历史记录；
		-------------
		更多功能敬请期待！
		因学校服务器经常抽风，导致功能时而不可用，请见谅！
		-------------
		各种问题：
		1.系统返回一条空语句，说明：学号或密码错误，或者学期选择错误。
		2.系统无任何返回，说明：学校的服务器抽风了，请等一会后重新发送。
		3.科院学号开头大写K，查询语句中请不要留空格。
		-------------
		因为有你，所以彼岸-www.bi-anbbs.com';
}
  else if ($weixin->msg ['Content'] == '1') {
		// 用户发送"音乐"时回复音乐信息
		$note = '请输入你的学号密码(格式如@学号@密码@年份@学期)注：0为春季学期，1为秋季学期';
	}
  else if ($weixin->msg ['Content'] == '2') {
		// 用户发送"音乐"时回复音乐信息
		$note = '请输入功能代码、楼栋号、寝室号(格式如@1@楼栋号@寝室号)';
	}
  else if($weixin->msg ['Content'] == '3'){
  $note='www.baidu.com';
  }
  else if(preg_match("/@(\d{9})@(.*)@(\d{4})@(\d{1})/i", $weixin->msg ['Content'],$match)){
      $note=file_get_contents("http://jackdowosn.gnway.net:81/mysearch/index.php?id=".$match[1]."&password=".$match[2]."&year=".$match[3]."&term=".$match[4]);
	}
  else if(preg_match("/@(.{10})@(.*)@(\d{4})@(\d{1})/i", $weixin->msg ['Content'],$match)&&preg_match("/K/",$match[1][0],$matches)){
	  $note=file_get_contents("http://jackdowosn.gnway.net:81/mysearch/index3.php?id=".$match[1]."&password=".$match[2]."&year=".$match[3]."&term=".$match[4]);
  }
  else if(preg_match("/@(\d)@(.*)@(.*)/", $weixin->msg ['Content'],$match)&&($match[1]=='1')){
  $note='亲，你们寝室还有'.file_get_contents("http://jackdowosn.gnway.net:81/mysearch/index1.php?loudong=".$match[2]."&fangjian=".$match[3]).'度电哦！';
  }
  else if(preg_match("/@(\d)@(.*)@(.*)/", $weixin->msg ['Content'],$match)&&($match[1]=='2')){
  $note=file_get_contents("http://jackdowosn.gnway.net:81/mysearch/index2.php?loudong=".$match[2]."&fangjian=".$match[3]);
  }
    else if ($weixin->msg['Content']=='音乐') {
		//用户发送"音乐"时回复音乐信息
		$note =  array(
				'type' => 'music',
				'title' => '生日快乐',//音乐标题
				'description' => '祝您生日快乐',//音乐简介
				'musicurl' => $domain,//音乐链接地址
				'hqmusicurl' => $domain.'/mp3/Happy-Birthday.mp3',//高质量音乐链接，WIFI环境优先使用该链接播放音乐
				'url' => $domain);
	}else{
    $note = '1.发送‘@学号@密码@年份@学期’可以查询成绩(1为上学期，0为下学期)（本学期为2013@0）；
		2.发送‘@1@楼栋号@寝室号’可以查询所剩电量；
		3.发送‘@2@楼栋号@寝室号’可以查询缴费历史记录；
		-------------
		更多功能敬请期待！
		因学校服务器经常抽风，导致功能时而不可用，请见谅！
		-------------
		各种问题：
		1.系统返回一条空语句，说明：学号或密码错误，或者学期选择错误。
		2.系统无任何返回，说明：学校的服务器抽风了，请等一会后重新发送。
		3.科院学号开头大写K，查询语句中请不要留空格。
		-------------
		因为有你，所以彼岸-www.bi-anbbs.com';
    }
}

// 处理结果
$reply = $weixin->makeEter ( $note );
// 输出
$weixin->reply ( $reply );
?>