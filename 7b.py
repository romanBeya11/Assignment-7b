'''
Created by Roman Beya
Created on 5-12-17
Created for ICS3U
This program generates a fibonocci sequence, then has the ability to pause for however long the user wants
'''
import ui
import time

#Handling first case which is obviously just 1
print 0 + 1

# Create an array that holds the only 2 numbers needed to generate the sequence of numbers
original_array = [0, 1]

def fib(n):
	# This procedure will generate the fibonocci sequence using the original array as a guide
	
	global original_array
	
	# Reverse the original array so that I can access the 'last element', ergo the current number in the sequence
	reversed_array = original_array[::-1]
	current_number = reversed_array[0]
	
	# Remove the current number from the reversed array, so that I can access the subsequent element, aka the previous number in the sequence
	reversed_array.remove(current_number)
	previous_number = reversed_array[0]
	
	# The sequnce works by adding the current number + the previous one in the sequence
	next_num = current_number + previous_number
	
	# Add the new number to the original array to be used as a 'new guide' for the next iteration
	original_array.append(next_num)
	
	# Reverse the 'new guide' and display its most recent element, ergo the current number
	r = original_array[::-1]
	view['sequence_label'].text = str(r[0])
	
	# Pause the sequence for 1 second at a time for asthetics
	time.sleep(1)
	
	# Use recursive procedure to compute all the numbers in the sequence!
	fib(original_array)

@ui.in_background
def generate_sequence_touch_up_inside(sender):
	# Will generate the fibonocci sequence until the user presses pause
	fib(original_array)

def pause_sequence_touch_up_inside(sender):
	# Will pause for 10 seconds on current iteration, then window will close
	
	# Use a try-expect block to catch errors
	try:
		# Pause the view for a user specified amount of time
		pause_time = int(view['user_pause_duration_textfield'].text)
		time.sleep(pause_time)
		view.close()
	except:
		# If they choose not to specify a duration of time, 5 seconds of pause time is the default
		time.sleep(5)
		view.close()
		
view = ui.load_view()
view.present('sheet')
