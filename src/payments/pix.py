import uuid
import qrcode


class Pix: 
    def __init__(self): 
        pass

    def create_payment(self):
        # Implement the logic to create a Pix payment
        bank_payment_id = str(uuid.uuid4())

        hash_payment = f'hash_payment_{bank_payment_id}'

        # qr code
        img = qrcode.make(hash_payment)
        img.save(f'./static/img/qr_{bank_payment_id}.png')


        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f'./static/img/qr_{bank_payment_id}.png' 
        }