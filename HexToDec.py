# Todo: Need to change FFFF values to 0 for inactivity. Currently reads as 255 and does not accurately display inactivity
def HexToDec(file):
    with open("test5t_converted_out.txt", 'w') as out_file, open('test5t_converted.txt') as in_file:
        for hex in in_file.read().split():
            print(int(hex, 16), file=out_file)
    return out_file.name
