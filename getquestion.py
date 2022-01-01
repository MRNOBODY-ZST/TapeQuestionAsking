#get content from txt by line
def get_content(file_name):
    with open(file_name, 'r',encoding='utf-8') as f:
        content = f.readlines()
    return content