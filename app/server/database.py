import motor.motor_asyncio

MONGO_DETAILS = "mongodb://djangoadmin:admin@mongo-dev:27017/?authSource=admin"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.students
student_collection = database.get_collection('student_collection')
class_collection = database.get_collection('class_collection')
user_collection = database.get_collection('user')

