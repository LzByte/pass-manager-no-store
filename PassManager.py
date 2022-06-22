import hashlib
import getpass
import subprocess

maxPassLen = 20
encodeBase = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
upAlpTen = "ABCDEFGHIJ"
lwAlpTen = "abcdefghij"

#masterPasInp = getpass.getpass("Master password: ")
masterPasInp = input("Master password: ")
serviceInp = input("Web or service name: ")
print("Write your user if you have multiple accounts on the service, otherwise press enter")
userInp = input("User: ")

strToHash = masterPasInp + serviceInp + userInp

result = hashlib.md5(strToHash.encode())
decimalResult = int(result.hexdigest(),16)

generatedPass = ""

for i in range(len(str(decimalResult))):
    indexNum = int(str(decimalResult)[i:i+2])
    i=i+2
    if indexNum > len(encodeBase):
        indexNum = indexNum - len(encodeBase)
    try:
        generatedPass= generatedPass + encodeBase[indexNum]
    except:
        pass

#Adjust to general web password security standards
finalGeneratedPass = (generatedPass[:maxPassLen-6])
finalGeneratedPass =  finalGeneratedPass + str(decimalResult)[-2:]              #2 numbers
finalGeneratedPass = finalGeneratedPass + upAlpTen[int(str(decimalResult)[0])]  #2 uppercase
finalGeneratedPass = finalGeneratedPass + lwAlpTen[int(str(decimalResult)[1])]  #2 lowercase

print("Password: " +finalGeneratedPass)

#Copying the pass to the clipboard
cmd="echo " + finalGeneratedPass.strip() + "|clip"
subprocess.check_call(cmd, shell=True)