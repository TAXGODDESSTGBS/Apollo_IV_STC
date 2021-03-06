# Generated by Django 3.1.7 on 2021-08-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insightly', '0037_auto_20210715_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0001SetupClientTasksP4',
            new_name='AssembleSTCCTC0009',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0001SetupClientTasksdays',
            new_name='AssembleSTCCTC0009P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0002AdminforCTCPlanPrepP4',
            new_name='CSFUPALLSTCCTC0011',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0002AdminforCTCPlanPrepdays',
            new_name='CSFUPALLSTCCTC0011P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0003CreateIdeasforClientP4',
            new_name='ClearReviewPointsSTCCTC0007',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0003CreateIdeasforClientdays',
            new_name='ClearReviewPointsSTCCTC0007P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject00051QAwiththeclientP4',
            new_name='CreateIdeasforClientSTCCTC0003',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject00051QAwiththeclientdays',
            new_name='CreateIdeasforClientSTCCTC0003P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0005InputPrepP4',
            new_name='FinalReviewSTCCTC0008',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0005InputPrepdays',
            new_name='FinalReviewSTCCTC0008P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0006ReviewProjectP4',
            new_name='InputPrepSTCCTC0004',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0006ReviewProjectdays',
            new_name='InputPrepSTCCTC0004P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0007CLRRVWPTSP4',
            new_name='IntakesSTCCTC0002',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0007CLRRVWPTSdays',
            new_name='IntakesSTCCTC0002P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0008FinalReviewP4',
            new_name='ProformadSTCCTC0001',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0008FinalReviewdays',
            new_name='ProformadSTCCTC0001P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0009AssembleCTCPlanP4',
            new_name='QAwithClientSTCCTC0005',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0009AssembleCTCPlandays',
            new_name='QAwithClientSTCCTC0005P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0011AdminWrapupP4',
            new_name='ReviewProjectSTCCTC0006',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='billableCTCSTCProject0011AdminWrapupdays',
            new_name='ReviewProjectSTCCTC0006P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='endP4',
            new_name='RolloverSTCCTC0013',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='enddays',
            new_name='RolloverSTCCTC0013P4',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='startDays',
            new_name='SalesFUPALLSTCCTC0012',
        ),
        migrations.RenameField(
            model_name='projectctcstcproject',
            old_name='startP4',
            new_name='SalesFUPALLSTCCTC0012P4',
        ),
        migrations.AddField(
            model_name='projectctcstcproject',
            name='WrapupSTCCTC0010',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectctcstcproject',
            name='WrapupSTCCTC0010P4',
            field=models.IntegerField(default=0),
        ),
    ]
