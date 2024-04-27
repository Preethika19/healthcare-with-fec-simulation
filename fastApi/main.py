import getpass
import oracledb

from model import Student

def connect_db() :
    pw = getpass.getpass("Enter password: ")
    connection = oracledb.connect(
        user="system",
        password=pw,
        dsn="localhost/xe")
    print("Successfully connected to Oracle Database")
    return connection

def get_students(connection) :
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student")

    results = cursor.fetchall()

    for row in results:
        for r in row:
            print(r)
    return results

def save_student(student : Student , connection) :
    try :
        cursor = connection.cursor()
        sql = "INSERT INTO student VALUES (" + str(student.student_id) + ",'" +student.first_name + \
            "','" + student.last_name + "',TO_DATE('" + str(student.dob) + "','YYYY-MM-DD'),'" + student.gender  + \
                "','" + student.major + "'," + str(student.cgpa) + ",'" + student.email + \
                    "','" + student.door_no + "','" + student.street + "','" + student.city + "')"
        # sql = "INSERT INTO student VALUES (:student_id, :first_name, :last_name, :dob, :major, :cgpa, :email, :door_no, :street , :city )"
        # print(sql)
        # print(student)
        # param = {"student_id" : student.student_id, "first_name" : student.first_name,
        #          "last_name": student.last_name, "dob" : student.dob, "major" : student.major, 
        #          "cgpa" : student.cgpa, "email" : student.email, "door_no": student.door_no,
        #          "street" : student.street, "city" : student.city }
        # print(param)
        cursor.execute(sql)
        connection.commit()
        return "Student inserted successfully with student id : " + str(student.student_id)
    except Exception as e:
        print(e)
        return "Error while saving. Retry !! "
    
def searchStudent(part_name : str, connection ) :
    sql = "SELECT * FROM student where last_name like '%" + part_name + "%' OR first_name like '%" + part_name + "%'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return result

def deleteStudent(student_id : int, connection) :
    try :
        sql = "DELETE FROM student WHERE student_id= :param1"
        param = { "param1" : student_id}
        cursor = connection.cursor()
        i = cursor.execute(sql, param)
        connection.commit()
        print(i)
        # result = cursor.fetchall()
        # print(result)
        return "Student with student id " + str(student_id) + " deleted !!"
    except Exception  as e :
        print(e)
        return "Error : " + str(e)
    
def getStudentByStudentId(student_id : int, connection) :
    try :
        sql = "SELECT * FROM student WHERE student_id =:id"
        param = { "id" : student_id}
        cursor = connection.cursor()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        if len(result) == 0 :
            return { "Error" : "No matching records in table - student for student id " + str(student_id)}
        print(result)
        return result;
    except Exception as ex :
        print(ex)
        return { "Error" : ex}
def searchStudentByPhoneNo(phone_no : str, connection) :
    sql = "SELECT student_id from student_phone WHERE phone_no ='" + phone_no + "' "
    param = {"phone" : phone_no}
    try :
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        if len(result) == 0 :
            return { "message" : "No student record found for phone no " + phone_no}
        else :
            row = result[0]
            print(row)
            id = row[0]
            return getStudentByStudentId(id,connection)
    except Exception as ex :
        print(ex)
        return {"Error " : ex }
def insertStudentPhone(student_id : int, phone_no : str, connection) :
    try:
        sql = "INSERT INTO STUDENT_PHONE VALUES ( :student_id , :phone_no)"
        param = { "student_id" : student_id, "phone_no": phone_no}
        cursor = connection.cursor()
        result = cursor.execute(sql,param)
        print(result)
        connection.commit()
        return { "message" : "Phone number inserted for student id " + str(student_id)}
    except Exception as ex :
        print(ex)
        return { "Error" : ex}
        
def close_db(connection) :
    connection.close()