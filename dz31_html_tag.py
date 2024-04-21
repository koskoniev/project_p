import codecs
import string

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        html = html[html.find("<body>"):html.find("</body>")]
        output = str()
        tag_begin = ("<h1", "<p")
        tag_end = ("</h1>", "</p>")
        # count = html.count(tag_end[0]) + html.count(tag_end[1])
        # print(count)
        # print(range(tag_close))
        html.find("")
        for i in range(len(tag_end)):
        # for i in range(1):
            # print(tag_begin[i], tag_end[i])
            next = 0
            while next != -1:
                start = html.find(tag_begin[i], next)
                end = html.find(tag_end[i], start)
                print(html.find(tag_end[i], start))

                output += html[start:end].replace(tag_begin[i] + ">", '\n')
                next = html.find(tag_begin[i], end)
                print(tag_begin[i], tag_end[i], "start:", start, "end:", end, "next:", next)

        # print(range(len(tag_close)))
        # next = 0
        # next = 0
        # while count > 0:
        #     for t in range(len(tag_close)):
        #         start = html.find(tag_open[t], next)
        #         end = html.find(tag_close[next + 1])
        #         next = html.find(tag_close[t], end)
        #         # print(html.find(tag_open[t]), html.find(tag_close[t]))
        #         output += html[start:end]
        #         count -= 1

            


    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write(output)


html_text = "draft.html"
print(html_text)
print(delete_html_tags(html_text))
# s = "d"
# print(html_text.find(s, int(html_text.find(s)) + 1))
