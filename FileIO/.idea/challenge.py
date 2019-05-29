#write a program to append the times tables to our jabberwocky poem
#in sampletext.txt. We want the tables from 2 to 12(similar to the out put from the
#For loops part 2 lecture in section 6)


 #i have created sample.txt with the same content now
 #after running table should append to the poem
with open("sample.txt","a") as asd: #if we change it to "w"
    # then it will delete the contents and create the file each time you run
    for j in range(2,13):
        for i in range(1,13):
            print("{:4} times {} is {}".format(i,j,i*j),file=asd)

        print("-"*30,file=asd)
#__________________________________________________

#if ran again it will append the table again

#__________________________________________________
# for i in range(1,13):
#     print("{:4} times 2 is {}".format(i,2*i))