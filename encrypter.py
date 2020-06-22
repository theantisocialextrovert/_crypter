import binascii
import pyaes
import sys
import cry_lizzie

#----------------------------------------------------------------------------------------------------------------------------------
# encryption
#----------------------------------------------------------------------------------------------------------------------------------
with open("your_file_name","rb") as my_data:
    file_data                  = my_data.read()
    key                        = "7I{#|Q]f[n|e)hOx"  # 16 bytes key - change for your key
    aes_obj                    = pyaes.AESModeOfOperationCTR(key)
    aes_encrypted_data         = aes.encrypt(file_data)
    aes_and_hex_encrypted_data = binascii.hexlify(aes_encrypted_data)

with open("encrypted_file","wb") as temp_file:
    temp_file.write(aes_and_hex_encrypted_data)
#-----------------------------------------------------------------------------------------------------------------------------------


