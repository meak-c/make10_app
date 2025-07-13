import os

from flask import Flask, render_template, request
from solver import solve

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error = None
    target = ''
    numbers_raw = ''

    if request.method == 'POST':
        target = request.form['target']
        numbers_raw = request.form['numbers']
        try:
            target_val = float(target)
            numbers = list(map(int, numbers_raw.replace(',', ' ').split()))
            if len(numbers) < 2:
                error = "2つ以上の数値を入力してください。"
            else:
                results = solve(target_val, numbers)
                if not results:
                    error = "条件を満たす式は見つかりませんでした。"
        except ValueError:
            error = "入力が正しくありません。"

    return render_template('index.html',
                           results=results,
                           error=error,
                           target=target,
                           numbers=numbers_raw)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
