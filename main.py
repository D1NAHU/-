class myClass(7мт):
  def method1(self):
      print("палкин")

  def method2(self,someString):    
      print("Software Testing:" + someString)


def main():           
  # exercise the class methods
  c = myClass ()
  c.method1()
  c.method2(" Testing is fun")

if __name__== "__main__":
  main()
