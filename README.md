# 数字パズル（Make10）

指定した整数の組み合わせと四則演算（＋−×÷）を使って、目標の数を作る式を自動生成するWebアプリです。  
Flaskを用いて構築されており、手軽にブラウザ上で遊ぶことができます。

➡️ 公開アプリ：  
https://make10-puzzle-solver.onrender.com/

---

## ✨ 特徴

- 任意の目標値（整数）を自由に指定
- 正負を含む任意の整数をスペースまたはカンマで区切って入力
- 数字の並べ替え・四則演算・括弧によって作れる数式を最大10通り出力
- スマホにも対応した軽量なWebインターフェース

---

## 🛠 使用技術

- Python 3.13.5
- Flask
- Render（無料プランでデプロイ）

---

## ▶️ ローカルでの使い方

```bash
# 仮想環境の作成（任意）
python -m venv venv

# 仮想環境の有効化（Windows）
.\venv\Scripts\activate

# パッケージのインストール
pip install -r requirements.txt

# アプリの起動
python app.py
