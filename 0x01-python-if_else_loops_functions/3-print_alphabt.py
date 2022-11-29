#!/usr/bin/python3
for asci_value in range(97, 123):
    if asci_value == 101 or asci_value == 113:
        continue
    print('{}'.format(chr(asci_value)), end="")
