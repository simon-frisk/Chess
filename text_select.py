import threading
import board

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


text_select = None


def set_text_select(box):
    global text_select
    text_select = box


def get_text_select():
    return text_select


class TextSelectThread(threading.Thread):
    def __init__(self, callback):
        self.callback = callback
        super(TextSelectThread, self).__init__(name='text_select_thread')
        self.start()

    def run(self):
        while True:
            text = input('Click a box: ')
            if len(text) != 2 or not text[0] in columns or not int(text[1]) in list(range(1, 9)):
                print('Invalid box!')
                continue
            row = 8 - int(text[1])
            column = columns.index(text[0])
            box = board.get_box(row, column)
            self.callback(box)


thread = TextSelectThread(set_text_select)


def exit():
    thread.join()
