import codecs
import string

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

        html = html[html.find("<body>"):html.find("</body>")]

        while html.count("<") > 0:
            html = html.replace(html[html.find("<a "):html.find("/a>") + 3], "")
            html = html.replace(html[html.find("<"):html.find(">") + 1], "")
            html = html.replace("\n\n", "\n")
            if html[0] == '\n':
                html = html[1:]
            # begin = html.find('\n')
            # end = html.find('\n', begin + 1)
            # if begin < end:
            #     if html[begin:end].isspace():
            #         html = html.replace(html[begin+1:end], '')
            output = html.split('\n')
            html = ""
            for i in output:
                if i.count(' ') != len(i):
                    html += i + '\n'
                    
        # print(html.count("\n\n"))
        # print(hex(ord(html[0])))
        # print(hex(ord(html[1])))
        # print()
        # ss = "0-nn       n+1"
        # print(ss[:])
        # bb = ss.find('n')
        # ee = ss.find('n', bb + 1)
        # print(f"b:{ss[bb]}, e:{ss[ee]}")
        # print(bb, ee)
        # print(ss[bb:ee])
        # print("'", ss[bb:ee], "'")
        # print(ss[bb+1:ee].isspace())
        # print(ss[:bb] + ss[ee:])
        # for i in range(html.count("\n")):
        #     # print(b, e)
        #     if html[0] == '\n':
        #         html = html[1:]

        #     b = html.find('\n')
        #     e = html.find('\n', b + 1)
        #     # e = b + 1
        #     if html[b+1:e].isspace():
        #         # html.replace(html[b:e], '')
        #         html = html[:b] + html[e:]
        # html = "" #file.readline()
        # html = html.replace(html[html.find("<"):html.find(">") + 1], "")
        # for i in html:
        #     
        # for i in file.readlines():
        #     html += i.replace(i[i.find("<"):i.find(">") + 1], "")



        # while html.count("\n\n") > 0:
        #     html = html.replace("\n\n", "\n")
        # print(html[:5])
        # html = html.split("\n")
        


    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write(html)
        # file.close()
        # result.close()

        return 

html_text = "draft.html"
print(html_text)
print(delete_html_tags(html_text))
