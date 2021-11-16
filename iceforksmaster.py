from sys import path
from os import path as os_path
path.append(os_path.join('chia-source'))

from chia-source.chia.util.ints import uint32
from chia-source.chia.util.bech32m import encode_puzzle_hash
from chia-source.chia.util.keychain import generate_mnemonic, mnemonic_to_seed
from chia-source.chia.consensus.coinbase import create_puzzlehash_for_pk
from chia-source.chia.wallet.derive_keys import master_sk_to_farmer_sk, master_sk_to_wallet_sk
from blspy import AugSchemeMPL


coin_list = ["Chia", "Flax", "Flora", "HDD", "STAI", "Stor", "AedgeCoin", "Apple", "Avocado", "Beer", "Beet", "BTCgreen", "C*ntCoin", "Cactus",
             "Cannabis", "Chaingreen", "Covid", "CryptoDoge", "DogeChia", "Equality", "ETHgreen", "Fork", "Goji", "Goldcoin", "GreenDoge", "Kale",
             "Kiwi", "Kujenga", "LittleLamboCoin", "Lotus", "Lucky", "Maize", "Melati", "mELON", "Mint", "Mogua", "N-Chain", "Olive", "Peas", "PecanRolls",
             "Pipscoin", "Rose", "Salvia", "Scam", "Sector", "Seno", "SHIBgreen", "Skynet", "Socks", "Spare", "Taco", "Tad", "Thyme", "Tranzact", "Venidium",
             "Wheat", "Xcha"]

prefix_list = ["xch", "xfx", "xfl", "hdd", "stai", "stor", "aec", "apple", "avo", "xbr", "xbt", "xbtc", "vag", "cac",
               "cans", "cgn", "cov", "xcd", "xdg", "xeq", "xeth", "xfk", "xgj", "ozt", "gdog", "xka",
               "xkw", "xkj", "llc", "lch", "six", "xmz", "xmx", "melon", "xkm", "mga", "nch", "xol", "pea", "rolls",
               "pips", "xcr", "xslv", "scm", "xsc", "xse", "xshib", "xnt", "sock", "spare", "xtx", "tad", "xth", "trz", "xvm",
               "wheat", "xca"]

passphrase = ""


def cold_wallets():
    mnemonic = generate_mnemonic()
    seed = mnemonic_to_seed(mnemonic, passphrase)
    key = AugSchemeMPL.key_gen(seed)
    fingerprint = (key.get_g1().get_fingerprint())
    mpk = (key.get_g1())
    fpk = (master_sk_to_farmer_sk(key).get_g1())
    puzhash = (create_puzzlehash_for_pk(master_sk_to_wallet_sk(key, uint32(0)).get_g1()))

    with open('iceforksmaster.txt', 'a') as file:

        print("Master Public Key:", mpk)
        print("Farmer Public Key:", fpk)
        print("Fingerprint:", fingerprint)
        print("Puzzle Hash:", puzhash)
        print("\n" + "Master Mnemonic: " + mnemonic + "\n")

        file.write("\n\n" + "Master Public Key:" + str(mpk))
        file.write("\n" + "Farmer Public Key:" + str(fpk))
        file.write("\n" + "Fingerprint:" + str(fingerprint))
        file.write("\n" + "Puzzle Hash:" + str(puzhash))
        file.write("\n\n" + "Master Mnemonic: " + mnemonic + "\n")

        for prefix, name in zip(prefix_list, coin_list):
            address = encode_puzzle_hash(create_puzzlehash_for_pk(master_sk_to_wallet_sk(key, uint32(0)).get_g1()), prefix)
            print(name + ": " + address)
            file.write("\n" + name + ": " + address)

    file.close()

if __name__ == '__main__':
    cold_wallets()
