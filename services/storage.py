import json
from json import JSONDecodeError
from models.subject import Subject 
class StorageManager:
    def save_data(self, subjects):
        if not isinstance(subjects, list):
            raise TypeError("subjects must be of list type")
        subjectsList = []
        for subject in subjects:
            subjectsList.append(subject.to_dict())
        data = {
            "subjects": subjectsList
        }
        with open("data/data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open("data/data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []
        except JSONDecodeError:
            raise ValueError("Could not Decode the Json file")
        subjects_data = data.get("subjects", [])
        subjects = []
        for subject_data in subjects_data:
            subject = Subject.from_dict(subject_data)
            subjects.append(subject)
        return subjects