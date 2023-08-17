

# 1225. 암호생성기

# import sys
# sys.stdin = open('input_1225.txt', 'r')
#
# T = 10
# for tc in range(1, T+1):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     Queue = []
#     for i in range(len(arr)):
#         Queue.append(arr[i])
#
#     j = 1
#     while Queue[7] != 0:
#         tmp = Queue.pop(0)-j
#
#         if tmp < 0:
#             Queue.append(0)
#         else:
#             Queue.append(tmp)
#
#         if j < 5:
#             j += 1
#         else:
#             j = 1
#
#     print(f'#{tc}', *Queue)


# 1860. 진기의 최고급 붕어빵

# import sys
# sys.stdin = open('input_1860.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     people, time, num = map(int, input().split())
#     visit_people = list(map(int, input().split()))
#     Queue = 0  # 완성 된 붕어빵 보관
#     clock = 0
#     result = 'Possible'
#     visit_people = sorted(visit_people)
#     while clock != 11112:
#         clock += 1
#         if clock % time == 0:
#             Queue += num
#
#         for i in range(people):
#             if visit_people[i] == 0:
#                 result = 'Impossible'
#             if visit_people[i] == clock:
#                 if Queue <= 0:
#                     result = 'Impossible'
#                     clock = 11112
#                     break
#                 else:
#                     Queue -= 1
#
#     print(f'#{tc} {result}')

# 18400. 회전

# import sys
# sys.stdin = open('input_18400.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     Queue = list(map(int, input().split()))
#
#     while M != 0:
#         tmp = Queue.pop(0)
#         Queue.append(tmp)
#         M -= 1
#
#     print(f'#{tc} {Queue[0]}')
#


# 18401. 피자 굽기

# import sys
# sys.stdin = open('input_18401.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     my_list = []    # 피자의 번호를 알기 위한 리스트
#     for i in range(len(arr)):
#         my_list.append([i+1, arr[i]])   # 피자에 번호를 매겨준다
#
#     Queue = []      # 화덕
#     for _ in range(N):        # 화덕의 크기만큼 피자 투입
#         tmp = my_list.pop(0)
#         Queue.append(tmp)
#
#     while len(Queue) != 1:      # 화덕에 피자 한개 남을 때까지 반복
#         Queue[0][1] //= 2       # 화덕의 첫번째 치즈의 수치를 반으로 나눠준다.
#         check = Queue.pop(0)    # 치즈가 0이면 꺼내기 위해 체크해준다.
#         if check[1] == 0:       # 치즈가 0이라면
#             if len(my_list) != 0:   # 만약 추가 투입할 피자가 있다면
#                 change = my_list.pop(0)     # 리스트에서 남은 피자를 가져와
#                 Queue.append(change)        # 화덕에 추가 투입한다.
#         else:
#             Queue.append(check)     # 치즈가 0이 아니라면 다시 화덕 맨 뒤에 넣는다.
#
#     print(f'#{tc} {Queue[0][0]}')   # 최종적으로 한개 남은 피자의 번호 값 출력

