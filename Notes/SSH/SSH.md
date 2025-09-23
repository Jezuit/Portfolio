Configured the IP on the computer I was working on as follows:
  
  IP: 10.0.10.10
  Subnet mask: 255.255.255.0
  Gateway: 10.0.10.1
  DNS: 8.8.8.8


Connected to a switch and conducted a connectivity test between the client and the server using the ping command:

  $ ping 8.8.8.8
  $ ping www.onet.pl


Connecting to the server via SSH.
I used the command:

  $ ssh mbpadmin@10.0.10.5


I executed four commands to download and update the latest APT packages and NTP:

  $ sudo apt update
  
  $ sudo apt upgrade -y
  
  $ sudo apt install zentyal
  
  $ sudo apt install ntp


I installed Midnight Commander:

  $ sudo apt install mc


Launched Midnight Commander to verify that it was working correctly:

  $ mc


Closed MC using F10.


Using the Zentyal Web GUI, under the Software & Management section, I installed additional useful programs and features such as Docker and FTP. I also enabled the Domain Controller and File Sharing module.


In Users and Computers → Manage, I:

  Created three groups: HR, IT, and Staff (regular employees)
  
  Added a user: jan.kowalski
