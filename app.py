from puzzle import solve_sudoku
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/solve', methods=["POST"])
def solve():
    data = request.json
    board = data.get('board')
    solution = solve_sudoku(board)
    return jsonify({"board": solution})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)