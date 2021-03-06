from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel
from django.contrib.postgres.fields import ArrayField
from jsonfield import JSONField


#class Category(SoftDeletableModel, TimeStampedModel):
#    category_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline(SoftDeletableModel, TimeStampedModel):
#    pipeline_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

class Stage(models.Model):
    stage_id = models.PositiveIntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#User Model 
#class UserModel(models.Model):
#    usermodel_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


class Project(SoftDeletableModel, TimeStampedModel):
    project_id = models.IntegerField()
    name = models.CharField(max_length=250)
    starteddate = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    project_status = models.CharField(max_length=250)
   # user_responsible = models.ForeignKey(UserModel, to_field='usermodel_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stage, to_field='stage_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #category = models.ForeignKey(
    #    Category, on_delete=models.SET_NULL, null=True)
    woi = models.BooleanField(null=True, default=list)
    projprofilefilter = models.BooleanField(null=True, default=list)
    proname = models.BooleanField(null=True, default=list)
    allprojectcustomfieldsOOI = JSONField()
    dateprojcounter = models.IntegerField(null=False, default=0)
    hitlist = models.BooleanField(null=True, default=list)
    projintakes = models.BooleanField(null=True, default=list)
    projectstatuscancelled = models.BooleanField(null=True, default=list)
    projectstatuscompleted = models.BooleanField(null=True, default=list)
    projectstatusinprogress = models.BooleanField(null=True, default=list)
    startDays = models.IntegerField(null=False, default=0) 
    billabledmtproject0001setupclienttasksdays = models.IntegerField(null=False, default=0)
    billabledmtproject0002createideasforclientdays = models.IntegerField(null=False, default=0)
    billabledmtproject0003inputprepbillableinputprepdays = models.IntegerField(null=False, default=0)
    billabledmtproject00031qawiththeclientdays = models.IntegerField(null=False, default=0)
    billabledmtproject1streviewdays = models.IntegerField(null=False, default=0)
    billabledmtprojectclrrvwptsdays = models.IntegerField(null=False, default=0)
    billabledmtproject0004finalreviewdays = models.IntegerField(null=False, default=0)
    billabledmtproject0005assemblectcplandays = models.IntegerField(null=False, default=0)
    billabledmtproject0006adminwrapupdays = models.IntegerField(null=False, default=0)
    enddays = models.IntegerField(null=False, default=0)  
    startP4 = models.IntegerField(null=False, default=0)
    billabledmtproject0001setupclienttasksP4 = models.IntegerField(null=False, default=0)
    billabledmtproject0002createideasforclientP4 = models.IntegerField(null=False, default=0)
    billabledmtproject0003inputprepbillableinputprepP4 = models.IntegerField(null=False, default=0)    
    billabledmtproject00031qawiththeclientP4 = models.IntegerField(null=False, default=0) 
    billabledmtproject1streviewP4 = models.IntegerField(null=False, default=0)    
    billablectcstcproject0006reviewprojectP4 = models.IntegerField(null=False, default=0)
    billablectcstcproject0007clrrwptsP4 = models.IntegerField(null=False, default=0)
    billabledmtprojectclrrvwptsP4 = models.IntegerField(null=False, default=0)    
    billabledmtproject0004finalreviewP4 = models.IntegerField(null=False, default=0)  
    billabledmtproject0005assemblectcplanP4 = models.IntegerField(null=False, default=0)
    billabledmtproject0006adminwrapupP4 = models.IntegerField(null=False, default=0)
    billabledmtprojectendP4 = models.IntegerField(null=False, default=0)
    endP4 = models.IntegerField(null=False, default=0)
    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
    TotalDaysPerStage = models.IntegerField(null=False, default=0)
    TurnAroundTime  = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

#class Category13WCF(SoftDeletableModel, TimeStampedModel):
#    category13wcf_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline13WCF(SoftDeletableModel, TimeStampedModel):
#    pipeline13wcf_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage13WCF(models.Model):
#    stage13wcf_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel13WCF(models.Model):
#    usermodel13wcf_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name
    
#class Project13WCF(SoftDeletableModel, TimeStampedModel):
#    project13wcf_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel13WCF, to_field='usermodel13wcf_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline13WCF, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage13WCF, to_field='stage13wcf_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category13WCF, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    startDays = models.IntegerField(null=False, default=0)   
#    proformad13WCF0001P4 = models.IntegerField(null=False, default=0)
#    setupof13WCF13WCF0002P4 = models.IntegerField(null=False, default=0)
#    ongoing13WCFwork13WCF0003P4 = models.IntegerField(null=False, default=0)
#    proformad13WCF0001Days = models.IntegerField(null=False, default=0)  
#    setupof13WCF13WCF0002days = models.IntegerField(null=False, default=0)
#    ongoing13WCFwork13WCF0003days = models.IntegerField(null=False, default=0)
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime = models.IntegerField(null=False, default=0)##

#    def __str__(self):
#        return self.name

#class Categorybookkeepingspecialprojects(SoftDeletableModel, TimeStampedModel):
#    categorybookkeepingspecialprojects_id = models.IntegerField()
#    name = models.CharField(max_length=250)##

#    def __str__(self):
#        return self.name


#class Pipelinebookkeepingspecialprojects(SoftDeletableModel, TimeStampedModel):
#    pipelinebookkeepingspecialprojects_id = models.IntegerField()
#    name = models.CharField(max_length=250)##

#    def __str__(self):
 #       return self.name

#class Stagebookkeepingspecialprojects(models.Model):
#    stagebookkeepingspecialprojects_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)###
#
 #   def __str__(self):
 #       return self.name

#User Model 
#class UserModelbookkeepingspecialprojects(models.Model):
#    usermodelbookkeepingspecialprojects_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Projectbookkeepingspecialprojects(SoftDeletableModel, TimeStampedModel):
#    projectbookkeepingspecialprojects_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModelbookkeepingspecialprojects, to_field='usermodelbookkeepingspecialprojects_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipelinebookkeepingspecialprojects, on_delete=models.SET_NULL, null=True)
 #   stage = models.ForeignKey(Stagebookkeepingspecialprojects, to_field='stagebookkeepingspecialprojects_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
 #       Categorybookkeepingspecialprojects, on_delete=models.SET_NULL, null=True)
 #   woi = models.BooleanField(null=True, default=list)
 #   projprofilefilter = models.BooleanField(null=True, default=list)
 #   proname = models.BooleanField(null=True, default=list)
 #   allprojectcustomfieldsOOI = JSONField()
 #   dateprojcounter = models.IntegerField(null=False, default=0)
 #   hitlist = models.BooleanField(null=True, default=list)
 #   projintakes = models.BooleanField(null=True, default=list)
 #   projectstatuscancelled = models.BooleanField(null=True, default=list)
 #   projectstatuscompleted = models.BooleanField(null=True, default=list)
 #   projectstatusinprogress = models.BooleanField(null=True, default=list)
 #   startP4 = models.BooleanField(null=True, default=0)
 #   bkpspecial0001inputprepP4 = models.BooleanField(null=True, default=0)
 #   bkpspecial0002reviewP4 = models.BooleanField(null=True, default=0)
 #   bkpspecial0003clearreviewpointsP4 = models.BooleanField(null=True, default=0)
  #  bkpspecial0003finalreviewP4 = models.BooleanField(null=True, default=0)
  #  endP4 = models.BooleanField(null=True, default=0)
  #  startdays = models.BooleanField(null=True, default=0)   
  #  bkpspecial0001inputprepdays = models.BooleanField(null=True, default=0) 
  #  bkpspecial0002reviewdays = models.BooleanField(null=True, default=0)
  #  bkpspecial0003clearreviewpointsdays = models.BooleanField(null=True, default=0)
  #  bkpspecial0003finalreviewdays = models.BooleanField(null=True, default=0)              
  #  enddays = models.BooleanField(null=True, default=0)
  #  TotalP4DaysPerStage = models.BooleanField(null=True, default=0)
  #  TotalDaysPerStage = models.BooleanField(null=True, default=0) 
  #  TurnAroundTime = models.BooleanField(null=True, default=0)
           

  #  def __str__(self):
  #      return self.name


#class Categoryctcstcdmtupdate(SoftDeletableModel, TimeStampedModel):
#    categoryctcstcdmtupdate_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipelinectcstcdmtupdate(SoftDeletableModel, TimeStampedModel):
#    pipelinectcstcdmtupdate_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

class Stagectcstcdmtupdate(models.Model):
    stagectcstcdmtupdate_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#User Model 
#class UserModelctcstcdmtupdate(models.Model):
#    usermodelctcstcdmtupdate_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


class Projectctcstcdmtupdate(SoftDeletableModel, TimeStampedModel):
    projectctcstcdmtupdate_id = models.IntegerField()
    name = models.CharField(max_length=250)
    starteddate = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    project_status = models.CharField(max_length=250)
    #user_responsible = models.ForeignKey(UserModelctcstcdmtupdate, to_field='usermodelctcstcdmtupdate_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #pipeline = models.ForeignKey(Pipelinectcstcdmtupdate, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stagectcstcdmtupdate, to_field='stagectcstcdmtupdate_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #category = models.ForeignKey(
    #    Categoryctcstcdmtupdate, on_delete=models.SET_NULL, null=True)
    woi = models.BooleanField(null=True, default=list)
    projprofilefilter = models.BooleanField(null=True, default=list)
    proname = models.BooleanField(null=True, default=list)
    allprojectcustomfieldsOOI = JSONField()
    dateprojcounter = models.IntegerField(null=False, default=0)
    hitlist = models.BooleanField(null=True, default=list)
    projintakes = models.BooleanField(null=True, default=list)
    projectstatuscancelled = models.BooleanField(null=True, default=list)
    projectstatuscompleted = models.BooleanField(null=True, default=list)
    projectstatusinprogress = models.BooleanField(null=True, default=list)
    startP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0001SetupClientTasksP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0002AdminforCTCPlanPrepP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0003CreateIdeasforClientP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0005InputPrepP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject00051QAwiththeclientP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0006ReviewProjectP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0007CLRRVWPTSP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0008FinalReviewP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0009AssembleCTCPlanP4 = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0011AdminWrapupdays = models.IntegerField(null=False, default=0) 
    endP4 = models.IntegerField(null=False, default=0) 
    startDays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0001SetupClientTasksdays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0002AdminforCTCPlanPrepdays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0003CreateIdeasforClientdays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0005InputPrepdays = models.IntegerField(null=False, default=0)              
    billableCTCSTCProject00051QAwiththeclientdays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0006ReviewProjectdays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0007CLRRVWPTSdays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0008FinalReviewdays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0009AssembleCTCPlandays = models.IntegerField(null=False, default=0) 
    billableCTCSTCProject0011AdminWrapupdays = models.IntegerField(null=False, default=0) 
    enddays = models.IntegerField(null=False, default=0)     
    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
    TotalDaysPerStage = models.IntegerField(null=False, default=0)
    TurnAroundTime  = models.IntegerField(null=False, default=0)
  
    def __str__(self):
        return self.name
    
