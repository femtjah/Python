
class Car:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        car=self.session.get("car")
        if not car:
            car=self.session["car"]={}
        #else:
        self.car=car

    def add_car(self, product):
        if(str(product.id)not in self.car.keys()):
            self.car[product.id]={
                'product_id':product.id,
                'name':product.name,
                'price':str(product.price),
                'quantity':1,
                'img':product.img.url,
            }
        else:
            for key, value in self.car.items():
                if key==str(product.id):
                    value['quantity']=value['quantity']+1
                    value["price"]=float(value["price"])+product.price
                    break
        self.save_car()
    
    def save_car(self):
        self.session['car']=self.car
        self.session.modified=True

    def remove_add(self, product):
        product.id=str(product.id)
        if product.id in self.car:
            del self.car[product.id]
            self.save_car()

    def subtract_product(self, product):
        for key, value in self.car.items():
            if key==str(product.id):
                value['quantity']=value['quantity']-1
                value["price"]=float(value["price"])-product.price
                if value['quantity']<1:
                    self.remove_add(product)
                break
        self.save_car()

    def clean_car(self):
        self.session['car']={}
        self.session.modified=True
