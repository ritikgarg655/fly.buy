
<html>
<body>
    
<?php
// File to connect seller web to mysql database : search_shop , username: root , password: ''
require_once "pdo.php";

if (!empty($_POST['shopname']) && !empty($_POST['shop_address']) && !empty($_POST['price']) && !empty($_POST['specifications'])){
    var_dump($_POST);
    echo("yes");
}
else{
    var_dump($_POST);
    echo("no");
}
?>
</html>
</body>