from data import major_keys, minor_keys

choose_keys = True

while choose_keys:
    note = input("Choose a note you want to see the scale for. Type 'q' to quit: ")
    if note == 'q':
        choose_keys = False
    else:
        if note in major_keys:
            print("The major scale for the key of {} is".format(note), major_keys[note])
            print("The relative minor of {} is".format(note), major_keys[note][5])
            print()

            modes = input(f"Would you like to see the modes for the key of {note}? Type 'yes' or 'no'. ")
            print()

            while modes == 'yes'.lower():
                mode_dict = {
                    "dorian": major_keys[note][1::] + major_keys[note][:1:],
                    "phrygian": major_keys[note][2::] + major_keys[note][:2:],
                    "lydian": major_keys[note][3::] + major_keys[note][:3:],
                    "mixolydian": major_keys[note][4::] + major_keys[note][:4:],
                    "aeolian": major_keys[note][5::] + major_keys[note][:5:],
                    "locrian": major_keys[note][6::] + major_keys[note][:6:],
                }
                valid_choices = []
                for m in mode_dict:
                    valid_choices.append(m)
                print("Below is a list of modes")
                print()
                print(valid_choices)
                print()
                mode = input("Which mode would you like to see? Type 'all' if you want to see them all. ")
                print()
                if mode == "all":
                    for mode in mode_dict:
                        print(mode, mode_dict[mode])
                else:
                    print(mode_dict[mode])
                print()
                go_again = input("Would you like to see another key? Type 'y' or 'n'. ")
                if go_again == 'n':
                    choose_keys = False
                    modes = False

            else:
                choose_keys = False
                print()
                print("See you soon.")
        else:
            print("You've chosen an invalid key")
            print()
