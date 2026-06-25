
#opening a file in read mode

para = open("bucket_list.txt", "r")
print(para.read())
para.close()

#opening a file in write mode

para = open("bucket_list.txt", "w")
para.write("""
            what is distance travelled and displacement \n \t 
            1. distance travelled - a body which covered a path irrespective of the magnitude(direction)
            2. displacement - the shortest distance between inital point and final position
            """)
para.close()

#opening a file using append mode

para = open("bucket_list.txt", "a")
para.write("""
           
           what is velocity and speed
           
           velocity - rate of displacement
           speed - rate of distance 
           
           """)
para.close()