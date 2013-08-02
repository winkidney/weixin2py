<?php
require_once 'login.class.php';

	$ch = curl_init ();
	$note = postid_password ( 031140107, 02185758 ,2012,1,$ch);
	echo $note;
?>