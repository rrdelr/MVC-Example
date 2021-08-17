import csv

class Users():
    Collection = []
    file = "users.csv"

    def __init__(self):
        raise RuntimeError('not supported')

    @classmethod
    def write_user(self, name, email):
        self.Collection.append([name, email])
        self.savedata()
        return True

    @classmethod
    def get_users(self):
        try:
            with open(self.file, 'r+', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for item in reader:
                    if item not in self.Collection:
                        self.Collection.append(item)
            return self.Collection
        except:
            with open(self.file, "w+") as csvfile:
                pass
            return []

    @classmethod
    def remove_user(self, name, email):
        self.Collection.remove([name, email])
        self.savedata()
        return True

    @classmethod
    def savedata(self):
        with open(self.file, 'w+', encoding="utf-8", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            for item in self.Collection:
                csv_writer.writerow(item)
        return True