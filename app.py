from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Mengambil data dari form POST
    name = request.form.get('name', '')
    message = request.form.get('message', '')
    
    # Validasi data
    if not name:
        return {
            'success': False,
            'error': 'Nama harus diisi!'
        }, 400
    
    # Proses data
    result = f"Halo {escape(name)}, {escape(message)}"
    
    return {
        'success': True,
        'message': result,
        'data': {
            'name': name,
            'message': message
        }
    }

if __name__ == "__main__":
    app.run(debug=True)
