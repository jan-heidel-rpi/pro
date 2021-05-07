from qtpy import uic
import sys
print('compile prozess start')
print('')
print('compiling')
uic.compileUiDir("./Gui")
print('ready')
sys.exit(0)