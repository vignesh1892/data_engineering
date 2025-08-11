from mysql_operations import DBOperations

print("start")
mydb =DBOperations()
print(mydb.getall_databases())
mydb.create_tbl("tblcustomer_vignesh",["custid","fullname","age","profession"])

with open("custs.txt","r") as file:
    custrec= [ line.strip().split(",") for line in file.readlines()[1:]]
    #mydb.insert_tbl(custrec)

prof_cnt = mydb.execute_query("select count(*) cnt,profession from kbnhzraf_ticketdb.tblcustomer_vignesh group by profession")


with open("prof_count.txt","w") as file:
    for row in prof_cnt:
        file.write(",".join(str(item) for item in row)+ "\n")
    

if __name__ == "__main__":
    print("start")