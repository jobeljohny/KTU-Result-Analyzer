
import webbrowser
################NAMES######################

#CHANGE THE VALUES WITH YOUR CLASS/GROUP DATA.......

names={
"SHR17CS060":"jessin",
"SHR17CS061":"jobel",
"SHR17CS062":"jobin",
"SHR17CS063":"john",
"SHR17CS064":"joseph",
"SHR17CS065":"joyal",
"SHR17CS066":"karthic",
"SHR17CS067":"kavya",
"SHR17CS069":"linda",
"SHR17CS070":"maria AS",
"SHR17CS071":"mark",
"SHR17CS072":"mary",
"SHR17CS073":"mayrose",
"SHR17CS074":"melwin",
"SHR17CS077":"yazin",
"SHR17CS078":"naveena",
"SHR17CS079":"neethu",
"SHR17CS080":"neha",
"SHR17CS081":"nimisha",
"SHR17CS082":"nina",
"SHR17CS083":"nithin",
"SHR17CS084":"paul",
"SHR17CS085":"perez",
"SHR17CS086":"rachel",
"SHR17CS087":"resi",
"SHR17CS089":"rini",
"SHR17CS090":"riya",
"SHR17CS091":"rona",
"SHR17CS092":"ronica",
"SHR17CS093":"rose maria",
"SHR17CS094":"roshan johny",
"SHR17CS095":"roshan",
"SHR17CS096":"sachin",
"SHR17CS097":"sandhra simon",
"SHR17CS098":"sandra pv",
"SHR17CS099":"sanjana",
"SHR17CS100":"saranya",
"SHR17CS101":"sharon",
"SHR17CS102":"sherin",
"SHR17CS103":"sneha biju",
"SHR17CS104":"sneha shijo",
"SHR17CS105":"snimle",
"SHR17CS106":"sona francis",
"SHR17CS107":"sona john",
"SHR17CS108":"sreelakshmi",
"SHR17CS109":"sreya",
"SHR17CS111":"swetha",
"SHR17CS112":"syam",
"SHR17CS113":"theres",
"SHR17CS114":"thomas",
"SHR17CS115":"varna",
"SHR17CS116":"varsha",
"SHR17CS117":"vimal",
"SHR17CS118":"vishnu chandhran",
"SHR17CS119":"vishnu vijayan"

}
################# GRADES ######################

# CHANGE IF GRADING PATTERNS ARE DIFFERENT .....
grades={
    "O":10,
    "A+":9,
    "A":8.5,
    "B+":8,
    "B":7,
    "C":6,
    "P":5,
    "$":0
}
########################################################################################
# PROCESSING PART
def failure(stud):
    stud=stud.replace("(F)","($)")
    stud=stud.replace("(FA)","($)")
    stud=stud.replace("(FE)","($)")
    stud=stud.replace("(Absent)","($)")
    stud=stud.replace("(Debarred)","($)")
    stud=stud.replace("(Student Cancelled)","($)")
    
    return stud
def get_Rank_List(data):
    data=failure(data)
    for key in credit.keys():
        data=data.replace(key,str(credit[key])) 
    for key in grades.keys():
        data=data.replace(key,str(grades[key])) 
    data=data.replace("(","*(")

    
    mat=data.split("\n")
    mat =[x.split(",") for x in mat]
    for i in range(len(mat)):
        for j in range(1,len(mat[i])):
            mat[i][j]=eval(mat[i][j])
    lis=[]
    for x in mat:
        lis.append([x.pop(0),round(sum(x)/sum(credit.values()),2)])
    lis.sort(key=lambda x:x[1],reverse=True)
    return prepare_list(lis)

def htm(lis):
    subscript=''
    for i in lis:
        st="{:<16} : {:<4}".format(i[0].upper(),i[1])
        subscript=subscript+"<li><a href=#><b><pre>"+st+"</pre></b></a></li>\n"

    return subscript
