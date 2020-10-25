class listofnames:

    def config(self):
        pass

    def printname(self, name):
        self.name = name
        print(name)
    
    def getage(self, age):
        self.age = age
        age = 2*age
        return age

if __name__ == '__main__':

    man = listofnames()
    man.printname('str')
    age = man.getage(2)
    print(age)