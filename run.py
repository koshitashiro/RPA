#run.py
import os
import sys

# プロジェクトのルートディレクトリを取得する
root_dir = os.path.dirname(os.path.abspath(__file__))

# src/main.py を読み込む
sys.path.append(os.path.join(root_dir, 'src'))
from main import main

# my_function を実行する
main()