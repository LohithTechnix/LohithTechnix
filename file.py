# file_name = input()
# file1 = open(file_name,'r')#w,a+,r,w,w+
# content = file1.readlines()
# # file.write('Hello I am Lohith good day')
# print(content)


# import webbrowser

# webbrowser.open('www.onedrive.live.com')


# file_name = input()
# file1 = open(file_name,'w')#w,a+,r,w,w+
# content = file1.readlines()
# file1.write('Krishna Kanth')
# print(content)


# content1 = tuple(content)

file_name = input('Script name : ')
file = open(file_name,'w')
sons1 = int(input('Enter a value for sons:'))
print(sons1)
daughters1 = int(input('Enter a value for daughters:'))
print(daughters1)
# content1 = file.readlines()
# print(content1)
son = str(sons1)
daughter = str(daughters1)
file.write(son)
file.write(daughter)

print('children equals', sons1 + daughters1)
exit

