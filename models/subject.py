from .study_session import StudySession
class Subject:
    def __init__(self, name):
        self.name = name 
        self.__sessions = []
    
    @property
    def name(self):
        return self._name
    @property
    def sessions(self):
        return self.__sessions.copy()
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("The name must be of string type")
        name = name.strip()
        if not name:
            raise ValueError("The name cannot be empty")
        self._name = name

    def add_session(self, mySession):
        if not isinstance (mySession, StudySession):
            raise TypeError("The Session must be a StudySession object")
        self.__sessions.append(mySession)

    def total_study_time(self):
        total = 0
        for session in self.__sessions:
            total+=session.duration
        return total
    
    def to_dict(self):
        sessions = []
        for session in self.__sessions:
            sessions.append(session.to_dict())
        return {
            "name": self.name,
            "sessions": sessions
        }
    
    @classmethod
    def from_dict(cls, data):
        subject = cls(data.get("name", ""))
        sessions_data = data.get("sessions", [])
        for session_data in sessions_data:
            session = StudySession.from_dict(session_data)
            subject.add_session(session)
        return subject

    def __repr__(self):
        return f"Subject(name='{self.name}', sessions={len(self.__sessions)})"

    