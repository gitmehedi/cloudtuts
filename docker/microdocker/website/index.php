<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Shop</title>
</head>
<body>
<h1>My Shop</h1>
  <ul>
    <?php
        $json = file_get_contents('http://product-service');
        $obj = json_decode($json);
        $products = $obj->product;
        foreach($products as $product){
           echo "<li>$product</li>";
        }
     ?>
</body>
</html>