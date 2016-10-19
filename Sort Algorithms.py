# Seven classic sort algorithm 

# 1. Bubble Sort
# Best: O(n) Worst:O(n^2) Ave:O(n^2)
def bubble_sort(s):
	n = len(s)
	for i in range(n):
		for j in range(1,n-i):
			if s[j-1]>s[j]:
				s[j-1],s[j] = s[j],s[j-1]
	return s

# 2. Select Sort
# Best: O(n^2) Worst:O(n^2) Ave:O(n^2)
def select_sort(s):
	n = len(s)
	for i in range(n):
		smin = i
		for j in range(i+1,n):
			if s[j] < s[smin]:
				smin = j
		s[smin], s[i] = s[i], s[smin]
	return s

# 3. Insert Sort
# Best: O(n) Worst:O(n^2) Ave:O(n^2)
def insert_sort(s):
	n = len(s)
	for i in range(1,n):
		if s[i] < s[i-1]:
			index = i 
			temp = s[i]
			for j in range(i-1,-1,-1):
				if s[j]>temp:
					s[j+1] = s[j]
					index = j
				else:
					break
			s[index] = temp
	return s


# 4. Quick Sort
# Best: O(nlogn) Worst:O(n^2) Ave:O(nlogn)
def quick_sort(s):
	return qsort(s,0,len(s)-1)

def qsort(s, l, r):
	if l>= r:
		return s
	key = s[l]
	lp = l
	rp = r
	while lp<rp:
		while s[rp] >= key and lp<rp:
			rp -= 1
		while s[lp] <= key and lp<rp:
			lp += 1
		s[lp], s[rp] = s[rp], s[lp]
	s[l], s[lp] = s[lp], s[l]
	qsort(s,l,lp-1)
	qsort(s,rp+1,r)
	return s

# 5. Merge Sort
# Best: O(nlogn) Worst:O(nlogn) Ave:O(nlogn)
def merge_sort(s):
	if len(s)<=1:
		return s
	mid = len(s)/2
	left = merge_sort(s[:mid])
	right = merge_sort(s[mid:])
	return merge(left,right)

def merge(left,right):
	l, r = 0,0
	res = []
	while(l<len(left) and r<len(right)):
		if left[l] < right[r]:
			res.append(left[l])
			l += 1
		else:
			res.append(right[r])
			r += 1
	res += left[l:]
	res += right[r:]
	return res

# 6. Heap Sort
# Best: O(nlogn) Worst:O(nlogn) Ave:O(nlogn)

if __name__ == '__main__':
	array = [7,3,4,1,15,24,2,9,11,13,0,6,14]
	print insert_sort(array)