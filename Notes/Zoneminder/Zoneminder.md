1. Installed the Oracle VirtualBox virtual machine

2. Installed Linux Ubuntu 24.04 on VirtualBox from an .iso image

3. Downloaded and updated packages to ensure they were up to date using the command:

   ~$ sudo apt update && sudo apt upgrade -y

4. Added the ZoneMinder PPA using the commands:

   ~$ sudo add-apt-repository ppa\:iconnor/zoneminder-1.36
   
   ~$ sudo apt update

5. Installed ZoneMinder using the command:

   ~$ sudo apt install zoneminder -y

6. Enabled and started the services using the commands:

   ~$ sudo systemctl enable zoneminder
   
   ~$ sudo systemctl start zoneminder

7. Added www-data to the video group (so Apache has access to cameras):

   ~$ sudo usermod -aG video www-data

8. Manually created and set the correct settings for the directories:

   ~$ sudo mkdir -p /var/cache/zoneminder /var/log/zoneminder
   
   ~$ sudo chown -R www-data\:www-data /var/cache/zoneminder /var/log/zoneminder
   
   ~$ sudo chmod -R 755 /var/cache/zoneminder /var/log/zoneminder

9. Installed the dependencies providing Apache, PHP, MariaDB, and multimedia libraries needed for ZoneMinder

   ~$ sudo apt update
   
   ~$ sudo apt install -y apache2 mariadb-server php php-mysql libapache2-mod-php&#x20;
   php-gd php-mbstring php-xml php-zip libcurl4-openssl-dev libjpeg-dev&#x20;
   libavcodec-dev libavformat-dev libavutil-dev libavfilter-dev libavdevice-dev&#x20;
   libswscale-dev ffmpeg

10. Installed MariaDB (client + server)

    ~$ sudo apt update
    
    ~$ sudo apt install -y mariadb-server mariadb-client

11. Enabled and started the MariaDB service

    ~$ sudo systemctl enable mariadb
    
    ~$ sudo systemctl start mariadb
    
    ~$ sudo systemctl status mariadb

12. After making sure that MariaDB was running properly (“active (running)”), logged in to the service

    ~$ sudo mariadb

13. Created the database and user with the password

    CREATE DATABASE zm;
    GRANT ALL PRIVILEGES ON zm.\* TO 'zmuser'@'localhost' IDENTIFIED BY 'password';
    FLUSH PRIVILEGES;
    EXIT;

14. Exited MariaDB with the command “exit;”

15. Loaded the ZoneMinder database schema:

    ~$ sudo mysql -u root -p zm < /usr/share/zoneminder/db/zm\_create.sql

16. Restarted Apache

    ~$ sudo systemctl restart apache2

17. Checked the IP address of the machine:

    ~$ hostname -I

18. Enabled the required Apache modules:

    ~$ sudo a2enmod cgi rewrite

19. Enabled the ZoneMinder configuration:

    ~$ sudo a2enconf zoneminder

20. Enabled the ZoneMinder service in systemd:

    ~$ sudo systemctl enable zoneminder
    
    ~$ sudo systemctl start zoneminder

21. Restarted Apache

    ~$ sudo systemctl restart apache2

22. Opened the Apache configuration file for ZoneMinder

    ~$ cat /etc/apache2/conf-enabled/zoneminder.conf

23. Opened the ZoneMinder configuration file and added the missing “AllowOverride All” and “Require all granted” to the “/usr/share/zoneminder/www” section to give Apache full access:

<Directory /usr/share/zoneminder/www>
    Options -Indexes +FollowSymLinks
    AllowOverride All
    Require all granted
    <IfModule mod_dir.c>
        DirectoryIndex index.php
    </IfModule>
</Directory>


24. Saved and exited the file (Ctrl + O > Enter > Ctrl + X)

25. Restarted Apache again

    ~$ sudo systemctl restart apache2

26. Opened the ZoneMinder configuration itself

    ~$ sudo nano /etc/zm/zm.conf

27. Found the line where the password used by ZoneMinder is set and changed it to the configured one password:

    ZM\_DB\_PASS='...'    ➡️   ZM\_DB\_PASS='password'

28. Saved and exited the file (Ctrl + O > Enter > Ctrl + X)

29. Restarted ZoneMinder

    ~$ sudo systemctl restart zoneminder

30. Checked that it works by entering the following link in a browser: “http://localhost/zm”

31. Everything is working correctly! Proceeding to the next steps.

