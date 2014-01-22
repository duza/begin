"""It is the program for description of a physical material (substance)"""

__metaclass__ = type

class Material:
    """Class Material describes a material.
        Method __init__ accept two parametrs: name and density.
        Methods gets  return value of attribute, sets - accept new value of attribute. 
        Method ToString output values of fields in csv format."""
    def __init__(self, nameMaterial="Default",density=3940):
        if isinstance(nameMaterial, str):
            self.__nameMaterial = nameMaterial
        else:
            raise TypeError("Incorrect input 'nameMaterial' ")
        if isinstance(density,int):
            self.__densityOfMaterial = density
        else:
            raise TypeError("Incorrect input 'density' ")

    @property
    def nameMaterial(self):
        return self.__nameMaterial

    @nameMaterial.setter   
    def nameMaterial(self, x):
        if isinstance(x, str):
            self.__nameMaterial = x
        else:
            raise AttributeError("Incorrect input 'nameMaterial' ")
        
    @property
    def densityOfMaterial(self):
        return self.__densityOfMaterial
    
    @densityOfMaterial.setter    
    def densityOfMaterial(self, x):
        if isinstance(x, int):
            self.__densityOfMaterial = x
        else:
            raise AttributeError("Incorrect input 'density' ")

    def ToString(self):
        return "%s;%d" % (self.nameMaterial, self.densityOfMaterial)

    def __str__(self):
        return self.ToString()

class UniformMaterial(Material):
    """Class UniformMaterial is intended for description uniform object 
    consisting of a single material. Method __init__ accept four
     parametrs: name of material, density of material, name of object,
      volume of object. Method GetMass calculates weight of object """
    def __init__(self, nameMaterial = "Default", density = 3940,
        nameStuff = "Default",volume = 15):
        super(UniformMaterial, self).__init__(nameMaterial, density)
        if isinstance(nameStuff, str):
            self.__nameUniformMaterial = nameStuff
        else:
            raise TypeError("Incorrect input 'nameStuff' ")
        if isinstance(volume, float):
            self.__volumeUniformMaterial = volume
        else:
            raise TypeError("Incorrect input 'volume' ")

    @property
    def volumeUniformMaterial(self):
        return self.__volumeUniformMaterial

    @volumeUniformMaterial.setter
    def volumeUniformMaterial(self,x):
        if isinstance(x, float):
            self.__volumeUniformMaterial = x
        else:
            raise AttributeError("Incorrect input 'volume' ")

    @property
    def nameUniformMaterial(self):
        return self.__nameUniformMaterial

    @nameUniformMaterial.setter
    def nameUniformMaterial(self,x):
        if isinstance(x, str):
            self.__nameUniformMaterial = x
        else:
            raise AttributeError("Incorrect input 'nameStuff' ")

    def GetMass(self):
        self.__weightUniformMaterial = self.volumeUniformMaterial * \
        self.densityOfMaterial
        return self.__weightUniformMaterial      
        
    def ToString(self):
        return "%s;%s;%d;%.2f;%.2f" %(self.nameUniformMaterial, self.nameMaterial, 
            self.densityOfMaterial, self.volumeUniformMaterial, self.GetMass())

    def __str__(self):
        return self.ToString()

Steel_Wire = UniformMaterial( nameStuff = "wire", nameMaterial = "steel",
 volume = 0.03)
print Steel_Wire
Steel_Wire.nameMaterial = "copper"
Steel_Wire.densityOfMaterial = 8500
print Steel_Wire.GetMass()