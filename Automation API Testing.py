import requests
import json
api_endpoint = "https://bfhldevapigw.healthrx.co.in/automation-campus/create/user"
headers = {
    "roll-number": "72288652H",
    "Content-Type": "application/json"
}


def  positive_case():
    data = {
        "firstName": "Devashish",
        "lastName": "Bhor",
        "phoneNumber": 8329284273,
        "emailId": "bhordevashish0@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 200:
        print("Positive Test Case: User account created successfully with all fields having new values")
        print("printting",response.content)
        print("Message==",(json.loads((response.content.decode('utf-8').replace("\'",'')).replace("'",'"')))['message'])
    else:
        print("Positive Test Case: Failed")
        print("Message==",(json.loads((response.content.decode('utf-8').replace("\'",'')).replace("'",'"')))['message'])





def  missing_roll_number():
    data = {
        "firstName": "Akanksha",
        "lastName": "Ghule",
        "phoneNumber": 4455663312,
        "emailId": "akankshaghule.sknsitssse.comp@gmail.com"
    }
    response = requests.post(api_endpoint,headers={"roll-number":'',"content-type":"application/json"}, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Missing roll number - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Missing roll number - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])







def  missing_first_name():
    data = {
        "lastName": "User",
        "phoneNumber": 775588996,
        "emailId": "randomemailid1@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Missing first name - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Missing first name - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])




def  missing_last_name():
    data = {
        "firstName": "Test",
        "phoneNumber": 8762462334,
        "emailId": "randomemailid1@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Missing last name - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Missing last name - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])





def  missing_phone_number():
    data = {
        "firstName": "Test",
        "lastName": "User",
        "emailId": "randomemailid1@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Missing phone number - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Missing phone number - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])






def  missing_email_id():
    data = {
        "firstName": "Test",
        "lastName": "User",
        "phoneNumber": 1222211
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Missing email ID - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Missing email ID - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])






def  duplicate_roll_number():
    data = {
        "firstName": "Test",
        "lastName": "User",
        "phoneNumber": 134324254,
        "emailId": "randomemailid1@gmail.com"
    }
    response1 = requests.post(api_endpoint, headers=headers, json=data)
    response2 = requests.post(api_endpoint, headers=headers, json=data)
    if response2.status_code == 400:
        print("Negative Test Case: Duplicate roll number - Passed")
        print("Message==",(json.loads(response2.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Duplicate roll number - Failed")
        print("Message==",(json.loads(response2.content.decode('utf-8').replace("'",'"')))['message'])








def  duplicate_phone_number():
    data1 = {
        "firstName": "Test",
        "lastName": "User",
        "phoneNumber": 990909090,
        "emailId": "randomemailid132@gmail.com"
    }
    data2 = {
        "firstName": "Test",
        "lastName": "User",
        "phoneNumber": 990909093,
        "emailId": "randomemailid132@gmail.com"
    }
    response1 = requests.post(api_endpoint, headers=headers, json=data1)
    response2 = requests.post(api_endpoint, headers=headers, json=data2)
    if response2.status_code == 400:
        print("Negative Test Case: Long first name - Passed")
        print("Message==",(json.loads((response2.content.decode('utf-8').replace("\'",'')).replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Long first name - Failed")
        print("Message==",(json.loads((response2.content.decode('utf-8').replace("\'",'')).replace("'",'"')))['message'])


    # data1 = {
    #     "firstName": "Test",
    #     "lastName": "User",
    #     "phoneNumber": 987789099,
    #     "emailId": "someTestEmailID232@test.com"
    # }
    # data2 = {
    #     "firstName": "Test",
    #     "lastName": "User",
    #     "phoneNumber": 987789099,
    #     "emailId": "someTestEmailID245@test.com"
    # }
    # response1 = requests.post(api_endpoint, headers=headers, json=data1)
    # response2 = requests.post(api_endpoint, headers=headers, json=data2)
    # if response2.status_code == 400:
    #     print("Negative Test Case: Duplicate phone number - Passed")
    #     print("Message==",(json.loads(response2.content.decode('utf-8').replace("'",'"')))['message'])
    # else:
    #     print("Negative Test Case: Duplicate phone number - Failed")
    #     print("Message==",(json.loads(response2.content.decode('utf-8').replace("'",'"')))['message'])





def  duplicate_email_id():
    data1 = {
        "firstName": "Test1",
        "lastName": "User1",
        "phoneNumber": 9999999998,
        "emailId": "randomemailid111@gmail.com"
    }
    data2 = {
        "firstName": "Test2",
        "lastName": "User2",
        "phoneNumber": 9999999997,
        "emailId": "randomemailid111@gmail.com"
    }
    response1 = requests.post(api_endpoint, headers=headers, json=data1)
    response2 = requests.post(api_endpoint, headers=headers, json=data2)
    if response2.status_code == 400:
        print("Negative Test Case: Duplicate email ID - Passed")
        print("Message==",(json.loads(response2.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Duplicate email ID - Failed")
        print("Message==",(json.loads(response2.content.decode('utf-8').replace("'",'"')))['message'])





def  invalid_phone_number():
    data = {
        "firstName": "Test",
        "lastName": "User",
        "phoneNumber": "12345",
        "emailId": "randomemailid1@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Invalid phone number - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Invalid phone number - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])





def  invalid_email_id():
    data = {
        "firstName": "Test",
        "lastName": "User",
        "phoneNumber": 3452783059,
        "emailId": "invalidEmail"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:

        print("Negative Test Case: Invalid email ID - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Invalid email ID - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])




def  long_first_name():
    data = {
        "firstName": "A"*9000,
        "lastName": "User",
        "phoneNumber": 3452783059,
        "emailId": "randomemailid132@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Long first name - Passed")
        print("Message==",(json.loads((response.content.decode('utf-8').replace("\'",'')).replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Long first name - Failed")
        print("Message==",(json.loads((response.content.decode('utf-8').replace("\'",'')).replace("'",'"')))['message'])


def  long_last_name():
    data = {
        "firstName": "A",
        "lastName": "User"*900,
        "phoneNumber": 3452783059,
        "emailId": "randomemailid132@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Long first name - Passed")
        print("Message==",(json.loads((response.content.decode('utf-8').replace("\'",'')).replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Long first name - Failed")
        print("Message==",(json.loads((response.content.decode('utf-8').replace("\'",'')).replace("'",'"')))['message'])



def  integer_as_firstname():
    data = {
        "firstName": 23524534,
        "lastName": "user",
        "phoneNumber": 66677755,
        "emailId": "randomemailid3@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Long last name - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Long last name - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])

def  integer_as_lastname():
    data = {
        "firstName": 'User',
        "lastName": 324244353,
        "phoneNumber": 66677755,
        "emailId": "randomemailid3@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Long last name - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Long last name - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])



def  symbols_in_firstname():
    data = {
        "firstName": "#$%asg",
        "lastName": "user",
        "phoneNumber": 66677755,
        "emailId": "randomemailid3@gmail.com"
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 400:
        print("Negative Test Case: Long last name - Passed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])
    else:
        print("Negative Test Case: Long last name - Failed")
        print("Message==",(json.loads(response.content.decode('utf-8').replace("'",'"')))['message'])




# Execute the test cases
Test_Cases=['positive_case()','missing_roll_number()','missing_first_name()','missing_last_name()','missing_phone_number()','missing_email_id()','duplicate_roll_number()','duplicate_phone_number()','duplicate_email_id()','invalid_phone_number()','invalid_email_id()','long_first_name()','long_last_name()','integer_as_firstname()','integer_as_lastname()']
for i in range(len(Test_Cases)):
    print("\n\nTest Case No.",i+1,'====>',Test_Cases[i])
    exec(Test_Cases[i])
