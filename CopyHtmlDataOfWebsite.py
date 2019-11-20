from urllib import request
urldata = r'https://www.geeksforgeeks.org/scope-resolution-operator-or-this-pointer-in-cpp/'
def dfi(url):
    fileOpen = request.urlopen(url)
    file_info = fileOpen.read()
    file_info_str = str(file_info)
    file_lines = file_info_str.split('\\n')

    newfile = open('copyfile.txt',"w")

    for info in file_lines:
        newfile.write(info + '\n')
    newfile.close()
dfi(urldata)