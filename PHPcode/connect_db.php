
<?php
echo '<p>Hello World</p>';
$mysqli = new mysqli("localhost", "testingg", "testingg", "guarddb");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
echo $mysqli->host_info . "\n";

$mysqli = new mysqli("127.0.0.1", "testingg", "testingg", "guarddb", 3306);
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

echo $mysqli->host_info . "\n";

mysqli_query($mysqli,"INSERT INTO users (USERID, Email, Password, PrimarySerialNumber)
VALUES ('4','$_POST[emailaddress]','$_POST[password]','$_POST[serialnumber]')");

mysqli_close($mysqli);
echo '<p>Bye World</p>';
?>
