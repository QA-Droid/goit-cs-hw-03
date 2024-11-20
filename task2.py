from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient("mongodb://localhost:27017/")
db = client["cats_database"] 
collection = db["cats_collection"]

def create_cat(name, age, features):
    try:
        collection.insert_one({
            "name": name,
            "age": age,
            "features": features
        })
        print(f"Кіт '{name}' успішно доданий до бази даних.")
    except DuplicateKeyError:
        print("Помилка: Кіт із таким ім'ям вже існує!")
    except Exception as e:
        print(f"Помилка: {e}")

def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка: {e}")

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка: {e}")

def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count:
            print(f"Вік кота '{name}' оновлено до {new_age}.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка: {e}")

def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
        if result.matched_count:
            print(f"До кота '{name}' додано характеристику: {feature}.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка: {e}")

def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"Кіт з ім'ям '{name}' видалений.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка: {e}")

def delete_all_cats():
    try:
        collection.delete_many({})
        print("Усі записи видалені з бази даних.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("Murzik", 5, ["чорний", "ласкавий", "грає в м'яч"])

    print("\nВсі коти в базі:")
    read_all_cats()

    print("\nІнформація про кота 'Barsik':")
    read_cat_by_name("Barsik")

    print("\nОновлення віку 'Barsik':")
    update_cat_age("Barsik", 4)

    print("\nДодавання характеристики до 'Barsik':")
    add_feature_to_cat("Barsik", "грає на піаніно")

    print("\nВидалення кота 'Murzik':")
    delete_cat_by_name("Murzik")

    print("\nВидалення всіх записів:")
    delete_all_cats()