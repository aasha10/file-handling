file_read = open('codingal.txt')
print(file_read.read())
file_read.close()

file_write = open('codingal1.txt', 'w')
file_write.write("Hi! I am penguin. I am 1 year old.")
file_write.close()

file_append = open('codingal1.txt', 'a')
file_append.write("Hi! I am penguin. I am 1 yr old.")
file_append.close()
