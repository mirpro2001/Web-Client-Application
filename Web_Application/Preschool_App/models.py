from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime



class Request(models.Model):
    """Заявка"""

    class Meta:
        db_table = "Request"
        verbose_name = "Информация о заявках на обучение"
        verbose_name_plural = "Информация о заявках на обучение"

    Request_Code = models.AutoField(primary_key=True, verbose_name="Код заявки")
    Request_Name = models.IntegerField(verbose_name="Наименование заявки")
    Request_Date_Submitted = models.DateTimeField(verbose_name="Дата поступления заявки")
    Request_Status = models.CharField(max_length=20, verbose_name="Статус заявки")



class Payment(models.Model):
    """Платеж"""

    class Meta:
        db_table = "Payment"
        verbose_name = "Информация о платежах"
        verbose_name_plural = "Информация о платежах"

    Payment_Code = models.AutoField(primary_key=True, verbose_name="Код платежа")
    Payer = models.CharField(max_length=100, verbose_name="Плательщик")
    Payer_TIN = models.CharField(max_length=20, verbose_name="ИНН плательщика")
    Payer_Bank = models.CharField(max_length=50, verbose_name="Банка плательщика")
    Payee = models.CharField(max_length=100, verbose_name="Получатель")
    Payee_TIN = models.CharField(max_length=20, verbose_name="ИНН получателя")
    Payee_RRC = models.CharField(max_length=20, verbose_name="КПП получателя")
    Payee_Bank = models.CharField(max_length=50, verbose_name="Банк получателя")
    Amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    Payment_Purpose = models.CharField(max_length=100, verbose_name="Назначение платежа")
    Account_Number = models.CharField(max_length=20, verbose_name="Номер счета")



class Parent(models.Model):
    """Родитель"""

    class Meta:
        db_table = "Parent"
        verbose_name = "Данные о родителе"
        verbose_name_plural = "Данные о родителях"

    Parent_Code = models.AutoField(primary_key=True, verbose_name="Код родителя")
    Parent_Full_Name = models.CharField(max_length=100, verbose_name="ФИО родителя")
    Parent_Phone_Number = models.CharField(max_length=20, verbose_name="Телефон родителя")
    Relationship_Degree = models.CharField(max_length=50, verbose_name="Степень родства")
    Parent_Passport_Series = models.CharField(max_length=10, verbose_name="Серия паспорта родителя")
    Parent_Passport_Number = models.CharField(max_length=10, verbose_name="Номер паспорта родителя")
    Parent_Email = models.CharField(max_length=100, verbose_name="Электронная почта родителя")
    Parent_Gender = models.CharField(max_length=10, verbose_name="Пол родителя")
    Parent_Registration_Address = models.CharField(max_length=100, verbose_name="Адрес регистрации родителя")
    Parent_Residential_Address = models.CharField(max_length=100, verbose_name="Адрес фактического проживания родителя")



class Preschooler(models.Model):
    """Воспитанник"""

    class Meta:
        db_table = "Preschooler"
        verbose_name = "Воспитанник"
        verbose_name_plural = "Воспитанники"

    Preschooler_Code = models.AutoField(primary_key=True, verbose_name="Код воспитанника")
    Group_Code = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name="Код группы")
    Preschooler_Full_Name = models.CharField(max_length=100, verbose_name="ФИО воспитанника")
    Admission_Date = models.DateTimeField(verbose_name="Дата поступления")
    Departure_Date = models.DateTimeField(verbose_name="Дата выбытия")
    Preschooler_Status = models.CharField(max_length=20, verbose_name="Статус воспитанника")
    Birth_Certificate_Series = models.CharField(max_length=10, verbose_name="Серия свидетельства о рождении")
    Birth_Certificate_Number = models.CharField(max_length=10, verbose_name="Номер свидетельства о рождении")
    Date_Of_Birth = models.DateTimeField(verbose_name="Дата рождения")
    Preschooler_Gender = models.CharField(max_length=10, verbose_name="Пол воспитанника")
    Registered_Address = models.CharField(max_length=100, verbose_name="Адрес регистрации воспитанника")
    Residential_Address = models.CharField(max_length=100, verbose_name="Адрес фактического проживания воспитанника")