#class Categoryctcstcproject(SoftDeletableModel, TimeStampedModel):
#    categoryctcstcproject_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipelinectcstcproject(SoftDeletableModel, TimeStampedModel):
#    pipelinectcstcproject_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

class Stagectcstcproject(models.Model):
    stagectcstcproject_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#User Model 
#class UserModelctcstcproject(models.Model):
#    usermodelctcstcproject_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


class Projectctcstcproject(SoftDeletableModel, TimeStampedModel):
    projectctcstcproject_id = models.IntegerField()
    name = models.CharField(max_length=250)
    #starteddate = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    project_status = models.CharField(max_length=250)
    #user_responsible = models.ForeignKey(UserModelctcstcproject, to_field='usermodelctcstcproject_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #pipeline = models.ForeignKey(Pipelinectcstcproject, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stagectcstcproject, to_field='stagectcstcproject_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #category = models.ForeignKey(
    #    Categoryctcstcproject, on_delete=models.SET_NULL, null=True)
    woi = models.BooleanField(null=True, default=list)
    projprofilefilter = models.BooleanField(null=True, default=list)
    proname = models.BooleanField(null=True, default=list)
    allprojectcustomfieldsOOI = JSONField()
    dateprojcounter = models.IntegerField(null=False, default=0)
    hitlist = models.BooleanField(null=True, default=list)
    projintakes = models.BooleanField(null=True, default=list)
    projectstatuscancelled = models.BooleanField(null=True, default=list)
    projectstatuscompleted = models.BooleanField(null=True, default=list)
    projectstatusinprogress = models.BooleanField(null=True, default=list)
    ProformadSTCCTC0001P4 = models.IntegerField(null=False, default=0)
    IntakesSTCCTC0002P4 = models.IntegerField(null=False, default=0)
    CreateIdeasforClientSTCCTC0003P4 = models.IntegerField(null=False, default=0)
    InputPrepSTCCTC0004P4 = models.IntegerField(null=False, default=0)
    ReviewProjectSTCCTC0006P4 = models.IntegerField(null=False, default=0)
    ClearReviewPointsSTCCTC0007P4 = models.IntegerField(null=False, default=0)
    FinalReviewSTCCTC0008P4 = models.IntegerField(null=False, default=0)
    AssembleSTCCTC0009P4 = models.IntegerField(null=False, default=0)
    WrapupSTCCTC0010P4 = models.IntegerField(null=False, default=0)
    CSFUPALLSTCCTC0011P4 = models.IntegerField(null=False, default=0)
    SalesFUPALLSTCCTC0012P4 = models.IntegerField(null=False, default=0)
    RolloverSTCCTC0013P4 = models.IntegerField(null=False, default=0)
    QAwithClientSTCCTC0005P4 = models.IntegerField(null=False, default=0)
    ProformadSTCCTC0001 = models.IntegerField(null=False, default=0)
    IntakesSTCCTC0002 = models.IntegerField(null=False, default=0)
    CreateIdeasforClientSTCCTC0003 = models.IntegerField(null=False, default=0)
    InputPrepSTCCTC0004 = models.IntegerField(null=False, default=0)
    ReviewProjectSTCCTC0006 = models.IntegerField(null=False, default=0)
    ClearReviewPointsSTCCTC0007 = models.IntegerField(null=False, default=0)
    FinalReviewSTCCTC0008 = models.IntegerField(null=False, default=0)
    AssembleSTCCTC0009 = models.IntegerField(null=False, default=0)
    WrapupSTCCTC0010 = models.IntegerField(null=False, default=0)
    CSFUPALLSTCCTC0011 = models.IntegerField(null=False, default=0)
    SalesFUPALLSTCCTC0012 = models.IntegerField(null=False, default=0)
    RolloverSTCCTC0013 = models.IntegerField(null=False, default=0)
    QAwithClientSTCCTC0005 = models.IntegerField(null=False, default=0)
    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
    TotalDaysPerStage = models.IntegerField(null=False, default=0)
    TurnAroundTime  = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

#class Categoryirsnotice(SoftDeletableModel, TimeStampedModel):
#    categoryirsnotice_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipelineirsnotice(SoftDeletableModel, TimeStampedModel):
#    pipelineirsnotice_id = models.IntegerField()
#    name = models.CharField(max_length=250)#

#    def __str__(self):
#        return self.name

class Stageirsnotice(models.Model):
    stageirsnotice_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#User Model 
#class UserModelirsnotice(models.Model):
#    usermodelirsnotice_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


class Projectirsnotice(SoftDeletableModel, TimeStampedModel):
    projectirsnotice_id = models.IntegerField()
    name = models.CharField(max_length=250)
    starteddate = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    project_status = models.CharField(max_length=250)
    #user_responsible = models.ForeignKey(UserModelirsnotice, to_field='usermodelirsnotice_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #pipeline = models.ForeignKey(Pipelineirsnotice, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stageirsnotice, to_field='stageirsnotice_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #category = models.ForeignKey(
    #    Categoryirsnotice, on_delete=models.SET_NULL, null=True)
    woi = models.BooleanField(null=True, default=list)
    projprofilefilter = models.BooleanField(null=True, default=list)
    proname = models.BooleanField(null=True, default=list)
    allprojectcustomfieldsOOI = JSONField()
    dateprojcounter = models.IntegerField(null=False, default=0)
    hitlist = models.BooleanField(null=True, default=list)
    projintakes = models.BooleanField(null=True, default=list)
    projectstatuscancelled = models.BooleanField(null=True, default=list)
    projectstatuscompleted = models.BooleanField(null=True, default=list)
    projectstatusinprogress = models.BooleanField(null=True, default=list)
    startP4 = models.IntegerField(null=False, default=0) 
    irsnotice0001intakesforirsnoticeadminP4 = models.IntegerField(null=False, default=0) 
    irsnotice00021streviewCPAleveltaxteammemberP4 = models.IntegerField(null=False, default=0) 
    irsnotice0003clearreviewpointsP4 = models.IntegerField(null=False, default=0) 
    irsnotice00032ndreviewmanagerleveldeptheadP4 = models.IntegerField(null=False, default=0) 
    irsnotice0004mailingphysicalazadminP4 = models.IntegerField(null=False, default=0) 
    irsnotice0005followupmanagerleveldeptheadP4 = models.IntegerField(null=False, default=0) 
    irsnotice0006followupadminP4 = models.IntegerField(null=False, default=0) 
    irsnotice0007followupCPAP4 = models.IntegerField(null=False, default=0) 
    irsnotice0008closeoutnoticeAdminP4 = models.IntegerField(null=False, default=0) 
    endP4 = models.IntegerField(null=False, default=0) 
    startDays = models.IntegerField(null=False, default=0)     
    irsnotice0001intakesforirsnoticeadmindays = models.IntegerField(null=False, default=0) 
    irsnotice00021streviewCPAleveltaxteammemberdays = models.IntegerField(null=False, default=0) 
    irsnotice0003clearreviewpointsdays = models.IntegerField(null=False, default=0) 
    irsnotice00032ndreviewmanagerleveldeptheaddays = models.IntegerField(null=False, default=0)               
    irsnotice0004mailingphysicalazadmindays = models.IntegerField(null=False, default=0) 
    irsnotice0005followupmanagerleveldeptheaddays = models.IntegerField(null=False, default=0) 
    irsnotice0006followupadmindays = models.IntegerField(null=False, default=0) 
    irsnotice0007followupCPAdays = models.IntegerField(null=False, default=0) 
    irsnotice0008closeoutnoticeAdmindays = models.IntegerField(null=False, default=0) 
    enddays = models.IntegerField(null=False, default=0) 
    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
    TotalDaysPerStage = models.IntegerField(null=False, default=0)
    TurnAroundTime  = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

#class Categorymonthlybookkeeping(SoftDeletableModel, TimeStampedModel):
#    categorymonthlybookkeeping_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name#


#class Pipelinemonthlybookkeeping(SoftDeletableModel, TimeStampedModel):
#    pipelinemonthlybookkeeping_id = models.IntegerField()
#    name = models.CharField(max_length=250)#

#    def __str__(self):
#        return self.name

#class Stagemonthlybookkeeping(models.Model):
#    stagemonthlybookkeeping_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModelmonthlybookkeeping(models.Model):
#    usermodelmonthlybookkeeping_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Projectmonthlybookkeeping(SoftDeletableModel, TimeStampedModel):
#    projectmonthlybookkeeping_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModelmonthlybookkeeping, to_field='usermodelmonthlybookkeeping_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipelinemonthlybookkeeping, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stagemonthlybookkeeping, to_field='stagemonthlybookkeeping_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Categorymonthlybookkeeping, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
 #   allprojectcustomfieldsOOI = JSONField()
 #   dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    SetupP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKP0001InputReconcileP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKP0002SelfReviewPrintWPSP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKP0003ReviewWPSP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKP0004ClearReviewPointsP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKP0005FinalReviewP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKP00060BooksDonebutWOIfromClientP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKP00061RereviewwithclientsadditionalanswersP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKP0006FinalCPAsignoffsendtoclientP4 = models.BooleanField(null=True, default=0)
#    MonthlyBKPENDP4 = models.BooleanField(null=True, default=0)
 #   SetupDays = models.BooleanField(null=True, default=0)  
 #   MonthlyBKP0001InputReconciledays = models.BooleanField(null=True, default=0) 
 #   MonthlyBKP0002SelfReviewPrintWPSdays = models.BooleanField(null=True, default=0)
#    MonthlyBKP0003ReviewWPSdays = models.BooleanField(null=True, default=0)
#    MonthlyBKP0004ClearReviewPointsdays = models.BooleanField(null=True, default=0)              
#    MonthlyBKP0005FinalReviewdays = models.BooleanField(null=True, default=0)
 #   MonthlyBKP00060BooksDonebutWOIfromClientdays = models.BooleanField(null=True, default=0)
