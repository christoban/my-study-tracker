from datetime import datetime
class StudySession:
    def __init__(self, date, duration, notes):
        self.date = date
        self.duration = duration
        self.notes = notes

    @property
    def date(self):
        return self._date
    @property
    def duration(self):
        return self._duration
    @property
    def notes(self):
        return self._notes
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("The date must be a string (format YYYY-MM-DD)")
        try:
            dateFormat = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError ("OhOH! The format used is incorrect. Instead use this format YYYY-MM-DD.")
        self._date = dateFormat
    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, (int, float)):
            raise TypeError("The duration must be of int or float type")
        if duration <= 0:
            raise ValueError("The duration must be strictly positive, that means bigger than 0")
        self._duration = duration
    @notes.setter
    def notes(self, notes):
        if not isinstance(notes, str):
            raise TypeError("The notes must be of string type")
        self._notes = notes

    def to_dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "duration": self.duration,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            date=data.get("date", ""),
            duration=data.get("duration", 0),
            notes=data.get("notes", "")
        )
    
    def __str__(self):
        return f"The study session of {self.date} lasted {self.duration} and here are the notes {self.notes}."
    
    def __repr__(self):
        return f"StudySession(date='{self.date}', duration={self.duration}, notes='{self.notes}')"
