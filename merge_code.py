# #Taking 3 text files as input and giving a final text file(result.txt) as output after merging unique elements from all 3 given input texts
# # try:
# f1 = open("x1.txt")
# string1=f1.read()
# f2 = open("x2.txt")
# string2=f2.read()
# f3=  open("x3.txt")
# string3 =f3.read()

# f1.close()
# f2.close()
# f3.close()
# string4=string1.splitlines()
# string5=string2.splitlines()
# string6=string3.splitlines()
# set1= set(string4)
# set2=set(string5)
# set3= set(string6)
# set_after_merge = set1.union(set2)
# final_set=set3.union(set_after_merge)
# set1.clear()
# set2.clear()
# set3.clear()
# s = '\n '
# with open('result.txt', 'a+') as f:
#   f.write(s.join(final_set))
# # except:
# #     print("An exception occured")


f1 = open('/home/cadbury/Desktop/download_and_extract_files/Output/extracted1/BL/webtv/domains')
string1 = f1.read()
f1.close()

string2=''
print("CHECK1")
print(string1.splitlines())
print("CHECK2")
print(string2.splitlines())