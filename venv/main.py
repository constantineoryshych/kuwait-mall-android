# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.app import App

Window.size = (1024, 600)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Scaner"
# Window.fullscreen = True
from kivy.network.urlrequest import UrlRequest

scanObj = {"barcode": "testprod1","price": 155, "url" : "testprod1.png"},{"barcode" : "testprod2","price": 551, "url" : "testprod2.png"}}
playlist = {"title": "img_1", "url": "1.jpg"},{"title": "img_2", "url": "2.jpg"}}

class Scaner(App):
    slidesNumber = 0
    slidesCount  = 4   #OT OBSHCHEGO KOLICHESTVA NEOBHODIMO OTNEMAT 1
    def changeSlides(self, args):
        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/plain'}
        self.req = UrlRequest('http://185.25.116.24:2225/')
        self.req.wait()
        print(self.req.result, "werwrwerwer")
        if(self.slidesNumber == self.slidesCount):
            self.slidesNumber = 1
        else:
            self.slidesNumber = self.slidesNumber + 1
        self.slider.source = playlist[self.slidesNumber]["url"];

    def build(self):
        Window.bind(on_key_down=self.key_action)
        Window.bind(on_touch_down=self.on_touch_down)

        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/plain'}
        self.req = UrlRequest('http://185.25.116.24:2225/')
        self.req.wait()

        self.box         = BoxLayout()
        self.secondBox   = BoxLayout(orientation='horizontal', padding=(-700, 410 , 0, 0))
        self.slider      = Rectangle(size=(1024, 600), source='1.jpg')
        self.productCard = Rectangle(size=(1024, 600), source='')
        self.box.canvas.add(self.slider)
        self.secondBox.canvas.add(self.productCard)
        self.secondBox.canvas.opacity = 0
        self.eptyText = Label(text="", font_size=60, color=(0,0,0,1),pos_hint={'right':0},halign='left', valign='bottom')
        self.price = Label(text="125", font_size=90, color="#1e1e1e",pos_hint={'right':0},halign='left', padding_x = [420,420], valign='center')
        self.test = Button(text='', color=(0,0,0,1,), background_color=(0,0,0,0), font_size=80)

        self.wimg = Image(source='', opacity=0)
        self.box.add_widget(self.wimg, 5)
        self.box.add_widget(self.secondBox)
        self.secondBox.add_widget(self.test, 0)

        self.searchValue = "";
        Clock.schedule_interval(self.changeSlides, 3)
        return self.box

    def cheackBarcodeDataBase(self, searchValue):
        for x in self.req.result:
            print(x, "fdksjdkfjskdfjksdj")
            if(x["barcode"] == searchValue):

                if(x["barcode"].startswith("testprod") == True):
                    self.productCard.source = x["barcode"] + ".png"
                else:
                    self.productCard.source = "font_not_basse.jpg"

                self.secondBox.canvas.opacity = 1
                self.test.text = str(x["price"])
                break
            else:
                self.productCard.source = "error.png"
                self.secondBox.canvas.opacity = 1
                self.test.text = ""

    def searchScaner(self, id,  search):
        if (id != 40):
            self.searchValue = self.searchValue + search
        else:
            self.cheackBarcodeDataBase(self.searchValue)
            self.searchValue = ""

    def screenSaverDisable(self):
        self.secondBox.canvas.opacity = 0

    def key_action(self, *args):
        self.searchScaner(args[2], args[3])

    def on_touch_down(self, *args):
        self.screenSaverDisable()

if __name__ == '__main__':
    Scaner().run()
