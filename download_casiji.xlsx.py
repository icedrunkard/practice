import urllib2
file = urllib2.urlopen('http://www.amorbond.com/caiji.xlsx')
m=file.read()
with open("caiji.xlsx", "wb") as code:     
    code.write(m)
print 'over'
print 'over'
