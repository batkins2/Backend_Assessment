#/bin/bash
mkdir -p /data/db
/usr/bin/mongod &
python3 -m swagger_server 
