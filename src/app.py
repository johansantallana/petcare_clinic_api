from flask import Flask, jsonify
app = Flask(__name__)

#Ruta de pueba
@app.route('/')
def home():
    return jsonify({
        "message": "PetCare CLinic API",
        "status": "runing"
    })
    
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True)