from bson.objectid import ObjectId

class DriverDAO:
  def __init__(self, database):
    self.db = database

  def create(self):
    try:
      res = self.db.collection.insert_one({"nota": 0, "corridas": []})
      print(f"Driver created with id: {res.inserted_id}")
      return res.inserted_id
    except Exception as e:
      print(f"An error occurred while creating Driver: {e}")
      return None

  def read_by_id(self, id: str):
    try:
      res = self.db.collection.find_one({"_id": ObjectId(id)})
      print(f"Driver found: {res}")
      return res
    except Exception as e:
      print(f"An error occurred while reading Driver: {e}")
      return None

  def update(self, id: str, ride):
    try:
      driver = self.read_by_id(id)
      if len(driver['corridas']) > 0:
        ridesLength = len(driver['corridas'])
      else :
        ridesLength = 1
      
      newGrade = ((driver['nota'] * ridesLength) + ride.grade) / ridesLength

      res = self.db.collection.update_one(
        {"_id": ObjectId(id)}, {"$set": {"nota": newGrade}, "$addToSet": {"corridas": {
          "nota": ride.grade,
          "distancia": ride.distance,
          "valor": ride.value,
          "passageiro": {
            "nome": ride.passenger.name,
            "document": ride.passenger.document
          },
        }}}
      )
      print(f"Driver updated: {res.modified_count} document(s) modified")
      return res.modified_count
    except Exception as e:
      print(f"An error occurred while updating Driver: {e}")
      return None

  def delete(self, id: str):
    try:
      res = self.db.collection.delete_one({"_id": ObjectId(id)})
      print(f"Driver deleted: {res.deleted_count} document(s) deleted")
      return res.deleted_count
    except Exception as e:
      print(f"An error occurred while deleting Driver: {e}")
      return None