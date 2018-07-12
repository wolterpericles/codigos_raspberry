# Compila e executa codigo
# no arduino nano usando spi

avrdude -p m328p -c gpio -e -U flash:w:build-nano/plotar.hex