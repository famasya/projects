<?php
//definisi username dan password
$servername = "localhost";
$username = "1303131018";
$password = "1303131018";
$db = "1303131018";

//membuat koneksi
$conn = mysql_connect($servername, $username, $password);
$conn = mysql_select_db($db,$conn);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

//jika dapat parameter HTTP GET
if(isset($_GET)){
  //ambil dari variabel URL "pulsa"
  $pulsa = $_GET['pulsa'];

  //ambil pulsa terakhir
  $latest = mysql_query("SELECT pulsa  FROM sisapulsa ORDER BY id DESC") or die(mysql_error());
  $latestpulsa = mysql_fetch_array($latest)[0]-$_GET['pulsa'];

  //masukkan data baru pulsa terakhir dikurangi variabel pulsa dari URL
  $q = mysql_query("INSERT INTO sisapulsa(pulsa) VALUES(".$latestpulsa.") ") or die(mysql_error());
  if($q){
    //tampilkan pulsa terakhir
    $sql = mysql_query("SELECT * FROM sisapulsa ORDER BY id DESC") or die(mysql_error());
    $f = mysql_fetch_assoc($sql);
    print $f['pulsa'];
  }
} else {
    //tampilkan pulsa terakhir
    $sql = mysql_query("SELECT * FROM sisapulsa ORDER BY id DESC") or die(mysql_error());
    $f = mysql_fetch_assoc($sql);
    print $f['pulsa'];
}
