import re
import json
import docx2txt

category = { }

def read_training_set():
    with open('training_set.json') as json_data:
        for key, value in json.load(json_data).items():
            yield key, value


def read_file(filepath):
    content = docx2txt.process(filepath)
    for item in re.sub(r'(\W+)', ' ', content).split(' '):
        yield item


def distinguish(filepath):
    for key, value in read_training_set():
        for k, v in value.items():
            category[k] = 0
            for item in read_file(filepath):
                for i in v:
                    if i == item:
                        category[k] = category[k] + 1
                        
        
    print(k, category[k], end='\r')
    return category

