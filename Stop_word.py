
def get_stop_dic():
    file_path = r"./stopwords_Chinese.txt"
    data = open(file_path, "r", encoding="utf-8").read()
    new_data = data.split("\n")
    new_data.append("哈")
    new_data.append('呵')
    new_data.append("啊")
    return new_data

