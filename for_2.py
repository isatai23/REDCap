school = 'Massachusetss Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
        or char == 'o' or char == 'u':
            numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1
print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)


num = 10
for num in range(5):
    print num
    
print num

for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!'
        
        
count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x)>=epsilon:
    if guess<=x:
        guess+=step
    else:
        print "guess"+str(guess)
        break
if abs(guess**2-x)>=epsilon:
    print 'failed'
else:
    print 'succeeded:'+str(guess)
    
print "Please think of a number between 0 and 100!"
high=100
low=0
anw=(high+low)/2
while True:
    print "Is your secret number " + str(anw) + "?"
    reply = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too  low. Enter 'c' to indicate I guessed correctly.")
    if reply == 'c':
        print "Game over. Your secret number was:"+ str(anw)
        break
    elif reply == 'l':
        low = anw
        anw = (high+low)/2
    elif reply == 'h':
        high =anw
        anw = (high+low)/2
    else:
        print "Sorry, I did not understand your input"
      