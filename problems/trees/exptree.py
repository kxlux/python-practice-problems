from abc import ABC, abstractmethod

class ExprNode(ABC):
    @abstractmethod
    def is_const(self):
        raise NotImplementedError

    @abstractmethod
    def num_nodes(self):
        raise NotImplementedError
    
    @abstractmethod
    def eval(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

class Int(ExprNode):
    def __init__(self, n):
        self.n = n

    def is_const(self):
        return True

    def num_nodes(self):
        return 1

    def eval(self):
        return self.n

    def __str__(self):
        return str(self.n)

class BinOp(ExprNode):
    def __init__(self, op1: ExprNode, op2: ExprNode):
        self.op1 = op1
        self.op2 = op2

    def is_const(self):
        return False

    def num_nodes(self):
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self):
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return self._operator(op1_value, op2_value)

    def __str__(self):
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} {self._sign()} {op2_str})"
    
    @abstractmethod
    def _operator(self) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def _sign(self) -> str:
        raise NotImplementedError

class Plus(BinOp):
    def __init__(self, op1: ExprNode, op2: ExprNode):
        super().__init__(op1, op2)

    def _operator(self, val1: int, val2: int) -> int:
        return val1 + val2
    
    def _sign(self) -> str:
        return "+"

class Times(BinOp):
    def __init__(self, op1: ExprNode, op2: ExprNode):
        super().__init__(op1, op2)

    def _operator(self, val1: int, val2: int) -> int:
        return val1 * val2
    
    def _sign(self) -> str:
        return "*"

class Minus(BinOp):
    def __init__(self, op1: ExprNode, op2: ExprNode):
        super().__init__(op1, op2)

    def _operator(self, val1: int, val2: int) -> int:
        return val1 - val2
    
    def _sign(self) -> str:
        return "-"
    
class FloorDiv(BinOp):
    def __init__(self, op1: ExprNode, op2: ExprNode):
        super().__init__(op1, op2)

    def _operator(self, val1: int, val2: int) -> int:
        return val1 // val2
    
    def _sign(self) -> str:
        return "//"

class Abs(ExprNode):
    def __init__(self, op1):
        self.op1 = op1

    def is_const(self):
        return False

    def num_nodes(self):
        return 1 + self.op1.num_nodes()

    def eval(self):
        op1_value = self.op1.eval()

        return abs(op1_value)

    def __str__(self):
        op1_str = str(self.op1)

        return f"|{op1_str}|"

class Boolean(ABC):
    @abstractmethod
    def is_const(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def num_nodes(self) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def eval(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def __str__(self) -> str:
        raise NotADirectoryError

class BinBool(Boolean):
    def __init__(self, op1: Boolean, op2: Boolean):
        self.op1 = op1
        self.op2 = op2
    
    def is_const(self) -> bool:
        return False
    
    def num_nodes(self) -> int:
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()
    
    def eval(self) -> bool:
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return self._eval(op1_value, op2_value)
    
    def __str__(self) -> str:

        return f"({str(self.op1)} {self._op()} {str(self.op2)})"
        
    @abstractmethod
    def _eval(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def _op(self) -> str:
        raise NotImplementedError

class Bool(Boolean):
    def __init__(self, val: bool) -> None:
        self.val = val
    
    def is_const(self) -> bool:
        return True

    def num_nodes(self) -> int:
        return 1

    def eval(self) -> bool:
        return self.val

    def __str__(self) -> str:
        return f"{self.val}"
    
class Not(Boolean):
    def __init__(self, op1: Boolean) -> None:
        self.op1 = op1
    
    def is_const(self) -> bool:
        return False

    def num_nodes(self) -> int:
        return 1 + self.op1.num_nodes()

    def eval(self) -> bool:
        return not self.op1.eval()

    def __str__(self) -> str:
        return f"(not {str(self.op1)})"

class And(BinBool):
    def __init__(self, op1: Boolean, op2: Boolean):
        super().__init__(op1, op2)

    def _eval(self, op1_value: bool, op2_value: bool) -> bool:
        return op1_value and op2_value

    def _op(self) -> str:
        return "and"

class Or(BinBool):
    def __init__(self, op1: Boolean, op2: Boolean):
        super().__init__(op1, op2)

    def _eval(self, op1_value: bool, op2_value: bool) -> bool:
        return op1_value or op2_value

    def _op(self) -> str:
        return "or"

if __name__ == "__main__":

    # Sample expression tree for (2 + (3 * 5))
    op1 = Times(FloorDiv(Int(-5), Int(2)), Int(5))
    op2 = Abs(Minus(Int(3), Int(5)))
    expt = Plus(op1, op2)

    op1 = And(Bool(True), Bool(True))
    op2 = Not(Or(Bool(False), Bool(False)))
    expt = And(op1, op2)

    print(f"{expt} = {expt.eval()}")