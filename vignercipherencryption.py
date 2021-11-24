def encrypt():
    plain=input('Enter your plain text: ')
    key=input('Enter the key: ')
    coun=0
    newk=key
    if len(key)<len(plain):
        while True:
            a=coun%len(key)
            newk+=key[a]
            if len(newk)==len(plain):
                break
            else:
                coun+=1
                continue
    cipher=''    
    l1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(plain)):
        p=l1.index(plain[i])
        k=l1.index(newk[i])
        cipher+=l1[(p+k)%26]
    
    autok=key
    autok+=plain[0:len(plain)-len(key)]
    autocipher=''
    for i in range(len(plain)):
        ap=l1.index(plain[i])
        ak=l1.index(autok[i])
        autocipher+=l1[(ap+ak)%26]
    print(f'Encrypted text from key extending key: {cipher}')
    print(f'Encrypted text from key auto key: {autocipher}')
        
        
def decrypt(): 
    plain=input('Enter your cipher text: ')
    key=input('Enter the key: ')
    coun=0
    newk=key
    if len(key)<len(plain):
        while True:
            a=coun%len(key)
            newk+=key[a]
            if len(newk)==len(plain):
                break
            else:
                coun+=1
                continue
    cipher=''    
    l1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(plain)):
        p=l1.index(plain[i])
        k=l1.index(newk[i])
        cipher+=l1[(p-k)%26]
        
    
    print(f'Decrypted text from key extending key: {cipher}')
    