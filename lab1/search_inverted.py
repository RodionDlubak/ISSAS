import sys
import json


def search_inverted(index, keyword):
    result = index[keyword] if keyword in index else []
    return result


if __name__ == "__main__":
    try:
        index_file = open('data/output_files/inverted_index.json', 'r')
    except:
        print("Failed to open file data/output_files/inverted_index.json")

    index = json.loads(index_file.read())
    result = search_inverted(index, sys.argv[1:][0])
    result_str = ', '.join(result)
    print(f'{sys.argv[1:][0]}: {result_str}')