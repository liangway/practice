"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""
class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')


class Dog(Toy):
    def __str__(self):
        return 'dog'
    def talk(self):
        print 'wang'

class Cat(Toy):
    def __str__(self):
        return 'cat'
    def talk(self):
        print 'miao'


class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, type):
        if type=='cat':
            return Cat()
        elif type == 'dog':
            return Dog()

if __name__ == '__main__':
    tf = ToyFactory()
    c = tf.getToy('cat')
    c.talk()