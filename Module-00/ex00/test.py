from matrix import *
import numpy as np


print("m1 = Matrix((1, 1))")
try:
    m1 = Matrix((1, 1))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m1.shape: {m1.shape}")
    print(f"repr(m1):{repr(m1)}")
    print(f"m1.T(): {repr(m1.T())}")
    print(f"str(m1):\n{m1}")
print("___________________________________")


print("\nm2 = Matrix((0, 1))")
try:
    m2 = Matrix((0, 1))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m2.shape: {m2.shape}")
    print(f"repr(m2): {repr(m2)}")
    print(f"m2.T(): {repr(m2.T())}")
    print(f"str(m2):\n{m2}")
print("___________________________________")


print("\nm3 = Matrix((1, 0))")
try:
    m3 = Matrix((1, 0))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m3.shape: {m3.shape}")
    print(f"repr(m3): {repr(m3)}")
    print(f"m3.T(): {repr(m3.T())}")
    print(f"str(m3):\n{m3}")
print("___________________________________")


print("\nm4 = Matrix((-1, 1))")
try:
    m4 = Matrix((-1, 1))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m4.shape: {m4.shape}")
    print(f"repr(m4): {repr(m4)}")
    print(f"m4.T(): {repr(m4.T())}")
    print(f"str(m4):\n{m4}")
print("___________________________________")


print("\nm5 = Matrix((3, 5))")
try:
    m5 = Matrix((3, 5))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m5.shape: {m5.shape}")
    print(f"repr(m5): {repr(m5)}")
    print(f"m5.T(): {repr(m5.T())}")
    print(f"str(m5):\n{m5}")
print("___________________________________")


print("\nm6 = Matrix((1.5, 3))")
try:
    m6 = Matrix((1.5, 3))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m6.shape: {m6.shape}")
    print(f"repr(m6): {repr(m6)}")
    print(f"m6.T(): {repr(m6.T())}")
    print(f"str(m6):\n{m6}")
print("___________________________________")


