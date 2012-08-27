def sub_dict(somedict, somekeys, default=None):
    list_keys = [(k, somedict.get(k, default)) for k in somekeys]
    return dict(list_keys)

d = {"1":"a", "2":"b", "3":"c"}
sub = ("2", "3","4")
print sub_dict(d, sub)
print sub_dict(d, sub, "d")
print d, '\n'
