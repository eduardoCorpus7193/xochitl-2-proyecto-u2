import ds_queue
import ds_stack
import ds_linked_list

print("Welcome")
while True:
	while True:
		while True:
			try:
				option = int(input("Choose the option\n1.- Queue\n2.- Stack\n3.- Linked list\nYour answer: "))
				if(option!=1 and option!=2 and option!=3):
					print("\nOops!  That was no valid option.  Try again...")
				else:	
					break
			except ValueError:
				print("Oops!  That was no valid number.  Try again...")

		# Options for queue
		if option==1:
			while True:
				optQ = int(input("You choose queue, what do you want to do?\n"))


		# Options for stack
		elif option==2:


		# Options for linked list
		elif option==2:


		break


	