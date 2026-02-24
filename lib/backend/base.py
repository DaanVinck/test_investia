def different(data):
    data_list = []
    for item in data:
        if item not in data_list:
            data_list.append(item)
    return data_list
def unpack(data1):
    rijen = data1.data
    namen = [rij['comp'] for rij in rijen]
    
    return namen
