import pandas as pd
df=pd.read_csv("hotels.csv",dtype={"id":str})


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
print(df)
hotel_id=input("Enter the Hotel ID you want to book :")
hotel=Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name=input("Enter Your Name :")
    reservation_ticket= Reservation(name,hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not empty")