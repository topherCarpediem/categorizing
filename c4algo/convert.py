import os
import re
import json
import docx2txt
import PyPDF2

category = { }

def read_training_set():
    
    with open('training_set.json') as json_data:
        for key, value in json.load(json_data).items():
            yield key, value


def read_file(filepath):
    
    extension = os.path.splitext(filepath)[1].lower()

    if extension == '.docx':

        content = docx2txt.process(filepath)
        for item in re.sub(r'(\W+)', ' ', content).split(' '):
            yield item

    elif extension == '.pdf':
        pdfFileObj = open(filepath, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        pdf_content = ' '

        for i in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            page_content = pageObj.extractText()
            pdf_content += ' ' + page_content
        
        for item in re.sub(r'(\W+)', ' ', pdf_content).split(' '):    
            yield item


def distinguish(filepath):
    print(30 * "=")
    print('Reading the training set....')
    print(30 * "=")
    print('Reading the file...')
    print(30 * "=")
    for key, value in read_training_set():
        for k, v in value.items():
            category[k] = 0
            for item in read_file(filepath):
                for i in v:
                    if i == item:
                        category[k] = category[k] + 1
                        
        
    for key, value in category.items():
        print(key,": ",value, "occurence")

    print(60 * "*")
   
    column = max(category, key=category.get)
    table = [k for k, v in read_training_set() if column in v]
    
    result = { "table": ''.join(table), "column": column  }

    print('Highest occurence is', column, "with", category[column], "occurences")
    print(60 * "*")
   
    return json.dumps(result)

