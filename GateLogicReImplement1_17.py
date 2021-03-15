# Implement gate logic - classes include gates and connectors. AND and OR gates inherit from binary gate class, NOT gate inherits from unary gate class. Binary and unary inherit from Logic Gate class

# All gates will (1) have names and (2) output. They will have different number of pins and logic, which will be written later

#pylint: disable=no-member
#pylint: disable=unused-variable

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
            self.pinA = int(input("Enter Pin A input for gate " + self.get_label() + ": "))
            return self.pinA
        elif isinstance(self.pinA,int):
            return self.pinA
        else:
            return self.pinA.get_from().get_output()
    
    def get_pin_B(self):
        if self.pinB == None:
            self.pinB = int(input("Enter Pin B input for gate " + self.get_label() + ": "))
            return self.pinB
        elif isinstance(self.pinB,int):
            return self.pinB
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

class XorGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def perform_gate_logic(self):
        if self.get_pin_A() == self.get_pin_B():
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
            self.pin = int(input("Enter Pin input for gate " + self.get_label() + ": "))
            return self.pin
        elif isinstance(self.pin,int):
            return self.pin
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

# Special case - gate for input values with no connected gates
class Input(UnaryGate):
    def __init__(self,n):
        super().__init__(n)
    def perform_gate_logic(self):
        return self.get_pin()

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

    InputA = Input("INPUTA")
    InputB = Input("INPUTB")
    InputC = Input("INPUTC")


    Xor1 = XorGate("XOR1")
    Xor2 = XorGate("XOR2")
    And1 = AndGate("AND1")
    And2 = AndGate("AND2")
    Or1 = OrGate("OR1")

    c1 = Connector(InputA,Xor1)
    c2 = Connector(InputA,And1)
    c3 = Connector(InputB,Xor1)
    c4 = Connector(InputB,And1)
    c5 = Connector(InputC,And2)
    c6 = Connector(InputC,Xor2)
    c7 = Connector(Xor1,And2)
    c8 = Connector(Xor1,Xor2)
    c9 = Connector(And1,Or1)
    c10 = Connector(And2,Or1)


    InputA.get_pin()
    InputB.get_pin()
    InputC.get_pin()
    print(Xor2.get_output())
    print(And2.get_output())
    
main()

    

