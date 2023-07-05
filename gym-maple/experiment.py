from time import time

start_time = time() # 501
print('start_time:',start_time)

while True:
    current_time = time() #502 502-501 = 1  503 - 501 = 2 504 - 501 = 3 
    elapsed_time = current_time - start_time
   # print(f"Elapsed time: {elapsed_time} seconds")
    print(elapsed_time)




