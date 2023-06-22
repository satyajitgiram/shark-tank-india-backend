import json
from models import Shark

def add_sharks_from_json():
    with open('sharks_s1.json', 'r') as file:
        json_data = json.load(file)

    for data in json_data:
        shark = Shark()
        shark.name = data['shark']
        shark.bio = data['bio']
        shark.profession = data['profession']
        shark.save()
        print("Shark Added" - {data['shark']} )

# Call the function to add the sharks from JSON to the database
add_sharks_from_json()
