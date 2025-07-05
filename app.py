from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'result': a + b})

# ✅ 新しいエンドポイント
@app.route('/multiply')
def multiply():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 1))
    return jsonify({'result': a * b})

if __name__ == '__main__':
    app.run(debug=True)
