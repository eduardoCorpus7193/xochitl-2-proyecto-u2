import ds_queue
import ds_stack
import ds_linked_list

myQueue = ds_queue.Queue()
myStack = ds_stack.Stack()
myLinkedList = ds_linked_list.LinkedList()
print("Welcome")


# While to repeat the main menu
while True:
	# While to repeat the menu of each option
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
				# is_empty method returns a boolean, checking the value to know if the queue os empty or not
				if(myQueue.is_empty()):
					print("\nThe queue is empty")
				else:
					print("\nThe queue is not empty")
			elif opt==2:
				print("You choosed 'Enqueue'")
				data = input("Intruduce the new element\nYour answer:")
				# The enqueue method ask for the value to add as a parameter
				myQueue.enqueue(data)
				print(data, " enqueued succesfully")
			elif opt==3:
				print("You choosed 'Dequeue'")
				# dequeue method returns the value dequeued
				dequeuedData = myQueue.dequeue()
				print (dequeuedData, " dequeued succesfully")
			elif opt==4:
				print("You choosed 'Peek'")
				# peek method returns the the firts value added
				dataFront = myQueue.peek()
				print("The value is: ", dataFront)
			elif opt==5:
				print("You choose exit\n")
				break

	# Options for stack
	elif option==2:
		while True:
			opt = int(input("\nYou choose stack, what do you want to do?\n1.- Check if is_empty\n2.- push\n3.- pop\n4.- peek\n5.- Exit\nYour answer: "))
			if opt==1:
				print("\nYou choosed 'Check if the stack is empty'")
				# is_empty method returns a boolean, checking the value to know if the queue os empty or not
				if(myStack.is_empty()):
					print("\nThe stack is empty")
				else:
					print("\nThe stack is not empty")
			elif opt==2:
				print("You choosed 'Push'")
				data = input("Intruduce the new element\nYour answer:")
				# The push method ask for the value to add as a parameter
				myStack.push(data)
				print(data, " stack succesfully")
			elif opt==3:
				print("You choosed 'pop'")
				# pop method returns the value deleted
				popeed_data = myStack.pop()
				print (popeed_data, " popped succesfully")
			elif opt==4:
				print("You choosed 'Peek'")
				# peek method returns the the last value added
				topData = myStack.peek()
				print("The value is: ", topData)
			elif opt==5:
				print("You choose exit\n")
				break
			
	# Options for linked list
	elif option==3:
		while True:
			optQ = int(input("\nYou choose linked list, what do you want to do?\n1.- Insert at beginning\n2.- Insert at end\n3.- Insert after node\n4.- Delete node\n5.- Display\n6.- Exit\nYour answer: "))
			if optQ==1:
				print("You choose 'Insert at beginning'")
				data = input("Introduce the new element\nYour answer: ")
				myLinkedList.insert_at_beginning(data)
				print(data, " enqueued correctly")
			elif optQ==2:
				print("You choose 'Insert at end'")
				data = input("Introduce the new element\nYour answer: ")
				myLinkedList.insert_at_end(data)
				print(data, " enqueued correctly at the end")
			elif optQ==3:
				print("You choose 'Insert after node'")
				target_data = input("After which elemente you want to add the element\nYour answer: ")
				data = input("Introduce the new element\nYour answer:")
				myLinkedList.insert_after_node(target_data, data)
				print(data, "enqueued after ", target_data, " correctly")
			elif optQ==4:
				print("You choose 'delete node'")
				target_data = input("Which element do you want to delete?\nYour answer: ")
				myLinkedList.delete_node(target_data)
				print(target_data, "Deleted correctly")
			elif optQ==5:
				print("You choose 'Display'")
				myLinkedList.display()
			elif optQ==6:
				print("You choose 'Exit'")
				break
		
	# Option for exit
	elif option==4:
		print("Thank u! we love u teacher")
		break
	