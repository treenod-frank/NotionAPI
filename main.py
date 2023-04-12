from notion_client import Client
from pprint import pprint

notion_secret = 'secret_VXQz8rG8bpjeRUxvdxoXWA0Hp1F3Xgzg0yAvGn4Bjir'
database_id = '50bbb80448324fb79fbbf41a941fd7fa'

notion = Client(auth=notion_secret)

pages = notion.search()
notionDb = notion.databases.query(database_id=database_id)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pprint(notionDb['results'][0]['properties']['점수'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
