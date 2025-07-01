import pandas as pd
df=pd.read_csv("hotels.csv",dtype={"id":str})
df_card=pd.read_csv("cards.csv",dtype=str).to_dict(orient="records")
df_secure=pd.read_csv("card_security.csv",dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id=hotel_id
        self.name=df.loc[df["id"]==self.hotel_id,"name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"]="no"
        df.to_csv("hotels.csv",index=False)

    def available(self):
        availablity=df.loc[df["id"]==self.hotel_id,"available"].squeeze()
        if availablity == "yes":
            return True
        else:
            return False


class Reservation:
    def __init__(self,customer_name,hotel_object):
        self.customer_name=customer_name
        self.hotel=hotel_object

    def generate(self):
        content=f"""
        Thank you! for booking hotel with us
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class CreditCard():
    def __init__(self,number):
        self.number=number
    def validate(self,expiration,cvc,holder):
        card_reader={"number" :self.number, "expiration":expiration,"cvc":cvc,"holder":holder}
        if card_reader in df_card:
            return True
        else :
            return False

class Securecard(CreditCard):
    def authenticate(self,password):
        passowrd=df_secure.loc[df_secure["number"]==self.number,"password"].squeeze()
        if (passowrd == password):
            return True
        else:
            return False


print(df)
hotel_id=input("Enter the Hotel ID you want to book :")
hotel=Hotel(hotel_id)
if hotel.available():
    credit=Securecard(number="1234")
    if credit.validate(expiration="12/26",cvc="123",holder="JOHN SMITH"):
        if credit.authenticate(password="mypass"):
            hotel.book()
            name=input("Enter Your Name :")
            reservation_ticket= Reservation(name,hotel)
            print(reservation_ticket.generate())
        else:
            print("Your card Password is Wrong ")
    else:
        print("There is problem in Your card")
else:
    print("Hotel is not empty")