from IPython.display import clear_output,display
import time, sys
for i in range(10):
    display(i)
    time.sleep(0.5)
    clear_output(wait=True)
