s = "Шел осенний дождь.  \
Поздним вечером в июле Чубакабра прогуливалась под зонтом. \
И зашла она в чебуречную!  \
решила купить чебурек, съела и отравилась. \
и восстали Чупакабры.\
И тут я проснулся? "
count = 0
for i in s:
    if i in (".","!","?"):
        count += 1
print(count)