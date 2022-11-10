

def compute_data(a, b, c, d):
    return round((a / b) * (a / (c ** 2 + d **2 )), 3)
def test_data():
    data = []
    data.append([5, 4, 3, 2, .481])
    data.append([9, 1, 4, 6, 1.558])
    for test in data:
        print (compute_data(test[0], test[1], test[2], test[3]) == test[4])

test_data()
