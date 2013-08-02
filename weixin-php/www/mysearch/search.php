<?php
function search($year, $term, $ch) {
	$curlPost = "configData.openYear=$year&configData.openTerm=$term";
	curl_setopt ( $ch, CURLOPT_URL, 'http://211.67.32.144/edu/gradeEnteringStudent!getAllGradeEnter.action' );
	curl_setopt ( $ch, CURLOPT_HEADER, 0 );
	curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );
	curl_setopt ( $ch, CURLOPT_POST, 1 );
	curl_setopt ( $ch, CURLOPT_POSTFIELDS, $curlPost );
	curl_setopt ( $ch, CURLOPT_COOKIEFILE, $cookiejar ); // 要回传cookie
	$data = curl_exec ( $ch );
	curl_close ( $ch );
	preg_match_all ( '/\<tr style.*?\<\/td\>\s*\<td\>(.*?)\<\/td\>\s*\<td\>(.*?)\<\/td\>/is', $data, $matches );
	foreach ( $matches [1] as $key => $val )
		$nav =$nav ."\n". $val . "---" . $matches [2] [$key];
	return $nav;
}
function search1($loudong, $fangjian, $ch) {
	$curlPost = "loudong=$loudong&fangjian=$fangjian&action=+%CC%E1++%BD%BB+";
	curl_setopt ( $ch, CURLOPT_URL, 'http://211.67.32.161/chenweb/..%5Cdbpool%5Cindex_jhxmeter.jsp' );
	curl_setopt ( $ch, CURLOPT_HEADER, 0 );
	curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );
	curl_setopt ( $ch, CURLOPT_POST, 1 );
	curl_setopt ( $ch, CURLOPT_POSTFIELDS, $curlPost );
	curl_setopt ( $ch, CURLOPT_COOKIEFILE, $cookiejar ); // 要回传cookie
	$data = curl_exec ( $ch );
	curl_close ( $ch );
	$data = mb_convert_encoding ( $data, "utf-8", "gb2312" );
	preg_match_all ( '/\>(\-?\d+\.\d+)\<\/font\>/i', $data, $matches );
	return $matches [1] [0];
}
function search2($loudong, $fangjian, $ch) {
	$curlPost = "loudong=$loudong&fangjian=$fangjian&action=+%CC%E1++%BD%BB+";
	curl_setopt ( $ch, CURLOPT_URL, 'http://211.67.32.161/chenweb/..%5Cdbpool2%5Cindex_shuidian.jsp' );
	curl_setopt ( $ch, CURLOPT_HEADER, 0 );
	curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );
	curl_setopt ( $ch, CURLOPT_POST, 1 );
	curl_setopt ( $ch, CURLOPT_POSTFIELDS, $curlPost );
	curl_setopt ( $ch, CURLOPT_COOKIEFILE, $cookiejar ); // 要回传cookie
	$data = curl_exec ( $ch );
	curl_close ( $ch );
	$data = mb_convert_encoding ( $data, "utf-8", "gb2312" );
	preg_match_all ( '/\<tr\>\s*\<td.*\>\&nbsp\;(.*)    \&nbsp\;\<\/font\>\s*\<\/td\>\s*.*\s*\/td\>\s*\<td.*\'\>\&nbsp\;(.*)\&nbsp\;\<\/font\>\s*\<\/td\>\s*\<td.*\>\&nbsp\;(.*)\&nbsp\;\<\/font\>\s*\<\/td\>\s*.*\s*<\/tr\>/i', $data, $matches );
	foreach ( $matches [1] as $key => $val )
		$nav = $nav ."\n".$val . "在" . $matches [3] [$key].'的时候充了'.$matches [2] [$key].'块钱!';
	return $nav;
}
?>