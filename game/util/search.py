def findInList(list, name):
    list.sort(key=lambda x: x.name)

    for l in list:
      if l.name.lower().startswith(name.lower()):
        return l
    else:
      return None