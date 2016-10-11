import sys
from Feedback import Feedback
from cisco7decrypt import decrypt_type7

pw = sys.argv[1]

fb = Feedback()
cleartext = decrypt_type7(pw)
fb.add_item(cleartext, arg=cleartext, subtitle='Press Enter to Copy, Press CMD+Enter to Paste to front most Window')
print (fb)