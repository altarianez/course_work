from utils import load_data, filter_sort_spisok, formatted_data


JSON_FILE = 'list.json'


def main():
    data = load_data(JSON_FILE)
    data = filter_sort_spisok(data)

    for i in range(5):
        print(formatted_data(data[i]))


if __name__ == '__main__':
    main()
