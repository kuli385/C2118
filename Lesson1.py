print('Lesson2, Python OOP')

class Marker:
    color: str
    thikness: int
    isAvailable: bool

    def __init__(self, color, thikness, isAvailabe = True):
      self.color= color
      self.thikness = thikness
      self.isAvailabe = isAvailabe


      def getInfo(self):
          print('general')
        if self.isAvailabe:
         print(f'color-{self.color} | thk - {self.thikness}')
        else:
             print('\tthis marker is absent in storage')


markerRed = Marker('red' , 2)
markerRed.get_info()
markerRed.color = 'black'
markerRed.get_info()

