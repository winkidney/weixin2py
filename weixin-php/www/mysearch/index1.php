<?php
header ( "content-Type: text/html; charset=gbk" );
require_once 'search.php';
$loudong=$_GET['loudong'];
$fangjian=$_GET['fangjian'];
$ch = curl_init ();
echo search1($loudong,$fangjian,$ch);
?>