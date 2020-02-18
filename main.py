import requests
import random
from kivy.app import App
from kivy.lang.builder import Builder
# from kivy.uix.button import Button
# from kivy.uix.image import Image, AsyncImage
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config


def get_data(book, attribute):
    # req1 = requests.get(
    #     f'http://127.0.0.1:5000/books')
    req1 = requests.get(
        f'http://chaos565.pythonanywhere.com/books')
    requested_info = req1.json()[book].get(attribute)
    return requested_info


# req2 = requests.get(
#     f'http://127.0.0.1:5000/books')

req2 = requests.get(
    f'http://chaos565.pythonanywhere.com/books')

# req3 = requests.get(
#     f'http://127.0.0.1:5000/genres')

req3 = requests.get(
    f'http://chaos565.pythonanywhere.com/genres')

# req4 = requests.get(
#     f'http://127.0.0.1:5000/genres/books/1')

req4 = requests.get(
    f'http://chaos565.pythonanywhere.com/genres/books/1')

# req5 = requests.get(
#     f'http://127.0.0.1:5000/genres/books/2')

req5 = requests.get(
    f'http://chaos565.pythonanywhere.com/genres/books/2')

bookbygenre1 = []
bookbygenre2 = []

genres = []

[genres.append(category['category_name']) for category in req3.json()]
[bookbygenre1.append(name1['name']) for name1 in req4.json()]
[bookbygenre2.append(name2['name']) for name2 in req5.json()]
print(bookbygenre1)
print(genres)
titles = []
authors = []
annotations = []
prices = []
categories = []
status = []
images = [
    'images/orwell1.jpg',
    'images/Pythoncrash.png',
    'images/lord.jpg',
    'images/pythonhard.jpg',
    'images/pythonhard.jpg',
    'images/pythonhard.jpg',
    'images/pythonhard.jpg',


]
buy_images = [
    'images/buy.jpg',
    'images/buy1.jpg',
    'images/buy2.jpg',
    'images/buy3.jpg',
    'images/buy4.jpg'


]
buy_im = random.choice(buy_images)
# def buy_image():
#     for image in buy_images:
#         random.choice(buy_images)
#         return image
[titles.append(name['name']) for name in req2.json()]
[authors.append(author['author_name']) for author in req2.json()]
[annotations.append(annotation['product_description'])
 for annotation in req2.json()]
[prices.append(str(price['price'])) for price in req2.json()]
[categories.append(category['category']) for category in req2.json()]
[status.append(status_['status']) for status_ in req2.json()]

x = "images/bookfon1.jpg"

genrebutton1 = ''
genrebutton2 = ''
button = ''
screen = ''
for name_3 in bookbygenre1:
    if name_3:
        genrebutton1 += f"""
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: '{name_3}'
                on_press: app.root.current = "{name_3}"
"""
for name_4 in bookbygenre2:
    if name_4:
        genrebutton2 += f"""
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: '{name_4}'
                on_press: app.root.current = "{name_4}"
"""
for name in titles:
    if name:
        button += f"""
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: '{name}'
                on_press: app.root.current = "{name}"
"""
        bookauthor = str(authors[0])
        bookannot = str(annotations[0])
        bookprice = str(prices[0])
        bookcateg = str(categories[0])
        bookstatus = str(status[0])
        bookimage = str(images[0])

        screen += f"""
    Screen:
        name: "{name}"

        BoxLayout:
            canvas.before:
                Rectangle:
                    source:'fon5.jpg'
                    pos: self.pos
                    size: self.size
            orientation: "vertical"
            padding: [30, 0, 0, 0]

            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                text: "Title:" +" "+ '{name}'
                Image: 
                    size_hint_x: 0.0005
                    size_hint_y: 0.0005
                    pos: (570,50)
                    size: self.texture_size
                    source: '{bookimage}'

            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                text: "Author:" +" "+ '{bookauthor}'
            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                font_size: 12
                text: "Annotation:" +" "+ "{bookannot}"
            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                text: "Price:" +" "+ '{bookprice}' + "USD"
            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                text: "Genre:" +" "+ '{bookcateg}'
            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                text: "Status:" +" "+ '{bookstatus}'

            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Home"
                on_press: app.root.current = "main_screen"

            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Buy"
                on_press:
                    app.root.current = "buy_screen"

"""
        titles = titles[1:-1]
        authors.pop(0)
        annotations.pop(0)
        prices.pop(0)
        categories.pop(0)
        status.pop(0)
        images.pop(0)

