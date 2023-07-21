import pyautogui 


# Captura tela de um retângulo de 500x300 a partir da posição, (0, 0)

screenshot = pyautogui.screenshot(region=(0, 0, 500, 300))
screenshot.save('screenshot_2.png')