#    MonthlyBKP00061Rereviewwithclientsadditionalanswersdays = models.BooleanField(null=True, default=0)
#    MonthlyBKP0006FinalCPAsignoffsendtoclientdays = models.BooleanField(null=True, default=0)
 #   MonthlyBKPENDdays = models.BooleanField(null=True, default=0)
 #   TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
 #   TotalDaysPerStage = models.IntegerField(null=False, default=0)
 #   TurnAroundTime  = models.IntegerField(null=False, default=0)

 #   def __str__(self):
 #       return self.name
    
#class Categorymonthlyperiodic(SoftDeletableModel, TimeStampedModel):
#    categorymonthlyperiodic_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#
#    def __str__(self):
#        return self.name


#class Pipelinemonthlyperiodic(SoftDeletableModel, TimeStampedModel):
#    pipelinemonthlyperiodic_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#
#    def __str__(self):
#        return self.name

#class Stagemonthlyperiodic(models.Model):
#    stagemonthlyperiodic_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)###

#    def __str__(self):
#        return self.name

#User Model 
#class UserModelmonthlyperiodic(models.Model):
#    usermodelmonthlyperiodic_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)
#
#    def __str__(self):
 #       return self.name


#class Projectmonthlyperiodic(SoftDeletableModel, TimeStampedModel):
#    projectmonthlyperiodic_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
 #   user_responsible = models.ForeignKey(UserModelmonthlyperiodic, to_field='usermodelmonthlyperiodic_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
 #   pipeline = models.ForeignKey(Pipelinemonthlyperiodic, on_delete=models.SET_NULL, null=True)
 #   stage = models.ForeignKey(Stagemonthlyperiodic, to_field='stagemonthlyperiodic_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
 #   category = models.ForeignKey(
#        Categorymonthlyperiodic, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    startP4 = models.IntegerField(null=False, default=0)
#    profitCentsMonthlyReports0001InputPrepP4 = models.IntegerField(null=False, default=0)
 #   profitCentsMonthlyReports0002ReviewP4 = models.IntegerField(null=False, default=0)
 #   profitCentsMonthlyReports0003ClearReviewPointsP4 = models.IntegerField(null=False, default=0)
 #   endP4 = models.IntegerField(null=False, default=0)
 #   startDays = models.IntegerField(null=False, default=0)  
 #   profitCentsMonthlyReports0001InputPrepdays = models.IntegerField(null=False, default=0)
 #   profitCentsMonthlyReports0002Reviewdays = models.IntegerField(null=False, default=0)
 #   profitCentsMonthlyReports0003ClearReviewPointsdays = models.IntegerField(null=False, default=0)
 #   enddays = models.IntegerField(null=False, default=0)
 #   TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
 #   TotalDaysPerStage = models.IntegerField(null=False, default=0)
 #   TurnAroundTime  = models.IntegerField(null=False, default=0)#

  #  def __str__(self):
  #      return self.name

#class Categoryoptinupdate(SoftDeletableModel, TimeStampedModel):
#    categoryoptinupdate_id = models.IntegerField()
#    name = models.CharField(max_length=250)

 #   def __str__(self):
 #       return self.name


#class Pipelineoptinupdate(SoftDeletableModel, TimeStampedModel):
#    pipelineoptinupdate_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stageoptinupdate(models.Model):
#    stageoptinupdate_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)##
#
#    def __str__(self):
#        return self.name

#User Model 
#class UserModeloptinupdate(models.Model):
#    usermodeloptinupdate_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name#


#class Projectoptinupdate(SoftDeletableModel, TimeStampedModel):
#    projectoptinupdate_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModeloptinupdate, to_field='usermodeloptinupdate_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipelineoptinupdate, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stageoptinupdate, to_field='stageoptinupdate_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
 #   category = models.ForeignKey(
 #       Categoryoptinupdate, on_delete=models.SET_NULL, null=True)
 #   woi = models.BooleanField(null=True, default=list)
 #   projprofilefilter = models.BooleanField(null=True, default=list)
 #   proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
 #   projectstatuscancelled = models.BooleanField(null=True, default=list)
 #   projectstatuscompleted = models.BooleanField(null=True, default=list)
 #   projectstatusinprogress = models.BooleanField(null=True, default=list)
 #   startP4 = models.IntegerField(null=False, default=0)
 #   OPTINUpdateProc0001CreateOPTINupdateletterP4 = models.IntegerField(null=False, default=0)
 #   OPTINUpdateProc0002SendOPTINupdateletterP4 = models.IntegerField(null=False, default=0)
  ##  OPTINUpdateProc0003UpdateProcessingP4 = models.IntegerField(null=False, default=0)
 #   endP4 = models.IntegerField(null=False, default=0)
 #   startDays = models.IntegerField(null=False, default=0)  
 #   OPTINUpdateProc0001CreateOPTINupdateletterdays = models.IntegerField(null=False, default=0)
 #   OPTINUpdateProc0002SendOPTINupdateletterdays = models.IntegerField(null=False, default=0)
 #   OPTINUpdateProc0003UpdateProcessingdays = models.IntegerField(null=False, default=0)     
 #   enddays = models.IntegerField(null=False, default=0)
 #   TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
 #   TotalDaysPerStage = models.IntegerField(null=False, default=0)
 #   TurnAroundTime  = models.IntegerField(null=False, default=0)

 #   def __str__(self):
 #       return self.name
    
#class Categoryquarterlyestimates(SoftDeletableModel, TimeStampedModel):
#    categoryquarterlyestimates_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipelinequarterlyestimates(SoftDeletableModel, TimeStampedModel):
#    pipelinequarterlyestimates_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stagequarterlyestimates(models.Model):
#    stagequarterlyestimates_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModelquarterlyestimates(models.Model):
#    usermodelquarterlyestimates_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)#

#    def __str__(self):#
#        return self.name


#class Projectquarterlyestimates(SoftDeletableModel, TimeStampedModel):
#    projectquarterlyestimates_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModelquarterlyestimates, to_field='usermodelquarterlyestimates_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipelinequarterlyestimates, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stagequarterlyestimates, to_field='stagequarterlyestimates_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Categoryquarterlyestimates, on_delete=models.SET_NULL, null=True)
 #   woi = models.BooleanField(null=True, default=list)
 #   projprofilefilter = models.BooleanField(null=True, default=list)
 #   proname = models.BooleanField(null=True, default=list)
 #   allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
 #   projectstatuscompleted = models.BooleanField(null=True, default=list)
 #   projectstatusinprogress = models.BooleanField(null=True, default=list)
 #   startDays = models.IntegerField(null=False, default=0)   
#    ProformadQtrlyEst0001Days = models.IntegerField(null=False, default=0) 
#    ClientInterviewQtrlyEst0002days = models.IntegerField(null=False, default=0) 
#    InputPrepQtrlyEst0003days = models.IntegerField(null=False, default=0) 
#    ReviewQtrlyEst0004days = models.IntegerField(null=False, default=0) 
#    ClearReviewPointsQtrlyEst0005days = models.IntegerField(null=False, default=0) 
#    FinalReviewQtrlyEst0006days = models.IntegerField(null=False, default=0) 
 #   DeliverQtrlyEst0007days = models.IntegerField(null=False, default=0) 
#    RolloverProcessQtrlyEst0008days = models.IntegerField(null=False, default=0)     
#    startP4 = models.IntegerField(null=False, default=0)       
#    ProformadQtrlyEst0001P4 = models.IntegerField(null=False, default=0) 
 #   ClientInterviewQtrlyEst0002P4 = models.IntegerField(null=False, default=0) 
 #   InputPrepQtrlyEst0003P4 = models.IntegerField(null=False, default=0) 
#    ReviewQtrlyEst0004P4 = models.IntegerField(null=False, default=0) 
 #   ClearReviewPointsQtrlyEst0005P4 = models.IntegerField(null=False, default=0) 
 #   FinalReviewQtrlyEst0006P4 = models.IntegerField(null=False, default=0) 
 #   DeliverQtrlyEst0007P4 = models.IntegerField(null=False, default=0) 
 #   RolloverProcessQtrlyEst0008P4 = models.IntegerField(null=False, default=0) 
 #   TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
# #   TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)

 #   def __str__(self):
 #       return self.name

#class Categorysalestaxreturn(SoftDeletableModel, TimeStampedModel):
#    categorysalestaxreturn_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipelinesalestaxreturn(SoftDeletableModel, TimeStampedModel):
#    pipelinesalestaxreturn_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

class Stagesalestaxreturn(models.Model):
    stagesalestaxreturn_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#User Model 
#class UserModelsalestaxreturn(models.Model):
#    usermodelsalestaxreturn_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


class Projectsalestaxreturn(SoftDeletableModel, TimeStampedModel):
    projectsalestaxreturn_id = models.IntegerField()
    name = models.CharField(max_length=250)
    starteddate = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    project_status = models.CharField(max_length=250)
    #user_responsible = models.ForeignKey(UserModelsalestaxreturn, to_field='usermodelsalestaxreturn_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #pipeline = models.ForeignKey(Pipelinesalestaxreturn, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stagesalestaxreturn, to_field='stagesalestaxreturn_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #category = models.ForeignKey(
    #    Categorysalestaxreturn, on_delete=models.SET_NULL, null=True)
    woi = models.BooleanField(null=True, default=list)
    projprofilefilter = models.BooleanField(null=True, default=list)
    proname = models.BooleanField(null=True, default=list)
    allprojectcustomfieldsOOI = JSONField()
    dateprojcounter = models.IntegerField(null=False, default=0)
    hitlist = models.BooleanField(null=True, default=list)
    projintakes = models.BooleanField(null=True, default=list)
    projectstatuscancelled = models.BooleanField(null=True, default=list)
    projectstatuscompleted = models.BooleanField(null=True, default=list)
    projectstatusinprogress = models.BooleanField(null=True, default=list)
    ProformadSalesTax0001P4 = models.IntegerField(null=False, default=0)
    InputPrepSalesTax0002P4 = models.IntegerField(null=False, default=0)
    ReviewProcessSalesTax0003P4 = models.IntegerField(null=False, default=0)
    RolloveProcessSaleTax0004P4 = models.IntegerField(null=False, default=0)
    ProformadSalesTax0001Days = models.IntegerField(null=False, default=0) 
    InputPrepSalesTax0002days = models.IntegerField(null=False, default=0) 
    ReviewProcessSalesTax0003days = models.IntegerField(null=False, default=0) 
    RolloveProcessSaleTax0004days = models.IntegerField(null=False, default=0) 
    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
    TotalDaysPerStage = models.IntegerField(null=False, default=0)
    TurnAroundTime  = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name



