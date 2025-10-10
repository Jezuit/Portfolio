#SSH protocol and Zentyal configuration
---

## 1. Configured the IP on the computer I was working on as follows:
  
*  IP: 
  
 * Subnet mask: 
  
 * Gateway: 
  
*  DNS: 8.8.8.8


## 2. Connected to a switch and conducted a connectivity test between the client and the server using the ping command:
```
  ping 8.8.8.8
```
```
  ping www.onet.pl
```

## 3. Connecting to the server via SSH.
I used the command:
```
  ssh password@*IP*
```

## 4. I executed four commands to download and update the latest APT packages and NTP:
```
  $ sudo apt update
  ```
```
  $ sudo apt upgrade -y
  ```
```
  $ sudo apt install zentyal
  ```
```
  $ sudo apt install ntp
```

## 5. I installed Midnight Commander:
```
  $ sudo apt install mc
  ```

## 6. Launched Midnight Commander to verify that it was working correctly:
```
  $ mc

```
## 7. Closed MC using F10.


## 8. Using the Zentyal Web GUI, under the Software & Management section, I installed additional useful programs and features such as Docker and FTP.


## 9. I enabled the Domain Controller and File Sharing module.


## 10. In Users and Computers → Manage, I:

*  Created three groups: HR, IT, and Staff (regular employees)
  
  Added a user: jan.kowalski


## 11. [Next steps](https://github.com/Jezuit/crypto_event_monitor)
