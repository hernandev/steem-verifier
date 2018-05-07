# steem-verifier.

**steem-verifier** helps you debug signatures on Steem transactions.

## Install:

You can use pip to install this tool:

```
pip install steem-verifier
``` 

## Usage:

Really simple, after installing, you can call the command line tool
passing a transaction id as parameter:

```
steem-verifier 6a3e9a99cf3bc9464c6aa26c7daf63454de8d411
```

This will query the Steem blockchain for the transaction
and verify it's signature(s). An example result is shown bellow:

```
=> Retrieving transaction...

=> Extracting public keys...

=> Extracted public keys are:
STM5vgGoHBrUuDCspAPYi3dLwSyistyrz61NWkZNUAXAifZJaDLPF

=> The accounts who signed the transaction (public key owners) are:
blocktrades
```
