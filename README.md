## ZCash command line wallet in Python. 

Works using ZCash RPC. Created primarily for personal use. Must be running full ZCash node for it to 
work. Supports t-addresses and z-addresses.  
  
zcash.conf file should look like:
~~~
# testnet=1
# addnode=testnet.z.cash
addnode=mainnet.z.cash
rpcconnect=127.0.0.1
rpcport=9050
server=1
rpcuser=username
rpcpassword=password
~~~
