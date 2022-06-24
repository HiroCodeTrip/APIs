import requests
import pykakasi
# global宣言は変更したが、
# やはり再帰になってしまいました。

def jsonOutput_Overview():
    content = ""
    def jsonOutput_Overview(jsonData):
        nonlocal content
        if type(jsonData) == dict:
            for key in jsonData.keys():
                if (type(jsonData[key]) == str) & (key=='extract'):
                    return jsonData[key]
                content += jsonOutput_Overview(jsonData[key])
        return content
    return jsonOutput_Overview

any_words = input("Wikipediaで検索したいワードは何ですか？ ")
url = f"https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&explaintext&titles={any_words}"
resultData = requests.get(url).json()

# 予定しない動作
'''
カメはあるが亀はない問題 -->pykakasiによる変換
概要strが空文字だった場合もしくは日本語表現ではない場合(ja.wikipedia)
日本語入力では無い入力
wikipediaにない情報
不正な入力
'''

jsonOutput_Overview = jsonOutput_Overview()
resultText = jsonOutput_Overview(resultData)

if resultText != "":
    print(resultText)
else:
    print(f"'{any_words}'はエラーもしくはWikipediaに無い情報もしくは日本語ではないです。入力し直してください。")

