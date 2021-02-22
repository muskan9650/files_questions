import json
with open("user.json") as data_file:    
    data = json.load(data_file)

    users = data['users']

    for user in users:
        counter = 0
        #print ("users full name is " + user["firstName"] + ' ' + user["lastName"])
    while counter < len(user['details']):
        if counter==1:
            print ("users full name is " + user["firstName"] + ' ' + user["lastName"])
            print ("users mobile number is ",  user['details']['mobileNo'])
            print ("users age  is ",  user['details']['age'])
            print ("users city is ",  user['details']['City'])
        counter+=1