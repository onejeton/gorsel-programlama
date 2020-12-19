value = input("İfade giriniz : ")
search = input("Aranacak ifade giriniz : ")

index = value.find(search)

if index > -1:
    before = value[index-1:index]
    after = value[len(search)+index:len(search)+index+1]
    print(before + search + after)
else:
    print("İfade içinde bulunamadı")