def prepare_list(lis):
    global rl
    rl=htm(lis)
    data="\n\n{:<2} {:<16}     {:<5} ".format("NO"," NAME","GRADE POINT")
    for i in range(len(lis)):
        a,b=lis[i]
        data=data+"\n\n{:<2}) {:<16} -   {:<5} ".format(i+1,a.upper(),b)
    return data

def initScript():
    script='''
    <html>
    <head><title>REPORT</title>
    <style>

    h1 {
        letter-spacing : 2px;
  text-shadow: 0 1px 0 #ccc,
               0 2px 0 #c9c9c9,
               0 3px 0 #bbb,
               0 4px 0 #b9b9b9,
               0 5px 0 #aaa,
               0 6px 1px rgba(0,0,0,.1),
               0 0 5px rgba(0,0,0,.1),
               0 1px 3px rgba(0,0,0,.3),
               0 3px 5px rgba(0,0,0,.2),
               0 5px 10px rgba(0,0,0,.25),
               0 10px 10px rgba(0,0,0,.2),
               0 20px 20px rgba(0,0,0,.15);
    color:white;
}
h2 {
  text-shadow: 0 1px 0 #ccc,
               0 2px 0 #c9c9c9,
               0 3px 0 #bbb,
               0 4px 0 #b9b9b9,
               0 5px 0 #aaa,
               0 6px 1px rgba(0,0,0,.1),
               0 0 5px rgba(0,0,0,.1),
               0 1px 3px rgba(0,0,0,.3),
               0 3px 5px rgba(0,0,0,.2),
               0 5px 10px rgba(0,0,0,.25),
               0 10px 10px rgba(0,0,0,.2),
               0 20px 20px rgba(0,0,0,.15);
    color:white;
    letter-spacing : 2px;
}
h3 {
  text-shadow: 0 1px 0 #ccc,
               0 2px 0 #c9c9c9,
               0 3px 0 #bbb,
               0 4px 0 #b9b9b9,
               0 5px 0 #aaa,
               0 6px 1px rgba(0,0,0,.1),
               0 0 5px rgba(0,0,0,.1),
               0 1px 3px rgba(0,0,0,.3),
               0 3px 5px rgba(0,0,0,.2),
               0 5px 10px rgba(0,0,0,.25),
               0 10px 10px rgba(0,0,0,.2),
               0 20px 20px rgba(0,0,0,.15);
    color:white;
    letter-spacing : 2px;
}
    body{
        font-family:"Raleway",sans-serif;
        background-image: linear-gradient(to right,rgba(69, 0, 158, 0.7),rgba(0, 0, 0, 1));
     }
     .list-type1{
width:400px;
margin:0 auto;
}

.list-type1 ol{
counter-reset: li;
list-style: none;
*list-style: decimal;
font-size: 15px;
font-family: 'Raleway', sans-serif;
padding: 0;
margin-bottom: 4em;
}
.list-type1 ol ol{
margin: 0 0 0 2em;
}

.list-type1 a{
position: relative;
display: block;
padding: .4em .4em .4em 2em;
*padding: .4em;
margin: .5em 0;
background: #93C775;
color: #000;
text-decoration: none;
-moz-border-radius: .3em;
-webkit-border-radius: .3em;
border-radius: 10em;
transition: all .2s ease-in-out;
}

.list-type1 a:hover{
background: #d6d4d4;
text-decoration:none;
transform: scale(1.1);
}

.list-type1 a:before{
content: counter(li);
counter-increment: li;
position: absolute;
left: -1.3em;
top: 50%;
margin-top: -1.3em;
background:#93C775;
height: 2em;
width: 2em;
line-height: 2em;
border: .3em solid #fff;
text-align: center;
font-weight: bold;
-moz-border-radius: 2em;
-webkit-border-radius: 2em;
border-radius: 2em;
color:#FFF;
}
.list-type3{
margin:0 auto;
width:1200px;
}
.list-type3 li, .list-type3 a{
display: block;
padding : 5px 15px;
float:left;
height:35px;
line-height:35px;
position:relative;
font-size:15px;
margin-bottom: 12px;
font-family: 'Raleway', sans-serif;
transition: background-color 1.5s ease;
}
.list-type3 a{

padding:0 60px 0 12px;
background:#0089e0;
color:#fff;
text-decoration:none;
-moz-border-radius-bottomright:4px;
-webkit-border-bottom-right-radius:4px;
border-bottom-right-radius:4px;
-moz-border-radius-topright:4px;
-webkit-border-top-right-radius:4px;
border-top-right-radius:4px;
}

.list-type3 a:before{
content:"";
float:left;
position:absolute;
top:0;
left:-12px;
width:0;
height:0;
border-color:transparent #0089e0 transparent transparent;
border-style:solid;
border-width: 18px 12px 18px 0;
}

.list-type3 a:after{
content:"";
position:absolute;
top:15px;
left:0;
float:left;
width:6px;
height:6px;
-moz-border-radius:2px;
-webkit-border-radius:2px;
border-radius:2px;
background:#fff;
-moz-box-shadow:-1px -1px 2px #004977;
-webkit-box-shadow:-1px -1px 2px #004977;
box-shadow:-1px -1px 2px #004977;
}
.list-type3 a:hover{
background:#555;
}

.list-type3 a:hover:before{
border-color:transparent #0089e0 transparent transparent;
}
.list-type5{
width:410px;
margin:0 auto;
}
.list-type5 ol {
list-style-type: none;
list-style-type: decimal !ie; 
margin: 0;
margin-left: 1em;
padding: 0;
counter-reset: li-counter;
}
.list-type5 ol li{
position: relative;
margin-bottom: 1.5em;
padding: 0.5em;
background-color: #F0D756;
padding-left: 58px;
}

.list-type5 a{
text-decoration:none;
color:black;
font-size:15px;
font-family: 'Raleway', sans-serif;
}

.list-type5 li:hover{
box-shadow:inset -1em 0 #6CD6CC;
-webkit-transition: box-shadow 0.5s; /* For Safari 3.1 to 6.0 */
transition: box-shadow 0.5s;
}

.list-type5 ol li:before {
position: absolute;
top: -0.3em;
left: -0.5em;
width: 1.8em;
height: 1.2em;
font-size: 2em;
line-height: 1.2;
font-weight: bold;
text-align: center;
color: white;
background-color: #6CD6CC;
transform: rotate(-20deg);
-ms-transform: rotate(-20deg);
-webkit-transform: rotate(-20deg);
z-index: 99;
overflow: hidden;
content: counter(li-counter);
counter-increment: li-counter;
}
.list-type2{
width:400px;
margin:0 auto;
}

.list-type2 ol{
counter-reset: li;
list-style: none;
*list-style: decimal;
font-size: 15px;
font-family: 'Raleway', sans-serif;
padding: 0;
margin-bottom: 4em;
}

.list-type2 ol ol{
margin: 0 0 0 2em;
}

.list-type2 a{
position: relative;
display: block;
padding: .4em .4em .4em 2em;
*padding: .4em;
margin: .5em 0;
background: #FC756F;
color: #444;
text-decoration: none;
transition: all .2s ease-in-out;
}

.list-type2 a:hover{
background: #d6d4d4;
text-decoration:none;
transform: scale(1.1);
}

.list-type2 a:before{
content: counter(li);
counter-increment: li;
position: absolute;
left: -1.3em;
top: 50%;
margin-top: -1.3em;
background:#FC756F;
height: 2em;
width: 2em;
line-height: 2em;
border: .3em solid #fff;
text-align: center;
font-weight: bold;
color:#FFF;
}

 
    </style>
    </head>
    <body>
    <h1 align="center"><i>REPORT</i></h1><br><br><br>
    

    '''
    return script

