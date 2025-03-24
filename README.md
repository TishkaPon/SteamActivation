<div align="center">
  <h1>Steam Key Activator</h1>
</div>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Steam Key Activator is a Python-based tool that automatically applies Steam keys to activate games. It streamlines the activation process and helps you get your games up and running with minimal hassle.

---

## Features

- **Automated Activation:** Instantly activate Steam keys with a few lines of code.
- **OCR Integration:** Utilizes EasyOCR for text recognition.
- **Robust Dependencies:** Built with powerful libraries such as OpenCV, NumPy, PyAutoGUI, and pywin32.
- **Easy to Use:** Simple, intuitive API for integrating key activation in your projects.

---

## Dependencies

Make sure you have the following dependencies installed:

- `easyocr==1.7.2`
- `numpy==2.2.4`
- `opencv_python==4.11.0.86`
- `opencv_python_headless==4.11.0.86`
- `pyautogui==0.9.54`
- `pywin32==309`

Install them via pip:

```bash
pip install easyocr==1.7.2 numpy==2.2.4 opencv_python==4.11.0.86 opencv_python_headless==4.11.0.86 pyautogui==0.9.54 pywin32==309
```
or
```bash
pip install -r requirements.txt
```

---

## Quick Start

Here's a simple example to get you started:

```python
from SteamKeyActivator.Activator import SteamActivator

activator = SteamActivator() 
answer_activation = activator.activate_key(code) 

print(answer_activation)
```

Replace `code` with the actual Steam key you want to activate.

---

## Contributing

Contributions are welcome! If you have any ideas, bug reports, or enhancements, please feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Disclaimer

Use this software responsibly and ensure compliance with Steam's terms of service and any other relevant guidelines.
