from sys import path
from os import path as os_path
path.append(os_path.join('chia_source'))

from chia_source.chia.util.ints import uint32
from chia_source.chia.util.bech32m import encode_puzzle_hash
from chia_source.chia.util.keychain import generate_mnemonic, mnemonic_to_seed
from chia_source.chia.consensus.coinbase import create_puzzlehash_for_pk
from chia_source.chia.wallet.derive_keys import master_sk_to_farmer_sk, master_sk_to_wallet_sk
from blspy import AugSchemeMPL


coin_list = ["Chia", "Flax", "Flora", "HDD", "STAI", "Stor", "AedgeCoin", "Apple", "Avocado", "Beer", "Beet", "BTCgreen", "C*ntCoin", "Cactus",
             "Cannabis", "Chaingreen", "Covid", "CryptoDoge", "DogeChia", "Equality", "ETHgreen", "Fork", "Goji", "Goldcoin", "GreenDoge", "Kale",
             "Kiwi", "Kujenga", "LittleLamboCoin", "Lotus", "Lucky", "Maize", "Melati", "mELON", "Mint", "Mogua", "N-Chain", "Olive", "Peas", "PecanRolls",
             "Pipscoin", "Rose", "Salvia", "Scam", "Sector", "Seno", "SHIBgreen", "Skynet", "Socks", "Spare", "Taco", "Tad", "Thyme", "Tranzact", "Venidium",
             "Wheat", "Xcha", "Achi", "Silicoin", "Gold", "Profit", "Ecostake"]

prefix_list = ["xch", "xfx", "xfl", "hdd", "stai", "stor", "aec", "apple", "avo", "xbr", "xbt", "xbtc", "vag", "cac",
               "cans", "cgn", "cov", "xcd", "xdg", "xeq", "xeth", "xfk", "xgj", "ozt", "gdog", "xka",
               "xkw", "xkj", "llc", "lch", "six", "xmz", "xmx", "melon", "xkm", "mga", "nch", "xol", "pea", "rolls",
               "pips", "xcr", "xslv", "scm", "xsc", "xse", "xshib", "xnt", "sock", "spare", "xtx", "tad", "xth", "trz", "xvm",
               "wheat", "xca", "ach", "sit", "gl", "profit", "eco"]

passphrase = ""


def cold_wallets():

    for prefix, name in zip(prefix_list, coin_list):
        mnemonic = generate_mnemonic()
        seed = mnemonic_to_seed(mnemonic, passphrase)
        key = AugSchemeMPL.key_gen(seed)
        fingerprint = (key.get_g1().get_fingerprint())
        mpk = (key.get_g1())
        fpk = (master_sk_to_farmer_sk(key).get_g1())
        puzhash = (create_puzzlehash_for_pk(master_sk_to_wallet_sk(key, uint32(0)).get_g1()))
        address = encode_puzzle_hash(create_puzzlehash_for_pk(master_sk_to_wallet_sk(key, uint32(0)).get_g1()), prefix)
        staking_address = encode_puzzle_hash(create_puzzlehash_for_pk(master_sk_to_farmer_sk(key).get_g1()), prefix)
        print("\n" + name + " Mnemonic: " + mnemonic)
        print(name + " Address: " + address)
        print(name + " Master Public Key:", mpk)
        print(name + " Farmer Public Key:", fpk)
        print(name + " Fingerprint:", fingerprint)
        print(name + " Puzzle Hash:", puzhash)
        if prefix == "sit" or prefix == "gl" or prefix == "profit" or prefix == "eco":
            print(name + " Staking Address:", staking_address)

        with open('iceforksunique.txt', 'a') as file:
            file.write("\n\n" + name + " Mnemonic: " + mnemonic)
            file.write("\n" + name + " Address: " + address)
            file.write("\n" + name + " Master Public Key:" + str(mpk))
            file.write("\n" + name + " Farmer Public Key:" + str(fpk))
            file.write("\n" + name + " Fingerprint:" + str(fingerprint))
            file.write("\n" + name + " Puzzle Hash:" + str(puzhash))
            if prefix == "sit" or prefix == "gl" or prefix == "profit" or prefix == "eco":
                file.write("\n" + name + " Staking Address:" + str(staking_address))
            file.close()


if __name__ == '__main__':
    cold_wallets()


