######
#####
#### python3 -m pip install wifi


from wifi import Cell

net = Cell.all('wlan0')

color = ("\033[0;33m\033[1;33m")


for i in net:
    print(color)
    print("\n------------------------------------------------------------------------\n")
    print("\t Network Name : {} \n".format(i.ssid))
    print("\t Signal Strength : {} \n".format(i.signal))
    print("\t MAC : {} \n \n \t Quality : {} \n".format(i.address,i.quality))
    print("\t Wi-Fi real max speed : {} \n".format(i.bitrates))
    print("\t Network encryption : {} \n".format(i.encrypted))
    print("\t Wi-Fi Security : {} \n".format(i.encryption_type))
    print("\t CHANNEL : {} \n \n \t Frequency band : {} \n".format(i.channel,i.frequency))
    print("\t WiFI Mode : {} \n".format(i.mode))