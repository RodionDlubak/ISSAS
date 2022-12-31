import json


def inverted_index(text, index_result, filename):
    words = text.replace('\n', ' ').split(' ')
    for word in words:
        lower_case_word = word.lower()
        if len(word) > 0:
            if lower_case_word not in index_result:
                index_result[lower_case_word] = []

            if filename not in index_result[lower_case_word]:
                index_result[lower_case_word].append(filename)

    return


if __name__ == "__main__":
    input_filenames = ['data_1.txt', 'data_2.txt', 'data_3.txt']
    output_filename = 'data/output_files/inverted_index.json'
    inverted_index_results = {}
    for filename in input_filenames:
        f = open('data/input_files/' + filename, 'r')
        inverted_index(f.read(), inverted_index_results, filename)

    output = open(output_filename, 'w')
    output.write(json.dumps(inverted_index_results, indent=4))
