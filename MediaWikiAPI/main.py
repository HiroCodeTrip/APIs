from .module import jsonOutput_Overview,hira_kana_kanji
import requests
import pykakasi

def main(any_words)    
    any_words = input("Wikipediaで検索したいワードは何ですか？ ")
    word_list = hira_kana_kanji(any_words)

    wiki_url = "https://ja.wikipedia.org/w/api.php"
    wiki_params = {
            'action':'query',
            'format':'json',
            'prop':'extracts',
            'exintro':True,
            'explaintext': True,
            'titles':'',
        }

    resultTexts = ""

    i = 1
    for word in word_list:
        #文字列のリストだった場合
        wiki_params['titles'] = word
        resultData = requests.get(wiki_url,params=wiki_params).json()
        jsonOutput_Overview = jsonSearch('extract')
        resultText = jsonOutput_Overview(resultData)
        if resultText != "":    
            resultTexts += "{},{}\n\n".format(i,resultText)
            resultTexts.replace(' ','')
            i+=1

    try:
        #resultTextは必ず文字列で返ってくるので空文字列の場合のみを処理する
        if resultTexts == "":
            raise Exception
        print(resultTexts)
    except:
        errorText = "'{}'は入力エラーもしくはWikipediaに無い情報です。入力し直してください。".format(any_words)
        print(errorText)


if __name__ == "__main__": 
    any_words = input("Wikipediaで検索したいワードは何ですか？ ")
    main(any_words)