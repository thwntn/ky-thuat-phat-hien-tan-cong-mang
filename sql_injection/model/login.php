<?php
    $conn = new MySQLi('localhost', 'root', '', 'data');

    $userName = $_POST['username'];
    $password = $_POST['password'];
    if(isset($_POST['username']) && isset($_POST['password'])){
        $query = 'SELECT * FROM userdata WHERE username = '.$userName.' AND password = '.$password;
    }
    $exec = $conn -> query($query);
    $result = $exec -> fetch_assoc();
    if($result == null) {
        echo "Faild!!";
    }
    else echo "Loggin Success!";
?>