#class Categoryquarterlyestimates(SoftDeletableModel, TimeStampedModel):
#    categoryquarterlyestimates_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipelinequarterlyestimates(SoftDeletableModel, TimeStampedModel):
#    pipelinequarterlyestimates_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stagequarterlyestimates(models.Model):
#    stagequarterlyestimates_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModelquarterlyestimates(models.Model):
#    usermodelquarterlyestimates_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
 #       return self.name


#class Projectquarterlyestimates(SoftDeletableModel, TimeStampedModel):
#    projectquarterlyestimates_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModelquarterlyestimates, to_field='usermodelquarterlyestimates_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipelinequarterlyestimates, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stagequarterlyestimates, to_field='stagequarterlyestimates_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Categoryquarterlyestimates, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    startDays = models.IntegerField(null=False, default=0)   
#    ProformadQtrlyEst0001Days = models.IntegerField(null=False, default=0) 
#    ClientInterviewQtrlyEst0002days = models.IntegerField(null=False, default=0) 
#    InputPrepQtrlyEst0003days = models.IntegerField(null=False, default=0) 
#    ReviewQtrlyEst0004days = models.IntegerField(null=False, default=0) 
#    ClearReviewPointsQtrlyEst0005days = models.IntegerField(null=False, default=0) 
#    FinalReviewQtrlyEst0006days = models.IntegerField(null=False, default=0) 
#    DeliverQtrlyEst0007days = models.IntegerField(null=False, default=0) 
#    RolloverProcessQtrlyEst0008days = models.IntegerField(null=False, default=0)     
#    startP4 = models.IntegerField(null=False, default=0)       
#    ProformadQtrlyEst0001P4 = models.IntegerField(null=False, default=0) 
#    ClientInterviewQtrlyEst0002P4 = models.IntegerField(null=False, default=0) 
#    InputPrepQtrlyEst0003P4 = models.IntegerField(null=False, default=0) 
#    ReviewQtrlyEst0004P4 = models.IntegerField(null=False, default=0) 
#    ClearReviewPointsQtrlyEst0005P4 = models.IntegerField(null=False, default=0) 
#    FinalReviewQtrlyEst0006P4 = models.IntegerField(null=False, default=0) 
#    DeliverQtrlyEst0007P4 = models.IntegerField(null=False, default=0) 
#    RolloverProcessQtrlyEst0008P4 = models.IntegerField(null=False, default=0) 
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)

#    def __str__(self):
#        return self.name

#class Categorysalestaxreturn(SoftDeletableModel, TimeStampedModel):
#    categorysalestaxreturn_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipelinesalestaxreturn(SoftDeletableModel, TimeStampedModel):
#    pipelinesalestaxreturn_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stagesalestaxreturn(models.Model):
#    stagesalestaxreturn_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModelsalestaxreturn(models.Model):
#    usermodelsalestaxreturn_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Projectsalestaxreturn(SoftDeletableModel, TimeStampedModel):
#    projectsalestaxreturn_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModelsalestaxreturn, to_field='usermodelsalestaxreturn_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipelinesalestaxreturn, on_delete=models.SET_NULL, null=True)
#   stage = models.ForeignKey(Stagesalestaxreturn, to_field='stagesalestaxreturn_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Categorysalestaxreturn, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    ProformadSalesTax0001P4 = models.IntegerField(null=False, default=0)
#    InputPrepSalesTax0002P4 = models.IntegerField(null=False, default=0)
#    ReviewProcessSalesTax0003P4 = models.IntegerField(null=False, default=0)
#    RolloveProcessSaleTax0004P4 = models.IntegerField(null=False, default=0)
#    ProformadSalesTax0001Days = models.IntegerField(null=False, default=0) 
#    InputPrepSalesTax0002days = models.IntegerField(null=False, default=0) 
#    ReviewProcessSalesTax0003days = models.IntegerField(null=False, default=0) 
#    RolloveProcessSaleTax0004days = models.IntegerField(null=False, default=0) 
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)

#    def __str__(self):
#        return self.name


# NEW PROJECTS STARTS HERE

#class Category1040(SoftDeletableModel, TimeStampedModel):
#    category1040_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline1040(SoftDeletableModel, TimeStampedModel):
#    pipeline1040_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1040(models.Model):
#    stage1040_id = models.PositiveIntegerField(unique=True, primary_key=True)
        #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

    #User Model 
#class UserModel1040(models.Model):
#    usermodel1040_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project1040(SoftDeletableModel, TimeStampedModel):#
#    project1040_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1040, to_field='usermodel1040_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1040, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1040, to_field='stage1040_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1040, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list) 
#    Proformad10400001P4 = models.IntegerField(null=False, default=0)
#    Intakes10400002P4 = models.IntegerField(null=False, default=0)
#    BKKPNGRevTRPrintRevPreCompileP4 = models.IntegerField(null=False, default=0)
#    FinalReviewofBKWPS10400004P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBk10400005P4 = models.IntegerField(null=False, default=0)
#    InputPrep10400006P4 = models.IntegerField(null=False, default=0)
#    Waitingonk110400007P4 = models.IntegerField(null=False, default=0)
#    Review10400008P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsTR10400009P4 = models.IntegerField(null=False, default=0)
#    Finalize1stReview10400010P4 = models.IntegerField(null=False, default=0)
#    FinalReview10400011P4 = models.IntegerField(null=False, default=0)
#    PartnerSignoff10400012P4 = models.IntegerField(null=False, default=0)
#    BillPrintTRsAssembly10400013P4 = models.IntegerField(null=False, default=0)
#    WaitingforClientSignature10400014P4 = models.IntegerField(null=False, default=0)
#    CloseOutTaxReturn10400015P4 = models.IntegerField(null=False, default=0)
#    FeeAnalysis10400018P4 = models.IntegerField(null=False, default=0)
#    RolloverProcess10400019P4 = models.IntegerField(null=False, default=0)
 #   Proformad10400001 = models.IntegerField(null=False, default=0)
 #   Intakes10400002 = models.IntegerField(null=False, default=0)
 #   BKKPNGRevTRPrintRevPreCompile = models.IntegerField(null=False, default=0)
#   FinalReviewofBKWPS10400004 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBk10400005 = models.IntegerField(null=False, default=0)
#    InputPrep10400006 = models.IntegerField(null=False, default=0)
#    Waitingonk110400007 = models.IntegerField(null=False, default=0)
#    Review10400008 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsTR10400009 = models.IntegerField(null=False, default=0)
#    Finalize1stReview10400010 = models.IntegerField(null=False, default=0)
#    FinalReview10400011 = models.IntegerField(null=False, default=0)
#    PartnerSignoff10400012 = models.IntegerField(null=False, default=0)
#    BillPrintTRsAssembly10400013 = models.IntegerField(null=False, default=0)
#    WaitingforClientSignature10400014 = models.IntegerField(null=False, default=0)
 #   CloseOutTaxReturn10400015 = models.IntegerField(null=False, default=0)
#    FeeAnalysis10400018 = models.IntegerField(null=False, default=0)
#    RolloverProcess10400019 = models.IntegerField(null=False, default=0)
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)##

#    def __str__(self):
 #       return self.name
    
#class Category1040X(SoftDeletableModel, TimeStampedModel):
#    category1040x_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline1040X(SoftDeletableModel, TimeStampedModel):
#    pipeline1040x_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1040X(models.Model):
#    stage1040x_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1040X(models.Model):
#    usermodel1040x_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project1040X(SoftDeletableModel, TimeStampedModel):
#    project1040x_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1040X, to_field='usermodel1040x_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1040X, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1040X, to_field='stage1040x_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1040X, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    Proformad1040X0001P4 = models.IntegerField(null=False, default=0)
#    Intakes1040X0002P4 = models.IntegerField(null=False, default=0)
#    BKKPNGRFORTRPRINTReviewPreCompile40XP4 = models.IntegerField(null=False, default=0)
#    FinalReviewofBKWPS1040X0004P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBk1040X0005P4 = models.IntegerField(null=False, default=0)
#    InputPrep1040X0006P4 = models.IntegerField(null=False, default=0)
#    Waitingonk11040X0007P4 = models.IntegerField(null=False, default=0)
#    Review1040X0008P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsTR1040X0009P4 = models.IntegerField(null=False, default=0)
#    Finalize1stReview1040X0010P4 = models.IntegerField(null=False, default=0)
#    FinalReview1040X0011P4 = models.IntegerField(null=False, default=0) 
#    PartnerSignoff1040X0012P4 = models.IntegerField(null=False, default=0)
#    BillPrintTRsAssembly1040X0013P4 = models.IntegerField(null=False, default=0)
#    WaitingforClientSignature1040X0014P4 = models.IntegerField(null=False, default=0)
#    CloseOutTaxReturn1040X0015P4 = models.IntegerField(null=False, default=0)
#    FeeAnalysis1040X0016P4 = models.IntegerField(null=False, default=0)
#    RolloverProcess1040X0017P4 = models.IntegerField(null=False, default=0)
#    Proformad1040X0001 = models.IntegerField(null=False, default=0)
#    Intakes1040X0002 = models.IntegerField(null=False, default=0)
#    BKKPNGRFORTRPRINTReviewPreCompile40X = models.IntegerField(null=False, default=0)
#    FinalReviewofBKWPS1040X0004 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBk1040X0005 = models.IntegerField(null=False, default=0)
#    InputPrep1040X0006 = models.IntegerField(null=False, default=0)
 #   Waitingonk11040X0007 = models.IntegerField(null=False, default=0)
 #   Review1040X0008 = models.IntegerField(null=False, default=0)
 #   ClearReviewPointsTR1040X0009 = models.IntegerField(null=False, default=0)
 #   Finalize1stReview1040X0010 = models.IntegerField(null=False, default=0)
 #   FinalReview1040X0011 = models.IntegerField(null=False, default=0) 
 #   PartnerSignoff1040X0012 = models.IntegerField(null=False, default=0)
#    BillPrintTRsAssembly1040X0013 = models.IntegerField(null=False, default=0)
#    WaitingforClientSignature1040X0014 = models.IntegerField(null=False, default=0)
#    CloseOutTaxReturn1040X0015 = models.IntegerField(null=False, default=0)
#    FeeAnalysis1040X0016 = models.IntegerField(null=False, default=0)
#    RolloverProcess1040X0017 = models.IntegerField(null=False, default=0)   
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)#

#    def __str__(self):
#        return self.name

#class Category1041estateincome(SoftDeletableModel, TimeStampedModel):
#    category1041estateincome_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self): 
#        return self.name


