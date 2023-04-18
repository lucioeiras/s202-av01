from config.database import Database
from services.driver import DriverDAO
from cli import DriverCLI

db = Database(database="uber", collection="motoristas")
driverDAO = DriverDAO(database=db)

driverCLI = DriverCLI(driverDAO)
driverCLI.run()