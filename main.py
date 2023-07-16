import threading
import time

from pynput import mouse, keyboard


class Clicker:
    __thread = None
    __running = False
    __button = mouse.Button.left
    __key = keyboard.Key.f7

    def __init__(self):
        print(f"Toggle Key: {self.__key}")
        print(f"Button: {self.__button}")

        self.__mouse = mouse.Controller()
        self.__interval = int(input("Interval (ms): ")) / 1000

        with keyboard.Listener(on_release=self.__on_release) as listener:
            listener.join()

    def __on_release(self, key):
        if not self.__key:
            self.__key = key
            print(key)
        elif self.__key is key:
            self.__running = not self.__running
            if self.__running or not self.__thread:
                print("running")
                self.__thread = threading.Thread(target=self.__loop, daemon=True)
                self.__thread.start()
            else:
                print("stopped")
                self.__thread.join()

    def __loop(self):
        while self.__running:
            self.__mouse.click(self.__button)
            time.sleep(self.__interval)


if __name__ == '__main__':
    Clicker()
