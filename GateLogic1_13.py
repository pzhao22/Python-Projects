# Implement gate logic - classes include gates and connectors. AND and OR gates inherit from binary gate class, NOT gate inherits from unary gate class. Binary and unary inherit from Logic Gate class

# All gates will (1) have names and (2) output. They will have different number of pins and logic, which will be written later

# pylint: disable=no-member 

class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label
    
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    # Keep the inheritance of the parent's init function, then add pins
    def __init__(self,n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None
    
    def get_pin_A(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.get_label() + ": "))
        else:
            return self.pinA.get_from().get_output()
    
    def get_pin_B(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.get_label() + ": "))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self,source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else: 
            print("No empty pins for Gate " + self.get_label())

class AndGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def perform_gate_logic(self):
        a = self.get_pin_A()
        b = self.get_pin_B()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def perform_gate_logic(self):
        a = self.get_pin_A()
        b = self.get_pin_B()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NorGate(OrGate):
    def __init__(self,n):
        super().__init__(n)
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class NandGate(AndGate):
    def __init__(self,n):
        super().__init__(n)
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class UnaryGate(LogicGate):
    # Keep the inheritance of the parent's init function, then add pins
    def __init__(self,n):
        super().__init__(n)
        self.pin = None
    
    def get_pin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self,source):
        if self.pin == None:
            self.pin = source
        else: 
            print("No empty pins for Gate " + self.get_label())

class NotGate(UnaryGate):
    def __init__(self,n):
        super().__init__(n)
    def perform_gate_logic(self):
        a = self.get_pin()
        if a == 0:
            return 1
        else:
            return 0

class Connector():
    def __init__(self, f, t):
        self.fromGate = f
        self.toGate = t
        t.set_next_pin(self)
    def get_from(self):
        return self.fromGate
    def get_to(self):
        return self.toGate



def main():

    # First equality
    test1 = AndGate("And1")
    test2 = AndGate("And2")
    test3 = NorGate("Nor1")
    c1 = Connector(test1,test3)
    c2 = Connector(test2,test3)
    print(test3.get_output())

     # Second equality
    test1 = NandGate("Nand1")
    test2 = NandGate("Nand2")
    test3 = AndGate("And1")
    c1 = Connector(test1,test3)
    c2 = Connector(test2,test3)
    print(test3.get_output())
main()

    

