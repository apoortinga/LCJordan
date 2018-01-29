credentials = {"servirmekong" : u"{\"refresh_token\": \"1/aN_Ut-zSwUo2GvDrzHJ9BFIZ8-VpBb0-c4DDkYabd40\"}",
               "servir-mekong" : u"{\"refresh_token\": \"1/3aky7YBsmeql7fFZwt1u3OVi9KmiCLDEuxGEnDF0JPQ\"}",
			   "ate" : u"{\"refresh_token\": \"1/XOND7Lh6fautTNAW_1o0vEem7DtlT1sNF6RoNvPrH8Y\"}",
			   "quyen" : u"{\"refresh_token\": \"1/K-lGnrKM1-GGQvYBgM3yU7N9OeBwkV81rFzSDJXDL0ctSxDvM05kDUeSyhvIRsNQ\"}",
			   "biplov" : u"{\"refresh_token\": \"1/IdbCW173GpLe42rnoiHR9Rv__8E-CBi0nXRmcv0U6xRxkAKp8UlzpdmbLQSPvBn8\"}",
			   "atesig" : u"{\"refresh_token\": \"1/-xQHpYCjVItDl-TI4_GHN_zyYh_9gEQRQvsbWAZTrao\"}"}

def addUserCredentials(username):
	infile = open("C:\Users\SERVIRWK\.config\earthengine\credentials","w") 
	infile.write(credentials[username])
	infile.close()