#class Pipeline1041estateincome(SoftDeletableModel, TimeStampedModel):
#    pipeline1041estateincome_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1041estateincome(models.Model):
#    stage1041estateincome_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)#
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1041estateincome(models.Model):
#    usermodel1041estateincome_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project1041estateincome(SoftDeletableModel, TimeStampedModel):
#    project1041estateincome_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1041estateincome, to_field='usermodel1041estateincome_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1041estateincome, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1041estateincome, to_field='stage1041estateincome_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1041estateincome, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
 #   hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
 #   projectstatuscancelled = models.BooleanField(null=True, default=list)
 #   projectstatuscompleted = models.BooleanField(null=True, default=list)
 #   projectstatusinprogress = models.BooleanField(null=True, default=list)
 #   STARTP4 = models.IntegerField(null=False, default=0)
 #   estateincome1041EstateIncome0001ProformadP4 = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0002IntakeProcessP4 = models.IntegerField(null=False, default=0)
#    EstateIncome0003BookkeepingReviewTRP4 = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0004FinalReviewofBKWPSP4 = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0005ClearReviewPointsforBKP4 = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0006InputPrepP4 = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0007ReviewP4 = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0008ClearReviewPointsForTRP4 = models.IntegerField(null=False, default=0)
#    EstateIncome0009FinalReviewP4 = models.IntegerField(null=False, default=0)
#    EstateIncome0010PartnerSignoffP4 = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0012AssembleP4 = models.IntegerField(null=False, default=0)
 #   estateincome1041EstateIncome0013WaitingforSignatureP4 = models.IntegerField(null=False, default=0)#
 #   estateincome1041EstateIncome0014CloseOutTaxReturnP4 = models.IntegerField(null=False, default=0)
#    ENDP4 = models.IntegerField(null=False, default=0)
#    START = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0001Proformad = models.IntegerField(null=False, default=0)
 #   estateincome1041EstateIncome0002IntakeProcess = models.IntegerField(null=False, default=0)
 #   EstateIncome0003BookkeepingReviewTR = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0004FinalReviewofBKWPS = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0005ClearReviewPointsforBK = models.IntegerField(null=False, default=0)
 #   estateincome1041EstateIncome0006InputPrep = models.IntegerField(null=False, default=0)
 #   estateincome1041EstateIncome0007Review = models.IntegerField(null=False, default=0)
 #   estateincome1041EstateIncome0008ClearReviewPointsForTR = models.IntegerField(null=False, default=0)
 #   EstateIncome0009FinalReview = models.IntegerField(null=False, default=0)
 #   EstateIncome0010PartnerSignoff = models.IntegerField(null=False, default=0)
 #   estateincome1041EstateIncome0012Assemble = models.IntegerField(null=False, default=0)
# #  estateincome1041EstateIncome0013WaitingforSignature = models.IntegerField(null=False, default=0)
#    estateincome1041EstateIncome0014CloseOutTaxReturn = models.IntegerField(null=False, default=0)
#    END = models.IntegerField(null=False, default=0)
#
#
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)

#    def __str__(self):
#        return self.name

#class Category1041trust(SoftDeletableModel, TimeStampedModel):
#    category1041trust_id = models.IntegerField()
#    name = models.CharField(max_length=250)#

#    def __str__(self):
#        return self.name


#class Pipeline1041trust(SoftDeletableModel, TimeStampedModel):
#    pipeline1041trust_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1041trust(models.Model):
#    stage1041trust_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1041trust(models.Model):
#    usermodel1041trust_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project1041trust(SoftDeletableModel, TimeStampedModel):
#    project1041trust_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1041trust, to_field='usermodel1041trust_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1041trust, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1041trust, to_field='stage1041trust_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1041trust, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
 #   projectstatuscancelled = models.BooleanField(null=True, default=list)
 #   projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    STARTP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0001ProformadP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0002IntakeProcessP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0003BookkeepingReviewTRP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0004FinalReviewofBKWPSP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0005ClearReviewPointsforBKP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0006InputPrepP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0007ReviewP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0008ClearReviewPointsForTRP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0009FinalReviewP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0010PartnerSignoffP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0011BillPrintTRsP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0012AssembleP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0013WaitingforSignatureP4 = models.IntegerField(null=False, default=0)
#    trust1041Trust0014CloseOutTaxReturnP4 = models.IntegerField(null=False, default=0)
#    ENDP4 = models.IntegerField(null=False, default=0)
 #   START = models.IntegerField(null=False, default=0)
 #   trust1041Trust0001Proformad = models.IntegerField(null=False, default=0)
 #   trust1041Trust0002IntakeProcess = models.IntegerField(null=False, default=0)
 #   trust1041Trust0003BookkeepingReviewTR = models.IntegerField(null=False, default=0)
  #  trust1041Trust0004FinalReviewofBKWPS = models.IntegerField(null=False, default=0)
  #  trust1041Trust0005ClearReviewPointsforBK = models.IntegerField(null=False, default=0)
  #  trust1041Trust0006InputPrep = models.IntegerField(null=False, default=0)
  #  trust1041Trust0007Review = models.IntegerField(null=False, default=0)
  #  trust1041Trust0008ClearReviewPointsForTR = models.IntegerField(null=False, default=0)
  #  trust1041Trust0009FinalReview = models.IntegerField(null=False, default=0)
  #  trust1041Trust0010PartnerSignoff = models.IntegerField(null=False, default=0)
  #  trust1041Trust0011BillPrintTRs = models.IntegerField(null=False, default=0)
  #  trust1041Trust0012Assemble = models.IntegerField(null=False, default=0)
  #  trust1041Trust0013WaitingforSignature = models.IntegerField(null=False, default=0)
  #  trust1041Trust0014CloseOutTaxReturn = models.IntegerField(null=False, default=0)
  #  END = models.IntegerField(null=False, default=0)
  #  TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
  #  TotalDaysPerStage = models.IntegerField(null=False, default=0)
  #  TurnAroundTime  = models.IntegerField(null=False, default=0)

 #   def __str__(self):
 #       return self.name

#class Category1065(SoftDeletableModel, TimeStampedModel):
#    category1065_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Pipeline1065(SoftDeletableModel, TimeStampedModel):
#    pipeline1065_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1065(models.Model):
#    stage1065_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)#

#    def __str__(self):
#        return self.name#

#User Model 
#class UserModel1065(models.Model):
#    usermodel1065_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)#

#    def __str__(self):
#        return self.name


#class Project1065(SoftDeletableModel, TimeStampedModel):
#    project1065_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1065, to_field='usermodel1065_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1065, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1065, to_field='stage1065_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1065, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    Proformad10650001P4 = models.IntegerField(null=False, default=0)
#    Intakes10650002P4 = models.IntegerField(null=False, default=0)
#    BKPNGRevTRPrintRevPreCompileP4 = models.IntegerField(null=False, default=0)
#    FinalReviewofBKWPS10650004P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBKWPS10650005P4 = models.IntegerField(null=False, default=0)
 #   InputPrep10650006P4 = models.IntegerField(null=False, default=0)
 #   WaitingonK110650007P4 = models.IntegerField(null=False, default=0)
 #   Review10650008P4 = models.IntegerField(null=False, default=0)
#3   ClearReviewPointsforTR10650009P4 = models.IntegerField(null=False, default=0)
 #   Finalize1stReview10650010P4 = models.IntegerField(null=False, default=0)
 # 3  FinalReview10650011P4 = models.IntegerField(null=False, default=0)
 # 3  PartnerSignoff10650012P4 = models.IntegerField(null=False, default=0)
 #   BillPrintAssembly10650013P4 = models.IntegerField(null=False, default=0)
 #   WaitingforClientSignature10650014P4 = models.IntegerField(null=False, default=0)
 #   CloseOutTR10650015P4 = models.IntegerField(null=False, default=0)
 #   FeeAnalysis10650016P4 = models.IntegerField(null=False, default=0)
 #   Rollover10650017P4 = models.IntegerField(null=False, default=0)   
 #   Proformad10650001 = models.IntegerField(null=False, default=0)
 #   Intakes10650002 = models.IntegerField(null=False, default=0)
 #   BKPNGRevTRPrintRevPreCompile = models.IntegerField(null=False, default=0)
 #   FinalReviewofBKWPS10650004 = models.IntegerField(null=False, default=0)
 #   ClearReviewPointsforBKWPS10650005 = models.IntegerField(null=False, default=0)
 #   InputPrep10650006 = models.IntegerField(null=False, default=0)
 #   WaitingonK110650007 = models.IntegerField(null=False, default=0)
 #   Review10650008 = models.IntegerField(null=False, default=0)
 #   ClearReviewPointsforTR10650009 = models.IntegerField(null=False, default=0)
 #   Finalize1stReview10650010 = models.IntegerField(null=False, default=0)
 #   FinalReview10650011 = models.IntegerField(null=False, default=0)
 #   PartnerSignoff10650012 = models.IntegerField(null=False, default=0)
 #   BillPrintAssembly10650013 = models.IntegerField(null=False, default=0)
 #   WaitingforClientSignature10650014 = models.IntegerField(null=False, default=0)
 #   CloseOutTR10650015 = models.IntegerField(null=False, default=0)
 #   FeeAnalysis10650016 = models.IntegerField(null=False, default=0)
 #   Rollover10650017 = models.IntegerField(null=False, default=0) 
 #   TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
 #   TotalDaysPerStage = models.IntegerField(null=False, default=0)
 #   TurnAroundTime  = models.IntegerField(null=False, default=0)

#    def __str__(self):
#        return self.name

    
#class Category1065X(SoftDeletableModel, TimeStampedModel):
#    category1065x_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):#
#        return self.name


#class Pipeline1065X(SoftDeletableModel, TimeStampedModel):
#    pipeline1065x_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1065X(models.Model):
#    stage1065x_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1065X(models.Model):
#    usermodel1065x_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project1065X(SoftDeletableModel, TimeStampedModel):
#    project1065x_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1065X, to_field='usermodel1065x_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1065X, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1065X, to_field='stage1065x_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
 #       Category1065X, on_delete=models.SET_NULL, null=True)
 #   woi = models.BooleanField(null=True, default=list)
 #   projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
 #   projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    STARTP4 = models.IntegerField(null=False, default=0)
#    x1065X0001IntakeProcessP4 = models.IntegerField(null=False, default=0)
#    x1065X0002PrintPBCFinancialStatementsforBKTRRVWP4 = models.IntegerField(null=False, default=0)
#    x1065X0003BookkeepingReviewTRP4 = models.IntegerField(null=False, default=0)
#    x1065X0004FinalReviewofBKWPSP4 = models.IntegerField(null=False, default=0)
 #   x1065X0005ClearReviewPointsforBKP4 = models.IntegerField(null=False, default=0)
 #   x1065X0006InputPrepP4 = models.IntegerField(null=False, default=0)
 #   x1065X0007ReviewP4 = models.IntegerField(null=False, default=0)
 #   x1065X0008ClearReviewPointsForTRP4 = models.IntegerField(null=False, default=0)
