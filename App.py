from flask import Flask, render_template, request, session, flash

import mysql.connector
import sys, fsdk, math, ctypes, time
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/NewFaculty')
def NewFaculty():
    return render_template('NewFaculty.html')


@app.route('/FacultyLogin')
def FacultyLogin():
    return render_template('FacultyLogin.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb")
            data = cur.fetchall()
            flash("Your are Logged In...!")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName Or PassWord is Wrong...!")
            return render_template('index.html', error=error)


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AStudentInfo")
def AStudentInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb")
    data = cur.fetchall()
    return render_template('AStudentInfo.html', data=data)


@app.route("/AAttendanceInfo")
def AAttendanceInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM attentb")
    data = cur.fetchall()
    return render_template('AAttendanceInfo.html', data=data)


@app.route("/newfac", methods=['GET', 'POST'])
def newfac():
    if request.method == 'POST':
        name = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into regtb values('','" + name + "','" + mobile + "','" + email + "','" + username + "','" + password + "')")
        conn.commit()
        conn.close()
        flash("Record Saved!")
    return render_template('FacultyLogin.html')


@app.route("/facultylogin", methods=['GET', 'POST'])
def facultylogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash("Username or Password is wrong...!")
            return render_template('index.html')
        else:
            session['email'] = data[3]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and password='" + password + "'")
            data = cur.fetchall()

            flash("you are successfully logged in")
            return render_template('FacultyHome.html', data=data)

@app.route('/FacultyHome')
def FacultyHome():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where username='" + uname + "'")
    data = cur.fetchall()
    return render_template('FacultyHome.html', data=data)

@app.route('/NewStudent')
def NewStudent():
    import LiveRecognition  as liv

    liv.att()
    del sys.modules["LiveRecognition"]
    return render_template('NewStudent.html')


@app.route("/newstudent", methods=['GET', 'POST'])
def newstudent():
    if request.method == 'POST':
        regno = request.form['regno']
        uname = request.form['uname']
        gender = request.form['gender']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['Address']
        depart = request.form['depart']
        Batch = request.form['Batch']
        year = request.form['year']
        Shift = request.form['Shift']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into studenttb values('','" + regno + "','" + uname + "','" + gender + "','" + mobile + "','" + email + "','" + address + "' ,'" + depart + "','" + Batch + "','" + year + "','" + Shift + "')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM studenttb  ")
        data = cur.fetchall()

        flash("Record Saved!")
        return render_template('FStudentInfo.html', data=data)


@app.route('/FStudentInfo')
def FStudentInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb  ")
    data = cur.fetchall()
    return render_template('FStudentInfo.html', data=data)


@app.route('/FAttendance')
def FAttendance():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb  ")
    data = cur.fetchall()
    return render_template('FAttendance.html', data=data)


@app.route("/attendance", methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        if request.form["submit"] == "submit":
            import datetime
            date1 = request.form['date']
            date = datetime.datetime.strptime(date1, '%Y-%m-%d')
            print(date)
            check = request.form.getlist("check")
            check1 = request.form.getlist("check1")

            for m in check1:

                if m in check:
                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='')
                    cursor = conn.cursor()
                    cursor.execute("SELECT  *  FROM studenttb where  RegisterNo='" + m + "'")
                    data = cursor.fetchone()

                    if data:
                        regno = data[1]
                        name = data[2]
                        Mobile = data[4]
                        Department = data[7]
                        Batch = data[8]
                        Year = data[9]
                        Shift = data[10]

                        sendmsg(Mobile, "Your Son Or daughter Present today")

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='5collegestuatIOdb')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into attentb values('','" + regno + "','" + name + "','" + Mobile + "','" + Department + "','" + Batch + "','" + Year + "' ,'" + Shift + "','" + str(
                            date) + "','1')")
                    conn.commit()
                    conn.close()

                    print(m + 'is present in the list')


                else:
                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='5collegestuatIOdb')
                    cursor = conn.cursor()
                    cursor.execute("SELECT  *  FROM studenttb where  RegisterNo='" + m + "'")
                    data = cursor.fetchone()

                    if data:
                        regno = data[1]
                        name = data[2]
                        Mobile = data[4]
                        Department = data[7]
                        Batch = data[8]
                        Year = data[9]
                        Shift = data[10]

                        sendmsg(Mobile,"Your Son Or daughter Absent today")

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='5collegestuatIOdb')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into attentb values('','" + regno + "','" + name + "','" + Mobile + "','" + Department + "','" + Batch + "','" + Year + "' ,'" + Shift + "','" + str(
                            date) + "','0')")
                    conn.commit()
                    conn.close()

                    flash("Record Saved!")
                    return render_template('FAttendance.html')

        else:
            depart = request.form['depart']
            Batch = request.form['Batch']
            year = request.form['year']
            Shift = request.form['Shift']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM studenttb where Department='" + depart + "' and Batch='" + Batch + "'  and year='" + year + "' and Shift='" + Shift + "' ")
            data = cur.fetchall()
            return render_template('FAttendance.html', data=data)

