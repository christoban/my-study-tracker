from models.subject import Subject
from models.study_session import StudySession
from .motivation_api import MotivationAPI
from .storage import StorageManager

class StudyTracker:
    def __init__(self):
        self.__subjects = []
        self.__storage = StorageManager()
        self.__api = MotivationAPI()

    @property
    def subjects(self):
        return self.__subjects.copy()
    @property
    def storage(self):
        return self.__storage
    @property
    def api(self):
        return self.__api
    
    def add_subject(self, subject_name):
        exist = False
        for subj in self.__subjects:
            if subj.name == subject_name:
                exist = True
        if not exist:
            self.__subjects.append(Subject(subject_name))
    
    def add_session(self, subject):
        subj_t = None
        for subj in self.__subjects:
            if subj.name == subject:
                subj_t = subj
                break
        if subj_t:
            date = input("Fill in the session's date: ")
            duration = int(input("Enter the time you spent in minute: "))
            notes = input("Detail what you learned ")
            session = StudySession(date, duration, notes)
            subj_t.add_session(session)

    

    def save_data(self):
        self.__storage.save_data(self.__subjects)

    def load_data(self):
        self.__subjects = self.__storage.load()
    def get_motivation(self):
        return self.__api.get_quote()