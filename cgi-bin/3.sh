#!/bin/bash
ip='localhost'
port=9090

exec 3<>/dev/tcp/$ip/$port
if [ $? = 0 ]; then
 echo -n "3" >&3
fi

