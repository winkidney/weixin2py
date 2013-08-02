<?php
header ( "content-Type: text/html; charset=utf-8" );
 //require_once 'search.php';
// 第一步:提交数据,生成cookie,将cookie保存在临时目录下
$cookiejar = realpath ( 'cookie.txt' );
$id=$_GET['id'];
$password=$_GET['password'];
$year=$_GET['year'];
$term=$_GET['term'];
exchange(&$year, &$term);
function exchange($year,$term){
	if($term=='0')
	{
		$years=$year-1;
		$year=$years.'-'.$year;
		$term=2;
	}
	else if($term=='1')
	{
		$years=$year+1;
		$year=$year.'-'.$years;
	}
	
}
$ch = curl_init ();
$login_url = "http://211.67.32.51/default3.aspx";
$curlPost = "__VIEWSTATE=dDw5NTI3MzM0NTQ7dDw7bDxpPDE%2BO2k8NT47PjtsPHQ8O2w8aTw4PjtpPDExPjs%2BO2w8dDxwPDtwPGw8b25jbGljazs%2BO2w8d2luZG93LmNsb3NlKClcOzs%2BPj47Oz47dDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjs7Pjs%2BPjt0PHA8bDxWaXNpYmxlOz47bDxvPGY%2BOz4%2BOzs%2BOz4%2BO2w8aW1nREw7aW1nVEM7aW1nUU1NOz4%2BiyfPvg3FujyU8xX773LO%2FCbCuTw%3D&tbYHM=$id&tbPSW=$password&ddlSF=学生&imgDL.x=40&imgDL.y=7";
$curlPost = iconv("UTF-8", "GBK", $curlPost);
curl_setopt ( $ch, CURLOPT_URL, $login_url );
// 启用时会将头文件的信息作为数据流输出
curl_setopt ( $ch, CURLOPT_PROXY, 'jackdowosn.gnway.net:81');
curl_setopt ( $ch, CURLOPT_HEADER, 0 );
curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1) Gecko/20061204 Firefox/4");
curl_setopt($ch,CURLOPT_FOLLOWLOCATION,true);
curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );
curl_setopt ( $ch, CURLOPT_REFERER, 'http://211.67.32.51/' );
curl_setopt ( $ch, CURLOPT_POST, 1 );
curl_setopt ( $ch, CURLOPT_POSTFIELDS, $curlPost );
// 设置连接结束后保存cookie信息的文件
curl_setopt ( $ch, CURLOPT_COOKIEJAR, $cookiejar );
$data=curl_exec ( $ch );
//$data = mb_convert_encoding ( $data, "utf-8", "GBK" );
//echo '<xmp>'.$data.'</xmp>';
$curlPost = "xh=$id";
$curlPost = iconv("UTF-8", "GBK", $curlPost);
curl_setopt ( $ch, CURLOPT_URL, "http://211.67.32.51/xscj.aspx?xh=$id" );
// 启用时会将头文件的信息作为数据流输出
curl_setopt ( $ch, CURLOPT_PROXY, 'jackdowosn.gnway.net:81');
curl_setopt ( $ch, CURLOPT_HEADER, 0 );
curl_setopt ( $ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1) Gecko/20061204 Firefox/4");
curl_setopt ( $ch, CURLOPT_FOLLOWLOCATION,true);
curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );
curl_setopt ( $ch, CURLOPT_REFERER, 'http://211.67.32.51/xsleft.aspx?flag=xxcx' );
curl_setopt ( $ch, CURLOPT_POST, 0 );
curl_setopt ( $ch, CURLOPT_POSTFIELDS, $curlPost );
// 设置连接结束后保存cookie信息的文件
//curl_setopt ( $ch,  CURLOPT_COOKIEJAR, $cookiejar );
$data=curl_exec ( $ch );
$data = mb_convert_encoding ( $data, "utf-8", "GBK" );
//preg_match_all ( '/\<input\s+.*?__VIEWSTATE.*?value="(.*)"\s+\/\>/i', $data, $matches );
//上面的模式修正符不能加s
$pp="/\<td\>$year\<\/td\>\<td\>$term\<\/td\>\<td\>(.*)\<\/td\>\<td\>.*\<\/td\>\<td\>.*\<\/td\>\<td\>.*\<\/td\>\<td\>.*&nbsp;\<\/td\>\<td\>(.*)\<\/td\>\<td\>(.*)\<\/td\>\<td\>.*\<\/td\>(\<td\>&nbsp;\<\/td\>){3}/i";
preg_match_all ($pp, $data, $matches );
//file_put_contents("d://value.txt",$matches[1][0]);
//echo var_dump($matches)."<br/>";
//echo   '<xmp>'.$matches[1][1].'</xmp>';
foreach ( $matches [1] as $key => $val )
	$nav =$nav ."\n". $val . "---" . $matches [2] [$key]."---" . $matches [3] [$key];
echo $nav;
//echo search3($id,$year, $term,$ch,$matches[1][0]);
?>
