class Persona:
    def __init__(self, name, surname, post):
        self.name = name
        self.surname = surname 
        self.post = post    
persona = Persona("Иван", "Иванов", "Программист")

class Time:
    def __init__(self, work, after, fine):
        self.work = work
        self.after = after
        self.fine = fine
time = Time(50, 3, 1)

class Payment:
    def __init__(self, oklad, premium, material):
        self.oklad = oklad
        self.premium = premium
        self.material = material
payment = Payment(400, 600, 300)

print(persona.post +" "+ persona.name +" "+ persona.surname + " получит зарплату в размере "+ str(payment.premium+payment.material+(payment.oklad*(time.work-time.fine))+((payment.oklad*2)*time.after)))