Builder.load_string(f"""

#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import utils kivy.utils

<ScreenManager>:
    transition: SlideTransition()

    Screen:
        name: "main_screen"
        Image:
            source: '{x}'
            size: (12,12)

        BoxLayout:
            orientation: "vertical"
            Image:
                source: 'fon2.jpg'
                size: self.texture_size

            Label:
                text: "BookShop"
                color: utils.get_color_from_hex('#DFD919')
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#DFD919')
                background_normal: ''
                text: "Books"
                on_press:
                    app.root.current = "screen_1"
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#DFD919')
                text: "Book Genre"
                on_press: app.root.current = "screen_2"
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#DFD919')
                text: "Contact Us"
                on_press: app.root.current = "screen_3"
            Image:
                source: 'fon4.jpg'
                size: self.texture_size
    Screen:
        name: "screen_1"
        Image:
            source: 'images/bookfon1.jpg'
            size: (22,22)  
    
        BoxLayout:
            canvas.before:
                Rectangle:
                    source:'fon5.jpg'
                    pos: self.pos
                    size: self.size
            orientation: "vertical"
    
            Label:
                text: "Books"
                color: utils.get_color_from_hex('#12120C')
    
{button}
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Home"
                on_press: app.root.current = "main_screen"
{screen}

    Screen:
        name: 'screen_2'
    
        BoxLayout:
            canvas.before:
                Rectangle:
                    source:'fon5.jpg'
                    pos: self.pos
                    size: self.size
    
            orientation: "vertical"
    
            Label:
                text: "Book Genre"
                color: utils.get_color_from_hex('#12120C')
    
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Fiction Books"
                on_press: app.root.current = "fiction"
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Programming"
                on_press: app.root.current = "programming"

            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Home"
                on_press: app.root.current = "main_screen"
    Screen:
        name: "fiction"

        BoxLayout:
            canvas.before:
                Rectangle:
                    source:'fon5.jpg'
                    pos: self.pos
                    size: self.size

            orientation: "vertical"
    
            Label:
                text: "Fiction"
                color: utils.get_color_from_hex('#12120C')
{genrebutton1}
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Home"
                on_press: app.root.current = "main_screen"
    Screen:
        name: "programming"

        BoxLayout:
            canvas.before:
                Rectangle:
                    source:'fon5.jpg'
                    pos: self.pos
                    size: self.size

            orientation: "vertical"
    
            Label:
                text: "Programming"
                color: utils.get_color_from_hex('#12120C')
{genrebutton2}

            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Home"
                on_press: app.root.current = "main_screen"
    Screen:
        name: 'buy_screen'
    
        BoxLayout:
            canvas.before:
                Rectangle:
                    source:'fon5.jpg'
                    pos: self.pos
                    size: self.size
            orientation: "vertical"
    
            Label:
                text: "You book was send to our Delivery Service"
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                Image:
                    source: 'images/buy.jpg'
                    size: self.texture_size
                    size_hint_x: 0.0005
                    size_hint_y: 0.0005
                    pos: (300,115)                

            Label:
                text: "Thank You"
                color: utils.get_color_from_hex('#12120C')


            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
    
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Home"
                on_press: app.root.current = "main_screen"

    Screen:
        name: 'screen_3'
    
        BoxLayout:
            canvas.before:
                Rectangle:
                    source:'fon5.jpg'
                    pos: self.pos
                    size: self.size
            orientation: "vertical"
    
            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                text: "Email: makarongod@space.int"
            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                text: "Phone: 666 666 666 666"
            Label:
                halign: 'left'
                valign: 'middle'
                color: utils.get_color_from_hex('#12120C')
                text_size: self.size
                text: "Address: Hell, first circle of Hell,ask Julius Caesar"
    
            Button:
                background_color: (0, 0, 0, 0)
                color: utils.get_color_from_hex('#12120C')
                text: "Home"
                on_press: app.root.current = "main_screen"
""")

sm = ScreenManager()


class TestApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
