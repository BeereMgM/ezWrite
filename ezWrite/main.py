import ezWrite as text
import ezCryp as cryp

def main():
    decString = cryp.decryptString(string="b'gAAAAABk8dOc7Xcuq1MLDZvZ_q6VH5YR7E9uyiRYX-4XTV8WxAD-987mvq8Tu69MaObw1Su_xDQskIcTFVMuanVkMPL0kBes2w=='", keyFile="key.dat")
    print(decString)
if __name__ == '__main__':
    main()

