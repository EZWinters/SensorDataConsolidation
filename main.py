
import combine_csv
import menu
import sys

m = menu.Menu()
c = combine_csv.DataConsolidation()


def main():
    main_menu_choice = m.display_main_menu()
    match main_menu_choice:
        case 1:
            choice = m.display_IMU_menu()
            if choice == 1:
                c.consolidate_data('IMU data', 'S07')
            elif choice == 2:
                c.consolidate_data('IMU data', 'S08')
            elif choice == 3:
                c.consolidate_data('IMU data', 'S09')
            elif choice == 4:
                c.consolidate_data('IMU data', 'S10')
        case 2:
            choice = m.display_OMoCap_menu()
            if choice == 1:
                c.consolidate_data('OMoCap data', 'S11')
            elif choice == 2:
                c.consolidate_data('OMoCap data', 'S12')
            elif choice == 3:
                c.consolidate_data('OMoCap data', 'S13')
            elif choice == 4:
                c.consolidate_data('OMoCap data', 'S14')
        case 3:
            sys.exit("Terminating ! ! !")


main()
