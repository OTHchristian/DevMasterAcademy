<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .all{
            border: width 1px;
            border-style:solid;
            border-color:black;
        }
        .background{
            margin-top:25%;
            margin-left:40%;
            width: 200px;
            height:60PX;
            border-radius:60px;
            padding:4px;
            transition:0.8s;
            background-color:black;
        }
        .button{
            width: 60px;
            height:56px;
            border-radius:50px;
            transition:0.8s;
            background-color:white;
        }
        .move{
            transition:0.8s;
            
        }
    </style>
</head>
<body>
    <div class="all background" id="prpGood">
        <div class="move" id="forMove"><div class="all button" id='btn'></div></div>
    </div>
    <script src="togglebutton.js"></script>
</body>
</html>