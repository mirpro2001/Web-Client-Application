from django.contrib import admin
from .models import *


class RequestAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('Request_Code', 'Request_Name', 'Request_Date_Submitted', 'Request_Status')


class PaymentAdmin(admin.ModelAdmin):

    # поля для отображения
    list_display = ('Payment_Code', 'Payer', 'Payer_TIN', 'Payer_Bank',
                    'Payee', 'Payee_TIN', 'Payee_RRC', 'Payee_Bank', 'Amount', 'Payment_Purpose', 'Account_Number')

class ParentAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('Parent_Code', 'Parent_Full_Name', 'Parent_Phone_Number', 'Relationship_Degree', 'Parent_Passport_Series',
                    'Parent_Passport_Number', 'Parent_Email', 'Parent_Gender', 'Parent_Registration_Address', 'Parent_Residential_Address')


class PreschoolerAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Preschooler_Code', 'Group_Code', 'Preschooler_Full_Name', 'Admission_Date', 'Departure_Date', 'Preschooler_Status',
                    'Birth_Certificate_Series', 'Birth_Certificate_Number', 'Date_Of_Birth', 'Preschooler_Gender', 'Registered_Address', 'Residential_Address')

class EducationContractAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Education_Contract_Code', 'Request_Code', 'Payment_Code', 'Preschooler_Code', 'Parent_Code', 'Contract_Date',
                    'Contract_Place', 'Performer', 'Contract_Status')

class ParentsAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Preschooler_Code', 'Parent_Code', 'Party_Name')
    

class MedicalRecordAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Medical_Record_Code', 'Preschooler_Code', 'Healthcare_Institution_Name', 'Medical_Record_Creation_Date', 'Obligatory_Medical_Insurance_Number', 'Medical_Record_Number')


class MedicalRecordEntryAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Medical_Record_Entry_Code', 'Medical_Record_Code', 'Preschooler_Code', 'Doctor_Full_Name', 'Department', 'Date',
                    'Entry_Type', 'Diagnosis', 'Treatment_Stage', 'Note')

class GroupAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Group_Code', 'Group_Name', 'Group_Formation_Date', 'Number_Of_Preschoolers')


class AttendanceAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Attendance_Code', 'Preschooler_Code', 'Lesson_Code', 'Group_Code', 'Teacher_Code', 'Presence', 'Note', 'Date')

class LessonAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Lesson_Code', 'Group_Code', 'Teacher_Code', 'Lesson_Start_Datetime', 'Lesson_End_Datetime', 'Lesson_Title', 'Room')

class TeacherAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Teacher_Code', 'Employee_Code', 'Teacher_Specialization')
    
class EmployeeAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Employee_Code', 'Employee_Full_Name', 'Employee_Date_Of_Birth', 'Department', 'Employee_Position', 'Employee_Passport_Series',
                    'Employee_Passport_Number', 'Employee_TIN', 'Employee_PIPN', 'Employee_Email', 'Employee_Account_Number', 'Employee_Bank_Details', 'Employee_Registration_Address',
                    'Employee_Residential_Address', 'Employee_Salary')
    
class EducationDocumentAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Education_Document_Code', 'Employee_Code', 'Document_Type', 'Educational_Institution_Name', 'Issue_Date', 'Degree',
                    'Qualification', 'Education_Document_Series', 'Education_Document_Number', 'Registration_Number')
    
class PersonalMedicalBookAdmin(admin.ModelAdmin):
    
    # поля для отображения
    list_display = ('Medical_Book_Code', 'Employee_Code', 'Medical_Book_Number', 'Issuing_Place', 'Issue_Date')


admin.site.register(Request, RequestAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Preschooler, PreschoolerAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(EducationContract, EducationContractAdmin)
admin.site.register(Parents, ParentsAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(MedicalRecordEntry, MedicalRecordEntryAdmin)
admin.site.register(EducationDocument, EducationDocumentAdmin)
admin.site.register(PersonalMedicalBook, PersonalMedicalBookAdmin)