#    x1065X0009FinalReviewP4 = models.IntegerField(null=False, default=0)
#    x1065X0010PartnerSignoffP4 = models.IntegerField(null=False, default=0)
#    x1065X0011BillPrintTRsP4 = models.IntegerField(null=False, default=0)
#    x1065X0012AssembleP4 = models.IntegerField(null=False, default=0)
#    x1065X0013WaitingforSignatureP4 = models.IntegerField(null=False, default=0)
#    x1065X0014CloseOutTaxReturnP4 = models.IntegerField(null=False, default=0)
#    x1065X0015ENDP4 = models.IntegerField(null=False, default=0)
#    START = models.IntegerField(null=False, default=0)
#    x1065X0001IntakeProcess = models.IntegerField(null=False, default=0)
#    x1065X0002PrintPBCFinancialStatementsforBKTRRVW = models.IntegerField(null=False, default=0)
#    x1065X0003BookkeepingReviewTR = models.IntegerField(null=False, default=0)
#    x1065X0004FinalReviewofBKWPS = models.IntegerField(null=False, default=0)
#    x1065X0005ClearReviewPointsforBK = models.IntegerField(null=False, default=0)
 #   x1065X0006InputPrep = models.IntegerField(null=False, default=0)
 #   x1065X0007Review = models.IntegerField(null=False, default=0)
 #   x1065X0008ClearReviewPointsForTR = models.IntegerField(null=False, default=0)
 #   x1065X0009FinalReview = models.IntegerField(null=False, default=0)
 #   x1065X0010PartnerSignoff = models.IntegerField(null=False, default=0)
 #   x1065X0011BillPrintTRs = models.IntegerField(null=False, default=0)
  #  x1065X0012Assemble = models.IntegerField(null=False, default=0)
  #  x1065X0013WaitingforSignature = models.IntegerField(null=False, default=0)
  #  x1065X0014CloseOutTaxReturn = models.IntegerField(null=False, default=0)
  #  x1065X0015END = models.IntegerField(null=False, default=0)
  #  TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
  #  TotalDaysPerStage = models.IntegerField(null=False, default=0)
  #  TurnAroundTime  = models.IntegerField(null=False, default=0)

 #   def __str__(self):
 #       return self.name


#class Category706estate(SoftDeletableModel, TimeStampedModel):
#    category706estate_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline706estate(SoftDeletableModel, TimeStampedModel):
 #   pipeline706estate_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage706estate(models.Model):
#    stage706estate_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel706estate(models.Model):
#    usermodel706estate_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project706estate(SoftDeletableModel, TimeStampedModel):
#    project706estate_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel706estate, to_field='usermodel706estate_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline706estate, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage706estate, to_field='stage706estate_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category706estate, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
 #   dateprojcounter = models.IntegerField(null=False, default=0)
 #   hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    STARTP4 = models.IntegerField(null=False, default=0)
#    e7060001ProformadP4 = models.IntegerField(null=False, default=0)
#    e7060002IntakeProcessP4 = models.IntegerField(null=False, default=0)
#    e7060003BookkeepingReviewTRP4 = models.IntegerField(null=False, default=0)
#    e7060004FinalReviewofBKWPSP4 = models.IntegerField(null=False, default=0)
#    e7060005ClearReviewPointsforBKP4 = models.IntegerField(null=False, default=0)
 #   e7060006InputPrepP4 = models.IntegerField(null=False, default=0)
#    e7060007ReviewP4 = models.IntegerField(null=False, default=0)
#    e7060008ClearReviewPointsForTRP4 = models.IntegerField(null=False, default=0)
#    e7060009FinalReviewP4 = models.IntegerField(null=False, default=0)
#    e7060010PartnerSignoffP4 = models.IntegerField(null=False, default=0)
#    e7060011BillPrintTRsP4 = models.IntegerField(null=False, default=0)
#    e7060012AssembleP4 = models.IntegerField(null=False, default=0)
#    e7060013WaitingforSignatureP4 = models.IntegerField(null=False, default=0)
#    e7060014CloseOutTaxReturnP4 = models.IntegerField(null=False, default=0)
#    ENDP4 = models.IntegerField(null=False, default=0)
#    START = models.IntegerField(null=False, default=0)
#    e7060001Proformad = models.IntegerField(null=False, default=0)
#    e7060002IntakeProcess = models.IntegerField(null=False, default=0)
#    e7060003BookkeepingReviewTR = models.IntegerField(null=False, default=0)
#    e7060004FinalReviewofBKWPS = models.IntegerField(null=False, default=0)
#    e7060005ClearReviewPointsforBK = models.IntegerField(null=False, default=0)
#    e7060006InputPrep = models.IntegerField(null=False, default=0)
#    e7060007Review = models.IntegerField(null=False, default=0)
#    e7060008ClearReviewPointsForTR = models.IntegerField(null=False, default=0)
#    e7060009FinalReview = models.IntegerField(null=False, default=0)
 #   e7060010PartnerSignoff = models.IntegerField(null=False, default=0)
#    e7060011BillPrintTRs = models.IntegerField(null=False, default=0)
#    e7060012Assemble = models.IntegerField(null=False, default=0)
 #3   e7060013WaitingforSignature = models.IntegerField(null=False, default=0)
#    e7060014CloseOutTaxReturn = models.IntegerField(null=False, default=0)
#    END = models.IntegerField(null=False, default=0)
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)

#    def __str__(self):
#        return self.name

    
      
#class Category1099misc(SoftDeletableModel, TimeStampedModel):
#    category1099misc_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline1099misc(SoftDeletableModel, TimeStampedModel):
#    pipeline1099misc_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

class Stage1099misc(models.Model):
    stage1099misc_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#User Model 
#class UserModel1099misc(models.Model):
#    usermodel1099misc_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)
#
#    def __str__(self):
#        return self.name


class Project1099misc(SoftDeletableModel, TimeStampedModel):
    project1099misc_id = models.IntegerField()
    name = models.CharField(max_length=250)
    starteddate = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    project_status = models.CharField(max_length=250)
    #user_responsible = models.ForeignKey(UserModel1099misc, to_field='usermodel1099misc_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #pipeline = models.ForeignKey(Pipeline1099misc, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stage1099misc, to_field='stage1099misc_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
    #category = models.ForeignKey(
    #    Category1099misc, on_delete=models.SET_NULL, null=True)
    woi = models.BooleanField(null=True, default=list)
    projprofilefilter = models.BooleanField(null=True, default=list)
    proname = models.BooleanField(null=True, default=list)
    allprojectcustomfieldsOOI = JSONField()
    dateprojcounter = models.IntegerField(null=False, default=0)
    hitlist = models.BooleanField(null=True, default=list)
    projintakes = models.BooleanField(null=True, default=list)
    projectstatuscancelled = models.BooleanField(null=True, default=list)
    projectstatuscompleted = models.BooleanField(null=True, default=list)
    projectstatusinprogress = models.BooleanField(null=True, default=list)
    ProformadIntakes1099Prep0001P4 = models.IntegerField(null=False, default=0)
    GatherData1099Prep0002P4 = models.IntegerField(null=False, default=0)
    Review1099Prep0003P4 = models.IntegerField(null=False, default=0)
    CLRRVWPTS1099Prep0004P4 = models.IntegerField(null=False, default=0)
    Finalize1stReview1099Prep0005P4 = models.IntegerField(null=False, default=0)
    InputtoSoftware1099Prep0006P4 = models.IntegerField(null=False, default=0)
    ClientApproval1099Prep0007P4 = models.IntegerField(null=False, default=0)
    Deliver1099Prep0008P4 = models.IntegerField(null=False, default=0)
    EFileCloseout1099Prep0009P4 = models.IntegerField(null=False, default=0)
    FeeAnalysis1099Prep0010P4 = models.IntegerField(null=False, default=0)
    Rollover1099Prep0011P4 = models.IntegerField(null=False, default=0)
    ProformadIntakes1099Prep0001 = models.IntegerField(null=False, default=0)
    GatherData1099Prep0002 = models.IntegerField(null=False, default=0)
    Review1099Prep0003 = models.IntegerField(null=False, default=0)
    CLRRVWPTS1099Prep0004 = models.IntegerField(null=False, default=0)
    Finalize1stReview1099Prep0005 = models.IntegerField(null=False, default=0)
    InputtoSoftware1099Prep0006 = models.IntegerField(null=False, default=0)
    ClientApproval1099Prep0007 = models.IntegerField(null=False, default=0)
    Deliver1099Prep0008 = models.IntegerField(null=False, default=0)
    EFileCloseout1099Prep0009 = models.IntegerField(null=False, default=0)
    FeeAnalysis1099Prep0010 = models.IntegerField(null=False, default=0)
    Rollover1099Prep0011 = models.IntegerField(null=False, default=0)
    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
    TotalDaysPerStage = models.IntegerField(null=False, default=0)
    TurnAroundTime  = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

#class Category1120(SoftDeletableModel, TimeStampedModel):
#    category1120_id = models.IntegerField()
#    name = models.CharField(max_length=250)#
#
#    def __str__(self):
#        return self.name


#class Pipeline1120(SoftDeletableModel, TimeStampedModel):
#    pipeline1120_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1120(models.Model):
#    stage1120_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1120(models.Model):
#    usermodel1120_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)#

#    def __str__(self):
#        return self.name


#class Project1120(SoftDeletableModel, TimeStampedModel):
#    project1120_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
 #   user_responsible = models.ForeignKey(UserModel1120, to_field='usermodel1120_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
 #   pipeline = models.ForeignKey(Pipeline1120, on_delete=models.SET_NULL, null=True)
 #   stage = models.ForeignKey(Stage1120, to_field='stage1120_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1120, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    Proformad11200001P4 = models.IntegerField(null=False, default=0)
#    intakes11200002P4 = models.IntegerField(null=False, default=0)
 #   BKPNGRevTRPrintRevPreCompile113P4 = models.IntegerField(null=False, default=0)
#    FinalReviewofBKWPS11200004P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBk11200005P4 = models.IntegerField(null=False, default=0)
#    InputPrep11200006P4 = models.IntegerField(null=False, default=0)
 #   Waitingonk111200007P4 = models.IntegerField(null=False, default=0)
