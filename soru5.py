def textCommand(value):
    if value == "receive":
        return "Gelen"
    elif value == "send":
        return "Giden"
    else:
        return -1

def getSignal(value):
    value = int(value)
    if value >= 0 and value <= 50:
        return "Çok Zayıf Sinyal"
    elif value >= 50 and value <= 100:
        return "Zayıf Sinyal"
    elif value >= 100 and value <= 150:
        return "Orta Sinyal"
    elif value >= 150 and value <= 200:
        return "Güçlü Sinyal"
    elif value >= 200 and value <= 255:
        return "Çok Güçlü Sinyal"
    return -1

def getDeviceName(value):
    value = int(value)
    if value == 1:
        return "Televizyon"
    elif value == 2:
        return "Çamaşır Suyu"
    elif value == 3:
        return "Buzdolabı"
    elif value == 4:
        return "Fırın"
    else:
        return -1

def getDeviceStatus(value):
    value = int(value)
    if value == 0:
        return "Off"
    else:
        return "On"

def getDeviceInfo(value):
    if value == 0:
        return "Cevap İstenmiyor"
    else:
        return "Cevap İsteniyor"


command = input("Komut giriniz : ")

commands = command.split('\\n')

for i in range(0, len(commands)-1):
    parametre = commands[i].split('-')

    if parametre[0] == "send" or parametre[0] == "receive":
        if getSignal(parametre[1]) == -1:
            print("Error : Birinci bölüm hatalı")
        elif getDeviceName(parametre[2]) == -1:
            print("Error : İkinci bölüm hatalı")
        elif getDeviceStatus(parametre[3]) == -1:
            print("Error : Üçüncü bölüm hatalı")
        else:
            print("Kod Tipi : " + parametre[0] + " - " + textCommand(parametre[0]))
            print("Sinyal Gücü : " + parametre[1] + " - " + getSignal(parametre[1]))
            print("Cihaz : " + parametre[2] + " - " + getDeviceName(parametre[2]))
            print("Durumu : " + parametre[3] + " - " + getDeviceStatus(parametre[3]))

            if len(parametre)-1 == 4:
                print("Cevap : " + parametre[4] + " - " + getDeviceInfo(parametre[4]))
    else:
        print("Error : send ya da receive içermiyor")
    print('-----')
