from threading import Thread,Condition
import time 
import random
queue=[]
Max_num=10
condition=Condition()
class producer(Thread):
	def run(self):
		nums=range(6)
		global queue
		while True:
			condition.acquire()
			if len(queue)==Max_num:
				print("Queue is full producer is waitting")
				condition.wait()
			print("Space in queue consumer notified producer ")
			num=random.choice(nums)
			queue.append(num)
			print("produced:",num)
			condition.notify()
			condition.release()
			if num==5:
				break
			time.sleep(random.random())
class consumer(Thread):
	def run(self):
		global queue
		while True:
			condition.acquire()
			if not queue:
				print("Nothing in queue, consumer is waitting")
				condition.wait()
			print("Producer is added somethin in queue and notified consumer")
			num=queue.pop(0)
			print("Consumed",num)
			condition.notify()
			condition.release()
			if num==5:
				break
			time.sleep(random.random())
producer().start()
consumer().start()
