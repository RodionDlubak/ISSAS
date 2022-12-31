import sys
import json


def search_forward(index, keyword):
    result = []
    for filename in index:
        if keyword in index[filename]:
            result.append(filename)
    return result


if __name__ == "__main__":
    try:
        index_file = open('data/output_files/forward_index.json', 'r')
    except:
        print("Failed to open file data/output_files/forward_index.json")

    index = json.loads(index_file.read())
    result = search_forward(index, sys.argv[1:][0])
    result_str = ', '.join(result)
    print(f'{sys.argv[1:][0]}: {result_str}')
