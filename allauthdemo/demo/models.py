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


class Transcript(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='transcript')
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


class Certificate(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='certificate')
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

class CashMemo(models.Model):
    G_CHOICES = (('1','Male'),('2','Female'))
    
    user = models.ForeignKey('allauthdemo_auth.DemoUser',related_name='cash_memo')
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