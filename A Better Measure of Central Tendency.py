#start up
import statistics
print()
print("Welcome to The Greatest Measure of Central Tendency Calculator!")

#var setup
x=0
count = 0
rawdata =[]
v2datalayer3 = 0
v2datalayer4 = 0
v2=[]

#data input
q = input("How many numbers are in your dataset? ")

if q.isdigit() == False:
    q=input("Please enter a valid number: ")
r = int(q)

while r > count:
    a = input("Type a number in the dataset: ")
    if a.isdigit() == False:
        a=input("Please enter a valid number: ")
    b = int(a)
    rawdata.append(b)
    count = count + 1

#mean and median
mean = statistics.mean(rawdata)
median = statistics.median(rawdata)

#mode
frequency = {}
for number in rawdata:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

max_frequency = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_frequency]

#mode for no mode
if len(modes) == 1:
    mode = modes[0]
else:
    mode = None

#datafliter1
if mode == None:
    meanmedianmode = [mean, median]
    mean2=statistics.mean(meanmedianmode)
    median2=statistics.median(meanmedianmode)
    meanmedianmode2=(mean2, median2)
else:
    meanmedianmode = [mean, median, mode]
    mean2=statistics.mean(meanmedianmode)
    median2=statistics.median(meanmedianmode)
    mode2=statistics.mode(meanmedianmode)
    meanmedianmode2 = [mean2, median2, mode2]
one=statistics.mean(meanmedianmode2)

#datalayer2
if mode == None:
    meanmedian2 = [mean2, median2]
    mean3=statistics.mean(meanmedian2)
    median3=statistics.median(meanmedian2)
    meanmedianmode3=(mean3, median3)
else:
    meanmedianmode2 = [mean2, median2, mode2]
    mean3=statistics.mean(meanmedianmode2)
    median3=statistics.median(meanmedianmode2)
    mode3=statistics.mode(meanmedianmode2)
    meanmedianmode3 = (mean3, median3, mode3)
(two)=statistics.mean(meanmedianmode3)

#datalayer3
if mode == None:
    meanmedian3 = [mean3, median3]
    mean4=statistics.mean(meanmedian3)
    median4=statistics.median(meanmedian3)
    meanmedianmode4=(mean4, median4)
else:
    meanmedianmode3 = [mean3, median3, mode3]
    mean4=statistics.mean(meanmedianmode3)
    median4=statistics.median(meanmedianmode3)
    mode4=statistics.mode(meanmedianmode3)
    meanmedianmode4 = (mean4, median4, mode4)
(three)=statistics.mean(meanmedianmode4)

#datalayer4
if mode == None:
    meanmedian5 = [mean4, median4]
    mean5=statistics.mean(meanmedian5)
    median5=statistics.median(meanmedian5)
    meanmedianmode5=(mean5, median5)
else:
    meanmedianmode5 = [mean4, median4, mode4]
    mean5=statistics.mean(meanmedianmode5)
    median5=statistics.median(meanmedianmode5)
    mode5=statistics.mode(meanmedianmode5)
    meanmedianmode5 = (mean5, median5, mode5)
(four)=statistics.mean(meanmedianmode5)

if mode == None:
    meanmedian6 = [mean5, median5]
    mean6=statistics.mean(meanmedian6)
    median6=statistics.median(meanmedian6)
    meanmedianmode6=(mean6, median6)
else:
    meanmedianmode6 = [mean5, median5, mode5]
    mean6=statistics.mean(meanmedianmode6)
    median6=statistics.median(meanmedianmode6)
    mode6=statistics.mode(meanmedianmode6)
    meanmedianmode6 = (mean6, median6, mode6)
(five)=statistics.mean(meanmedianmode6)

if mode == None:
    meanmedian7 = [mean6, median6]
    mean7=statistics.mean(meanmedian7)
    median7=statistics.median(meanmedian7)
    meanmedianmode7=(mean7, median7)
else:
    meanmedianmode7 = [mean6, median6, mode6]
    mean7=statistics.mean(meanmedianmode7)
    median7=statistics.median(meanmedianmode7)
    mode7=statistics.mode(meanmedianmode7)
    meanmedianmode7 = (mean7, median7, mode7)
(six)=statistics.mean(meanmedianmode7)

if mode == None:
    meanmedian8 = [mean7, median7]
    mean8=statistics.mean(meanmedian8)
    median8=statistics.median(meanmedian8)
    meanmedianmode8=(mean8, median8)
else:
    meanmedianmode8 = [mean7, median7, mode7]
    mean8=statistics.mean(meanmedianmode8)
    median8=statistics.median(meanmedianmode8)
    mode8=statistics.mode(meanmedianmode8)
    meanmedianmode8 = (mean8, median8, mode8)
(seven)=statistics.mean(meanmedianmode8)


#final calculations
final= seven

#output
print("Dataset:", rawdata)
print()
print("Mean:", mean)
print("Median:", median)
if mode == None:
    print("Mode:", "No mode")
    print()
    print("Fliter 1:", one)
    print("Fliter 2:", two)
    print("Filter 3:", three)
    print("Filter 4:", four)
    print("Filter 5:", five)
    print("Filter 5:", five)
    print("Filter 6:", six)
    print("Filter 7:", seven)
    print ("Final: ", final)
else:
    print("Mode:", mode)
    print()
    print("Fliter 1:", one)
    print("Fliter 2:", two)
    print("Filter 3:", three)
    print("Filter 4:", four)
    print("Filter 5:", five)
    print("Filter 5:", five)
    print("Filter 6:", six)
    print("Filter 7:", seven)
    print ("Final: ", final)
print()
print("Thank you for using The Greatest Measure of Central Tendency Calculator!")