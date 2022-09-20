import os


def statistic(path):
    files = os.listdir(path)
    print(files)
    allfile ='./allpaper/allpaper1.txt'
    result = open(allfile, 'a', encoding='utf-8')
    for file in files:
        text_dir = path + '\\' + file
        print(text_dir)
        f = open(text_dir, 'r', encoding='utf-8')
        article = f.read()
        if len(article) > 3000:
            content = article.encode('utf-8').decode('utf-8')[0:3000]  # 截取字段
        result.write(content + '\n')  # 合并文件


if __name__ == '__main__':
    path = r"C:\Users\黄某人\PycharmProjects\papercarwling\papertxt1"
    statistic(path)
