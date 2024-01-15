from Queue import Queue

queue = Queue(9)

# Adding elements
print("Adding elements:")
queue.enqueue('🍏')
queue.enqueue('🍌')
queue.enqueue('🍊')
queue.enqueue('🍐')
print(queue.stringify())

# Peek element
peek = queue.peek()
print("Peek element: " + peek + "\n")

# Removing elements
print("Removing elements:")
queue.dequeue()
queue.dequeue()
print(queue.stringify())

# Adding more elements
print("Adding more elements:")
queue.enqueue('🍇')
queue.enqueue('🍉')
queue.enqueue('🍋')
queue.enqueue('🍍')
queue.enqueue('🥭')
queue.enqueue('🍑')
print(queue.stringify())

# Removing more elements
print("Removing more elements:")
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.stringify())