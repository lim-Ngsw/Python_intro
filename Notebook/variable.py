num = 1
name = 'Mike'
is_ok = True

print(num, type(num)) #int型
print(name, type(name)) #str型
print(is_ok, type(is_ok)) #bool型

num = name
print(num, type(num)) #str型として認識される

name = '1' #文字列としての1
new_num = int(name) #型変換
print(new_num, type(new_num)) #int型として変換される
