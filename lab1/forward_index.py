import json


def forward_index(text):
    forward_index_result = []
    words = text.replace('\n', ' ').split(' ')
    for word in words:
        lower_case_word = word.lower()
        if lower_case_word not in forward_index_result:
            forward_index_result.append(lower_case_word.lower())

    forward_index_result.sort()

    return forward_index_result


if __name__ == "__main__":
    input_filenames = ['data_1.txt', 'data_2.txt', 'data_3.txt']
    output_filename = 'data/output_files/forward_index.json'
    forward_index_results = {}
    for filename in input_filenames:
        f = open('data/input_files/' + filename, 'r')
        forward_index_results[filename] = forward_index(f.read())

    output = open(output_filename, 'w')
    output.write(json.dumps(forward_index_results, indent=4))
