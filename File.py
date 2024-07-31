import json

#filename = 'data.json'
#def open_file_read(filename):
 #   file = open('data.json', 'r')
  #  file_content = file.read()
   # parsed_content = json.loads(file_content)
    #return parsed_content


#def open_file_write():
 #   file = open('data.json', 'w')
  #  file_write = file.write()
   # return file_write


def open_file_for_read(file_name):
    file = open(file_name, 'r')
    file_content = file.read()
    data = json.loads(file_content)
    return data


def open_file_for_write(filename, data) :
    file = open(filename, 'w')
    file_content = file.write(data)
    data = json.dumps(file_content)
    return data
    