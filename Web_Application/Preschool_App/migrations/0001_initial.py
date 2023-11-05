# Generated by Django 4.2.6 on 2023-11-04 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код сотрудника')),
                ('Employee_Full_Name', models.CharField(max_length=100, verbose_name='ФИО сотрудника')),
                ('Employee_Date_Of_Birth', models.DateTimeField(verbose_name='Дата рождения сотрудника')),
                ('Department', models.CharField(max_length=50, verbose_name='Отдел')),
                ('Employee_Position', models.CharField(max_length=50, verbose_name='Должность сотрудника')),
                ('Employee_Passport_Series', models.CharField(max_length=10, verbose_name='Серия паспорта сотрудника')),
                ('Employee_Passport_Number', models.CharField(max_length=10, verbose_name='Номер паспорта сотрудника')),
                ('Employee_TIN', models.CharField(max_length=20, verbose_name='ИНН сотрудника')),
                ('Employee_PIPN', models.CharField(max_length=20, verbose_name='СНИЛС сотрудника')),
                ('Employee_Email', models.CharField(max_length=100, verbose_name='Электронная почта сотрудника')),
                ('Employee_Account_Number', models.CharField(max_length=20, verbose_name='Номер счета сотрудника')),
                ('Employee_Bank_Details', models.CharField(max_length=100, verbose_name='Реквизиты банка сотрудника')),
                ('Employee_Registration_Address', models.CharField(max_length=100, verbose_name='Адрес регистрации сотрудника')),
                ('Employee_Residential_Address', models.CharField(max_length=100, verbose_name='Адрес фактического проживания сотрудника')),
                ('Employee_Salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Зарплата сотрудника')),
            ],
            options={
                'verbose_name': 'Данные о сотрудниках ДОУ',
                'verbose_name_plural': 'Данные о сотрудниках ДОУ',
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('Group_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код группы')),
                ('Group_Name', models.CharField(max_length=50, verbose_name='Название группы')),
                ('Group_Formation_Date', models.DateTimeField(verbose_name='Дата формирования группы')),
                ('Number_Of_Preschoolers', models.IntegerField(verbose_name='Количество воспитанников')),
            ],
            options={
                'verbose_name': 'Данные о группах в ДОУ',
                'verbose_name_plural': 'Данные о группах в ДОУ',
                'db_table': 'Group',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('Medical_Record_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код медицинской карты')),
                ('Healthcare_Institution_Name', models.CharField(max_length=100, verbose_name='Наименование ЛПУ')),
                ('Medical_Record_Creation_Date', models.DateTimeField(verbose_name='Дата заведения медицинской карты')),
                ('Obligatory_Medical_Insurance_Number', models.CharField(max_length=20, verbose_name='Номер полиса ОМС')),
                ('Medical_Record_Number', models.CharField(max_length=10, verbose_name='Номер медицинской карты')),
            ],
            options={
                'verbose_name': 'Данные о медицинской карте',
                'verbose_name_plural': 'Данные о медицинских картах',
                'db_table': 'MedicalRecord',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('Parent_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код родителя')),
                ('Parent_Full_Name', models.CharField(max_length=100, verbose_name='ФИО родителя')),
                ('Parent_Phone_Number', models.CharField(max_length=20, verbose_name='Телефон родителя')),
                ('Relationship_Degree', models.CharField(max_length=50, verbose_name='Степень родства')),
                ('Parent_Passport_Series', models.CharField(max_length=10, verbose_name='Серия паспорта родителя')),
                ('Parent_Passport_Number', models.CharField(max_length=10, verbose_name='Номер паспорта родителя')),
                ('Parent_Email', models.CharField(max_length=100, verbose_name='Электронная почта родителя')),
                ('Parent_Gender', models.CharField(max_length=10, verbose_name='Пол родителя')),
                ('Parent_Registration_Address', models.CharField(max_length=100, verbose_name='Адрес регистрации родителя')),
                ('Parent_Residential_Address', models.CharField(max_length=100, verbose_name='Адрес фактического проживания родителя')),
            ],
            options={
                'verbose_name': 'Данные о родителе',
                'verbose_name_plural': 'Данные о родителях',
                'db_table': 'Parent',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('Payment_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код платежа')),
                ('Payer', models.CharField(max_length=100, verbose_name='Плательщик')),
                ('Payer_TIN', models.CharField(max_length=20, verbose_name='ИНН плательщика')),
                ('Payer_Bank', models.CharField(max_length=50, verbose_name='Банка плательщика')),
                ('Payee', models.CharField(max_length=100, verbose_name='Получатель')),
                ('Payee_TIN', models.CharField(max_length=20, verbose_name='ИНН получателя')),
                ('Payee_RRC', models.CharField(max_length=20, verbose_name='КПП получателя')),
                ('Payee_Bank', models.CharField(max_length=50, verbose_name='Банк получателя')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('Payment_Purpose', models.CharField(max_length=100, verbose_name='Назначение платежа')),
                ('Account_Number', models.CharField(max_length=20, verbose_name='Номер счета')),
            ],
            options={
                'verbose_name': 'Информация о платежах',
                'verbose_name_plural': 'Информация о платежах',
                'db_table': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('Request_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код заявки')),
                ('Request_Name', models.IntegerField(verbose_name='Наименование заявки')),
                ('Request_Date_Submitted', models.DateTimeField(verbose_name='Дата поступления заявки')),
                ('Request_Status', models.CharField(max_length=20, verbose_name='Статус заявки')),
            ],
            options={
                'verbose_name': 'Информация о заявках на обучение',
                'verbose_name_plural': 'Информация о заявках на обучение',
                'db_table': 'Request',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('Teacher_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='')),
                ('Teacher_Specialization', models.CharField(max_length=50, verbose_name='')),
                ('Employee_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.employee', verbose_name='')),
            ],
            options={
                'verbose_name': 'Данные о педагогах ДОУ',
                'verbose_name_plural': 'Данные о педагогах ДОУ',
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Preschooler',
            fields=[
                ('Preschooler_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код воспитанника')),
                ('Preschooler_Full_Name', models.CharField(max_length=100, verbose_name='ФИО воспитанника')),
                ('Admission_Date', models.DateTimeField(verbose_name='Дата поступления')),
                ('Departure_Date', models.DateTimeField(verbose_name='Дата выбытия')),
                ('Preschooler_Status', models.CharField(max_length=20, verbose_name='Статус воспитанника')),
                ('Birth_Certificate_Series', models.CharField(max_length=10, verbose_name='Серия свидетельства о рождении')),
                ('Birth_Certificate_Number', models.CharField(max_length=10, verbose_name='Номер свидетельства о рождении')),
                ('Date_Of_Birth', models.DateTimeField(verbose_name='Дата рождения')),
                ('Preschooler_Gender', models.CharField(max_length=10, verbose_name='Пол воспитанника')),
                ('Registered_Address', models.CharField(max_length=100, verbose_name='Адрес регистрации воспитанника')),
                ('Residential_Address', models.CharField(max_length=100, verbose_name='Адрес фактического проживания воспитанника')),
                ('Group_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.group', verbose_name='Код группы')),
            ],
            options={
                'verbose_name': 'Воспитанник',
                'verbose_name_plural': 'Воспитанники',
                'db_table': 'Preschooler',
            },
        ),
        migrations.CreateModel(
            name='PersonalMedicalBook',
            fields=[
                ('Medical_Book_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код медицинской книжки')),
                ('Medical_Book_Number', models.CharField(max_length=10, verbose_name='Номер медицинской книжки')),
                ('Issuing_Place', models.CharField(max_length=100, verbose_name='Место выдачи')),
                ('Issue_Date', models.DateTimeField(verbose_name='Дата выдачи')),
                ('Employee_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.employee', verbose_name='Код сотрудника')),
            ],
            options={
                'verbose_name': 'Данные о медицинской книжке сотрудника',
                'verbose_name_plural': 'Данные о медицинской книжке сотрудника',
                'db_table': 'PersonalMedicalBook',
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Party_Name', models.CharField(max_length=100, verbose_name='Наименование стороны')),
                ('Parent_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.parent', verbose_name='Код родителя')),
                ('Preschooler_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.preschooler', verbose_name='Код воспитанника')),
            ],
            options={
                'verbose_name': 'Данные о родителях их их детях',
                'verbose_name_plural': 'Данные о родителях их их детях',
                'db_table': 'Parents',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecordEntry',
            fields=[
                ('Medical_Record_Entry_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код записи медицинской карты')),
                ('Doctor_Full_Name', models.CharField(max_length=100, verbose_name='')),
                ('Department', models.CharField(max_length=50, verbose_name='')),
                ('Date', models.DateTimeField(verbose_name='')),
                ('Entry_Type', models.CharField(max_length=50, verbose_name='')),
                ('Diagnosis', models.CharField(max_length=100, verbose_name='')),
                ('Treatment_Stage', models.CharField(max_length=50, verbose_name='')),
                ('Note', models.CharField(max_length=100, verbose_name='')),
                ('Medical_Record_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.medicalrecord', verbose_name='Код медицинской карты')),
                ('Preschooler_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.preschooler', verbose_name='Код воспитанника')),
            ],
            options={
                'verbose_name': 'Запись медицинской карты',
                'verbose_name_plural': 'Записи медицинских карт',
                'db_table': 'MedicalRecordEntry',
            },
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='Preschooler_Code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.preschooler', verbose_name='Код воспитанника'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('Lesson_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код занятия')),
                ('Lesson_Start_Datetime', models.DateTimeField(verbose_name='Дата и время начала занятия')),
                ('Lesson_End_Datetime', models.DateTimeField(verbose_name='Дата и время окончания занятия')),
                ('Lesson_Title', models.CharField(max_length=50, verbose_name='Занятие')),
                ('Room', models.IntegerField(verbose_name='Комната')),
                ('Group_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.group', verbose_name='Код группы')),
                ('Teacher_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.teacher', verbose_name='Код педагога')),
            ],
            options={
                'verbose_name': 'Данные о занятии в ДОУ',
                'verbose_name_plural': 'Данные о занятиях в ДОУ',
                'db_table': 'Lesson',
            },
        ),
        migrations.CreateModel(
            name='EducationDocument',
            fields=[
                ('Education_Document_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код договора об обучении')),
                ('Document_Type', models.CharField(max_length=50, verbose_name='Тип документа')),
                ('Educational_Institution_Name', models.CharField(max_length=100, verbose_name='Наименование образовательного учреждения')),
                ('Issue_Date', models.DateTimeField(verbose_name='Дата выдачи')),
                ('Degree', models.CharField(max_length=100, verbose_name='Специальность')),
                ('Qualification', models.CharField(max_length=100, verbose_name='Квалификация')),
                ('Education_Document_Series', models.CharField(max_length=10, verbose_name='Серия документа об образовании')),
                ('Education_Document_Number', models.CharField(max_length=10, verbose_name='Номер документа об образовании')),
                ('Registration_Number', models.CharField(max_length=10, verbose_name='Регистрационный номер')),
                ('Employee_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.employee', verbose_name='Код сотрудника')),
            ],
            options={
                'verbose_name': 'Данные о документе об образовании сотрудни-ка',
                'verbose_name_plural': 'Данные о документе об образовании сотрудни-ка',
                'db_table': 'EducationDocument',
            },
        ),
        migrations.CreateModel(
            name='EducationContract',
            fields=[
                ('Education_Contract_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код договора об обучении')),
                ('Contract_Date', models.DateTimeField(verbose_name='Дата заключения договора')),
                ('Contract_Place', models.CharField(max_length=50, verbose_name='Место заключения договора')),
                ('Performer', models.CharField(max_length=100, verbose_name='Исполнитель')),
                ('Contract_Status', models.CharField(max_length=20, verbose_name='Статус договора')),
                ('Parent_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.parent', verbose_name='Код родителя')),
                ('Payment_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.payment', verbose_name='Код платежа')),
                ('Preschooler_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.preschooler', verbose_name='Код воспитанника')),
                ('Request_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.request', verbose_name='Код заявки')),
            ],
            options={
                'verbose_name': 'Договор об обучении',
                'verbose_name_plural': 'Договора об обучении',
                'db_table': 'EducationContract',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('Attendance_Code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код посещения')),
                ('Presence', models.CharField(max_length=20, verbose_name='Присутствие')),
                ('Note', models.CharField(max_length=50, verbose_name='Примечание')),
                ('Date', models.DateTimeField(verbose_name='Дата')),
                ('Group_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.group', verbose_name='Код группы')),
                ('Lesson_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.lesson', verbose_name='Код занятия')),
                ('Preschooler_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.preschooler', verbose_name='Код воспитанника')),
                ('Teacher_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preschool_App.teacher', verbose_name='Код педагога')),
            ],
            options={
                'verbose_name': 'Данные о посещаемости воспитанника в ДОУ',
                'verbose_name_plural': 'Данные о посещаемости воспитанников в ДОУ',
                'db_table': 'Attendance',
            },
        ),
    ]