<?php
    $conn = new MySQLi('localhost', 'root', '', 'data');

    if(isset($_POST['username']) && isset($_POST['password'])){
        $query = "SELECT * FROM userdata WHERE username='". $_POST['username'] . "' AND password = '" .$_POST['password'] ."'";
    }

    $exec = $conn -> query($query);
    $result = $exec -> fetch_assoc()

    print_r($result);
?>