import codecs
import string

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        
        while html.count(">") > 0:
            html = html.replace(html[html.find("<"):html.find(">") + 1], "")
        
        while html.count("\n\n") > 0:
            html = html.replace("\n\n", "\n")


    with codecs.open(result_file, 'w', 'utf-8') as result:
        res_html = result.write(html)
        file.close()
        result.close()


html_text = "draft.html"
print(html_text)
print(delete_html_tags(html_text))
