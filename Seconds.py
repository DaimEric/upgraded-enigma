secondstot = int(input("Enter seconds"))
hours = secondstot//3600
minutes = (secondstot%3600)//60
seconds = (secondstot%3600)%60
print ("this is it: " + '\n', str(hours)+ '\n', str(minutes) + '\n', str(seconds))
##print 'We are the {} who say "{}!"'.format('knights', 'Ni')
print("Input: {0} Hours: {1} Minutes: {2} Seconds: {3}".format(str(secondstot),str(hours), str(minutes), str(seconds)))
