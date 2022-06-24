from .module import jsonOutput_Overview
import requests
import pykakasi

def main(any_words)
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

    jsonOutput_Overview_inner= jsonOutput_Overview()
    resultText = jsonOutput_Overview_inner(resultData)

    if resultText != "":
        print(resultText)
    else:
        errorText = "'{}'はエラーもしくはWikipediaに無い情報もしくは日本語ではないです。入力し直してください。".format(any_words)
        print(errorText)


if __name__ == "__main__": 
    any_words = input("Wikipediaで検索したいワードは何ですか？ ")
    main(any_words)