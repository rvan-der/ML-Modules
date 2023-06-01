import numpy as np


class Matrix():

    def __init__(self, data):

        typeErrMsg = "Matrix requires a tuple or a list of lists. Tuple must contain two integers strictly greater than 0. Lists must contain only numbers."

        if isinstance(data, tuple):
            if len(data) != 2 or any(not isinstance(elem, int) or elem < 1 for elem in data):
                raise TypeError(typeErrMsg)
            nRows, nCols = data
            self.data = []
            for _ in range(nRows):
                self.data.append([0] * nCols)

        elif isinstance(data, (list, np.ndarray)):
            if len(data) < 1 or any(not isinstance(row, (list, np.ndarray)) for row in data):
                raise TypeError(typeErrMsg)
            rowLen = len(data[0])
            for row in data:
                if any(not isinstance(val, (int, float, np.int64, np.float64)) for val in row):
                    raise TypeError(typeErrMsg)
                if len(row) != rowLen:
                    raise ValueError(f"All rows of {type(self).__name__} must be of the same length.")
            self.data = data

        else:
            raise TypeError(typeErrMsg)

        self.shape = (len(self.data), len(self.data[0]))


    def T(self):
        return type(self)([[self.data[i][j] for i in range(self.shape[0])] for j in range(self.shape[1])])


    def __repr__(self):
        return f"{type(self).__name__}({self.data})"


    def __str__(self):
        colWidths = [max(len(str(val)) for val in col) for col in self.T().data]
        s = ""
        for row in self.data:
            s += "\n|" + "|".join([str(row[i]) + " " * (colWidths[i] - len(str(row[i]))) for i in range(len(row))]) + "|"
        return s[1:]


    def __add__(self, obj2):
        if not isinstance(obj2, type(self)):
            return NotImplemented
        if self.shape != obj2.shape:
            raise ValueError(f"Instances of {type(self).__name__} must have the same shape to add together.")
        return type(self)([[self.data[i][j] + obj2.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])


    def __radd__(self, obj1):
        if not isinstance(obj1, type(self)):
            return NotImplemented
        if self.shape != obj1.shape:
            raise ValueError(f"Instances of {type(self).__name__} must have the same shape to add together.")
        return type(self)([[self.data[i][j] + obj1.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])


    def __sub__(self, obj2):
        if not isinstance(obj2, type(self)):
            return NotImplemented
        if self.shape != obj2.shape:
            raise ValueError(f"Instances of {type(self).__name__} must have the same shape to substract.")
        return type(self)([[self.data[i][j] - obj2.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])


    def __rsub__(self, obj1):
        if not isinstance(obj1, type(self)):
            return NotImplemented
        if self.shape != obj1.shape:
            raise ValueError(f"Instances of {type(self).__name__} must have the same shape to substract.")
        return type(self)([[obj1.data[i][j] - self.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])


    def __truediv__(self, obj2):
        if not isinstance(obj2, (float, int)):
            return NotImplemented
        return type(self)([[val / obj2 for val in row] for row in self.data])


    def __rtruediv__(self, obj1):
        return NotImplemented


    def __mul__(self, obj2):
        if isinstance(obj2, (float, int)):
            return type(self)([[val * obj2 for val in row] for row in self.data])
        elif isinstance(obj2, Matrix):
            if self.shape[1] != obj2.shape[0]:
                raise ValueError(f"{type(self).__name__} and {type(obj2).__name__} must have compatible shapes to multiply together.")
            retType = type(self) if type(self) == type(obj2) else Vector
            obj2T = obj2.T()
            return retType([[sum(irow * jcol for irow,jcol in zip(self.data[i], obj2T.data[j])) for j in range(obj2T.shape[0])] for i in range(self.shape[0])])
        else:
            return NotImplemented


    def __rmul__(self, obj1):
        if isinstance(obj1, (float, int)):
            return type(self)([[val * obj1 for val in row] for row in self.data])
        elif isinstance(obj1, Matrix):
            if obj1.shape[1] != self.shape[0]:
                raise ValueError(f"{type(obj1).__name__} and {type(self).__name__} must have compatible shapes to multiply together.")
            retType = type(self) if type(self) == type(obj1) else Vector
            selfT = self.T()
            return retType([[sum(irow * jcol for irow,jcol in zip(obj1.data[i], selfT.data[j])) for j in range(selfT.shape[0])] for i in range(obj1.shape[0])])
        else:
            return NotImplemented



class Vector(Matrix):

    def __init__(self, data):

        typeErrMsg = "Vector requires a list of lists containing only numbers or a shape with at least one dimension equal to 1."

        if isinstance(data, tuple) and not 1 in data:
            raise TypeError(typeErrMsg)
        try:
            super().__init__(data)
        except TypeError:
            raise TypeError(typeErrMsg)
        except Exception as e:
            raise e
        if self.shape[0] > 1 and self.shape[1] != 1:
            raise ValueError("Column Vector must only have rows of length 1.")


    def dot(self, v):
        if not isinstance(v, Vector):
            raise TypeError("Dot product resuires a Vector.")
        v1 = [val for row in self.data for val in row]
        v2 = [val for row in v.data for val in row]
        if len(v1) != len(v2):
            raise ValueError("Dot product is not defined for vectors of different lengths.")
        return sum(a * b for a, b in zip(v1, v2))
