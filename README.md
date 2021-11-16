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

Supported Forks:
```
Chia: xch
Flax: xfx
Flora: xfl
HDD: hdd
STAI: stai
Stor: stor
AedgeCoin: aec
Apple: apple
Avocado: avo
Beer: xbr
Beet: xbt
BTCgreen: xbtc
C*ntCoin: vag
Cactus: cac
Cannabis: cans
Chaingreen: cgn
Covid: cov
CryptoDoge: xcd
DogeChia: xdg
Equality: xeq
ETHgreen: xeth
Fork: xfk
Goji: xgj
Goldcoin: ozt
GreenDoge: gdog
Kale: xka
Kiwi: xkw
Kujenga: xkj
LittleLamboCoin: llc
Lotus: lch
Lucky: six
Maize: xmz
Melati: xmx
mELON: melon
Mint: xkm
Mogua: mga
N-Chain: nch
Olive: xol
Peas: pea
PecanRolls: rolls
Pipscoin: pips
Rose: xcr
Salvia: xslv
Scam: scm
Sector: xsc
Seno: xse
SHIBgreen: xshib
Skynet: xnt
Socks: sock
Spare: spare
Taco: xtx
Tad: tad
Thyme: xth
Tranzact: trz
Venidium: xvm
Wheat: wheat
Xcha: xca
Achi: ach
```