def sendmsg(targetno,message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")

@app.route('/FAttendanceInfo')
def FAttendanceInfo():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM attentb")
    data = cur.fetchall()
    return render_template('FAttendanceInfo.html', data=data)


@app.route("/attendancesearch", methods=['GET', 'POST'])
def attendancesearch():
    if request.method == 'POST':

        depart = request.form['depart']
        Batch = request.form['Batch']
        year = request.form['year']
        Shift = request.form['Shift']

        import datetime
        date1 = request.form['date']
        date = datetime.datetime.strptime(date1, '%Y-%m-%d')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM attentb where Date='" + str(date) + "'  and Department='" + depart + "' and Batch='" + Batch + "'  and Year='" + year + "' and Shift='" + Shift + "' ")
        data = cur.fetchall()
        return render_template('FAttendanceInfo.html', data=data)


@app.route("/Aattendancesearch", methods=['GET', 'POST'])
def Aattendancesearch():
    if request.method == 'POST':
        depart = request.form['depart']
        Batch = request.form['Batch']
        year = request.form['year']
        Shift = request.form['Shift']

        import datetime
        date1 = request.form['date']
        date = datetime.datetime.strptime(date1, '%Y-%m-%d')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM attentb where Date='" + str(date) + "'  and Department='" + depart + "' and Batch='" + Batch + "'  and Year='" + year + "' and Shift='" + Shift + "' ")
        data = cur.fetchall()
        return render_template('AAttendanceInfo.html', data=data)

@app.route("/Remove")
def Remove():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cursor = conn.cursor()
    cursor.execute("delete from  studenttb  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb ")
    data = cur.fetchall()

    return render_template('FStudentInfo.html', data=data)


@app.route("/Remove1")
def Remove1():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cursor = conn.cursor()
    cursor.execute("delete from  studenttb  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb ")
    data = cur.fetchall()

    return render_template('AStudentInfo.html', data=data)

@app.route("/searchid")
def searchid():
    # eid= request.args.get('eid')
    # session['eid']=eid

    import LiveRecognition1  as liv1
    liv1.examvales()
    # liv1.att()
    # print(ExamName)
    del sys.modules["LiveRecognition1"]

    return render_template('index.html')

@app.route("/searchid1")
def searchid1():
    # eid= request.args.get('eid')
    # session['eid']=eid

    import LiveRecognition2  as liv2
    liv2.examvales()
    del sys.modules["LiveRecognition2"]

    return render_template('index.html')




@app.route("/Fattendance", methods=['GET', 'POST'])
def Fattendance():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM attentb")
    data = cur.fetchall()
    return render_template('Fattendance.html', data=data)


"""@app.route("/AUserSearch", methods=['GET', 'POST'])
def AUserSearch():
    if request.method == 'POST' and request.form["submit"] == "Close":
        date = request.form['date']
        regtb = ''  # Assuming this should be assigned to some meaningful value later.

        # Connect to the database once
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
        cursor = conn.cursor()
        # Fetch students data
        cursor.execute("SELECT * FROM studenttb")
        students_data = cursor.fetchone()
        out1 = ''
        out2 = ''
        for student in students_data:
            regno = students_data[1]
            name = students_data[2]
            Mobile = students_data[4]
            Department = students_data[7]
            Batch = students_data[8]
            Year = students_data[9]
            Shift = students_data[10]
            print(regno)


            # Check if attendance record already exists for the date and registration number
            cursor.execute("SELECT * FROM attentb WHERE Date=%s AND Regno=%s", (date, regno))
            attendance_data = cursor.fetchone()

            if attendance_data is None:
                # Insert new attendance record
                cursor.execute(
                    "insert into attentb values('','" + regno + "','" + name + "','" + Mobile + "','" + Department + "','" + Batch + "','" + Year + "' ,'" + Shift + "','" + str(
                        date) + "','Absent')")
                #flash("Attendance not recorded for today")
                reg = student[1]
                sname = student[2]
                if out2 == "":
                    out2 = "Absent details Regno " + reg + 'Student name ' + sname
                else:
                    out2 = out2 + " Regno " + reg + ' Student name ' + sname

                # sendmsg('9087259509', "Your Not attend college today")  # Uncomment if you have a function to send messages
                #sendmail(email, 'UserName ' + uname + " Password :" + password + "  HoneyKey " + generated_key)
            else:
                #flash("Attendance already recorded")
                reg = attendance_data[1]
                sname = attendance_data[2]
                if out1=="":
                    out1="Present details Regno "+reg+' Student name '+sname
                else:
                    out1=out1+" Regno "+reg+' Student name '+sname

            email = session['email']
            print(email)
            print(out1)
            print(out2)
            sendmail(email,out1+","+out2)
            conn.commit()

            # Fetch attendance data
            cursor.execute("SELECT * FROM attentb WHERE Date=%s", (date,))
            attendance_data = cursor.fetchall()

            conn.close()

            return render_template('Fattendance.html', data=attendance_data)
"""
@app.route("/AUserSearch", methods=['GET', 'POST'])
def AUserSearch():
    if request.method == 'POST' and request.form["submit"] == "Close":
        date = request.form['date']

        # Establish connection only once
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
        cursor = conn.cursor()

        # Fetch students data
        cursor.execute("SELECT * FROM studenttb")
        students_data = cursor.fetchall()

        out1 = ''
        out2 = ''

        for student in students_data:
            regno = student[1]
            name = student[2]
            Mobile = student[4]
            Department = student[7]
            Batch = student[8]
            Year = student[9]
            Shift = student[10]

            print(regno)

            # Use the same cursor to check attendance
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='5collegestuatIOdb')
            cursor = conn.cursor()

            # Fetch students data
            cursor.execute("SELECT * FROM attentb where Date='"+ date +"' and Regno='"+ regno +"' ")
            attendance_data = cursor.fetchone()

            if attendance_data is None:
                # Insert new attendance record
                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='5collegestuatIOdb')
                cursor = conn.cursor()
                cursor.execute(
                    "insert into attentb values('','" + regno + "','" + name + "','" + Mobile + "','" + Department + "','" + Batch + "','" + Year + "' ,'" + Shift + "','" + str(
                        date) + "','Absent')")
                conn.commit()
                conn.close()
                flash("Attendance not recorded for today")

                reg = student[1]
                sname = student[2]
                if out2 == "":
                    out2 = f"Absent details Regno {reg} Student name {sname}"
                else:
                    out2 += f" Regno {reg} Student name {sname}"

                # sendmsg('9087259509', "Your Not attend college today")  # Uncomment if you have a function to send messages
            else:
                flash("Attendance already recorded")
                reg = attendance_data[1]
                sname = attendance_data[2]
                if out1 == "":
                    out1 = f"Present details Regno {reg} Student name {sname}"
                else:
                    out1 += f" Regno {reg} Student name {sname}"

        email = session.get('email', '')  # Use .get() to avoid KeyError if email is missing
        print(email)
        print(out1)
        print(out2)

        sendmail(email, f"{out1}, {out2}")

        #conn.commit()  # Commit after all operations

        # Fetch attendance data
        cursor.execute("SELECT * FROM attentb WHERE Date=%s", (date,))
        attendance_data = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        conn.close()

        return render_template('Fattendance.html', data=attendance_data)


def sendmail(Mailid, message):
    print(Mailid)
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "qmgn xecl bkqv musr")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
