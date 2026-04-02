import sane
from datetime import datetime

sane.init()
dev = sane.open("pixma:04A9173A_428583")

dev.mode = "color"
dev.resolution = 300

dev.start()
image = dev.snap()
now = datetime.now()
image.save(f'scan_{now.strftime("%Y%m%d_%H%M%S")}.png')
print("스캔 완료!")

dev.close()
sane.exit()
