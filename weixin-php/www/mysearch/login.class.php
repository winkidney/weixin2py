<?php
function postid_password($id,$password,$year,$term,$ch){
	$login_url = "http://jackdowson.linkpc.net:81/mysearch/index.php";
	$curlPost = "id=$id&password=$password&year=$year&term=$term";
	curl_setopt ( $ch, CURLOPT_URL, $login_url );
	// 启用时会将头文件的信息作为数据流输出
	curl_setopt ( $ch, CURLOPT_HEADER, 0 );
	curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );
	curl_setopt ( $ch, CURLOPT_POST, 1 );
	curl_setopt ( $ch, CURLOPT_POSTFIELDS, $curlPost );
	return curl_exec ( $ch );
}
?> 