import   string 

class   PasswordValidator:
    def __init__ (self):
        self.passwords = self.checkpassword()

    @staticmethod
    def checkpassword():
        with open('passwords.txt','r')as file:
            return {line.strip() for line in file if line}
    def is_common(self,password):
            return password in self.passwords
    def rate(self,password):
         if self.is_common in self.passwords:
            return "poor password"
         score:int = 0
         if any(c.isupper()for c in password):
             score+=1
         if any(c in string.punctuation for c in password):
            score+=1
         if len(password)>=10:
             score+=1
         if  score ==3:
             return "secure"
         elif score ==2:
             return "medium"
         else:
             return "poor"
    
         
    def main(self): 
        validator = PasswordValidator()
        print((validator.passwords))
        print(string.punctuation)
        print("WELCOME TO PASSWORD VALIDATOR 🔐")
        print ("🔑enter the password🔑")
        while True:
            password = input("enter password:").strip()
            rating = validator.rate(password)
            if rating =="secure":
                print("your password is secured ☑️")
            # elif rating == "medium":
            #     print("password is of medium strength⚠️")
            # else:
            #     print("so weak password✖️")
            #     print("try adding symbols,uppercase,lowercase and increasing the length")
            



            if len(password) < 8:
             print("Use at least 8 characters")

    # Check uppercase
            if not any(c.isupper() for c in password):
                print("Add at least one uppercase letter")

    # Check lowercase
            if not any(c.islower() for c in password):
             print("Add at least one lowercase letter")

    # Check digits
            if not any(c.isdigit() for c in password):
                print("Add at least one number")

    # Check symbols/punctuation
            if not any(c in string.punctuation for c in password):
                print("Add at least one special character (e.g., !, @, #, $)")

  
   # to detect if there are any repeating pattern "aaa"or "111" and so on !
            def repeating(password,n=3):
                for i in range(len(password)-n+1):
                    if all(password[i]==password[i+j] for j in range(n)):
                        print("patterns repeated")
                    else:
                        return False
                

if __name__ =='__main__':
    PasswordValidator().main()  

