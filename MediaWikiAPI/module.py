# global宣言からは変更したが、
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
