# python-i2c-lcd
==============

Set of python scripts to launch manually or run as a service to display monitoring information on an I2C LCD display connected to the Raspberry Pi through the GPIO.

To set-up the hardware part, check [Using An I2C Enabled LCD Screen With The Raspberry Pi](https://fxmartin.github.io/How-to-set-up-a-LCD-display/).

![I2C LCD connected to PI3](https://fxmartin.github.io/images/2016-09-10-How-to-set-up-a-LCD-display.jpg)

# Setup

```
sudo apt-get install python-smbus i2c-tools python-dev
sudo pip install psutil
```

# Run as a service

```
sudo cp ./bin/*.sh /usr/bin
sudo cp ./service/* /etc/systemd+system/
sudo systemctl daemon-reload
sudo systemctl restart lcd-panel.service
```

To check that it runs successfully, enter ```sudo systemctl status lcd-panel.service```and you should get an output similar to the below:

```
╔[fxmartin@matrix:~/python-i2c-lcd]
╚>$ sudo systemctl status lcd-panel.service
● lcd-panel.service - LCD display
   Loaded: loaded (/etc/systemd/system/lcd-panel.service; enabled)
   Active: active (running) since Sun 2016-09-11 13:54:54 UTC; 7min ago
 Main PID: 1245 (lcd-panel.sh)
   CGroup: /system.slice/lcd-panel.service
           ├─1245 /bin/bash /usr/bin/lcd-panel.sh
           ├─1247 sudo python /home/fxmartin/python-i2c-lcd/monitor.py
           └─1251 python /home/fxmartin/python-i2c-lcd/monitor.py

Sep 11 13:54:54 matrix.local systemd[1]: Started LCD display.
Sep 11 13:54:54 matrix.local sudo[1247]: root : TTY=unknown ; PWD=/ ; USER=root ; COMMAND=/usr/bin/python /home/fxmartin/python-i2c-lcd/monitor.py
Sep 11 13:54:54 matrix.local sudo[1247]: pam_unix(sudo:session): session opened for user root by (uid=0)
```

# Usage

```
sudo python2 ./display.py line_1~line_2~line_3~line_4
```

or clock demo:


```
sudo python2 ./datetime-test.py
```

or monitoring:

```
sudo python2 ./monitor.py
```

### Based on
*  Forked from https://github.com/sweetpi/python-i2c-lcd
*  https://github.com/pimatic/pimatic/issues/271
*  http://www.gejanssen.com/howto/i2c_display_2004_raspberrypi/index.html
