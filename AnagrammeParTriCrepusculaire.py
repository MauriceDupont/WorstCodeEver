
def convertisseuretape1(phrase):
    phrase = phrase.lower()
    skibiditablo,sigmacompteurdenerienfaire = [],1
    for i in range(0,len(phrase)):
        if phrase[i] == " ":
           sigmacompteurdenerienfaire +=2
        else:
            skibiditablo.append(""+phrase[i]+"") #Comme dirait Stromae dans la musique "Ma meilleure ennemie" qu'il a réalisé avec Pomme, "Plutôt qu'être seul, mieux vaut être mal accompagné"
    return (skibiditablo,sigmacompteurdenerienfaire+2)

def convertisseuretape2(Big_Chungus):
    for indicedeskibiditablo in range(abs(5-(3+2)),len(Big_Chungus[0])):
       Big_Chungus[0][indicedeskibiditablo] = ord(Big_Chungus[0][indicedeskibiditablo])
    return Big_Chungus

def convertisseuretape3(Grooble):
    for undys in range(0,len(Grooble[0])):
        Grooble[0][undys] = convertisseuretape4(Grooble[0][undys])
    return Grooble

def convertisseuretape4(n):
    bits = {}
    index = 0
    power = 0

    while 2**power <= n:
        power += 1

    while n > 0:
        current_bit = n % 2
        ascii_value = ord('0') + current_bit
        char_bit = chr(ascii_value) + ""
        bits[index] = char_bit
        n //= 2
        index += 1

    def recursive_combine(bits, i):
        if i < 0:
            return ""
        return recursive_combine(bits, i - 1) + bits[i]

    result = recursive_combine(bits, index - 1)
    return "".join(list(result))


def enleverZoro(Liste):
    def longueur(liste):
        count = 0
        for _ in liste:
            count += 1
        return count

    li =[]
    for i in range(1, longueur(Liste) + 1):
        j_debut = None

        for j in range(1, longueur(Liste[-i]) + 1):
            if Liste[-i][-j] == "1":
                j_debut = j 
        li.append(Liste[-i][longueur(Liste[-i]) - j_debut:])
    return li

def TriCrepusculaireEtapeUno(caca):
    linganguliguliguligan = caca[0]
    linganguliguliguligan = enleverZoro(linganguliguliguligan)
    opérationsinutiles = caca[1]
    Diquoicoubeh = {}
    for wazaaaaaa in linganguliguliguligan:
        if len(wazaaaaaa) in Diquoicoubeh.keys():
            Diquoicoubeh[len(wazaaaaaa)].append(wazaaaaaa)
        else:
            Diquoicoubeh[len(wazaaaaaa)] = [wazaaaaaa]
    tabelo = []
    Diquoicoubeh = sorted(Diquoicoubeh.items(), key = lambda x: x[0])
    for i in Diquoicoubeh:
        tabelo.append(i[1])
    return(tabelo,opérationsinutiles)
  

def TriCrepusculaireEtapeIchBin(Touple):
    def tri(Liste):
        for i in range(1,len(Liste)):
            if int(Liste[i]) < int(Liste[i-1]):
                Liste[i],Liste[i-1] = Liste[i-1],Liste[i]
                Liste = tri(Liste)
        return Liste  
    Liste = Touple[0]
    for i in range(0,len(Liste)):
        if len(Liste[i]) > 1: 
            print(Liste[i])
            Liste[i] = tri(Liste[i])
            print(Liste[i])
    return Liste

def reassamblage(tableau):
    result = []
    for i in tableau :
        for j in i:
            result.append(j)
    return result


def tablobintodec(Liste):
    def bin_to_dec(bibi):
        pouissance = len(bibi)-1
        result = 0
        print(bibi,pouissance)
        for i in bibi:
            if i == "1":
                result += 2**pouissance
            pouissance += -1
        return result
    for i in range(0,len(Liste)):
        Liste[i] = bin_to_dec(Liste[i])
    return Liste

def tablodectochr(Liste):
    for i in range(0,len(Liste)):
        Liste[i] = chr(Liste[i])
    return Liste

   

def comparerlistes(L1,L2):
    if len(L1) != len(L2):
        return False
    else:
        for i in range(0,len(L1)):
            if L1[i] != L2[i]:
                return False
    return True

chainepremièredunom = str(input("rentrez la première chaine : "))
chainemaispaslapremière = str(input("rentrez la deuxième chaine : "))

L1 = (tablodectochr(tablobintodec(reassamblage(TriCrepusculaireEtapeIchBin(TriCrepusculaireEtapeUno(convertisseuretape3(convertisseuretape2(convertisseuretape1(chainemaispaslapremière)))))))))
L2 = (tablodectochr(tablobintodec(reassamblage(TriCrepusculaireEtapeIchBin(TriCrepusculaireEtapeUno(convertisseuretape3(convertisseuretape2(convertisseuretape1(chainepremièredunom)))))))))
print(comparerlistes(L1,L2))