class EducationContract(models.Model):
    """Договор об обучении"""

    class Meta:
        db_table = "EducationContract"
        verbose_name = "Договор об обучении"
        verbose_name_plural = "Договора об обучении"

    Education_Contract_Code = models.AutoField(primary_key=True, verbose_name="Код договора об обучении")
    Request_Code = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name="Код заявки")
    Payment_Code = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name="Код платежа")
    Preschooler_Code = models.ForeignKey(Preschooler, on_delete=models.CASCADE, verbose_name="Код воспитанника")
    Parent_Code = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="Код родителя")
    Contract_Date = models.DateTimeField(verbose_name="Дата заключения договора")
    Contract_Place = models.CharField(max_length=50, verbose_name="Место заключения договора")
    Performer = models.CharField(max_length=100, verbose_name="Исполнитель")
    Contract_Status = models.CharField(max_length=20, verbose_name="Статус договора")



class Parents(models.Model):
    """Родители"""

    class Meta:
        db_table = "Parents"
        verbose_name = "Данные о родителях их их детях"
        verbose_name_plural = "Данные о родителях их их детях"

    Preschooler_Code = models.ForeignKey(Preschooler, on_delete=models.CASCADE, verbose_name="Код воспитанника")
    Parent_Code = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="Код родителя")
    Party_Name = models.CharField(max_length=100, verbose_name="Наименование стороны")



class MedicalRecord(models.Model):
    """Медицинская карта"""

    class Meta:
        db_table = "MedicalRecord"
        verbose_name = "Данные о медицинской карте"
        verbose_name_plural = "Данные о медицинских картах"
    
    Medical_Record_Code = models.AutoField(primary_key=True, verbose_name="Код медицинской карты")
    Preschooler_Code = models.ForeignKey(Preschooler, on_delete=models.CASCADE, verbose_name="Код воспитанника")
    Healthcare_Institution_Name = models.CharField(max_length=100, verbose_name="Наименование ЛПУ")
    Medical_Record_Creation_Date = models.DateTimeField(verbose_name="Дата заведения медицинской карты")
    Obligatory_Medical_Insurance_Number = models.CharField(max_length=20, verbose_name="Номер полиса ОМС")
    Medical_Record_Number = models.CharField(max_length=10, verbose_name="Номер медицинской карты")



class MedicalRecordEntry(models.Model):
    """Запись медицинской карты"""

    class Meta:
        db_table = "MedicalRecordEntry"
        verbose_name = "Запись медицинской карты"
        verbose_name_plural = "Записи медицинских карт"

    Medical_Record_Entry_Code = models.AutoField(primary_key=True, verbose_name="Код записи медицинской карты")
    Medical_Record_Code = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, verbose_name="Код медицинской карты")
    Preschooler_Code = models.ForeignKey(Preschooler, on_delete=models.CASCADE, verbose_name="Код воспитанника")
    Doctor_Full_Name = models.CharField(max_length=100, verbose_name="")
    Department = models.CharField(max_length=50, verbose_name="")
    Date = models.DateTimeField(verbose_name="")
    Entry_Type = models.CharField(max_length=50, verbose_name="")
    Diagnosis = models.CharField(max_length=100, verbose_name="")
    Treatment_Stage = models.CharField(max_length=50, verbose_name="")
    Note = models.CharField(max_length=100, verbose_name="")



class Group(models.Model):
    """Группа"""

    class Meta:
        db_table = "Group"
        verbose_name = "Данные о группах в ДОУ"
        verbose_name_plural = "Данные о группах в ДОУ"

    Group_Code = models.AutoField(primary_key=True, verbose_name="Код группы")
    Group_Name = models.CharField(max_length=50, verbose_name="Название группы")
    Group_Formation_Date = models.DateTimeField(verbose_name="Дата формирования группы")
    Number_Of_Preschoolers = models.IntegerField(verbose_name="Количество воспитанников")



class Attendance(models.Model):
    """Посещаемость"""

    class Meta:
        db_table = "Attendance"
        verbose_name = "Данные о посещаемости воспитанника в ДОУ"
        verbose_name_plural = "Данные о посещаемости воспитанников в ДОУ"

    Attendance_Code = models.AutoField(primary_key=True, verbose_name="Код посещения")
    Preschooler_Code = models.ForeignKey(Preschooler, on_delete=models.CASCADE, verbose_name="Код воспитанника")
    Lesson_Code = models.ForeignKey('Lesson', on_delete=models.CASCADE, verbose_name="Код занятия")
    Group_Code = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Код группы")
    Teacher_Code = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name="Код педагога")
    Presence = models.CharField(max_length=20, verbose_name="Присутствие")
    Note = models.CharField(max_length=50, verbose_name="Примечание")
    Date = models.DateTimeField(verbose_name="Дата")



