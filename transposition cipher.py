take_data=open("secret_text.txt","r")
lyrics=''.join(take_data.readlines()) #read text from a file "secret_text"
take_data.close()

def ceil(num,div):
    if div==0:
        return 'Can`t divide by 0'
    elif num%div==0:
        return num//div
    else:
        return num//div+1

def encrypt(text,width):
    #create matrix with 'width' number of columns
    dat=[['']*width for i in range(ceil(len(text),width))]
    pos=0
    for j in range(len(dat)): #fill matrix with letters of the text
        for k in range(len(dat[0])):
            if pos<len(text):
                dat[j][k]=text[pos]
                pos+=1
            else:
                break
    new=[] #create new list to save an encrypted text 
    for i in range(len(dat[0])):
        for j in range(len(dat)):
            new.append(dat[j][i]) #read matrix and save letters into a list
    return new #return 1 dimensional list, which is encrypted version of the original text

def decrypt(text,width):
    new_string=''.join(text)
    #create matrix with 'width' number of columns
    decr=[['']*width for i in range(ceil(len(new_string),width))]
    pos=0
    for j in range(len(decr[0])):#fill matrix with letters of the text
        for k in range(len(decr)):
            decr[k][j]=new_text[pos]
            if (pos+1)<len(text):
                pos+=1
            else:
                break     
    fin=[] #create new list to save decrypted text 
    for i in range(len(decr)):
        for j in range(len(decr[0])):
            fin.append(decr[i][j]) #read matrix and save letters into a list
    return ''.join(fin) #return decryped text as a string

take_key=open("key.txt","r")
number=int(take_key.readline()) #read width of encrypted matrix from a file "key"
take_key.close()

new_text=encrypt(lyrics,number)
new_string=''.join(new_text)
print('We need your help to decrypt this text:\n'+new_string)

satisfied=False
while not satisfied:
    key=int(input('Please enter width for a transposition matrix(from 1 to 10): '))
    print('Decrypted text :\n'+decrypt(new_text,key))
    satisfied=int(input('Are you satisfied with the result(0/1): '))
    if satisfied not in (0,1):
        print('Irrelevant value. Let`s try again')
        satisfied=False

print('Congratulations! You read the secret text!')
