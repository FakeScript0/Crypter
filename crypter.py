import os
from cryptography.fernet import Fernet
import subprocess
from colored import fg

subprocess.call(["clear"])
# ASCII sanatı ile özelleştirilmiş yazı
custom_text = fg("red") + """
    ▁ ▂ ▄ ▅ ▆ ▇ █  𝔽𝕒𝕜𝕖𝕊𝕔𝕣𝕚𝕡𝕥𝟘 █ ▇ ▆ ▅ ▄ ▂ ▁"""
print(custom_text)
white=fg("white")
if not os.path.exists("generatedkey.key"):
    key = Fernet.generate_key()
    with open("generatedkey.key", "wb") as generatedkey:
        generatedkey.write(key)
else:
    with open("generatedkey.key", "rb") as generatedkey:
        key = generatedkey.read()

print("""
    ----------------------------------------
       CRIPTER PROQRAMIMA XOS GELMISINIZ!
    ----------------------------------------
"""+fg("green"))
while True:
    print(fg("green")+"""
    
    ----------------------------------------------------------------------------------------------------------------------------------------
    
    Fayllari Encrypt ucun (e) Decrypt ucun (d) Fayl Mezmununa Baxmaq Ucun (r) Terminalin Temizlenmesi (c) Proqram Sonlanmasi Ucun (q) basin: 
     
    ----------------------------------------------------------------------------------------------------------------------------------------
    
    """+fg("green"))
    check=input("""
    Seciminizi Girin: """+fg("white"))

    if check=="d":
        try:
            filename=input(fg("green")+"""
    Decrypt Edeceyiniz Faylin Adi(Ex=test.txt): """+fg("white"))
            if not (filename=="generatedkey.key" or filename=="crypter.py"):
                with open(filename,"rb") as thefile:
                    contest=thefile.read()
                decrypted_contest=Fernet(key).decrypt(contest)
                with open(filename ,"wb") as thefile:
                    thefile.write(decrypted_contest)
                print(fg("blue")+"""
    Emeliyyat Ugurlu Kecdi!""",white+"{}".format(filename),fg("blue")+"""Fayli DECRYPT Edildi!
    """)
            else:
                print(fg("red")+"""
    {} Faylini DECRYPT Etme Yetkiniz  Yoxdu!!!
                """.format(filename)+white)

        except:
            print(fg("red")+"""
    Ugursuz Emeliyyat!!!Bu Fayl Ya Bu Qovluqda Yoxdur, Yada Bu Fayli Artiq Decrypt Etmisiniz!!!
            
            """)
    elif check=="e":
        try:
            filename=input(fg("green")+"""
    Encrypt Edeceyiniz Faylin Adi(Ex=test.txt): """+white)
            if not (filename=="generatedkey.key" or filename=="crypter.py"):
                with open(filename,"rb") as thefile:
                    contest=thefile.read()
                encrypted_contest=Fernet(key).encrypt(contest)
                with open(filename ,"wb") as thefile:
                    thefile.write(encrypted_contest)
                print(fg("blue")+"""
    Emeliyyat Ugurlu Kecdi!""",white+"{}".format(filename),fg("blue")+"""Fayli ENCRYPT Edildi!
    """)
            else:
                print(fg("red")+"""
    {} Faylini Encrypt Etme Yetkiniz Yoxdu!!!
                """.format(filename))
        except:
            print(fg("red")+"""
    Ugursuz Emeliyyat.
            """)
    elif check=="r":
        try:
            filename=input(fg("green")+"""
    Fayl Adini Girin(Ex=test.txt): """+white)
            with open(filename,"rb") as thefile:
                contest=thefile.read()
            print(fg("green")+f""" 
    {filename}  Faylinda:
            """)
            print(fg("white")+f"""
    {contest}
            """)
        except:
            print(fg("red")+"""
    Bele Fayl Yoxdur.!""")
    elif check=="q":
        print(fg("blue")+"""
    Proqraminiz Sonlandi!""")
        break
    elif check=="c":
        subprocess.call(["clear"])
    else:
        print(fg("red")+"""
    Duzgun deyer Girin!!!""")
