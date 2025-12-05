import os
import datetime
tete = "tete.txt"
hist = "hist.txt"
def chrgmt():
    fai= {}
    if os.path.exists(tete):
        try:
            with open(tete,'r',encoding='utf-8') as f:
                for l in f:
                    if ':' in l:
                        kstion,rep= l.strip().split(':', 1)
                        fai[kstion.lower()] = rep
        except Exception as e:
            print(f"Error lors du chargement: {e}")
    return fai
def eng(fai):
    try:
        with open(tete,'a',encoding='utf-8') as f:
            for kstion,rep in fai.items():
                f.write(f"{kstion}:{rep}\n")
    except Exception as e:
        print(f"Erroe error error ds la sauvegarde:{e}")
def histo(czi,rep):
    try:
        tmp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(hist,'a',encoding='utf-8') as f:
            f.write(f"[{tmp}] Utilisateur: {czi}\n")
            f.write(f"[{tmp}] Bot: {rep}\n")
    except Exception as e:
        print(f"Error error error dans la sauvegarde:{e}")
def historika():
    if os.path.exists(hist):
        try:
            with open(hist,'r',encoding='utf-8') as f:
                print("hiistorique:")
                print(f.read())
        except Exception as e:
            print(f"Error error error dans le chrgmt de histrique: {e}")
    else:
        print("ya rien")
def app(kstion,fai):
    print(f"Je ne connais pas la réponse à : '{kstion}'")
    ch="Désolée je ne connais pas la reponse apprenez moi donc "
    nv= input("apprends moi la rep ")  
    if nv.strip():
        fai[kstion.lower()] = nv
        eng(fai)
        print("Merci je viens dapprendre qqchose de nv")
        return nv
    return ch
def main():
    fai= chrgmt()
    print(" Bonjour mon ami posez moi des questions vzy")
    print("Commandes speciales:")
    print("histo")
    print("'arret'")
    while True:
        czi= input("sa majete:").strip()
        if czi.lower()=='quit':
            print("bye take care")
            break
        elif czi.lower()=='historique':
            historika()
            continue
        elif not czi:
            continue
        if czi.lower() in fai:
            rep= fai[czi.lower()]
            print(f"Bot:{rep}")
        else:
            rep=app(czi,fai)
            print(f"Bot: {rep}")
        histo(czi,rep)
if __name__ == "__main__":
    main()
