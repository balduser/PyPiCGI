#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<!DOCTYPE html><html><head><meta charset="utf-8"><title>Stop!</title></head><body><form action="/cgi-bin/1.sh" method="POST"><p><input type="submit" value="Вперёд!"></p></br></form><form action="/cgi-bin/3.sh" method="POST"><p><input type="submit" value="Назад!"></p></br></form></body></html>"

ip='localhost'
port=9090

exec 3<>/dev/tcp/$ip/$port
if [ $? = 0 ]; then
 echo -n "2" >&3
fi

