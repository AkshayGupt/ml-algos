
# function that calculates distance b/w two points
def cal_Distance(dimension,ref_point,point,p):
	dist=0
	for i in range(0,dimension):
		dist=dist+(ref_point[i]-point[i])**p

	dist=dist**(1/p)
	return dist


dimension=int(input('Enter dimension '))
n=int(input('Enter number of points '))
k=int(input('Enter k '))
p=int(input('Enter p '))
points=[]
categories=[]

# Taking input points and its category
for i in range(0,n):
	point_temp=[]
	for j in range(0,dimension):
		point_temp.append(int(input('Enter '+str(j+1)+' coordindate '+str(i+1)+' point')))
	cat = input('Enter the category')
	points.append(point_temp)
	categories.append(cat)
	

# Taking refernce point as input
ref_point =[]
for i in range(0,dimension):
    ref_point.append(int(input('Enter '+str(i+1)+' coordindate '+'refernce point')))    

distances =[]
dictc={}

# Calculating distances from n points
for i in range(0,n):
    dist=cal_Distance(dimension,ref_point,points[i],p)
    distances.append(dist)
    dictc[dist]=categories[i]

distances.sort()

# Stores count wise category
category_cnt={}
    
    
maxCnt=0
res=''

# Calculating count of categories
for i in range(0,k):
    cat=dictc[distances[i]]
    if cat in category_cnt:
        category_cnt[cat]=category_cnt[cat]+1
    else:
        category_cnt[cat]=1
    if(category_cnt[cat]>maxCnt):
        maxCnt=category_cnt[cat]
        res=cat

#printing the probable category
print(res)
