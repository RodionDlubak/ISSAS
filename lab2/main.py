import json
from common import common


def create_index(filenames, inverted_index):
    for filename in filenames:
        f = open('documents/' + filename, 'r')
        words = f.read().replace('.', ' ').replace(',', ' ').replace('\n', ' ').split(' ')
        for word in words:
            lower_case_word = word.lower()
            if len(word) > 0:
                if lower_case_word not in inverted_index:
                    inverted_index[lower_case_word] = []

                if filename not in inverted_index[lower_case_word]:
                    inverted_index[lower_case_word].append(filename)


def search(index, query):
    results = None
    query_words = query.split(' ')
    for query_word in query_words:
        if query_word in index:
            current_list = index[query_word]
        else:
            current_list = []
        if current_list is None:
            continue
        if results is None:
            results = current_list
            continue
        results = common(results, current_list)
    return results


def titles_by_filename(filenames, titles):
    result = []
    for filename in filenames:
        result.append(titles[filename])
    return result


def run():
    titles_file = open('titles.json')

    index = {}
    titles = json.load(titles_file)
    list_of_filenames = ["doc1.txt", "doc2.txt", "doc3.txt"]

    create_index(list_of_filenames, index)

    while True:
        input_query = input("Enter search query\n")
        if len(input_query) < 1:
            print("Error. Query should be at least one word long")
            break
        found_filenames = search(index, input_query)

        found_titles = titles_by_filename(found_filenames, titles)
        if len(found_titles) == 0:
            print("Nothing found")
        else:
            for title in found_titles:
                print("Searched words were found in: " + title)


run()