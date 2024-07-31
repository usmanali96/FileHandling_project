import json
from File import open_file_for_read
from File import open_file_for_write
import os

username = input("Enter name")
acc_no = input("Enteer Account number")
acc_id = input("Enter Account id")

user_dic = {
    "name":username,
    "account no":acc_no,
    "Account id":acc_id,
}
filename = 'data.json'

if os.path.getsize('data.json') > 0:
    json_data = open_file_for_read(filename)
    file_data = open_file_for_write(filename)
else:
    new_data = open_file_for_write(filename, user_dic)
    new_data = json.dumps([user_dic])
    new_data.write(new_data)






    




