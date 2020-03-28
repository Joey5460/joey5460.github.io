control
-------
- ${variable}
- $(command)  

variable::

    v2=${v::-4}
    echo "$v --> $v2"

arguments

    $0 $1, $2

return code

    $?

if-else_::

    var0=0
    test $var0 -ge 1 && echo 0 || echo 1 

multi commands in one line using ()::
    
    test "$1" = "us1" \
    && (echo "****us1****" ; sslocal -c ~/apps.sh/ss-net-us1.json & ) \
    || (test "$1" = "" \
    && echo "****tky****" && sslocal -c ~/apps.sh/ss-net.json &)

    
.. _if-else: https://stackoverflow.com/questions/5130847/running-multiple-commands-in-one-line-in-shell

loop::

    for f in *.rst
    do
        echo $f
    done


    END=10
    for i in $(seq 1 $END) 
    do
        echo $i 
    done

    v="some string.rtf"


set -e Exit immediately if a command exits with a non-zero exit status.

cat files > /dev/null 2>&1
https://stackoverflow.com/questions/10508843/what-is-dev-null-21
CLI
---
- grep -r .
- grep -i -r .  
- find . -name filename
- find . -type f -exec chmod 655 {} \
- pkill processname
- mkdir -p
- chmod u+x file.sh
- chmod g+r file.sh
- chmod o+w file.sh
- chown -R myuser:mygroup otherfiles
- tree
- pstree
- uname -a 
- curl -T luca.zip ftp://119.81.148.101 --user lucadev:@f4stl4n3
- iptables -I INPUT 5 -i wlp3s0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
- iptables -I INPUT -p tcp --dport 3030 -j ACCEPT && sudo service iptables save
- du -sh   ----- file/folder size
- fdisk -l ----- check
- sudo fdisk /dev/sdb --- if your USB is sdb ------ format
   
    https://askubuntu.com/questions/832914/i-cant-format-my-live-usb-pendrive-udisks-error-quark-11

    https://www.techwalla.com/articles/format-linux-disk

dnf

  - dnf autoremove //remove depedance
  - dnf config-manager --add-repo https://dl.winehq.org/wine-builds/fedora/28/winehq.repo  
  - dnf config-manager --set-disabled 
  - dnf repolist
    
    https://ask.fedoraproject.org/en/question/97852/how-do-i-list-and-edit-repositories-in-fedora-25/

::  

    cat /etc/*-release

ssh key

    - ssh-copy-id demo@198.51.100.0 ----- https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
    - ssh-keygen -y -f mykey.pem > mykey.pub ------ generate a public key from a private key


ssh server
----------
sudo dnf install ssh
systemctl start sshd
netstat -ant | grep 22

Delete Symbolic Link File
-------------------------
- rm linkname
- unlink linkname

sudo systemctl start docker
sudo docker run hello-world
https://docs.docker.com/install/linux/docker-ce/fedora/
