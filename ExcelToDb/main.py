from functions import get_menu_information
import menu_functions

def main() :
    print("\nWELCOME TO THE BEGINNING OF THE APPLICATION !\n")
    csv, id_column, detail_column, function_column, menu_message = get_menu_information()
    print(menu_message)
    option = input()
    while option not in id_column:
        print("This option is not correct, please try again.")
        print(menu_message)
        option = input()
    function_to_call = getattr(menu_functions, csv["function"].iloc[int(option)])
    function_to_call()
    if option != "0" :
        main()

if __name__ == "__main__" :
    main()

#= DATE(STXT(CELLULE("filename"); TROUVE("["; CELLULE("filename")) + 1; TROUVE("."; CELLULE("filename")) - TROUVE("["; CELLULE("filename")) - 1); MOIS(DATEVAL(DROITE(CELLULE("filename"); NBCAR(CELLULE("filename"))-TROUVE("]"; CELLULE("filename"))) & "1")); A3)