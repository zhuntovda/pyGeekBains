from time import sleep

class TrafficLight:

    def __init__(self, dic_color):
        self.dic_color = dic_color
        self._color = ""

    def running(self,):

        def running_revers(revers=False):
            for key in (self.dic_color.keys() if not revers else reversed(self.dic_color.keys())):
                if key == self._color:
                    continue
                self._color = key
                print(key.format("  "))
                sleep(self.dic_color[key])
            running_revers(not revers)

        running_revers()


TL = TrafficLight({"\033[41m": 7, "\033[43m": 2, "\033[42m": 10})
TL.running()