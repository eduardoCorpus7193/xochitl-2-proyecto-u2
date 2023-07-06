import ds_queue
import ds_stack
import ds_linked_list

myQueue = ds_queue.Queue()
myStack = ds_stack.Stack()

print("Welcome")
while True:
	while True:
		while True:
			try:
				option = int(input("Choose the option\n1.- Queue\n2.- Stack\n3.- Linked list\n4.- Exit\nYour answer: "))
				if(option!=1 and option!=2 and option!=3 and option!=4):
					print("\nOops!  That was no valid option.  Try again...")
				else:	
					break
			except ValueError:
				print("Oops!  That was no valid number.  Try again...")

		# Options for queue
		if option==1:
			while True:
				opt = int(input("\nYou choose queue, what do you want to do?\n1.- Check if the queue is empty\n2.- Enqueue\n3.- Dequeue\n4.- Peek\n5.- Exit\nYour answer: "))
				if opt==1:
					print("\nYou choosed 'Check if the queue is empty'")
					if(myQueue.is_empty()):
						print("\nThe queue is empty")
					else:
						print("\nThe queue is not empty")
				elif opt==2:
					print("You choosed 'Enqueue'")
					data = input("Intruduce the new element\nYour answer:")
					myQueue.enqueue(data)
					print(data, " enqueued succesfully")
				elif opt==3:
					print("You choosed 'Dequeue'")
					dequeuedData = myQueue.dequeue()
					print (dequeuedData, " dequeued succesfully")
				elif opt==4:
					print("You choosed 'Peek'")
					dataFront = myQueue.peek()
					print("The value is: ", dataFront)
				elif opt==5:
					print("You choose exit\n")
					break

		# Options for stack
		elif option==2:
			while True:
				opt = int(input("\nYou choose stack, what do you want to do?\n1.- Check if is_empty\n2.- push\n3.- pop\n4.- peek\n5.- Exit\n"))
				if opt==1:
					print("\nYou choosed 'Check if the stack is empty'")
					if(myStack.is_empty()):
						print("\nThe stack is empty")
					else:
						print("\nThe stack is not empty")
				elif opt==2:
					print("You choosed 'Push'")
					data = input("Intruduce the new element\nYour answer:")
					myStack.push(data)
					print(data, " stack succesfully")
				elif opt==3:
					print("You choosed 'pop'")
					popeed_data = myStack.pop()
					print (popeed_data, " popped succesfully")
				elif opt==4:
					print("You choosed 'Peek'")
					topData = myStack.peek()
					print("The value is: ", topData)
				elif opt==5:
					print("You choose exit\n")
					break
				
		# Options for linked list
		elif option==3:
			while True:
				optQ = int(input("\nYou choose linked list, what do you want to do?\n1.- Check if __________\n2.- __________\n3.- __________\n4.- __________\n5.- __________\n6.- Exit"))
			
			break

		# Option for exit
		elif option==4:
			print("Thank u! we love u teacher")
			break
		break
