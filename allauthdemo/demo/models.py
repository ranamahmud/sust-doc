from django.db import models
from django.utils import timezone


class LibraryFine(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='library_fines')
    date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1,choices = G_CHOICES,default=1)
    book_count = models.IntegerField(default=1)
    amount_fined = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class ShahparanHall(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='shahparan_hall_fine')
    date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1,choices = G_CHOICES,default=1)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    father_name = models.CharField(max_length = 50,default="")
    mother_name = models.CharField(max_length = 50,default="")
    villagep = models.CharField(max_length = 50,default="")
    postp = models.CharField(max_length = 50,default="")
    thanap = models.CharField(max_length = 50,default="")
    zillp = models.CharField(max_length = 50,default="")
    villagec = models.CharField(max_length = 50,default="")
    postc = models.CharField(max_length = 50,default="")
    thanc = models.CharField(max_length = 50,default="")
    zillc = models.CharField(max_length = 50,default="")
    hons_first = models.CharField(max_length = 50,default="")
    firstst_cgpa = models.IntegerField(default=0)
    first_credit = models.IntegerField(default=0)
    second_cgpa = models.IntegerField(default=0)
    second_credit = models.IntegerField(default=0)
    third_cgpa = models.IntegerField(default=0)
    third_credit = models.IntegerField(default=0)
    fourth_cgpa = models.IntegerField(default=0)
    fourth_credit = models.IntegerField(default=0)
    
    bank_money =  models.DecimalField(max_digits = 10, decimal_places=2,blank=True, null=True)
    bank_no = models.IntegerField(default=0)


    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Transcript(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='transcript')
    date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1,choices = G_CHOICES,default=1)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    honors_reg = models.IntegerField(default=0)
    ms_reg = models.IntegerField(default=0)
    discipline = models.CharField(max_length = 100, default = "")
    exam_name_date = models.CharField(max_length = 100,default="")
    address = models.CharField(max_length = 200, default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Gradesheet(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='gradesheet')
    date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1,choices = G_CHOICES,default=1)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    honors_reg = models.IntegerField(default=0)
    discipline = models.CharField(max_length = 100, default = "")
    school = models.CharField(max_length = 100, default = "")
    exam_name_date = models.CharField(max_length = 100,default="")
    cgpa = models.DecimalField(max_digits = 2, decimal_places=2,default=0)
    letter = models.CharField(max_length=2,default="")
    address = models.CharField(max_length = 200, default="")
    nationlaity = models.CharField(max_length = 30,default="Bangladeshi")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class CashMemo(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='cash_memo')
    date = models.DateTimeField(default=timezone.now)
    #Memo Fields
    account_no = models.IntegerField(default=0)
    branch = models.CharField(max_length = 30,default="")
    name = models.CharField(max_length = 30,default="")
    money1 =  models.DecimalField(max_digits = 10, decimal_places=2,blank=True, null=True)
    moeny2 =  models.DecimalField(max_digits = 10, decimal_places=2,blank=True, null=True)
    money3 =  models.DecimalField(max_digits = 10, decimal_places=2,blank=True, null=True)
    total =  models.DecimalField(max_digits = 15, decimal_places=2,blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class S2(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='s_2')
    date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1,choices = G_CHOICES,default=1)
    #S2 Fields
    admission_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    tution_fee  = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    union_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    reg_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    welfare_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    library_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    computer_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    rover_scout = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    bncc = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    travel = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    hall_seet = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    other = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    meical_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    id_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    book_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    festival_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    syllabus_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    diary_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    marksheet_fee = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    fine = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra1 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra2 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra3 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra4 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra5 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)

    total = models.DecimalField(max_digits = 10, decimal_places=2,blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class STD6(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='std_6')
    date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=1,choices = G_CHOICES,default=1)
    #STD-6 Fields
    total_theory = models.IntegerField( blank=True,null=True)
    total_lab = models.IntegerField(blank=True,null=True)
    exam_theory = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    exam_lab = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    drop_theory = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    drop_lab = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    certiricate = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    duplicate = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    registration_late = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    non_colligiate = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    course_modificatoin = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    other = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra1 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra2 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra3 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra4 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)
    extra5 = models.DecimalField(max_digits = 5, decimal_places=2,blank=True, null=True)

    total = models.DecimalField(max_digits = 10, decimal_places=2,blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title