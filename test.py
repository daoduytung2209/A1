# list = [['Fish fingers', '12.95', '2', 'r'], ['Metal detector', '42.5', '3', 'r'], ['Coffee beans', '40.0', '1', 'r']]
# list.append(['Watch', '50.0', '2', 'r'])
# list.append(['Computer','100.0','3','r'])
# small_list = ['Watch', '50.0', '2', 'c']
# small_list2 = ['Fish fingers', '12.95', '2', 'c']
#
# # for each in range(len(list)):
# #     small_list[3]='c'
# #     if small_list[each] in list[each]:
# #         list[each] = small_list
# print(len(list))
# print(small_list2[1]in list[1])
# for each in range(len(list)):
#     # small_list[3]='c'
#     if small_list[1] in list[each]:
#         list[each] = small_list
# print(list)

# input_file = open("items.csv", "r")
# for each in input_file:
#     if "\n" in each:
#         each = each.replace("\n", "")
#     split_data = each.split(",")
#     print(split_data)

def load_items(filename):
    list_data = []
    input_file = open(filename, "r")
    for each in input_file:
        if "\n" in each:
            each = each.replace("\n", "")
        split_data = each.split(",")
        list_data.append(split_data)
    input_file.close()
    return list_data


def main():
    list_required_items = load_items("items.csv")
    list_completed_items = []
    print("""Shopping list 1.0 - by Dao Duy Tung
    {} items loaded from items.csv""".format(len(list_required_items)))
    menu = """Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit
    """
    print(menu)
    user_input = input().upper()
    while user_input != "Q":

        if user_input == "R":
            if len(list_required_items) == 0:
                print("No required items")
            else:
                print("Required items:")
            print(menu)

        elif user_input == "C":
            if len(list_completed_items) == 0:
                print("No completed items")
            else:
                print("Completed items:")
            print(menu)

        elif user_input == "A":
            new_items = []
            input_name = input("Item name: ")
            while input_name == "":
                print("Input can not be blank")
                input_name = input("Item name: ")
