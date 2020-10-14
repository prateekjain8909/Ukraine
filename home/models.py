from django.db import models

# Create your models here.
class Callback(models.Model):
    name=models.CharField(max_length=40, default="")
    # lastname=models.CharField(max_length=20)
    phone=models.CharField(max_length=13)
    # email = models.EmailField(max_length=30)
    time = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name
            
class Visitor(models.Model):
    date = models.DateField(auto_now=True)
    count = models.IntegerField()

    def __str__(self):
        return self.date.strftime("%d %b")

class Ip(models.Model):
    ip = models.CharField(max_length=30)

    def __str__(self):
        return self.ip

class College_predictor(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name


class Mopup(models.Model):
    college = models.CharField(db_column='COLLEGE',max_length=100, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION',max_length=25, blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE',max_length=25, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='COURSE',max_length=10, blank=True, null=True)  # Field name made lowercase.
    quota = models.CharField(db_column='QUOTA',max_length=10, blank=True, null=True)  # Field name made lowercase.
    gn_or = models.IntegerField(db_column='GN_OR', blank=True, null=True)  # Field name made lowercase.
    gn_cr = models.IntegerField(db_column='GN_CR', blank=True, null=True)  # Field name made lowercase.
    gn_seats = models.IntegerField(db_column='GN_SEATS', blank=True, null=True)  # Field name made lowercase.
    obc_or = models.IntegerField(db_column='OBC_OR', blank=True, null=True)  # Field name made lowercase.
    obc_cr = models.IntegerField(db_column='OBC_CR', blank=True, null=True)  # Field name made lowercase.
    obc_seats = models.IntegerField(db_column='OBC_SEATS', blank=True, null=True)  # Field name made lowercase.
    ew_or = models.IntegerField(db_column='EW_OR', blank=True, null=True)  # Field name made lowercase.
    ew_cr = models.IntegerField(db_column='EW_CR', blank=True, null=True)  # Field name made lowercase.
    ew_seats = models.IntegerField(db_column='EW_SEATS', blank=True, null=True)  # Field name made lowercase.
    sc_or = models.IntegerField(db_column='SC_OR', blank=True, null=True)  # Field name made lowercase.
    sc_cr = models.IntegerField(db_column='SC_CR', blank=True, null=True)  # Field name made lowercase.
    sc_seats = models.IntegerField(db_column='SC_SEATS', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_or = models.IntegerField(db_column='GN_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_cr = models.IntegerField(db_column='GN_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_seats = models.IntegerField(db_column='GN_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    st_or = models.IntegerField(db_column='ST_OR', blank=True, null=True)  # Field name made lowercase.
    st_cr = models.IntegerField(db_column='ST_CR', blank=True, null=True)  # Field name made lowercase.
    st_seats = models.IntegerField(db_column='ST_SEATS', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_or = models.IntegerField(db_column='OBC_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_cr = models.IntegerField(db_column='OBC_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_seats = models.IntegerField(db_column='OBC_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    # class Meta:
    #     managed = False
    #     db_table = 'MOPUP'

    def fill(self, college):        
        self.college = college[0]
        self.region = college[1]
        self.state = college[2]
        self.course = college[3]
        self.quota = college[4]
        self.gn_or = college[5]
        self.gn_cr = college[6]
        self.gn_seats = college[7]
        self.obc_or = college[8]
        self.obc_cr = college[9]
        self.obc_seats = college[10]
        self.ew_or = college[11]
        self.ew_cr= college[12]
        self.ew_seats = college[13]
        self.sc_or = college[14]
        self.sc_cr = college[15]
        self.sc_seats = college[16]
        self.gn_pwd_or = college[17]
        self.gn_pwd_cr = college[18]
        self.gn_pwd_seats = college[19]
        self.st_or = college[20]
        self.st_cr = college[21]
        self.st_seats = college[22]
        self.obc_pwd_or = college[23]
        self.obc_pwd_cr = college[24]
        self.obc_pwd_seats = college[25]
    
    def __str__(self):
        return self.college


class Round1(models.Model):
    college = models.CharField(db_column='COLLEGE',max_length=100, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION',max_length=25, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE',max_length=25, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='COURSE',max_length=10, blank=True, null=True)  # Field name made lowercase.
    quota = models.CharField(db_column='QUOTA',max_length=10, blank=True, null=True)  # Field name made lowercase.
    gn_or = models.IntegerField(db_column='GN_OR', blank=True, null=True)  # Field name made lowercase.
    gn_cr = models.IntegerField(db_column='GN_CR', blank=True, null=True)  # Field name made lowercase.
    gn_seats = models.IntegerField(db_column='GN_SEATS', blank=True, null=True)  # Field name made lowercase.
    obc_or = models.IntegerField(db_column='OBC_OR', blank=True, null=True)  # Field name made lowercase.
    obc_cr = models.IntegerField(db_column='OBC_CR', blank=True, null=True)  # Field name made lowercase.
    obc_seats = models.IntegerField(db_column='OBC_SEATS', blank=True, null=True)  # Field name made lowercase.
    sc_or = models.IntegerField(db_column='SC_OR', blank=True, null=True)  # Field name made lowercase.
    sc_cr = models.IntegerField(db_column='SC_CR', blank=True, null=True)  # Field name made lowercase.
    sc_seats = models.IntegerField(db_column='SC_SEATS', blank=True, null=True)  # Field name made lowercase.
    st_or = models.IntegerField(db_column='ST_OR', blank=True, null=True)  # Field name made lowercase.
    st_cr = models.IntegerField(db_column='ST_CR', blank=True, null=True)  # Field name made lowercase.
    st_seats = models.IntegerField(db_column='ST_SEATS', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_or = models.IntegerField(db_column='GN_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_cr = models.IntegerField(db_column='GN_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_seats = models.IntegerField(db_column='GN_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_or = models.IntegerField(db_column='OBC_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_cr = models.IntegerField(db_column='OBC_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_seats = models.IntegerField(db_column='OBC_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    sc_pwd_or = models.IntegerField(db_column='SC_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    sc_pwd_cr = models.IntegerField(db_column='SC_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    sc_pwd_seats = models.IntegerField(db_column='SC_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    st_pwd_or = models.IntegerField(db_column='ST_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    st_pwd_cr = models.IntegerField(db_column='ST_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    st_pwd_seats = models.IntegerField(db_column='ST_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    # class Meta:
        # managed = False
        # db_table = 'ROUND1'
        
    def fill(self, college):        
        self.college = college[0]
        self.region = college[1]
        self.state = college[2]
        self.course = college[3]
        self.quota = college[4]
        self.gn_or = college[5]
        self.gn_cr = college[6]
        self.gn_seats = college[7]
        self.obc_or = college[8]
        self.obc_cr = college[9]
        self.obc_seats = college[10]
        self.sc_or = college[11]
        self.sc_cr = college[12]
        self.sc_seats = college[13]
        self.st_or = college[14]
        self.st_cr = college[15]
        self.st_seats = college[16]
        self.gn_pwd_or = college[17]
        self.gn_pwd_cr = college[18]
        self.gn_pwd_seats = college[19]
        self.obc_pwd_or = college[20]
        self.obc_pwd_cr = college[21]
        self.obc_pwd_seats = college[22]
        self.sc_pwd_or = college[23]
        self.sc_pwd_cr = college[24]
        self.sc_pwd_seats = college[25]
        self.st_pwd_or = college[26]
        self.st_pwd_cr = college[27]
        self.st_pwd_seats = college[28]
    
    def __str__(self):
        return self.college


class Round2(models.Model):
    college = models.CharField(db_column='COLLEGE',max_length=100, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION',max_length=25, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE',max_length=25, blank=True, null=True)  # Field name made lowercase.
    course = models.CharField(db_column='COURSE',max_length=10, blank=True, null=True)  # Field name made lowercase.
    quota = models.CharField(db_column='QUOTA',max_length=10, blank=True, null=True)  # Field name made lowercase.
    gn_or = models.IntegerField(db_column='GN_OR', blank=True, null=True)  # Field name made lowercase.
    gn_cr = models.IntegerField(db_column='GN_CR', blank=True, null=True)  # Field name made lowercase.
    gn_seats = models.IntegerField(db_column='GN_SEATS', blank=True, null=True)  # Field name made lowercase.
    obc_or = models.IntegerField(db_column='OBC_OR', blank=True, null=True)  # Field name made lowercase.
    obc_cr = models.IntegerField(db_column='OBC_CR', blank=True, null=True)  # Field name made lowercase.
    obc_seats = models.IntegerField(db_column='OBC_SEATS', blank=True, null=True)  # Field name made lowercase.
    sc_or = models.IntegerField(db_column='SC_OR', blank=True, null=True)  # Field name made lowercase.
    sc_cr = models.IntegerField(db_column='SC_CR', blank=True, null=True)  # Field name made lowercase.
    sc_seats = models.IntegerField(db_column='SC_SEATS', blank=True, null=True)  # Field name made lowercase.
    st_or = models.IntegerField(db_column='ST_OR', blank=True, null=True)  # Field name made lowercase.
    st_cr = models.IntegerField(db_column='ST_CR', blank=True, null=True)  # Field name made lowercase.
    st_seats = models.IntegerField(db_column='ST_SEATS', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_or = models.IntegerField(db_column='GN_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_cr = models.IntegerField(db_column='GN_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    gn_pwd_seats = models.IntegerField(db_column='GN_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_or = models.IntegerField(db_column='OBC_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_cr = models.IntegerField(db_column='OBC_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    obc_pwd_seats = models.IntegerField(db_column='OBC_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    sc_pwd_or = models.IntegerField(db_column='SC_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    sc_pwd_cr = models.IntegerField(db_column='SC_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    sc_pwd_seats = models.IntegerField(db_column='SC_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    st_pwd_or = models.IntegerField(db_column='ST_PwD_OR', blank=True, null=True)  # Field name made lowercase.
    st_pwd_cr = models.IntegerField(db_column='ST_PwD_CR', blank=True, null=True)  # Field name made lowercase.
    st_pwd_seats = models.IntegerField(db_column='ST_PwD_SEATS', blank=True, null=True)  # Field name made lowercase.
    ew_or = models.IntegerField(db_column='EW_OR', blank=True, null=True)  # Field name made lowercase.
    ew_cr = models.IntegerField(db_column='EW_CR', blank=True, null=True)  # Field name made lowercase.
    ew_seats = models.IntegerField(db_column='EW_SEATS', blank=True, null=True)  # Field name made lowercase.
    # class Meta:
        # managed = False
        # db_table = 'ROUND2'
    # def fill(self,college):

    def fill(self, college):        
        self.college = college[0]
        self.region = college[1]
        self.state = college[2]
        self.course = college[3]
        self.quota = college[4]
        self.gn_or = college[5]
        self.gn_cr = college[6]
        self.gn_seats = college[7]
        self.obc_or = college[8]
        self.obc_cr = college[9]
        self.obc_seats = college[10]
        self.sc_or = college[11]
        self.sc_cr = college[12]
        self.sc_seats = college[13]
        self.st_or = college[14]
        self.st_cr = college[15]
        self.st_seats = college[16]
        self.gn_pwd_or = college[17]
        self.gn_pwd_cr = college[18]
        self.gn_pwd_seats = college[19]
        self.obc_pwd_or = college[20]
        self.obc_pwd_cr = college[21]
        self.obc_pwd_seats = college[22]
        self.sc_pwd_or = college[23]
        self.sc_pwd_cr = college[24]
        self.sc_pwd_seats = college[25]
        self.st_pwd_or = college[26]
        self.st_pwd_cr = college[27]
        self.st_pwd_seats = college[28]
        self.ew_or = college[29]
        self.ew_cr = college[30]
        self.ew_seats = college[31]
    def __str__(self):
        return self.college

