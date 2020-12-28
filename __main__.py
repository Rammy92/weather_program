from weatherutils.write_to_file import File
import time

while True:
    file = File()
    run = file.write_to_file()
    time.sleep(60*60*60*24)