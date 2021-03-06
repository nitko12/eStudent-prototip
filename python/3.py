import time
from Usb_interface import ArduinoUsbDevice

WAIT_TILL_PLAY = 0.05
WAIT_BETWEEN_WRITE = 0.01

pick = [(60, 28), (29, 61), (62, 30), (31, 63)]
last_picked = [0, 0, 0, 0]

notes = {
    'D0':   [(None, None, 0)],
    'D#0':  [(17, 33, 0)],
    'E0':   [(49, 33, 0)],
    'F0':   [(21, 37, 0)],
    'F#0':  [(53, 37, 0)],
    'G0':   [(25, 41, 0), (None, None, 1)],
    'G#0':  [(57, 41, 0)],
    'A0':   [(19, 35, 1)],
    'A#0':  [(51, 35, 1)],
    'H0':   [(23, 39, 1)],
    'C1':   [(55, 39, 1), (None, None, 2)],
    'C#1':  [(16, 32, 2)],
    'D1':   [(48, 32, 2)],
    'D#1':  [(20, 36, 2)],
    'E1':   [(52, 36, 2)],
    'F1':   [(24, 40, 2), (None, None, 3)],
    'F#1':  [(56, 40, 2)],
    'G1':   [(18, 34, 3)],
    'G#1':  [(50, 34, 3)],
    'A1':   [(22, 38, 3)],
    'A#1':  [(54, 38, 3)],
}


# notes = {
#     'D0':   [(None, None, 0)],
#     'G0':   [(None, None, 1)],
#     'C1':   [(None, None, 2)],
#     'F1':   [(None, None, 3)],
# }

if __name__ == "__main__":
    try:
        theDevice = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x5df)

        print("Found: 0x%04x 0x%04x %s %s" % (theDevice.idVendor,
                                              theDevice.idProduct,
                                              theDevice.productName,
                                              theDevice.manufacturer))
    except:
        pass

    theDevice = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x5df)

    while True:

        # for x in range(0, 4):
        #     theDevice.write(pick[x][1 - last_picked[x]])
        #     time.sleep(0.01)

        # time.sleep(1)

        # theDevice.write(notes["F0"][0][0])
        # time.sleep(WAIT_BETWEEN_WRITE)
        # theDevice.write(notes["A0"][0][0])
        # time.sleep(WAIT_BETWEEN_WRITE)

        # theDevice.write(60)
        # time.sleep(0.1)
        # theDevice.write(28)
        # time.sleep(0.1)

        # for x in range(32, 32+10):
        #     theDevice.write(x)
        #     time.sleep(0.01)

        # time.sleep(1)

        # continue

        time.sleep(WAIT_TILL_PLAY)

        for x in range(0, 4):
            theDevice.write(pick[x][last_picked[x]])
            last_picked[x] ^= 1
            time.sleep(0.01)

        for note, mappings in notes.items():
            print(note)
            for mapping in mappings:
                if mapping[0] is None:
                    continue

                theDevice.write(mapping[0])
                time.sleep(WAIT_BETWEEN_WRITE)
                time.sleep(WAIT_TILL_PLAY)

                theDevice.write(pick[mapping[2]][last_picked[mapping[2]]])
                last_picked[mapping[2]] ^= 1
                time.sleep(WAIT_BETWEEN_WRITE)

                time.sleep(0.5)

                theDevice.write(mapping[1])
                time.sleep(WAIT_BETWEEN_WRITE)
                time.sleep(WAIT_TILL_PLAY)

        time.sleep(0.5)

        # theDevice.write(26)
        # time.sleep(0.1)
        # theDevice.write(27)
        # time.sleep(0.1)
        # theDevice.write(28)
        # time.sleep(0.1)
        # theDevice.write(29)
        # time.sleep(1)
        # theDevice.write(58)
        # time.sleep(0.1)
        # theDevice.write(59)
        # time.sleep(0.1)
        # theDevice.write(60)
        # time.sleep(0.1)
        # theDevice.write(61)
        # time.sleep(1)

        # for x in range(16, 32):
        #     theDevice.write(x)
        #     time.sleep(0.01)

        # time.sleep(1)

        # for x in range(48, 64):
        #     theDevice.write(x)
        #     time.sleep(0.01)

        # time.sleep(0.05)

        # theDevice.write(31)
        # time.sleep(0.15)
        # theDevice.write(63)
        # time.sleep(0.15)

        # time.sleep(0.4)

        # theDevice.write(49)
        # time.sleep(0.1)
        # theDevice.write(61)
        # time.sleep(0.4)

        # theDevice.write(32)
        # time.sleep(0.1)

        # while 1 == 1:
        #     user_input = int(input("DigiUSB#"))
        #     # user_input = user_input+"\n"

        #     theDevice.write(int(user_input))
        #     time.sleep(0.01)