class Lesson(models.Model):
    """Занятие"""

    class Meta:
        db_table = "Lesson"
        verbose_name = "Данные о занятии в ДОУ"
        verbose_name_plural = "Данные о занятиях в ДОУ"

    Lesson_Code = models.AutoField(primary_key=True, verbose_name="Код занятия")
    Group_Code = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Код группы")
    Teacher_Code = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name="Код педагога")
    Lesson_Start_Datetime = models.DateTimeField(verbose_name="Дата и время начала занятия")
    Lesson_End_Datetime = models.DateTimeField(verbose_name="Дата и время окончания занятия")
    Lesson_Title = models.CharField(max_length=50, verbose_name="Занятие")
    Room = models.IntegerField(verbose_name="Комната")



class Teacher(models.Model):
    """Педагог"""

    class Meta:
        db_table = "Teacher"
        verbose_name = "Данные о педагогах ДОУ"
        verbose_name_plural = "Данные о педагогах ДОУ"

    Teacher_Code = models.AutoField(primary_key=True, verbose_name="")
    Employee_Code = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name="")
    Teacher_Specialization = models.CharField(max_length=50, verbose_name="")



class Employee(models.Model):
    """Сотрудника"""

    class Meta:
        db_table = "Employee"
        verbose_name = "Данные о сотрудниках ДОУ"
        verbose_name_plural = "Данные о сотрудниках ДОУ"
    
    Employee_Code = models.AutoField(primary_key=True, verbose_name="Код сотрудника")
    Employee_Full_Name = models.CharField(max_length=100, verbose_name="ФИО сотрудника")
    Employee_Date_Of_Birth = models.DateTimeField(verbose_name="Дата рождения сотрудника")
    Department = models.CharField(max_length=50, verbose_name="Отдел")
    Employee_Position = models.CharField(max_length=50, verbose_name="Должность сотрудника")
    Employee_Passport_Series = models.CharField(max_length=10, verbose_name="Серия паспорта сотрудника")
    Employee_Passport_Number = models.CharField(max_length=10, verbose_name="Номер паспорта сотрудника")
    Employee_TIN = models.CharField(max_length=20, verbose_name="ИНН сотрудника")
    Employee_PIPN = models.CharField(max_length=20, verbose_name="СНИЛС сотрудника")
    Employee_Email = models.CharField(max_length=100, verbose_name="Электронная почта сотрудника")
    Employee_Account_Number = models.CharField(max_length=20, verbose_name="Номер счета сотрудника")
    Employee_Bank_Details = models.CharField(max_length=100, verbose_name="Реквизиты банка сотрудника")
    Employee_Registration_Address = models.CharField(max_length=100, verbose_name="Адрес регистрации сотрудника")
    Employee_Residential_Address = models.CharField(max_length=100, verbose_name="Адрес фактического проживания сотрудника")
    Employee_Salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Зарплата сотрудника")



class EducationDocument(models.Model):
    """Документ об образовании"""

    class Meta:
        db_table = "EducationDocument"
        verbose_name = "Данные о документе об образовании сотрудни-ка"
        verbose_name_plural = "Данные о документе об образовании сотрудни-ка"

    Education_Document_Code = models.AutoField(primary_key=True, verbose_name="Код договора об обучении")
    Employee_Code = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Код сотрудника")
    Document_Type = models.CharField(max_length=50, verbose_name="Тип документа")
    Educational_Institution_Name = models.CharField(max_length=100, verbose_name="Наименование образовательного учреждения")
    Issue_Date = models.DateTimeField(verbose_name="Дата выдачи")
    Degree = models.CharField(max_length=100, verbose_name="Специальность")
    Qualification = models.CharField(max_length=100, verbose_name="Квалификация")
    Education_Document_Series = models.CharField(max_length=10, verbose_name="Серия документа об образовании")
    Education_Document_Number = models.CharField(max_length=10, verbose_name="Номер документа об образовании")
    Registration_Number = models.CharField(max_length=10, verbose_name="Регистрационный номер")



class PersonalMedicalBook(models.Model):
    """Личная медицинская книжка"""

    class Meta:
        db_table = "PersonalMedicalBook"
        verbose_name = "Данные о медицинской книжке сотрудника"
        verbose_name_plural = "Данные о медицинской книжке сотрудника"

    Medical_Book_Code = models.AutoField(primary_key=True, verbose_name="Код медицинской книжки")
    Employee_Code = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Код сотрудника")
    Medical_Book_Number = models.CharField(max_length=10, verbose_name="Номер медицинской книжки")
    Issuing_Place = models.CharField(max_length=100, verbose_name="Место выдачи")
    Issue_Date = models.DateTimeField(verbose_name="Дата выдачи")