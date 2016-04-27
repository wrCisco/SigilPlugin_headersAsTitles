#! /usr/bin/env python3

import sys
import sigil_bs4


def files_iter(bk, on_selected):
    if on_selected:
        for file_type, file_id in bk.selected_iter():
            if file_type == 'manifest' and \
                    bk.id_to_mime(file_id) == 'application/xhtml+xml':
                yield file_id, bk.id_to_href(file_id)
    else:
        for file_id, file_href in bk.text_iter():
            yield file_id, file_href
            
def run(bk):
    if any(bk.selected_iter()):
        on_selected = True
    else:
        on_selected = False
    for file_id, file_href in files_iter(bk, on_selected):
        xhtml_file = bk.readfile(file_id)
        xhtml_soup = sigil_bs4.BeautifulSoup(xhtml_file, 'lxml')
        if xhtml_soup.h1:
            header = xhtml_soup.h1.text
        elif xhtml_soup.h2:
            header = xhtml_soup.h2.text
        elif xhtml_soup.h3:
            header = xhtml_soup.h3.text
        elif xhtml_soup.h4:
            header = xhtml_soup.h4.text
        elif xhtml_soup.h5:
            header = xhtml_soup.h5.text
        elif xhtml_soup.h6:
            header = xhtml_soup.h6.text
        else:
            header = ''
        if not xhtml_soup.head.title:
            title = xhtml_soup.new_tag("title")
            xhtml_soup.head.append(title)
        xhtml_soup.head.title.string = header
        bk.writefile(file_id, xhtml_soup.prettyprint_xhtml(indent_chars="  "))
    return 0

def main():
    print("I reached main when I should not have\n")
    return -1

if __name__ == "__main__":
    sys.exit(main())