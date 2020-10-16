#project for python
registration_NO=input("enter your registration id: ")
password=input("enter your log in paasword: ")
email=input("enter your verified mail:")
list1=[]
for i in range(len(registration_NO)):
    list1.append(registration_NO[i])
k=int(list1[-3]+list1[-2]+list1[-1])
a=(list1[-4]+list1[-5])
list2=["a","e","i","o","u"]
list3=[]
list4=[]
list5=[]
list6=[]
#creating paasword
for i in range(len(email)):
    list3.append(email[i])
for item in list3:
    if item in list2:
        list4.append(item)
for i in range(len(password)):
    list5.append(password[i])
for item in list4:
    if item not in list5:
        list6.append(item)

#for metallugical and materials engineering
#data
if len(list6)==0:
    if a=="MM":
        listMM_1= ["ROHIT ORANG","DHEERAJ KUMAR","AKASH SHAIV","SOURAV KUMAR ","SHUBHAM KUMAR ROY","SAMAR GUIN","---","AJAY KUMAR SHARMA","VARUN KUMAR JHA","PRATIK KUMAR","SUBHAM BARNWAL","ADITI SHARMA","SUPARNA CHANDRA","PIYUS PRAJAPATI","SOURAV ROY","ABHISHEK RAJ","PIYUSH PRAKASH","SUMAN HANSDA","INDRAJEET GHOSH","PRABHAT KUMAR","BHAVNA KUMARI","VATSAL RAJ","PRIYANKA KUMARI","SAURAV SAROJ","ANKIT KUMAR","SALONI MAJHI","HARSH KUMAR","KISHAN PANDEY","SUMIT RAJA","JYOTI HANSDA"]
        listMM_2=["SURAJ KUMAR","SUPRIYO RANJAN","PANKAJ KUMAR","---","MOHAN KUMAR","SANKET KUMAR","ESLAVATH SRAVAN","DIVYA DIKSHANT KUMAR","KUMAR SAURAV","PRIYANKA RAJ","JAY PRAKASH","SHASHWAT SHARMA","NIRAJ KUMAR","SACHIN GUPTA","RIGAN RAJ","GARIMA SARAF","ADITI SINGH","GUSHAN KUMAR PANDEY","LAKHAN SINGH SEKHAWAT","M ABHINESH","SHRISHTI SINGH","PALLAVI KUMARI","KISHAN KUMAR","NEHA KEERTHI","SERAJ ANSARI","SHYAM KUMAR","VAIBHAV MISHRA","SAKET PRAKASH","SAMKIKSHA KHADKA","VENKAT RAMANA"]
        listMM_3=["NISHANT MEHTA","SAYON BANERJEE","SHAHID SIDIQQUI","PRITI KUMARI","SRISTI SINGH","BALRAM KUMAR","MOURDHWAJ KUMAR","KAMAL KANT PATRA","DEEPAK KUMAR","SHIVAM GUPTA","AGAM AGNIHOTRI","SANKET DAS","SHUBHAM NAYAK","SAI HEMANTH","RAM KRISHNA","SATYA PRAKASH SAHOO","PRAKASH CHANDRA","TRIVENI","GIRISH SAI KUMAR","AJAY MAHTO","PRABHAT SATYAPATY","NISHANT KUMAR","ANKITA BIT","MANISH KUMAR","AKSHAY SHARMA","RAJ KAMAL YADV","PRABHAT KATIYAR","OMKAR","PAMU SAIRAM","SONUKUMAR"]
        listMM_4=["SAI GANESH","PRABHAT KUMAR","SRIJAN BANDHYOPADHYAY","LAVISH PALIA","DAIVA PREETHI","SHASHANK VIRAG","---","TAHNMAYI","KISLAY KUMAR","GARIMA SARASWAT"]
        CGPA_1=[6.76, 7.16, 7.17, 6.49, 7.93, 7.05, 0, 8.3, 7.46, 7.71, 8.17,7.84, 7.82, 7.53, 8.04, 0,  9.12, 0,7.99, 7.67, 8.29, 8.07, 7.74, 6.74,8.36, 0 ,8.16, 7.93, 7.75, 7.63, 7.72, 7.51, 0, 0, 7.64,0,6.14, 7.76, 7.82, 0, 7.14, 0, 7.33, 8.36, 6.59, 7.41,  7.08, 7.61, 6.39, 0, 7.54, 8.99, 0, 6.87, 7.93, 6.95, 8.14, 8.08, 9.03, 6.42, 7.95, 8.87, 9.33, 8.22, 7.87, 7.71, 6.76, 7.93, 7.00, 8.63, 9.12, 8.34, 8.72, 6.57, 7.01, 7.07, 5.34, 0, 5.7,  6.75, 8.43, 6.46, 7.64, 7.64, 8.26, 6.57, 8.5 ,7.53, 7.11, 7.03, 7.13, 7.45, 7.28, 7.62, 7.74, 7.01, 0, 6.43, 6.11, 8.17,]
        

        #getting information        
        def get_name(n):
            if 0<n<=30:
                print(listMM_1[n-1])
            elif 30<n<=60:
                print(listMM_2[(n-30)-1])
            elif 60<n<=90:
                print(listMM_3[(n-60)-1])
            else:
                print(listMM_4[(n-90)-1])
            print("METALLURGICAL AND MATERIALS ENGINEERING")
        get_name(k)
        print("CGPA: ",CGPA_1[k-1])
        s=CGPA_1[k-1]
        CGPA_1.sort(reverse=True)
        #getting rank in class       
        print("RANK:",CGPA_1.index(s)+1)
        print("For further queries,log in to nitjsr.org")
        
        
      
else:
    print("ERROR! INCORRECT PAASWORD")
 
