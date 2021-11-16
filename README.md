## THIS CODE IS UNTESTED. USE AT YOUR OWN RISK. ##

### Chia Forks Cold Wallet Generator ###

Requirements: chia source code, bitstring, blspy, watchdog, keyrings.cryptfile, clvm, clvm-rs, clvm-tools

Install:
```
git clone https://github.com/sub256/iceforkwallets
cd iceforkwallets
pip3 install -r requirements.txt
git clone https://github.com/Chia-Network/chia-blockchain.git -b latest chia_source
```

Run:

IceFork Master - Generates 1 master mnemonic for all of the forks.
Prints the output to screen and saves to file 'iceforkmaster.txt' 
```
python3 iceforkmaster.py 
```
IceFork Unique - Generates a unique mnemonic for each of the forks.
Prints the output to screen and saves to file 'iceforkunique.txt' 
```
python3 iceforkunique.py
```
