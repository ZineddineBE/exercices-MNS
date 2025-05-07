<?php
$superglobal = $_SERVER;
?>
<style>
    thead,
    tfoot {
        background-color: #2c5e77;
        color: #fff;
    }

    tbody {
        background-color: #e4f0f5;
    }

    table {
        border-collapse: collapse;
        border: 2px solid rgb(140 140 140);
        font-family: sans-serif;
        font-size: 0.8rem;
        letter-spacing: 1px;
    }

    caption {
        caption-side: bottom;
        padding: 10px;
    }

    th,
    td {
        border: 1px solid rgb(160 160 160);
        padding: 8px 10px;
    }

    td {
        text-align: center;
    }
</style>



<h1><?= '$_SERVER'?></h1>

<table>
  <thead>
    <tr>
      <th scope="col">Key</th>
      <th scope="col">Value</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach ($superglobal as $key => $value) {?>

        <tr>
            <td><?= $key;?></td>
            <td><?= $value;?></td>
        </tr>
     <?php } ?>
  </tbody>
</table>



