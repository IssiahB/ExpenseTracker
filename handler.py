from database import database_decorator
from datetime import datetime

class DatabaseEntry:
    def __init__(self, desc: str, amount: int, entry_type: str, date=None, reoccur=False, reoccur_type=None):
        if desc is None or amount is None or entry_type is None:
            raise ValueError('Invalid values given to construct DatabaseEntry. Value of None')
        
        self.handle_types(entry_type, reoccur_type)
        self.date = self.handle_date(date)
        self.reoccur = reoccur 
        self.desc = desc
        self.amount = amount

    def handle_date(self, date: str):
        if date is None:
            return datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        else:
            return date
        
    def handle_types(self, entry_type: str, reoccur_type: str):
        allowed_entry_types = ['income', 'expense']
        allowed_reoccur_types = ['weekly', 'biweekly', 'monthly']
        if (entry_type in allowed_entry_types):
            self.entry_type = entry_type
        else:
            raise ValueError('Database Entry must have a correct value for arg entry_type (income | expense)')

        if reoccur_type in allowed_reoccur_types:
            self.reoccur_type = reoccur_type
        else:
            self.reoccur_type = None

@database_decorator
def addEntry(db, entry: DatabaseEntry):
    cursor = db.cursor()    
    cursor.execute("""
        INSERT INTO entries (description, date, type, amount, reoccur, reoccur_type)
                VALUES (?, ?, ?, ?, ?, ?)
    """, (entry.desc, entry.date, entry.entry_type, entry.amount, int(entry.reoccur), entry.reoccur_type))
    db.commit()

@database_decorator
def deleteEntry(db, id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM entries WHERE id = ?", (id))
    db.commit()

@database_decorator
def getEntries(db, type: str):
    valid_types = ['income', 'expense']
    if type in valid_types:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM entries WHERE type = ?", (type))
        db.commit()
    else:
        raise ValueError('Entry type must be (expense | income)')

