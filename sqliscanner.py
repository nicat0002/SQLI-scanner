import subprocess
import optparse

parser=optparse.OptionParser()
parser.add_option("-u","--url",dest="url",help="Bu funksiya URL-i daxil etmek uchundur.")
(user_input,args)=parser.parse_args()

url=user_input.url
print("""
 (         (    (      (                                   
 )\ )  (   )\ ) )\ )   )\ )                                
(()/(( )\ (()/((()/(  (()/(        )               (  (    
 /(_))((_) /(_))/(_))  /(_)) (  ( /(  (     (     ))\ )(   
(_))((_)_ (_)) (_))   (_))   )\ )(_)) )\ )  )\ ) /((_|()\  
/ __|/ _ \| |  |_ _|  / __| ((_|(_)_ _(_/( _(_/((_))  ((_) 
\__ \ (_) | |__ | |   \__ \/ _|/ _` | ' \)) ' \)) -_)| '_| 
|___/\__\_\____|___|  |___/\__|\__,_|_||_||_||_|\___||_|   
                                        
                                        BY: NICAT ABBASOV                              
""")
if not url:
    url=input("URL-i daxil edin: ")

komanda=["sqlmap","-u",url,"--batch","--dbs"]
netice=subprocess.check_output(komanda)

if b'available databases' in netice:
    print("SQL İnjection aşkarlandı.")
else:
    print("SQL İnjection aşkarlanmadı.")
