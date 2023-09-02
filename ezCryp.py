from cryptography.fernet import Fernet
import ezWrite as text



def encryptString(string: str, safeKeyToFile: bool = False):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             '1 ', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '.', '1']  
    
def decryptString(string: str, keyFile: str = None):
    if keyFile is None:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        decString = fernet.decrypt(string).decode()
        return decString
    elif keyFile is not None:
        key = text.read_file(filename=keyFile, line=1)
        fernet = Fernet(key)
        decString = fernet.decrypt(string).decode()
        return decString