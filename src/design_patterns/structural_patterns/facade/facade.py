class SubsystemA:
    def operation_a1(self):
        return "SubsystemA: Ready!\n"
    
    def operation_a2(self):
        return "SubsystemA: Doing Operation!\n"
    
class SubsystemB:
    def operation_b1(self):
        return "SubsystemB: Ready!\n"
    
    def operation_b2(self):
        return "SubsystemB: Doing Operation!\n"
    
class SubsystemC:
    def operation_c1(self):
        return "SubsystemC: Ready!\n"
    
    def operation_c2(self):
        return "SubsystemC: Doing Operation!\n"
    

class Facade:
    def __init__(self, subsystem_a: SubsystemA, subsystem_b: SubsystemB, subsystem_c: SubsystemC):
        self._subsystem_a = subsystem_a
        self._subsystem_b = subsystem_b
        self._subsystem_c = subsystem_c

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:\n")
        results.append(self._subsystem_a.operation_a1())
        results.append(self._subsystem_b.operation_b1())
        results.append(self._subsystem_c.operation_c1())
        results.append("Facade orders subsystems to perform the action:\n")
        results.append(self._subsystem_a.operation_a2())
        results.append(self._subsystem_b.operation_b2())
        results.append(self._subsystem_c.operation_c2())
        return "".join(results)
    
if __name__ == "__main__":
    subsystem_a = SubsystemA()
    subsystem_b = SubsystemB()
    subsystem_c = SubsystemC()
    facade = Facade(subsystem_a, subsystem_b, subsystem_c)

    print(facade.operation())