
<?php
echo '<p>Hello World</p>';
$mysqli = new mysqli("localhost", "testingg", "testingg", "guarddb");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
//echo $mysqli->host_info . "\n";

$mysqli = new mysqli("127.0.0.1", "testingg", "testingg", "guarddb", 3306);
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

//echo $mysqli->host_info . "\n";

mysqli_query($mysqli,"INSERT INTO plants (PlantID, DisplayName, LatinScientificName, Picture)
VALUES ('1','$_POST[commonname]','$_POST[genus]','$_POST[picture]')");

mysqli_close($mysqli);

echo '<br/><a href="add_plants_form.php">Add more plants</a>';
echo '<p>Bye World</p>';
?>