print("\nm7 = Matrix([[1,2,3], [3,2,1]])")
try:
    m7 = Matrix([[1,2,3], [3,2,1]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m7.shape: {m7.shape}")
    print(f"repr(m7): {repr(m7)}")
    print(f"m7.T(): {repr(m7.T())}")
    print(f"str(m7):\n{m7}")
print("___________________________________")


print("\nm8 = Matrix([[1,2,3,4], [3,2,1]])")
try:
    m8 = Matrix([[1,2,3,4], [3,2,1]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m8.shape: {m8.shape}")
    print(f"repr(m8): {repr(m8)}")
    print(f"m8.T(): {repr(m8.T())}")
    print(f"str(m8):\n{m8}")
print("___________________________________")


print("\nm9 = Matrix([[1,2,3], [-3,-2,-1]])")
try:
    m9 = Matrix([[1,2,3], [-3,-2,-1]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m9.shape: {m9.shape}")
    print(f"repr(m9): {repr(m9)}")
    print(f"m9.T(): {repr(m9.T())}")
    print(f"str(m9):\n{m9}")
print("___________________________________")


print("\nm10 = Matrix([[1.5, 2.6, 3.7], [-3.7, -2.6, -1.5]])")
try:
    m10 = Matrix([[1.5, 2.6, 3.7], [-3.7, -2.6, -1.5]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m10.shape: {m10.shape}")
    print(f"repr(m10): {repr(m10)}")
    print(f"m10.T(): {repr(m10.T())}")
    print(f"str(m10):\n{m10}")
print("___________________________________")


print("\nm11 = Matrix([[0, 0, 0, 111111, 0], [0,1111,0,0,0]])")
try:
    m11 = Matrix([[0, 0, 0, 111111, 0], [0,1111,0,0,0]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m11.shape: {m11.shape}")
    print(f"repr(m11): {repr(m11)}")
    print(f"m11.T(): {repr(m11.T())}")
    print(f"str(m11):\n{m11}")
print("___________________________________")


print("\nm12 = Matrix([[1,2,3,4,5]])")
try:
    m12 = Matrix([[1,2,3,4,5]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m12.shape: {m12.shape}")
    print(f"repr(m12): {repr(m12)}")
    print(f"m12.T(): {repr(m12.T())}")
    print(f"str(m12):\n{m12}")
print("___________________________________")


print("\nm13 = Matrix(np.array([[1,2,3,4,5]]))")
try:
    m13 = Matrix(np.array([[1,2,3,4,5]]))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"m13.shape: {m13.shape}")
    print(f"repr(m13): {repr(m13)}")
    print(f"m13.T(): {repr(m13.T())}")
    print(f"str(m13):\n{m13}")
print("___________________________________")


print("\nv1 = Vector([[1,2,3,4,5]])")
try:
    v1 = Vector([[1,2,3,4,5]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v1.shape: {v1.shape}")
    print(f"repr(v1): {repr(v1)}")
    print(f"v1.T(): {repr(v1.T())}")
    print(f"str(v1):\n{v1}")
print("___________________________________")


print("\nv2 = Vector([[1], [2], [3], [4], [5]])")
try:
    v2 = Vector([[1], [2], [3], [4], [5]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v2.shape: {v2.shape}")
    print(f"repr(v2): {repr(v2)}")
    print(f"v2.T(): {repr(v2.T())}")
    print(f"str(v2):\n{v2}")
print("___________________________________")


print("\nv3 = Vector([1, 2, 3])")
try:
    v3 = Vector([1, 2, 3])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v3.shape: {v3.shape}")
    print(f"repr(v3): {repr(v3)}")
    print(f"v3.T(): {repr(v3.T())}")
    print(f"str(v3):\n{v3}")
print("___________________________________")


print("\nv4 = Vector([[1], [2], [3], [4], [5, 6]])")
try:
    v4 = Vector([[1], [2], [3], [4], [5, 6]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v4.shape: {v4.shape}")
    print(f"repr(v4): {repr(v4)}")
    print(f"v4.T(): {repr(v4.T())}")
    print(f"str(v4):\n{v4}")
print("___________________________________")


print("\nv5 = Vector([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]])")
try:
    v5 = Vector([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v5.shape: {v5.shape}")
    print(f"repr(v5): {repr(v5)}")
    print(f"v5.T(): {repr(v5.T())}")
    print(f"str(v5):\n{v5}")
print("___________________________________")


print("\nv6 = Vector([[1]])")
try:
    v6 = Vector([[1]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v6.shape: {v6.shape}")
    print(f"repr(v6): {repr(v6)}")
    print(f"v6.T(): {repr(v6.T())}")
    print(f"str(v6):\n{v6}")
print("___________________________________")


print("\nv7 = Vector((1,5))")
try:
    v7 = Vector((1,5))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v7.shape: {v7.shape}")
    print(f"repr(v7): {repr(v7)}")
    print(f"v7.T(): {repr(v7.T())}")
    print(f"str(v7):\n{v7}")
print("___________________________________")


print("\nv8 = Vector((2,5))")
try:
    v8 = Vector((2,5))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v8.shape: {v8.shape}")
    print(f"repr(v8): {repr(v8)}")
    print(f"v8.T(): {repr(v8.T())}")
    print(f"str(v8):\n{v8}")
print("___________________________________")


print("\nv9 = Vector((5,1))")
try:
    v9 = Vector((5,1))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(f"v9.shape: {v9.shape}")
    print(f"repr(v9): {repr(v9)}")
    print(f"v9.T(): {repr(v9.T())}")
    print(f"str(v9):\n{v9}")
print("___________________________________")


print("\nm7 + m9")
try:
    r = m7 + m9
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm10 + 42")
try:
    r = m10 + 42
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm10 + [[42]]")
try:
    r = m10 + [[42]]
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm10 + m5")
try:
    r = m10 + m5
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm7 - m9")
try:
    r = m7 - m9
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm10 - 42")
try:
    r = m10 - 42
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm10 - [[42]]")
try:
    r = m10 - [[42]]
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm10 - m5")
try:
    r = m10 - m5
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm7 * 2")
try:
    r = m7 * 2
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\n2 * m7")
try:
    r = 2 * m7
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm7 * m9")
try:
    r = m7 * m9
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm7 * m9.T()")
try:
    r = m7 * m9.T()
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm7 / 2")
try:
    r = m7 / 2
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\n2 / m7")
try:
    r = 2 / m7
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nm9 * Vector([[2], [2], [2]])")
try:
    r = m9 * Vector([[2], [2], [2]])
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nVector([[2], [2], [2]]) * m9")
try:
    r = Vector([[2], [2], [2]]) * m9
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nv1 * v2")
try:
    r = v1 * v2
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nv1 * v1")
try:
    r = v1 * v1
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nv1.dot(v1)")
try:
    r = v1.dot(v1)
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nv1.dot(v2)")
try:
    r = v1.dot(v2)
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")


print("\nv1.dot(Vector([[2, 4, 6, 8, 1]]))")
try:
    r = v1.dot(Vector([[2, 4, 6, 8, 1]]))
except Exception as e:
    print(f"ERROR: {str(e)}")
else:
    print("SUCCESS")
    print(r)
print("___________________________________")