def addScript(data):
    global script
    script=script+data


def generate_report(details,all_pass,fail,ranklist):
    global script
    script=initScript()
    for student in details:
        student=failure(student)
        fail_count = student.count('$')
        fail[student.split(",")[0]]=fail_count
        if(fail_count==0):
            all_pass.append(student.split(",")[0])
    rep=open("report.txt","w")
    
    rep.write("\n\t\t\t\tREPORT\n\n")
    rep.write("\n\n\n* processed details : "+str(len(details)))
    
    rep.write("\n\n * no. of full pass students : "+str(len(all_pass)))
    rep.write("\n\n * no. of failed students : "+str(len(names)-len(all_pass)))
    rep.write("\n\n * list of full passed students :\n\n")
    addScript('''<div class="list-type1">
    <ol>
    <li><a href=#><b>Total Students     : '''+str(len(details))+'''</b></a></li>
    <li><a href=#><b>Full Pass Students : '''+str(len(all_pass))+'''</b></a></li>
    <li><a href=#><b>Failed Students    : '''+str(len(names)-len(all_pass))+'''</b></a></li>
    </ol>
    </div>''')
    addScript('''<br><h2 align="center">LIST OF FULL PASS STUDENTS </h2><br>''')
    addScript("")
    subscript=""
    for i in all_pass:
        subscript=subscript+"<li><a href=#><b>"+i.upper()+"</b></a></li>\n"
    addScript('''<div class="list-type3"><ol>'''+subscript+"</ol></div>")
    cnt=1
    n=4
    tpass=all_pass
    while(len(tpass)%n!=0):
        tpass.append("")

    final = [tpass[i * n:(i + 1) * n] for i in range((len(tpass) + n - 1) // n )]
    for i in final:
        a,b,c,d=i
        rep.write("{:<16} {:<16} {:<16} {:<16}\n\n".format(a,b,c,d))
    rep.write("\n\n\t\t\t STUDENT ARRIERS:\n\n")
    for i in range(14):

        addScript("<br>")
    
    
    addScript('''<br><h2 align= "center">STUDENT ARRIERS </h2><br>''')
    subscript=""
    fail = {k: v  for k,v in sorted(fail.items(),key=lambda item : item[1])}
    for i in fail.keys():
        st="\n{:<16} : {:<16} ".format(i.upper(),fail.get(i))
        rep.write(st)
        #rep.write("\n"+i+" : "+str(fail.get(i)))
        subscript=subscript+"<pre><li><a href=#><b>"+st+"</b></a></li></pre>\n"
    addScript('''<div class="list-type2"><ol>'''+subscript+"</ol></div>")
    rep.write("\n\n\n\t\t\tRANK LIST\n\n\n")
    addScript('''<br><h1 align="center">RANK LIST :</h1><br>''')
    addScript('''<div class="list-type5"><ol>'''+rl+"</ol></div>")
    rep.write(ranklist)
    rep.close()
    rep2=open("report.html","w")
    rep2.write(script+"</body></html>")
    rep2.close()
    webbrowser.open("report.html")
    

def extract(CC):
    a={}
    b={}
    for key,li in CC.items():
        a[key]=li[0]
        b[key]=li[1]
    return a,b


    


def feed(CC):
    global credit,codes
    codes,credit=extract(CC)
    f=open("res.txt","r")
    data=f.read()
    
    for key in names.keys():
        data=data.replace(key,names[key]+',')
    ranklist=get_Rank_List(data)
    for key in codes.keys():
        data=data.replace(key,codes[key])
    name=list(names.values())
    wr=open("processed.csv","w")
    wr.write(data)
    wr.close()


    for i in range(len(names)):
        fail[name[i]]=0

    details=data.split('\n')
    print("\n\tREPORT\n")
    print("processed details : ",len(details))
    generate_report(details,all_pass,fail,ranklist)

data=""
rl=[]
all_pass=[]
fail={}
codes={}
credit={}
script=""

        
