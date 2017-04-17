from flask import *
import mlab
from models.link_item import LinkItem
from models.button_item import ButtonItem
app = Flask(__name__)

mlab.connect()

@app.route('/')
def home():
    return redirect('/main')

link_item = []
index_button = ['music','movie','book','clip']
button = {}

def add_data():
    count_link = -1
    count_index_button = -1

    myfile = open("link_item.txt",'r', encoding='utf-16')

    while True:
        theline = myfile.readline()

        if len(theline) == 0:
            break
        if theline[0] == '-':
            count_index_button += 1
            button[index_button[count_index_button]] = []
        else:
            count_link += 1
            button[index_button[count_index_button]].append(count_link)
            link_item.append(theline)

    myfile.close()

# add_data()

# link = LinkItem()
# link.item = link_item
# link.save()

# button_ = ButtonItem()
# button_.music = button['music']
# button_.movie = button['movie']
# button_.book = button['book']
# button_.clip = button['clip']
# button_.save()

@app.route('/main')
def main():
    # print(LinkItem.objects()[0].item)
    # print(ButtonItem.objects()[0].to_dict())
    return  render_template('hiddenpassion.html', link_item=LinkItem.objects()[0].item, button=ButtonItem.objects()[0].to_dict())

if __name__ == '__main__':
    app.run()