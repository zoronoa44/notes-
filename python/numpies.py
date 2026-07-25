import numpy as np


# a = [1, 3, 5, 2, 4, 6]
# b = [4, 6, 3, 6, 2, 4]

# a = np.array([1,3,5,2,4,6])
# b = np.array([4,6,3,6,2,4])

# c = a * b
# # print(c)

# matrix = np.array([[1,2,3],[1,2,4],[4,5,6]])
# # print(matrix)

# # zeros = np.zeros((2,2))
# # ones =np.ones((3,3))
# # print(zeros)
# # print (ones)

# x = np.random.randn(2,4)
# y = np.random.randn(4,2)
# z = np.random.randn(3,3)
# # print (x,y,z)


# # print(x.shape ,y.shape ,z.shape)
# # print(x.ndim ,y.ndim ,z.ndim)
# # print(x.size ,y.size ,z.size)
# # print(x.dtype ,y.dtype ,z.dtype)



# a1 = np.array([[1, 3, 5],[2, 4, 6],[1,8,3]])
# b1 = np.array([[4, 6, 3],[6, 2, 4],[5,2,3]])

# # print(a1 + 10)
# # print(b1 * 2)
# # print (b1 ** 2)
# # print(b1 /10)

# # print (a1 * b1)
# # print(a -b)

# arr = np.array([10, 20, 30, 40, 50])
# # print(np.mean(arr))
# # print(np.std(arr))
# # print(np.min(arr))
# # print(np.max(arr))
# # print(np.sum(arr))

# # print(np.sum(a1))
# # print(np.mean(a1,axis =0)) # gives column mean
# # print(np.mean(a1,axis=1)) # gives row mean

# # print(np.dot(a1,b1))

# # print(arr[0])      # 10  → pehla element
# # print(arr[-1])     # 50  → aakhri element
# # print(arr[1:4])    # [20 30 40] → index 1 se 3 tak
# # print(arr[:3])     # [10 20 30] → start se index 2 tak

# a1 = np.array([[1, 3, 5],
#                [2, 4, 6],
#                [1,8,3]])


# b1 = np.array([[4, 6, 3],
#                [6, 2, 4],
#                [5,2,3]])

# # print(a1[0])
# # print(a1[0][2])# print(matrix_name[row][column])
# print(a1[0:2,0:2])

# arr = np.array([10, 20, 30, 40, 5,7])

# # print(arr.reshape(2,2))
# print(arr.reshape(2,3))
# # print(arr.reshape(3,2))
# # # print(arr.reshape(3,3))

# print(arr.reshape(2,-1))
# print(arr.reshape(-1,1))


# mask = arr <= 30 # [ True  True  True False  True  True]
# print (arr[mask])


matrix = np.array([[1,2,3],
                   [1,2,4],
                   [4,5,6]])

print(matrix[0,2])

print(np.linalg.det(matrix))


