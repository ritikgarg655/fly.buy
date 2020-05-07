<?php 
    exec('\usr\bin\python3 C:\xampp\htdocs\main.py' , $mystring);
    var_dump($mystring);
    if(!$mystring){
 
         echo "python exec failed";
             }
    else{
    echo "<br />";
    echo "successfully executed!";}
?>