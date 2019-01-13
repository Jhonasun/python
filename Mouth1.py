# coding:utf-8
def main():
    mouth = "JanFebMarAprMayJunJulAugSepOctNovDev"
    temp = input("Input the number of mouth:")
    if int(temp) in range(1,13):
        n = mouth[(int(temp)-1)*3:((int(temp)-1)*3)+3]
        print ("This mouth is:"+n)
    else:
        print ("Error!")

main()