from models.ride import Ride
from models.passenger import Passenger

class SimpleCLI:
  def __init__(self):
    self.commands = {}

  def add_command(self, name, function):
    self.commands[name] = function

  def run(self):
    while True:
      command = input("Enter a command: ")
      if command == "quit":
        print("Goodbye!")
        break
      elif command in self.commands:
        self.commands[command]()
      else:
        print("Invalid command. Try again.")

class DriverCLI(SimpleCLI):
  def __init__(self, driverDAO):
    super().__init__()
    self.driverDAO = driverDAO
    self.add_command("create", self.create)
    self.add_command("read", self.read)
    self.add_command("update", self.update)
    self.add_command("delete", self.delete)

  def create(self):
    driverID = self.driverDAO.create()

    numberOfRides = int(input("Entre com o número de corridas: "))

    for _ in range(0, numberOfRides):
      name = input("Entre com o nome do passageiro: ")
      document = input("Entre com o documento do passageiro: ")

      passenger = Passenger(name=name, document=document)

      grade = int(input("Entre com a nota da corrida: "))
      distance = float(input("Entre com a distancia da corrida: "))
      value = float(input("Entre com o valor da corrida: "))

      ride = Ride(grade=grade, distance=distance, value=value, passenger=passenger)

      self.driverDAO.update(id=driverID, ride=ride)

  def read(self):
    id = input("Enter the id: ")
    person = self.driverDAO.read_by_id(id)
    if person:
      print(f"Name: {person['name']}")
      print(f"Age: {person['age']}")

  def update(self):
    id = input("Entre com o ID do Motorista: ")
    name = input("Entre com o nome do passageiro: ")
    document = input("Entre com o documento do passageiro: ")

    passenger = Passenger(name=name, document=document)

    grade = int(input("Entre com a nota da corrida: "))
    distance = float(input("Entre com a distancia da corrida: "))
    value = float(input("Entre com o valor da corrida: "))

    ride = {grade: grade, distance: distance, value: value, passenger: passenger}

    self.driverDAO.update(id=id, ride=ride)

  def delete(self):
    id = input("Enter the id: ")
    self.driverDAO.delete(id)
      
  def run(self):
    print("Welcome to the person CLI!")
    print("Available commands: create, read, update, delete, quit")
    super().run()