#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<!DOCTYPE html><html><head><meta charset="utf-8"><title>Revers!</title></head><body><form action="/cgi-bin/1.sh" method="POST"><p><input type="submit" value="Вперёд!"></p></br></form><form action="/cgi-bin/2.sh" method="POST"><p><input type="submit" value="Стоп!"></p></br></form></body></html>"

ip='localhost'
port=9090

exec 3<>/dev/tcp/$ip/$port
if [ $? = 0 ]; then
 echo -n "3" >&3
fi

