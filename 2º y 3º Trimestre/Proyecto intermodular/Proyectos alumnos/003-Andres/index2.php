<!doctype>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        #ruleta {
            animation: frena 10s;
        }

        @keyframes frena {
            0% {
                transform: rotate(0deg);
            }

            100% {
                transform: rotate(359deg);
            }
        }
    </style>
</head>

<body>
    <img id="ruleta" src="ruleta.jpg">
</body>

</html>