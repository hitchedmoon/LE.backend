from ..extensions import db
from datetime import datetime

class Ticket(db.Model):
    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True)
    ticket_name = db.Column(db.String(100), nullable=False)
    ticket_urgency = db.Column(db.Integer, default=1)
    ticket_description = db.Column(db.Text, nullable=True)
    ticket_points = db.Column(db.Integer, default=0)
    
    # The Foreign Key: links to the 'id' column in the 'users' table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Ticket {self.ticket_name}>'