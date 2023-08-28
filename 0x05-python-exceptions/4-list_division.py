#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = []
    for i in range(list_length):
        try:
            r.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            r.append(0)
        except TypeError:
            print("wrong type")
            r.append(0)
        except IndexError:
            print("out of range")
            r.append(0)
        finally:
            pass
    return r
