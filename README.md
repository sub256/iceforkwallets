## THIS CODE IS UNTESTED. USE AT YOUR OWN RISK. ##

### Chia Forks Cold Wallet Generator ###

Requirements: chia source code, bitstring, blspy, watchdog, keyrings.cryptfile, clvm, clvm-rs, clvm-tools, inquirer

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
GetAddress Util - Choose fork, enter 24 word mnemonic and it returns the first address and staking address (on supported chains).
Prints the output to screen and saves to file 'getaddress.txt'
```
python3 getaddress.py
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
Silicoin: sit
Gold: gl
Profit: profit
Ecostake: eco
```

Donations welcome:
```
Chia: xch1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsngn9xz
Flax: xfx1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs2t5p9q
Flora: xfl1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs36uhl0
HDD: hdd1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsdvtapv
STAI: stai1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsla0gpm
Stor: stor1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcstj3hrr
AedgeCoin: aec1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs2jqkkq
Apple: apple1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsy82y4s
Avocado: avo1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcss4cx6v
Beer: xbr1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcshun42k
Beet: xbt1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs80gtkq
BTCgreen: xbtc1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcslygfw5
C*ntCoin: vag1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs7q52rs
Cactus: cac1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsvfet3g
Cannabis: cans1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsc8c837
Chaingreen: cgn1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsuhql7q
Covid: cov1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsxl3t3q
CryptoDoge: xcd1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs68vsh8
DogeChia: xdg1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs4uazw5
Equality: xeq1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsc8z8n9
ETHgreen: xeth1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs7zkq8u
Fork: xfk1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs7zhv78
Goji: xgj1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsq4eshj
Goldcoin: ozt1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsgq8vzg
GreenDoge: gdog1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcspucpkg
Kale: xka1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs2lgkps
Kiwi: xkw1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsxcf2g2
Kujenga: xkj1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsvguc3a
LittleLamboCoin: llc1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcswtm4w5
Lotus: lch1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs8vp3dt
Lucky: six1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsw37q3s
Maize: xmz1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcskxs78z
Melati: xmx1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcspse55h
mELON: melon1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcstjwmel
Mint: xkm1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsrshrs4
Mogua: mga1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsnwjt6y
N-Chain: nch1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs9umngx
Olive: xol1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcscsye0w
Peas: pea1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsvptdj5
PecanRolls: rolls1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsce4jvl
Pipscoin: pips1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsqke8az
Rose: xcr1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcskqdv7a
Salvia: xslv1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsjgcmj6
Scam: scm1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsqv4lna
Sector: xsc1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs96tv7m
Seno: xse1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs4fsjzd
SHIBgreen: xshib1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs0yqm84
Skynet: xnt1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcstjdrs0
Socks: sock1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs3acz4f
Spare: spare1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcslkjmkd
Taco: xtx1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcscldavz
Tad: tad1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs5dh8gk
Thyme: xth1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcsythlew
Tranzact: trz1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs9gulzr
Venidium: xvm1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs75q429
Wheat: wheat1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs5gev24
Xcha: xca1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcszfwp96
Achi: ach1r33ss7ekgrvvs5hf57anqlhuxuagg649mf7m58g99689a5sh6lcs2lzu97
```