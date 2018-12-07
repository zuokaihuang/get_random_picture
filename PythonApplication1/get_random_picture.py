import os
import urllib.request
import requests

from html.parser import HTMLParser



class GetPictureHTMLParser(HTMLParser):
    index = 0
    def handle_starttag(self, start_tag, attrs):
        if(start_tag=='img'):
            for attr in attrs:
                if(attr[0]=='src'):
                    try:
                        url = attr[1]

                        if url.startswith('//'):
                            continue
                        else:
                            img_url = attr[1]

                        img_file=urllib.request.urlopen(img_url)
                    except Exception as err:
                        print(err)
                        continue
                    else:
                        picture=img_file.read()
                    
                    if(picture.__len__() > 1000):
                        file_name = attr[1]
                        if(file_name.rfind('.')!=-1):
                            ext_index = file_name.rfind('.')
                            ext = file_name[ext_index:ext_index+4]
                            file_name =  '%s%d%s'%('picture_', self.index, ext)
                        print(file_name)
                        write_file=open('E:\\My_project\\my_python_project\\PythonApplication1\\'+file_name,'wb')
                        write_file.write(picture)
                        write_file.close()
                        self.index += 1
############################################################

def main():
    width = 300
    height = 200

    url = 'https://unsplash.it/%d/%d/?random'%(width, height)
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        print('response: ', response)
        if 300 <= response.status_code < 400:
            url = response.headers['location']
    except requests.exceptions.Timeout:
        print('timeout')
    print ('url: ', url)
    html_page = urllib.request.urlopen(url)
    source_code = html_page.read()
    output_html = open('E:\\My_project\\my_python_project\\PythonApplication1\\output.jpg','wb')
    output_html.write(source_code)
    output_html.close()

#    s = str(source_code, encoding = "utf-8")
#    parser = GetPictureHTMLParser()
#    parser.feed(s)

main()