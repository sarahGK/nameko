class Production():
  def setV(a):
    self.value = a

  def getV():
    return self.value
  
  def method(self,a,b,c):
    return a+b+c


from mock import patch
@patch('Production.ClassName1')
@patch('Production.ClassName2')
def test(MockClass1,MockClass2):
  module.ClassName1()
  module.ClassName2()

  assert MockClass1 is module.ClassName1
  assert MockClass2 is module.ClassName2
  assert MockClass1.called
  assert MockClass2.called

if __name__ == '__main__':
  thing = Production()
  print(thing.method(1,2,3))
