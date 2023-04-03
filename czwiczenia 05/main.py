import smtplib

users = {}
print(users)

users = {"lukasz": "email@gmail.com",
         "joe": "joe@gmail.com",
         "test": "test@gmail.com",
         "admin": "admin@gmail.com"}
print(users)

user1 = {"name": "lukasz", "email": "email@gmail.com"}
user2 = {"name": "joe", "email": "joe@gmail.com"}
user3 = {"name":  "test", "email":"test@gmail.com"}
user4 = {"name": "admin", "email": "admin@gmail.com"}
print(user1)

print(user1.get("name"))
print(users.get("lukasz"))
print(users.get("alice", "Invalid username"))

#print(users["alice"])
users["alice"] = "alice@gmail.com"
print(users["alice"])

#deleting user
if "alice" in users:
    del users["alice"]
print(users)

users["alice"] = "alice@gmail.com"
if "alice" in users:
    print(users.pop("alice"))
#wypisywanie key - username
for e in users:
    print(e)

# wypisywanie key - username
for e in users.keys():
    print(e)

# wypisywanie key and value - username and emails
for key, value in users.items():
    print("key is " + key + " values is " + value)

# wypisywanie value - emails
for value in users.values():
    print(value)

#sortowanie wartosci
sorted_dict = {}
for key in sorted(users.keys()):
    sorted_dict[key] = value

#sortowanie wartosci w inne strone
sorted_dict = {}
for key in sorted(users.keys(), reverse = True):
    value = users[key]
    sorted_dict[key] = value
print(sorted_dict)

users = {
    "lukasz": 100,
    "joe": 90,
    "test": 60,
    "admin": 75
}
print(users.items())

def get_value(item):
    return item[1]

sorted_values = sorted(users.items(), key = get_value)
print(sorted_values)
sorted_values = dict(sorted_values)
print(sorted_values)

dict_list = []
dict_list.append(user1)
dict_list.append(user2)
dict_list.append(user3)
dict_list.append(user4)
print(dict_list)

#wypisuje liczbe users
print(len(users))

#dodawanie hasla
for i in range(0, len(dict_list)):
     if "password" not in dict_list[i]:
         dict_list[i]["password"] = "haslo"
print(dict_list)

#zmiena hasla
for i in range(0, len(dict_list)):
     if "password" not in dict_list[i]:
         dict_list[i]["password"] = "zmieniam"
print(dict_list)

#dodawanie listy
for i in range(0, len(dict_list)):
    dict_list[i]["adresy"] = ["koszykowa 86",
                              "akademicka 9"]
print(dict_list)

#dodawanie listy
for i in range(0, len(dict_list)):
    dict_list[i]["adresy"] = {"adres 1": "koszykowa 86",
                              "adres 2": "akademicka 9"}
print(dict_list)

#czytanie z pliku i wypisywanie
filepath = "students0.txt"
with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())

##tworzenia pliku i zapisywanie danych do pliku:
#students = ["jan", "alicja"]
#filepath = "students01.txt"
#with open(filepath, "w") as file_object:
#    for e in students:
#        line = f"hello {e} \n"
#        file_object.write(line)
#
#def send_email(subject, body, sender, recipients, password):
#    msg = MINEText(body)
#    msg['Subject'] = subject
#    msg['From'] = sender
#    msg['To'] = ', '.join(recipients)
#    smtp_server = smtplib.SMTP_SSl('smtp.gmail.com', 465)
#    smtp_server.login(sender, password)
#    smtp_server.sendmail(sender, recipients, msg.as_string())
#    smtp_server.quit()



filepath = "students0.txt"
with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())





