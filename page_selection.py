from collections import OrderedDict
class Page:
    def __init__(self, name, words, count=9999):
        self.name = name
        self.word_list = {word: count - i for i, word in enumerate(words)}
        self.sum = 0

def create_page(value, i, typ):
    words = value.split()
    name = typ.upper() + str(i+1)
    return Page(name, words)

def search_main(queries, pages):  
    for query in queries:
        visited =[]
        d = {}
        for word in query.word_list:
            for page_name, page in pages.items():
                if word in page.word_list and page_name not in visited:
                    visited.append(page_name)
                    sop = sum_of_products(query, page)
                    d[page_name] = sop
        d = OrderedDict(sorted(d.items(), key=lambda x: (-x[1], (x[0][0], int(x[0][1:])))))
        print_result(query.name, d)

def sum_of_products(query, page):
    sop = 0
    for qword, qweight in query.word_list.items():
        if qword in page.word_list:
            sop += qweight * page.word_list[qword]
    return sop

def print_result(name, result):
    print(name + ":", end=" ")
    for i, page_name in enumerate(result):
        if i >= 5:
            break
        print(page_name, end=" ")
    print("")

def read_from_file():
    print("Input read from input.txt file:")
    with open('input.txt') as f:
        page_index = 0
        query_index = 0
        pages = {}
        queries = []
        for line in f:
            print(line, end="")
            if line[0] == 'P':
                page = create_page(line[1:].strip(), page_index, 'p')
                pages[page.name] = page
                page_index += 1
            elif line[0] == 'Q':
                query = create_page(line[1:].strip(), query_index, 'q')
                queries.append(query)
                query_index += 1
    print("\n")
    return queries, pages
queries, pages = read_from_file()
search_main(queries, pages)
