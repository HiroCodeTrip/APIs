import requests
import pykakasi

# 留学生が日本語の単語を調べられる様に英語に翻訳できたり、 ->日本語入力　日本語出力　   英語に翻訳できるオプション（引数にとる？　en か　ja）　
# 英語のwikiにも対応していたらいいね。 ->英語入力　英語出力　   　日本語に翻訳できるオプション（最後の方で確認）
# 必要なもの
# slack webhook?API の引数の取り方
# 文字列が何の言語かを判別するライブラリ、文章を翻訳するライブラリ(google　literate　APIでいいかもね)

#JSONデータの中からtargetをキーとしたバリューを探索して返します。
def jsonSearch(target):
    content = ""
    def jsonSearch(jsonData):
        nonlocal content
        if type(jsonData) == dict:
            for key in jsonData.keys():
                if (key==target):
                    return jsonData[key]
                content += str(jsonSearch(jsonData[key]))
        return content
    return jsonSearch

# ひらがなを漢字に変換する関数（goole) return kanji list
def hira_to_kanji(any_words):
    google_transliterate_url = "http://www.google.com/transliterate?"
    gt_param = {
        'langpair':'ja-Hira|ja',
        'text':any_words
    }
    convertedData = requests.get(google_transliterate_url,params=gt_param).json()
    return convertedData[0][1]

# ひらがなとカタカナを相互変換する関数 return hira or kana
def hira_kana(any_words):
    kks = pykakasi.kakasi()
    converted = kks.convert(any_words)
    convertedData = converted[0]
    return convertedData['kana'] if (convertedData['orig'] == convertedData['hira']) else convertedData['hira']


# return セット要素
def hira_kana_kanji(any_words):
    word_list = [any_words]
    kks = pykakasi.kakasi()
    converted = kks.convert(any_words)
    convertedData = converted[0]
    #any_words == kanji
    if (convertedData['orig'] != convertedData['hira']) & (convertedData['orig'] !=convertedData['kana']):
        return word_list
    # not kanji
    else:
        # any_words == ひらがな
        if (convertedData['orig'] == convertedData['hira']):
            word_list.append(hira_kana(any_words))
            word_list.extend(hira_to_kanji(any_words))
        # any_words == かたかな
        elif (convertedData['orig'] == convertedData['kana']):
            word_list.append(hira_kana(any_words))
            word_list.extend(hira_to_kanji(word_list[1]))
    return set(word_list)
