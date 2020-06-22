# _crypter #

**this project is purely for educational purpose only**


**encrypter.py**: this script is used for encrypting the malicious code, it uses "aes" encryption along with "hex" encryption to
                  encrypt the malicious code. which is decrypted and executed by stub at runtime


**crypter.py**  : crypter uses several techniques to evade the runtime analysis of anti-viruses,
                  for example: hash of a known file is calculated and stored, at the runtime the same file is downloaded and it's hash
                  is calculated, if both the hashes match then we can assume that the crypter is not running in a sandbox environment
                  created by the AV and hence indicates that it is safe to decrypt the malicious code and run it.
