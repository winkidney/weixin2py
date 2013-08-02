<?php
header ( "content-Type: text/html; charset=utf-8" );
 require_once 'search.php';
// 第一步:提交数据,生成cookie,将cookie保存在临时目录下
$cookiejar = realpath ( 'cookie.txt' );
$id=$_GET['id'];
$password=$_GET['password'];
$year=$_GET['year'];
$term=$_GET['term'];
//echo $id.'-'.$password.'-'.$year.'-'.$term;
 $ch = curl_init ();
$login_url = "http://211.67.32.144/edu/login!checkLogin.action";
$curlPost = "user.roleId=2&user.account=$id&user.password=$password";
curl_setopt ( $ch, CURLOPT_URL, $login_url );
// 启用时会将头文件的信息作为数据流输出
curl_setopt ( $ch, CURLOPT_HEADER, 0 );
curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );
curl_setopt ( $ch, CURLOPT_POST, 1 );
curl_setopt ( $ch, CURLOPT_POSTFIELDS, $curlPost );
// 设置连接结束后保存cookie信息的文件
curl_setopt ( $ch, CURLOPT_COOKIEJAR, $cookiejar );
curl_exec ( $ch );
	echo search($year, $term,$ch);
?>
