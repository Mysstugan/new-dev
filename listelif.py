def openOrSenior(members):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in members]

def openOrSenior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res