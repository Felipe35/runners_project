import csv
# Studen Name: Andres Felipe Penaranda
# Assigment Number: 4

def nameExists(nameList, name):
    names = []
    for i in nameList:
        names.append(i['name'])
    if name in names:
        return True
    else:
        return False


#def calcAvg(times):
    #timeList = []
    
    #for time in times:
        #timeList.extend([int(r["bos"]), int(r["chi"]), int(r["ny"])])
    #avg = sum(timeList) / len(timeList)
    #return avg

def readData():
    fields = ("name", "bos", "chi", "ny", "avg")
    f = open("runners.txt", "r")
    
    runs = []
    dReader = csv.DictReader(f, fieldnames = fields, delimiter = ",")
    
    for row in dReader:
        runs.append(row)
        
    f.close()
    return runs



def filterName(name):
    nameInput = input("Enter name to search: ").lower()
    print()
    fs = "%-8s %-8s %-8s %-8s %8s"
    print(fs % ("Name", "Boston", "Chicago", "New York", "Average"))
    
    for r in name:
        av = []
        fs = "%-8s %-8s %-8s %-8s %4s"
        av.extend([int(r["bos"]), int(r["chi"]), int(r["ny"])])
      
        if nameInput == r["name"]:
            r["avg"] = round((int(r["bos"]) + int(r["chi"]) + int(r["ny"])) / len(av))
            print(fs % (r["name"], r["bos"], r["chi"], r["ny"], r["avg"]))
            break
    else:
        print("Name: " + nameInput + " no found")



def displayData(runners):
    fs = "%-8s %-8s %-8s %-8s"
    print(fs % ("Name", "Boston", "Chicago", "New York"))
    
    for r in runners:
        fs = "%-8s %-8s %-8s %-8s"

        print(fs % (r["name"], r["bos"], r["chi"], r["ny"]))



def addRunner(runners):
	
    while True:
        name = input("Enter runner's name or quit to exit: ").lower()
        checkName = nameExists(runners, name)
        
        if name == '' or name.isdigit() == True:
            print("Please enter runner's name...")
            continue
            
        elif name == "quit":
            break
            
        elif checkName != True:   
            bos = input("Enter race time for Boston: ")
            chi = input("Enter race time for Chicago: ")
            ny = input("Enter race time for New York: ") 
          
            record = {"name":name, "bos":bos, "chi":chi, "ny":ny}
            runners.append(record)
            break
        else:
            print("Name: " + "%5s" % (name)+" already exists..")
    return runners




def storeData(runners):
    fields = ("name", "bos", "chi", "ny", "avg")
    f = open("runners.txt", "w")
    dWriter = csv.DictWriter(f, fieldnames = fields, delimiter = ",", lineterminator = "\n")
    dWriter.writerows(runners)
    
    f.close()

def main():
    
    runners = readData()
    
    while True:
        print("""
        Menu options. Choose 1, 2, 3, or 4
        1. Display all Data for all races
        2. Display all runners individual race average in minutes
        3. Add a new runner and race data
        4. Save and exit
        
        """)
        
        opt = input("    Enter your choice, 1, 2, 3, or 4: ")
        
        if opt == '1':
            print()
            displayData(runners)
        elif opt == '2':
            filterName(runners)
        elif opt == '3':
            runners = addRunner(runners)
        elif opt == '4':
            storeData(runners)
            print("Goodbye")
            break
        else:
            print('Invalid entry')

main()