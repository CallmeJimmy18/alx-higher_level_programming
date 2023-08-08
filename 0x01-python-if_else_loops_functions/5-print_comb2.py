#!/usr/bin/python3
for i in range(0, 100):
        lead_zer = str(i).zfill(2)
        if i < 99:
                print("{}".format(lead_zer), end=", ")
        else:
                print("{}".format(lead_zer))
