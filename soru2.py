
extension = ['edu.tr', 'com', 'org', 'net']

url = "www.alierbey.com"

def urlControl(url):
    for x in range(len(url)):
        for y in extension:
            if url[x:] == '.' + y:
                return True

    return False

print(urlControl(url))