class DataDao:
    def __init__(self):
        self.datas = []

    def add(self, data):
        self.datas.append(data)

    def show(self):
        for data in self.datas:
            print(data)