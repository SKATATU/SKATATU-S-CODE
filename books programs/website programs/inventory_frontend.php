<!DOCTYPE html>
  <html>
  <head>
      <title>Inventory Data</title>
      table, th, td {
      border: 1px solid black;
    }
  </head>
  <body>
      <h1>Inventory Data</h1>
      <?php
      $file = 'inventory.txt';
      $inventoryData = file($file, FILE_IGNORE_NEW_LINES);//Omit newline at the end of each array element 
      if (!empty($inventoryData)) {
          echo '<table>'; // print table at the front end
          echo '<tr><th colspan=3>Inventory Data</th> </tr>'; // the title of the table = "Inventory Data"
          echo '<tr><th>Product</th><th>Quantity</th><th>Price</th></tr>'; // cells of the table

          foreach ($inventoryData as $line) {
              $fields = explode(',', $line); 
              //$product = isset($fields[0]) ? trim($fields[0]) : '';
              $product = trim($fields[0]) ;
              $quantity = trim($fields[1]) ;
              $price = trim($fields[2]) ;
              echo '<tr>';
              echo '<td>'.$product.'</td>';
              echo '<td>'.$quantity.'</td>';
              echo '<td>'.'$'.$price.'</td>';
              echo '</tr>';
          }

          echo '</table>';
      } else {
          echo 'No inventory data available.';
      }
      ?>
  </body>
  </html>



