<html>
  <!--
    Exercise:
    - Write a PHP program and use variables like price[], sum, average, bookname to echo the following on a web page.
    The average price is $30/5, which is $6.
    The name of the book is 'The Galaxy'.

  -->
  
  <head>
    <title>Exercise 001</title>
  </head>
  <body>
    <?php  $price = 30;
    $average = $price /5;
    $bookname = 'The Galaxy';
    
    echo 
      "<p>The average price is $30/5, which is $$average.<br>
      The name of the book is '$bookname'.</p>
      "; ?> 


  <script src="https://replit.com/public/js/replit-badge-v2.js" theme="dark" position="bottom-right"></script>
  </body>
</html>