import pyfiglet
  

banner = """ 
 █████                                                       
░░███                                                        
 ░███████   ██████   ████████   ████████    ██████  ████████ 
 ░███░░███ ░░░░░███ ░░███░░███ ░░███░░███  ███░░███░░███░░███
 ░███ ░███  ███████  ░███ ░███  ░███ ░███ ░███████  ░███ ░░░ 
 ░███ ░███ ███░░███  ░███ ░███  ░███ ░███ ░███░░░   ░███     
 ████████ ░░████████ ████ █████ ████ █████░░██████  █████    
░░░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░                                                                                                                                                                                         
"""
print(banner)
print("---------------------------------------------------------")
fontlar = """ 
[1]isometric1   [2]letters    [3]banner3-D    [4]5lineoblique    [5]digital

         [6]3-D    [7] fontu ben belirlerim
"""
print(fontlar)

kelime = input("[+]OLUŞTURMAK İSTEDİGİNİZ KELİME: ")
font = input("[*]FONT NUMARASI GİRİNİZ: ")





if font == "1":

    output = pyfiglet.figlet_format(kelime, font = "isometric1"  )
    print(output)

elif font == "2":

    output = pyfiglet.figlet_format(kelime, font = "letters"  )
    print(output)

elif font == "3":

    output = pyfiglet.figlet_format(kelime, font = "banner3-D"  )
    print(output)
elif font == "4":


    output = pyfiglet.figlet_format(kelime, font = "5lineoblique"  )
    print(output)
elif font == "5":


    output = pyfiglet.figlet_format(kelime, font = "digital"  )
    print(output)

elif font == "6":

    output = pyfiglet.figlet_format(kelime, font = "3-D"  )
    print(output)


elif font == "7":

    kullanici = input(">>>[+]FONT GİRİNİZ: ")
    output = pyfiglet.figlet_format(kelime, font = kullanici  )
    print(output)


input()

