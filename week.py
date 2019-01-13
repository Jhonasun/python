# coding:utf-8
def main():
	week = "SunMonTueWedThuFriSat"
	temp = input("Input the data of week:")
	if int(temp) in range(1,8):
		n = week[(int(temp)-1)*3:((int(temp)-1)*3)+3]
		print ("This data is:"+n)
	else:
		print ("Error!")
		
main()