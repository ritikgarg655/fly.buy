<?php 

require_once "pdo.php";

if (!empty($_POST['name1']) && !empty($_POST['mob_num']) && !empty($_POST['shopname']) && !empty($_POST['add']) && !empty($_POST['email']) && !empty($_POST['pass']) && !empty($_POST['lic'])){
    echo("Signed up successfully.");
    # $sql = 'SELECT emp_id, emp_name, emp_salary FROM employee';
    $sql = "INSERT INTO `sellercredentials` (`sellername`, `shopname`, `phonenum`, `locationofshop`, `email`, `pass`, `licnum`) VALUES (:name1, :shopname, :mob_num, :add, :email, :pass, :lic )";
    echo "New profile created successfully";
    
    $stmt = $pdo->prepare($sql);
    $stmt->execute(array(
        ':email' => $_POST['email'],
        ':name1' => $_POST['name1'],
        ':shopname' => $_POST['shopname'],
        ':mob_num' => $_POST['mob_num'],
        ':add' => $_POST['add'],
        ':lic' => $_POST['lic'], 
        ':pass' => $_POST['pass']));
    $stmt = $pdo->query("SELECT * FROM sellercredentials WHERE licnum = ".$_POST['lic']."");
    echo $_POST['lic'];
    // $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
    // var_dump($rows);

    $last_id = $pdo->lastInsertId();
    echo "New record created successfully. Last inserted ID is: " . $last_id;
    $sql = "select * where last_id = $last_id";
    
}
else{
    //var_dump($_POST);
    echo("Invalid entry");
}


?>