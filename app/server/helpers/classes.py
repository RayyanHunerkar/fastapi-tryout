def class_helper(class_) -> dict:
    return {
        "id": str(class_["_id"]),
        "class_name": class_["class_name"],
        "class_code": class_["class_code"],
        "class_description": class_["class_description"],
    }