#    Review11200008P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPoints11200009P4 = models.IntegerField(null=False, default=0)
#    Finalize1stReview11200010P4 = models.IntegerField(null=False, default=0)
#    FinalReview11200011P4 = models.IntegerField(null=False, default=0)
#    PartnerSignoff11200012P4 = models.IntegerField(null=False, default=0)
#    BillPrintAssembly11200013P4 = models.IntegerField(null=False, default=0)
#    WaitingforClientSignature11200014P4 = models.IntegerField(null=False, default=0)
#    CloseOutTaxReturn11200015P4 = models.IntegerField(null=False, default=0)
 #   FeeAnalysis11200016P4 = models.IntegerField(null=False, default=0)
 #   Rollover11200017P4 = models.IntegerField(null=False, default=0)
#    Proformad11200001 = models.IntegerField(null=False, default=0)
#    intakes11200002 = models.IntegerField(null=False, default=0)
#    BKPNGRevTRPrintRevPreCompile113 = models.IntegerField(null=False, default=0)
#    FinalReviewofBKWPS11200004 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBk11200005 = models.IntegerField(null=False, default=0)
#    InputPrep11200006 = models.IntegerField(null=False, default=0)
#    Waitingonk111200007 = models.IntegerField(null=False, default=0)
#    Review11200008 = models.IntegerField(null=False, default=0)
 #   ClearReviewPoints11200009 = models.IntegerField(null=False, default=0)
 #   Finalize1stReview11200010 = models.IntegerField(null=False, default=0)
 #   FinalReview11200011 = models.IntegerField(null=False, default=0)
 #   PartnerSignoff11200012 = models.IntegerField(null=False, default=0)
 #   BillPrintAssembly11200013 = models.IntegerField(null=False, default=0)
 #   WaitingforClientSignature11200014 = models.IntegerField(null=False, default=0)
 #   CloseOutTaxReturn11200015 = models.IntegerField(null=False, default=0)
 #   FeeAnalysis11200016 = models.IntegerField(null=False, default=0)
 #   Rollover11200017 = models.IntegerField(null=False, default=0)
  #  TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
  #  TotalDaysPerStage = models.IntegerField(null=False, default=0)
  #  TurnAroundTime  = models.IntegerField(null=False, default=0)

  #  def __str__(self):
  #      return self.name

    
#class Category1120S(SoftDeletableModel, TimeStampedModel):
#    category1120s_id = models.IntegerField()
#    name = models.CharField(max_length=250)###

#    def __str__(self):
#        return self.name


#class Pipeline1120S(SoftDeletableModel, TimeStampedModel):
#    pipeline1120s_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1120S(models.Model):
#    stage1120s_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)
#
#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1120S(models.Model):
#    usermodel1120s_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project1120S(SoftDeletableModel, TimeStampedModel):
#    project1120s_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1120S, to_field='usermodel1120s_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1120S, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1120S, to_field='stage1120s_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
 #       Category1120S, on_delete=models.SET_NULL, null=True)
 #   woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
 #   projectstatuscancelled = models.BooleanField(null=True, default=list)
 #   projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    Proformad1120s0001P4 = models.IntegerField(null=False, default=0)
#    Intakes1120s0002P4 = models.IntegerField(null=False, default=0)
#    BKKPNGRevTRPrintRevPreComp3P4 = models.IntegerField(null=False, default=0)
 #   FinalReviewofBKWPS1120s0004P4 = models.IntegerField(null=False, default=0)
 #   ClearReviewPointsforBk1120s0005P4 = models.IntegerField(null=False, default=0)
 #   InputPrep1120s0006P4 = models.IntegerField(null=False, default=0)
 #   Waitingonk11120s0007P4 = models.IntegerField(null=False, default=0)
 #   Review1120s0008P4 = models.IntegerField(null=False, default=0)
 #   ClearReviewPoints1120s0009P4 = models.IntegerField(null=False, default=0)
 #   Finalize1stReview1120s0010P4 = models.IntegerField(null=False, default=0)
 #   FinalReview1120s0011P4 = models.IntegerField(null=False, default=0)
 #   PartnerSignoff1120s0012P4 = models.IntegerField(null=False, default=0)
 #   BillPrintAssembly1120s0013P4 = models.IntegerField(null=False, default=0)
 #   WaitingforClientSignature1120s0014P4 = models.IntegerField(null=False, default=0)
 #   CloseOutTaxReturn1120s0015P4 = models.IntegerField(null=False, default=0)
 #   FeeAnalysis1120s0016P4 = models.IntegerField(null=False, default=0)
 #   RolloverProcess1120s0017P4 = models.IntegerField(null=False, default=0)
 #   Proformad1120s0001 = models.IntegerField(null=False, default=0)
 #   Intakes1120s0002 = models.IntegerField(null=False, default=0)
  #  BKKPNGRevTRPrintRevPreComp3 = models.IntegerField(null=False, default=0)
 #   FinalReviewofBKWPS1120s0004 = models.IntegerField(null=False, default=0)
 #   ClearReviewPointsforBk1120s0005 = models.IntegerField(null=False, default=0)
 #   InputPrep1120s0006 = models.IntegerField(null=False, default=0)
 #   Waitingonk11120s0007 = models.IntegerField(null=False, default=0)
  #  Review1120s0008 = models.IntegerField(null=False, default=0)
  #  ClearReviewPoints1120s0009 = models.IntegerField(null=False, default=0)
  #  Finalize1stReview1120s0010 = models.IntegerField(null=False, default=0)
   ## FinalReview1120s0011 = models.IntegerField(null=False, default=0)
   # PartnerSignoff1120s0012 = models.IntegerField(null=False, default=0)
   # BillPrintAssembly1120s0013 = models.IntegerField(null=False, default=0)
    #WaitingforClientSignature1120s0014 = models.IntegerField(null=False, default=0)
    #CloseOutTaxReturn1120s0015 = models.IntegerField(null=False, default=0)
    #FeeAnalysis1120s0016 = models.IntegerField(null=False, default=0)
    #RolloverProcess1120s0017 = models.IntegerField(null=False, default=0)
    #TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
    #TotalDaysPerStage = models.IntegerField(null=False, default=0)
    #TurnAroundTime  = models.IntegerField(null=False, default=0)

    #def __str__(self):
     #   return self.name

#class Category1120X(SoftDeletableModel, TimeStampedModel):
#    category1120x_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#
#    def __str__(self):
#        return self.name


#class Pipeline1120X(SoftDeletableModel, TimeStampedModel):
#    pipeline1120x_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1120X(models.Model):
#    stage1120x_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)#

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1120X(models.Model):
#    usermodel1120x_id = models.PositiveIntegerField(unique=True, primary_key=True)
 #   name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project1120X(SoftDeletableModel, TimeStampedModel):
#    project1120x_id = models.IntegerField()
#    name = models.CharField(max_length=250)
 #   starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1120X, to_field='usermodel1120x_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1120X, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1120X, to_field='stage1120x_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1120X, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    xSTART = models.IntegerField(null=False, default=0)
#    x1120X0001IntakeProcess = models.IntegerField(null=False, default=0)
#    x1120X0002PrintPBCFinancialStatementsforBKTRRVW = models.IntegerField(null=False, default=0)
#    x1120X0003BookkeepingReviewTR = models.IntegerField(null=False, default=0)
#    x1120X0004FinalReviewofBKWPS = models.IntegerField(null=False, default=0)
##    x1120X0005ClearReviewPointsforBK = models.IntegerField(null=False, default=0)
#    x1120X0006InputPrep = models.IntegerField(null=False, default=0)
#    x1120X0007Review = models.IntegerField(null=False, default=0)
#    x1120X0008ClearReviewPointsForTR = models.IntegerField(null=False, default=0)
#    x1120X0009FinalReview = models.IntegerField(null=False, default=0)
 #   x1120X0010PartnerSignoff = models.IntegerField(null=False, default=0)
#    x1120X0011BillPrintTRs = models.IntegerField(null=False, default=0)
#    x1120X0012Assemble = models.IntegerField(null=False, default=0)
 #   x1120X0013WaitingforSignature = models.IntegerField(null=False, default=0)
#    x1120X0014CloseOutTaxReturn = models.IntegerField(null=False, default=0)
#    x1120X0015END = models.IntegerField(null=False, default=0)  
##    xSTARTP4 = models.IntegerField(null=False, default=0)
#    x1120X0001IntakeProcessP4 = models.IntegerField(null=False, default=0)
#    x1120X0002PrintPBCFinancialStatementsforBKTRRVWP4 = models.IntegerField(null=False, default=0)
#    x1120X0003BookkeepingReviewTRP4 = models.IntegerField(null=False, default=0)
#    x1120X0004FinalReviewofBKWPSP4 = models.IntegerField(null=False, default=0)
#    x1120X0005ClearReviewPointsforBKP4 = models.IntegerField(null=False, default=0)
#    x1120X0006InputPrepP4 = models.IntegerField(null=False, default=0)
#    x1120X0007ReviewP4 = models.IntegerField(null=False, default=0)
#    x1120X0008ClearReviewPointsForTRP4 = models.IntegerField(null=False, default=0)
#    x1120X0009FinalReviewP4 = models.IntegerField(null=False, default=0)
#    x1120X0010PartnerSignoffP4 = models.IntegerField(null=False, default=0)
#    x1120X0011BillPrintTRsP4 = models.IntegerField(null=False, default=0)
#    x1120X0012AssembleP4 = models.IntegerField(null=False, default=0)
#    x1120X0013WaitingforSignatureP4 = models.IntegerField(null=False, default=0)
#    x1120X0014CloseOutTaxReturnP4 = models.IntegerField(null=False, default=0)
#    x1120X0015ENDP4 = models.IntegerField(null=False, default=0)  
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)

#    def __str__(self):
 #       return self.name


#class Category1120SX(SoftDeletableModel, TimeStampedModel):
#    category1120sx_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline1120SX(SoftDeletableModel, TimeStampedModel):
#    pipeline1120sx_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage1120SX(models.Model):
#    stage1120sx_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1120SX(models.Model):
#    usermodel1120sx_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

 #   def __str__(self):
 #       return self.name


#class Project1120SX(SoftDeletableModel, TimeStampedModel):
#    project1120sx_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel1120SX, to_field='usermodel1120sx_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1120SX, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1120SX, to_field='stage1120sx_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1120SX, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
 #   STARTP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0001IntakeProcessP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0002PrintPBCFinancialStatementsforBKTRRVWP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0003BookkeepingReviewTRP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0004FinalReviewofBKWPSP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0005ClearReviewPointsforBKP4 = models.IntegerField(null=False, default=0)
