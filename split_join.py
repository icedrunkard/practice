str_='https://maimai.cn/contact/detail/12340000?from=contact_detail_interest&jsononly=1'
#i=s.split('?')[0].split('/')[-1]
#r=int(i)
#print type(r)
#m='?'.join(s.split('/'))
#print '==============='
#print m,type(m)
list_1=str_.split("?")
list_0=list_1[0].split("/")
id_=list_0[-1]
list_0.pop()

i=int(id_)
i-=1
id_=str(i)
list_0.append(id_)


url='/'.join(list_0)
url=url+'?'+list_1[1]
print url
