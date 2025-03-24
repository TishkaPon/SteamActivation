import pyautogui
import time
import cv2
import numpy as np
import win32gui
import win32con
import easyocr
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(script_dir, "templates") + "\\"

class SteamActivator:
    def __init__(self):
        self.activity_window = None
        self.input_key_coordinate = ()

    def _push_input_code(self, key):
        while True:
            hwnd = win32gui.FindWindow(None, "Steam")
            if hwnd != 0:
                time.sleep(0.5)
                break

        self.activity_window = hwnd

        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        width = right - left
        height = bottom - top

        if not self.input_key_coordinate:
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            input_code = cv2.imread(templates_dir + "input_code.png")

            input_code_h, input_code_w = input_code.shape[:2]

            templ = cv2.matchTemplate(screenshot, input_code, cv2.TM_CCOEFF_NORMED)
            button_input_code = np.where(templ >= 0.8)

            for pt in zip(*button_input_code[::-1]):
                x, y = pt

                center_x = x + (input_code_w // 2)
                center_y = y + (input_code_h // 2)

                screen_x = left + center_x
                screen_y = top + center_y

                self.input_key_coordinate = (screen_x, screen_y)
                break
        else:
            screen_x, screen_y = self.input_key_coordinate

        pyautogui.click(screen_x, screen_y)
        pyautogui.typewrite(key)
        pyautogui.press('enter')

        while True:
            screen = pyautogui.screenshot(region=(left, top, width, height))
            Loading = self._check_loading(screen)
            if not Loading:
                break

        return screen

    def _check_loading(self, img):
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        templ = cv2.imread(templates_dir + "loading.png")

        templ = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(templ)

        if max_val >= 0.8:
            return True
        else:
            return False

    def _get_answer(self, img):
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        check_templates = {
            "key_used.png": "Ключ активации уже использован",
            "invalid_key.png": "Неверный ключ активации",
            "key_activated.png": "Активация успешно выполнена: ",
            "activate_main_game.png": 'Активируйте сначала основную игру',
            "product_available.png": "У вас уже есть этот продукт"
        }

        for templ_photo in check_templates:
            template = cv2.imread(templates_dir + templ_photo)

            templ = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(templ)

            if max_val >= 0.8:
                if templ_photo == "key_activated.png":
                    x, y = max_loc
                    h, w = template.shape[:2]

                    right_region = img[y:y + h, x + w:]

                    right_region = cv2.cvtColor(right_region, cv2.COLOR_BGR2RGB)
                    reader = easyocr.Reader(['en'], gpu=False, verbose=False)

                    # Распознаваем название игры
                    results = reader.readtext(right_region)

                    for (bbox, text, prob) in results:
                        game_name = text
                        check_templates[templ_photo] += game_name

                return check_templates[templ_photo]



    def activate_key(self, key):
        os.startfile('steam://open/activateproduct')
        screenshot_activation = self._push_input_code(key)
        answer = self._get_answer(screenshot_activation)
        win32gui.PostMessage(self.activity_window, win32con.WM_CLOSE, 0, 0)
        return answer