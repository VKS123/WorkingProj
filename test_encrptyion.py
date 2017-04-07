#from Crypto.Cipher import AES
#from Crypto import Random

#key = b'Sixteen byte key'
#iv = Random.new().read(AES.block_size)
#print iv
#cipher = AES.new(key, AES.MODE_CFB, iv)
#msg = iv + cipher.encrypt(b'Attack at dawn')
#print msg
#res=cipher.decrypt(msg)
#print res

from Crypto.Cipher import AES
import base64


def ecb_encrypt(message, key):
    """ Encrypts a message in AES ECB mode with a given key
    ACCEPTS: Two strings, the plaintext message and the key
    RETURNS: A bytes string of base64 encoded ciphertext
    """

    aes = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(aes.encrypt(message)).decode()


def ecb_decrypt(encrypted, key):
    """ Decrypts a ciphertext in AES ECB mode with a given key
    ACCEPTS: Two strings, the base64 encoded ciphertext and the key
    RETURNS: A bytes string of the plaintext message
    """

    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(base64.b64decode(encrypted))


if __name__ == "__main__":

    Key = "10"*8
    plain_text = "1010101110101011"
    print len(Key)
    cipher_text = ecb_encrypt(plain_text, Key)
    decrypted_pt = ecb_decrypt(cipher_text, Key).decode()

    print("Original message: {}".format(plain_text))
    print("Encrypted message: {}".format(cipher_text))
    print("Decrypted message: {}".format(decrypted_pt))