#    sx1120SX0006InputPrepP4 = models.IntegerField(null=False, default=0)
#    sx1120SX0007ReviewP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0008ClearReviewPointsForTRP4 = models.IntegerField(null=False, default=0)
#    sx1120SX0009FinalReviewP4 = models.IntegerField(null=False, default=0)
#    sx1120SX0010PartnerSignoffP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0011BillPrintTRsP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0012AssembleP4 = models.IntegerField(null=False, default=0)
 #   sx120SX0013WaitingforSignatureP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0014CloseOutTaxReturnP4 = models.IntegerField(null=False, default=0)
 #   sx1120SX0014ENDP4 = models.IntegerField(null=False, default=0)
 #   START = models.IntegerField(null=False, default=0)
 #   sx1120SX0001IntakeProcess = models.IntegerField(null=False, default=0)
 #   sx1120SX0002PrintPBCFinancialStatementsforBKTRRVW = models.IntegerField(null=False, default=0)
 #   sx1120SX0003BookkeepingReviewTR = models.IntegerField(null=False, default=0)
 #   sx1120SX0004FinalReviewofBKWPS = models.IntegerField(null=False, default=0)
 #   sx1120SX0005ClearReviewPointsforBK = models.IntegerField(null=False, default=0)
 #   sx1120SX0006InputPrep = models.IntegerField(null=False, default=0)
 #   sx1120SX0007Review = models.IntegerField(null=False, default=0)
 #   sx1120SX0008ClearReviewPointsForTR = models.IntegerField(null=False, default=0)
 #   sx1120SX0009FinalReview = models.IntegerField(null=False, default=0)
 #   sx1120SX0010PartnerSignoff = models.IntegerField(null=False, default=0)
 #   sx1120SX0011BillPrintTRs = models.IntegerField(null=False, default=0)
 #   sx1120SX0012Assemble = models.IntegerField(null=False, default=0)
 #   sx120SX0013WaitingforSignature = models.IntegerField(null=False, default=0)
 #   sx1120SX0014CloseOutTaxReturn = models.IntegerField(null=False, default=0)
  #  sx1120SX0014END = models.IntegerField(null=False, default=0)
 #   TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
 #   TotalDaysPerStage = models.IntegerField(null=False, default=0)
  #  TurnAroundTime  = models.IntegerField(null=False, default=0)

 #   def __str__(self):
 #       return self.name

#class Category1120(SoftDeletableModel, TimeStampedModel):
#    category1120_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline1120(SoftDeletableModel, TimeStampedModel):
#    pipeline1120_id = models.IntegerField()
#    name = models.CharField(max_length=250)#

#    def __str__(self):
#        return self.name

#class Stage1120(models.Model):
#    stage1120_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel1120(models.Model):
#    usermodel1120_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project1120(SoftDeletableModel, TimeStampedModel):
#    project1120_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
 #   user_responsible = models.ForeignKey(UserModel1120, to_field='usermodel1120_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline1120, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage1120, to_field='stage1120_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category1120, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
 #   Proformad11200001P4 = models.IntegerField(null=False, default=0)
#    intakes11200002P4 = models.IntegerField(null=False, default=0)
#    BookkeepingReviewforTaxReturnPrintReviewPrepareCompile11200003P4 = models.IntegerField(null=False, default=0)
#    FinalReviewofBKWPS11200004P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBk11200005P4 = models.IntegerField(null=False, default=0)
#    InputPrep11200006P4 = models.IntegerField(null=False, default=0)
#    Waitingonk111200007P4 = models.IntegerField(null=False, default=0)
#    Review11200008P4 = models.IntegerField(null=False, default=0)
#    ClearReviewPoints11200009P4 = models.IntegerField(null=False, default=0)
#    Finalize1stReview11200010P4 = models.IntegerField(null=False, default=0)
#    FinalReview11200011P4 = models.IntegerField(null=False, default=0)
#    PartnerSignoff11200012P4 = models.IntegerField(null=False, default=0)
#    BillPrintAssembly11200013P4 = models.IntegerField(null=False, default=0)
#    WaitingforClientSignature11200014P4 = models.IntegerField(null=False, default=0)
#    CloseOutTaxReturn11200015P4 = models.IntegerField(null=False, default=0)
#    FeeAnalysis11200016P4 = models.IntegerField(null=False, default=0)
#    Rollover11200017P4 = models.IntegerField(null=False, default=0)
#    Proformad11200001 = models.IntegerField(null=False, default=0)
#    intakes11200002 = models.IntegerField(null=False, default=0)
#    BookkeepingReviewforTaxReturnPrintReviewPrepareCompile11200003 = models.IntegerField(null=False, default=0)
#    FinalReviewofBKWPS11200004 = models.IntegerField(null=False, default=0)
#    ClearReviewPointsforBk11200005 = models.IntegerField(null=False, default=0)
#    InputPrep11200006 = models.IntegerField(null=False, default=0)
#    Waitingonk111200007 = models.IntegerField(null=False, default=0)
#    Review11200008 = models.IntegerField(null=False, default=0)
#    ClearReviewPoints11200009 = models.IntegerField(null=False, default=0)
#    Finalize1stReview11200010 = models.IntegerField(null=False, default=0)
#    FinalReview11200011 = models.IntegerField(null=False, default=0)
#    PartnerSignoff11200012 = models.IntegerField(null=False, default=0)
#    BillPrintAssembly11200013 = models.IntegerField(null=False, default=0)
#    WaitingforClientSignature11200014 = models.IntegerField(null=False, default=0)
#    CloseOutTaxReturn11200015 = models.IntegerField(null=False, default=0)
#    FeeAnalysis11200016 = models.IntegerField(null=False, default=0)
#    Rollover11200017 = models.IntegerField(null=False, default=0)    
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)

#    def __str__(self):
#        return self.name

#class Category709gift(SoftDeletableModel, TimeStampedModel):
#    category709gift_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name


#class Pipeline709gift(SoftDeletableModel, TimeStampedModel):
#    pipeline709gift_id = models.IntegerField()
#    name = models.CharField(max_length=250)

#    def __str__(self):
#        return self.name

#class Stage709gift(models.Model):
#    stage709gift_id = models.PositiveIntegerField(unique=True, primary_key=True)
    #pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
 #   name = models.CharField(max_length=250)#

#    def __str__(self):
#        return self.name

#User Model 
#class UserModel709gift(models.Model):
#    usermodel709gift_id = models.PositiveIntegerField(unique=True, primary_key=True)
#    name = models.CharField(max_length=256)

#    def __str__(self):
#        return self.name


#class Project709gift(SoftDeletableModel, TimeStampedModel):
#    project709gift_id = models.IntegerField()
#    name = models.CharField(max_length=250)
#    starteddate = models.DateTimeField(null=True, blank=True)
#    datecompleted = models.DateTimeField(null=True, blank=True)
#    project_status = models.CharField(max_length=250)
#    user_responsible = models.ForeignKey(UserModel709gift, to_field='usermodel709gift_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    pipeline = models.ForeignKey(Pipeline709gift, on_delete=models.SET_NULL, null=True)
#    stage = models.ForeignKey(Stage709gift, to_field='stage709gift_id', on_delete=models.CASCADE, null=True, blank=True, unique=False)
#    category = models.ForeignKey(
#        Category709gift, on_delete=models.SET_NULL, null=True)
#    woi = models.BooleanField(null=True, default=list)
#    projprofilefilter = models.BooleanField(null=True, default=list)
#    proname = models.BooleanField(null=True, default=list)
#    allprojectcustomfieldsOOI = JSONField()
#    dateprojcounter = models.IntegerField(null=False, default=0)
#    hitlist = models.BooleanField(null=True, default=list)
#    projintakes = models.BooleanField(null=True, default=list)
#    projectstatuscancelled = models.BooleanField(null=True, default=list)
#    projectstatuscompleted = models.BooleanField(null=True, default=list)
#    projectstatusinprogress = models.BooleanField(null=True, default=list)
#    STARTP4 = models.IntegerField(null=False, default=0)
#    g7090001ProformadP4 = models.IntegerField(null=False, default=0)
#    g7090002IntakeProcessP4 = models.IntegerField(null=False, default=0)
#    g7090003BookkeepingReviewTRP4 = models.IntegerField(null=False, default=0)
#    g7090004FinalReviewofBKWPSP4 = models.IntegerField(null=False, default=0)
#    g7090005ClearReviewPointsforBKP4 = models.IntegerField(null=False, default=0)
#    g7090006InputPrepP4 = models.IntegerField(null=False, default=0)
#    g7090007ReviewP4 = models.IntegerField(null=False, default=0)
#    g7090008ClearReviewPointsForTRP4 = models.IntegerField(null=False, default=0)
#    g7090009FinalReviewP4 = models.IntegerField(null=False, default=0)
#    g7090010PartnerSignoffP4 = models.IntegerField(null=False, default=0)
 #   g7090011BillPrintTRsP4 = models.IntegerField(null=False, default=0)
#    g7090012AssembleP4 = models.IntegerField(null=False, default=0)
#    g7090013WaitingforSignatureP4 = models.IntegerField(null=False, default=0)
#    g7090014CloseOutTaxReturnP4 = models.IntegerField(null=False, default=0)
#    ENDP4 = models.IntegerField(null=False, default=0)
#    START = models.IntegerField(null=False, default=0)
#    g7090001Proformad = models.IntegerField(null=False, default=0)
#    g7090002IntakeProcess = models.IntegerField(null=False, default=0)
#    g7090003BookkeepingReviewTR = models.IntegerField(null=False, default=0)
#    g7090004FinalReviewofBKWPS = models.IntegerField(null=False, default=0)
#    g7090005ClearReviewPointsforBK = models.IntegerField(null=False, default=0)
#    g7090006InputPrep = models.IntegerField(null=False, default=0)
#    g7090007Review = models.IntegerField(null=False, default=0)
#    g7090008ClearReviewPointsForTR = models.IntegerField(null=False, default=0)
#    g7090009FinalReview = models.IntegerField(null=False, default=0)
#    g7090010PartnerSignoff = models.IntegerField(null=False, default=0)
#    g7090011BillPrintTRs = models.IntegerField(null=False, default=0)
#    g7090012Assemble = models.IntegerField(null=False, default=0)
#    g7090013WaitingforSignature = models.IntegerField(null=False, default=0)
#    g7090014CloseOutTaxReturn = models.IntegerField(null=False, default=0)
#    END = models.IntegerField(null=False, default=0)
#    TotalP4DaysPerStage = models.IntegerField(null=False, default=0)
#    TotalDaysPerStage = models.IntegerField(null=False, default=0)
#    TurnAroundTime  = models.IntegerField(null=False, default=0)

#    def __str__(self):
#        return self.name






