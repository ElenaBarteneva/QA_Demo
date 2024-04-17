
def sort_list(lst, value, reverse_value):
    # lst1 = [float(i.strip(value)) for i in lst]
    return sorted(lst, key=lambda i: float(i.strip(value)), reverse=reverse_value)
# def replace_value(lst, value):
#     lst1 = [float(i.strip(value)) for i in lst]
#     return lst1