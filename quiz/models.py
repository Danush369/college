from django.db import models

class qanda(models.Model):
    qus=models.CharField(max_length=30)
    op1=models.CharField(max_length=30)
    op2=models.CharField(max_length=30)
    op3=models.CharField(max_length=30)
    op4=models.CharField(max_length=30)
    ans=models.CharField(max_length=30)
    class Meta:                                   #inner class(default) used to give table name
        db_table="Questions"

class participantDetails(models.Model):
    name=models.CharField(max_length=50)
    school=models.CharField(max_length=50)
    class Meta:
        db_table="studentsList"

class response(models.Model):
    name=models.CharField(max_length=50)
    school=models.CharField(max_length=50)
    op1=models.IntegerField()
    op2=models.IntegerField()
    op3=models.IntegerField()
    op4=models.IntegerField()
    op5=models.IntegerField()
    op6=models.IntegerField()
    op7=models.IntegerField()
    op8=models.IntegerField()
    op9=models.IntegerField()
    op10=models.IntegerField()
    op11=models.IntegerField()
    op12=models.IntegerField()
    op13=models.IntegerField()
    op14=models.IntegerField()
    op15=models.IntegerField()
    op16=models.IntegerField()
    op17=models.IntegerField()
    op18=models.IntegerField()
    op19=models.IntegerField()
    op20=models.IntegerField()
    op21=models.IntegerField()
    op22=models.IntegerField()
    op23=models.IntegerField()
    op24=models.IntegerField()
    op25=models.IntegerField()
    op26=models.IntegerField()
    op27=models.IntegerField()
    op28=models.IntegerField()
    op29=models.IntegerField()
    op30=models.IntegerField()
    total=models.IntegerField()
    class Meta:
        db_table="studResponses"
