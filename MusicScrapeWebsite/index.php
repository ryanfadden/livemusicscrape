<!DOCTYPE html>
<?php
  include_once 'includes/dbh.inc.php';
?>

<html lang="en">
<head>
  <!-- <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
   -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" 
  integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
  
  <title>Document</title>
</head>
<body>

<table class="table table-striped">
    <thead>
      <tr>
        <th>Artist</th>
        <th>Date</th>
        <th>Time</th>
        <th>Location</th>
      </tr>
    </thead>
    <tbody>
      <?php
        
    $sql = "SELECT * FROM BandInfo;";
    $result = $conn->query($sql);
  
    while($row = $result->fetch_assoc()) {
      echo "<tr>
        <td>" . $row["Artist"] . "</td>
        <td>" . $row["Date"] . "</td>
        <td>" . $row["Time"] . "</td>
        <td>" . $row["Time"] . "</td>
        </tr>";
    }
  ?>
    </tbody>
  </table>


<br>
<br>
<br>
<br>
<br>





</body>
</html>