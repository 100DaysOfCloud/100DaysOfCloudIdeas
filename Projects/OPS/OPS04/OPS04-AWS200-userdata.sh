#!/usr/bin/env bash
su ec2-user
sudo yum install httpd -y
sudo service httpd start
sudo su -c "cat > /var/www/html/index.html <<EOL
<html>
  <head>
    <title>Call to Arms</title>
    <style>
      img { display: block; margin: 0px auto; }
    </style>
  </head>
  <body>
    <img src='https://github.com/100DaysOfCloud/100DaysOfCloudIdeas/blob/master/banner.png?raw=true' height='400px'/>
  </body>
</html>
EOL"
