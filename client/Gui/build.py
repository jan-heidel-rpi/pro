import subprocess
import os
import sys
import time
print("Start Builder")
while True:

    try:
        os.system("pyuic6 -o Gui/main_window_ui.py Gui/Main.ui")
        os.system("pyuic6 -o Gui/make_config_dia.py Gui/config.ui")
        print("Aktualisiert")
        time.sleep(120)
    except KeyboardInterrupt:
        print("Stop builder")
        sys.exit(0)