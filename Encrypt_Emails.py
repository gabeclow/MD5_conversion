import hashlib

open('result_list', 'w').close()  #clear result_list each run

def encrypt_string(hash_string):
    result = hashlib.md5(hash_string.encode())
    # print(result.hexdigest())
    return result.hexdigest()

def sha_encrypt(hash_string):
    result = hashlib.sha256(hash_string.encode())
    # print(result.hexdigest())
    return result.hexdigest()
 
list_to_encrypt = open('contact-list-template.csv', "r")

def add_md5_email(email):
    doc = open('result_list', "a")
    doc.write(email + ", " + encrypt_string(email))
    doc.write("\n")
    doc.close()

def add_sha256_email(email):
    doc = open('result_list', "a")
    doc.write(email + ", " + sha_encrypt(email))
    doc.write("\n")
    doc.close()

for line in list_to_encrypt:
    email_string = line.replace('\n','')
    # print(email_string)
    add_sha256_email(email_string)
