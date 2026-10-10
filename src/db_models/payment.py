from repository.database import db

class Payment(db.Model): 
    __tablename__ = 'payments'

    # id, value, paid, bank_payment_id, qr_code
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.String(100), nullable=True)
    qr_code = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())


    def __to_dict(self): 
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_payment_id,
            "qr_code": self.qr_code,
            "created_at": self.created_at
        }