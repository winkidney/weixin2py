<?php
require_once 'login.class.php';
function loginprocess($id,$password,$year,$term) {
	$ch = curl_init ();
	$note = postid_password ( $id, $password ,$year,$term,$ch);
}
?>