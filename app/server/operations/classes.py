from bson.objectid import ObjectId

from ..database import (
    class_collection
)

from ..helpers import (
    class_helper
)


async def retrieve_classes():
    classes = []
    async for class_ in class_collection.find():
        classes.append(class_helper(class_))
    return classes


async def add_class(class_data) -> dict:
    classes = await class_collection.insert_one(class_data)
    new_class = await class_collection.find_one({"_id": classes.inserted_id})
    return class_helper(new_class)
