import os

subdomain = input("Enter the subdomain: ")
max = int(input("Enter the number of log files: "))
new = input("create new clean log report (y/n): ")
report_name  = input("Enter the report name: ")
server = input("Enter the server name: ")

if new == "y":
    os.system(f"goaccess /home/benny/Dokumente/p3l/nginx_logs/{server}/{subdomain}.access.log -a -o /home/benny/Dokumente/p3l/nginx_logs/report_{report_name}.html --persist")
    print(f"created new clean log report")
else:
    os.system(f"goaccess /home/benny/Dokumente/p3l/nginx_logs/{server}/{subdomain}.access.log -a -o /home/benny/Dokumente/p3l/nginx_logs/report_{report_name}.html --restore --persist")
    print(f"appended log report")

print(f"{subdomain}.p3l.app.access.log processed")
range = range(1,max)
for i in range:
    os.system(f"goaccess /home/benny/Dokumente/p3l/nginx_logs/{server}/{subdomain}.access.log.{i} -a -o /home/benny/Dokumente/p3l/nginx_logs/report_{report_name}.html --restore --persist")
    print(f"{subdomain}.p3l.app.access.log.{i} processed")
print("All logs processed")


