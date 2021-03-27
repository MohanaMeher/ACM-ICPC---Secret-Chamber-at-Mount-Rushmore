def check(d,oc,tc,original):
	queue = []
	queue.append(oc)
	while(len(queue)!=0 and queue[0]!=tc):
		if queue[0] in d:
			for v in d[queue[0]]:
				if (v!=original): 
					queue.append(v)
		queue.pop(0)
	return len(queue) == 0
 
if __name__ == "__main__":
	d = {} 
	m,n = map(int,input().split())
	for i in range(m):
		A,B = input().split()
		if A not in d:
			d[A] = [] 
		d[A].append(B)
 
	ori,trans = [],[]
	for _ in range(n):
		A,B = input().split()
		ori.append(A) 
		trans.append(B)
 
	for k in range(n):
		original = ori[k] 
		translated = trans[k]
		if (len(original) != len(translated)): 
			print("no")
		elif (original == translated):
			print("yes")
		else:
			originallist = list(original)
			translatedlist = list(translated)
			length = len(originallist) 
			c = 0
			for t in range(length):
				if originallist[t]!=translatedlist[t] and check(d,originallist[t],translatedlist[t],originallist[t]==False):
					break
				c+=1
			if (c==length):
				print("yes")
			else:
				print("no")
