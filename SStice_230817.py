

# Queue의 구현

# def enQ(data):
#     global rear
#     rear += 1
#     Q[rear] = data
#
#
# def deQ():
#     global front
#
#     front += 1
#     return Q[front]
#
#
# Qsize = 3
# Q = [0] * Qsize
# rear = -1
# front = -1
#
# enQ(1)
# enQ(2)
# rear += 1
# Q[rear] = 3
#
# print(deQ())
# print(deQ())
# front += 1
# tmp = Q[front]
# print(tmp)


# 원형 큐

# def enQ(data):
#     global rear
#     if (rear+1)%cQsize == front:
#         print('CQ IS FULL')
#     else:
#         rear = (rear + 1)%cQsize
#         cQ[rear] = data
#
#
# def deq():
#     global front
#     front = (front + 1)%cQsize
#     return cQ[front]
#
#
# cQsize = 4
# cQ = [0]*cQsize
# front = 0
# rear = 0
#
# enQ(1)
# enQ(2)
# enQ(3)
# print(deq())
# print(deq())


# 덱 연습

# from collections import deque
#
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())

lis = [1,5,7,4,3,2,1,5]
for i in lis:
    lis.pop()
print(lis)