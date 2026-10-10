from flask import Flask, jsonify, request
from repository.database import db
from db_models.payment import Payment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)

@app.route("/payments/pix", methods=['POST'])
def create_pix_payment(): 
   data = request.get_json()

   # Validaçoes
   if 'value' not in data:
       return jsonify({"error": "Missing value"}), 400

   if 'expiration_date' not in data:
       return jsonify({"error": "Missing expiration_date"}), 400

   payment = Payment(
       value=data['value'],
       expiration_date=data['expiration_date']
   )
   db.session.add(payment)
   db.session.commit()

   return jsonify({"status": "created", "payment_id": payment.id}), 201


@app.route("/payments/pix/confirmation", methods=['POST'])
def confirm_pix_payment():
    return jsonify({"status": "confirmed"})

@app.route("/payments/pix/<payment_id>", methods=['GET'])
def get_pix_payment(payment_id):
    return jsonify({"status": "retrieved", "payment_id": payment_id})

if __name__ == "__main__": 
    app.run(debug=True)