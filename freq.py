def second_value(a):
    return a[1]

text = input('Enter Ciphertext: ').upper()
#'rbk dlcsqrpdzi pktmisrdml zlc drq amlqkosklakq bztk hkkl z cdqzqrkp ump rbk bsjzl pzak rbkx bztk fpkzrix dlapkzqkc rbk iduk kwnkarzlax mu rbmqk mu sq vbm idtk dl zctzlakc amslrpdkq hsr rbkx bztk ckqrzhdidykc qmadkrx bztk jzck iduk slusiudiidlf bztk qshekarkc bsjzl hkdlfq rm dlcdfldrdkq bztk ikc rm vdckqnpkzc nqxabmimfdazi qsuukpdlf dl rbk rbdpc vmpic rm nbxqdazi qsuukpdlf zq vkii zlc bztk dluidarkc qktkpk czjzfk ml rbk lzrspzi vmpic rbk amlrdlskc cktkimnjklr mu rkablmimfx vdii vmpqkl rbk qdrszrdml dr vdii akprzdlix qshekar bsjzl hkdlfq rm fpkzrkp dlcdfldrdkq zlc dluidar fpkzrkp czjzfk ml rbk lzrspzi vmpic dr vdii npmhzhix ikzc rm fpkzrkp qmadzi cdqpsnrdml zlc nqxabmimfdazi qsuukpdlf zlc dr jzx ikzc rm dlapkzqkc nbxqdazi qsuukpdlf ktkl dl zctzlakc amslrpdkq rbk dlcsqrpdzi rkablmimfdazi qxqrkj jzx qsptdtk mp dr jzx hpkzg cmvl du dr qsptdtkq dr jzx ktklrsziix zabdktk z imv iktki mu nbxqdazi zlc nqxabmimfdazi qsuukpdlf hsr mlix zurkp nzqqdlf rbpmsfb z imlf zlc tkpx nzdlusi nkpdmc mu zcesqrjklr zlc mlix zr rbk amqr mu nkpjzlklrix pkcsadlf bsjzl hkdlfq zlc jzlx mrbkp idtdlf mpfzldqjq rm klfdlkkpkc npmcsarq zlc jkpk amfq dl rbk qmadzi jzabdlk usprbkpjmpk du rbk qxqrkj qsptdtkq rbk amlqkosklakq vdii hk dlktdrzhik rbkpk dq lm vzx mu pkumpjdlf mp jmcduxdlf rbk qxqrkj qm zq rm npktklr dr upmj cknpdtdlf nkmnik mu cdfldrx zlc zsrmlmjx'.upper()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
length = len(alphabet)
alphabet_count = [['',0]]*length
starts_with_count = [['',0]]*length

for i in range(length):
    alphabet_count[i] = [alphabet[i],0]
    starts_with_count[i] = [alphabet[i],0]


for i in text:
    for j in range(length):
        if i==alphabet[j]:
            alphabet_count[j][1]+=1
            break

sorted_alphabet = alphabet_count
cipher_length = len(text)
sorted_alphabet.sort(reverse=1,key=second_value)

#sorting them
for i in range(length):
    sorted_alphabet[i][1]=round(sorted_alphabet[i][1]/cipher_length*100,2)

current_text = text
x=''
print("Current Ciphertext:")
print(current_text)
current_alphabet = alphabet

while(x!='X'):
    x= input("\nPress A to display current alphabet, F to display frequencies, C to display current ciphertext, R to replace a letter, or X to exit: ").upper()
    if x=='A':
        print(current_alphabet)
    if x=='F':
        print(sorted_alphabet)
    elif x=='C':
        print(current_text)
    elif x=='R':
        old_letter = input("Old letter: ").upper()
        new_letter = input("New letter: ").lower()
        current_text = current_text.replace(old_letter,new_letter)
        old_letter = old_letter
        current_alphabet = current_alphabet.replace(old_letter,new_letter)
        print("\nUpdated Ciphertext:")
        print(current_text)        
        print("\nUpdated Alphabet:")
        print(alphabet+" ->")
        print(current_alphabet)
        
    elif x!='X':
        print("Erm what the deuce")