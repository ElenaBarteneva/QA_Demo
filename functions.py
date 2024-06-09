
def sort_list(lst, value, reverse_value):
    # lst1 = [float(i.strip(value)) for i in lst]
    return sorted(lst, key=lambda i: float(i.strip(value)), reverse=reverse_value)
# def replace_value(lst, value):
#     lst1 = [float(i.strip(value)) for i in lst]
#     return lst1


# class Opposite_of(object):
#     def __init__(self, condition):
#         self.condition = condition
#     def __call__(self, driver1):
#         return not self.condition(driver1)

def opposite_of(condition):
    if condition == True:
        return False
    else:
        return True

