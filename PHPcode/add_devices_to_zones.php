<!DOCTYPE HTML>
<html>
<body>

<!-- check if the user is logged in before showing this page -->

<form action="add_devices_db.php" method="post">
Zone Number: <input type="text" name="zoneid" type="hidden">
Zone Name: <input type="text" name="commonname"><br>
Sensor 1: <input type="text" name="sensor1"><br>
Sensor 1 location: <input type="text" name="sensor1location"><br>
Sensor 1 type: <input type="text" name="sensor1type"><br>
Sensor 2: <input type="text" name="sensor2"><br/>
Sensor 2 location: <input type="text" name="sensor2location"><br>
Sensor 2 type: <input type="text" name="sensor2type"><br/>
Sprinkler 1: <input type="text" name="microcontroller1locatioin"><br>
Sprinkler 1 location: <input type="text" name="microcontroller1location"><br>
Sprinkler 2: <input type="text" name="microcontroller2"><br>
Sprinkler 2 location: <input type="text" name="microcontroller2location"><br>
<input type="submit" value="Add Devices">
</form>



</body>
</html>
