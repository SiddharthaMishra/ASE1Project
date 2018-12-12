<!DOCTYPE html>
<?php
  session_start();    
  ini_set('display_errors',1);  error_reporting(E_ALL);
  include("config.php");
  include('rememberme.php');
  if(!isset($_SESSION['login_user']))
        rememberMe();
  $myusername=$_SESSION['login_user'];
  function DisplayUserInfo(){
  $sql="Select * from users where username='$myusername';";
  $result=pg_query($sql);
  $row=pg_fetch_assoc($result);
  function createTable1(){
  $query="Select * from allscores where username=$myusername order by score desc;";
  $resulttable=pg_query($query);
  $rank=1;
  while($rows=pg_fetch_assoc($resulttable))
  {
    echo "<tr><td> $rank </td><td>".$rows["gamenumber"]."</td><td>".$rows["score"]."</td></tr>;";
    $rank++;
  }
}
function createTable2(){
    $query2="Select * from allscores where username=$myusername order by gamenumber desc;";
    $rtable=pg_query($query2);
    $rank=1;
    while($rws=pg_fetch_assoc($rttable))
    {
      echo "<tr><td> $rank </td><td>".$rows["gamenumber"]."</td><td>".$rows["score"]."</td></tr>;";
      $rank++;
    }
  }
  /*while($row=pg_fetch_assoc($result))
  {
    echo "<h2>UserName  ".$row['username']."</h2><hr>
    <label>Profile Name:   ".$row[firstname]." ".$row[lastname]."</label>
    <span>Something</span><br><br>
    <label>Date Of Birth:</label>
    <span>Something</span><br><br>
    <label class="l1">Email:</label>
    <span class="s1">Something</span><br><br>
    <label class="l2">Registered On:</label>
    <span class="s2">Something</span><br><br><hr>";
  }*/
  }

      header("location: HOMEPAGE.php");
?>
<html>
<head>
  <title>About</title>
  <link rel="stylesheet" type="text/css" href="gradient.css">
  <link rel="stylesheet" type="text/css" href="homepage2.css" />
  <link rel="stylesheet" type="text/css" href="profile.css">
</head>
<body>
   <div id="homemenu">
      <a href="">HOME</a>
      <a href="">GAMES</a>
      <a href="">LEADERBOARD</a>
      <a href="">ABOUT US</a>
      <a href="">FEEDBACK</a>
   <img src="logo.gif">     
   </div> 

     <div id="homemenu2">
        <a href="login.php">Log In</a>    
        <a href="register.php">Register</a>
     </div>   

    <div id="profile">
      <a href="">Home</a><hr>
      <img src="8.png"><h2>UserName</h2><hr>
        <label>Profile Name:</label>
        <span><?php echo $row['firstname']." ".$row['lastname'];?></span><br><br>
        <label>Date Of Birth:</label>
        <span><?php echo $row[dob];?></span><br><br>
        <label class="l1">Email:</label>
        <span class="s1"><?php echo $row['email'];?></span><br><br>
        <label class="l2">Registered On:</label>
        <span class="s2"><?php echo $row['joindate']?></span><br><br><hr>
        
        <h3>Table 1</h3>
        <table>
          <tr>
            <th>S. No.</th>
            <th>Game Number</th>
            <th>Score</th>
          </tr>>
          <!--<tr>
            <td>something</td>
            <td>something</td>
            <td>something</td>
          </tr>          
          <tr>
            <td>something</td>
            <td>something</td>
            <td>something</td>
          </tr>-->
          <?php createTable1(); ?>     
        </table><br>
        <hr>
        <h3>Table 2</h3>
        <table>
          <tr>
            <th>S. No</th>
            <th>Game Number</th>
            <th>Score</th>
          </tr>
          <?php createTable2(); ?>      
        </table>                
    </div> 
</body>
</html>