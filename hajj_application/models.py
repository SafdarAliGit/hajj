


from django.db import models

from hajj import settings


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

STAY_DURATION = (
    ('None', '--------'),
    ('Long', 'Long'),
    ('Short', 'Short'),
)
BLOOD_GROUP = (
    ('None', '--------'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)
GENDER = (
    ('None', '--------'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

FIQAH = (
    ('None', '--------'),
    ('Hanafi', 'Hanafi'),
    ('Maliki', 'Maliki'),
    ('Shafi', 'Shafi'),
    ('Hanbali', 'Hanbali'),
    ('Jafari', 'Jafari'),
)
MARRIED= (
    ('None', '--------'),
    ('Yes', 'Yes'),
    ('No', 'No'),
)
PERFORMED_HAJJ_IN_LAST_5_YEARS = (
    ('None', '--------'),
    ('Yes', 'Yes'),
    ('No', 'No'),
)
WANT_TO_PERFORM_HAJJ_E_BADAL = (
    ('None', '--------'),
    ('Yes', 'Yes'),
    ('No', 'No'),
)
WANT_TO_PERFORM_HAJJ_AS_GROUP_WORKER = (
    ('None', '--------'),
    ('Yes', 'Yes'),
    ('No', 'No'),
)
ARE_YOUR_MEHRAM = (
    ('None', '--------'),
    ('Yes', 'Yes'),
    ('No', 'No'),
)


class HajjApplication(TimeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='photo/', null=True, blank=True, verbose_name='Photo')
    hajj_application_no = models.CharField(max_length=20, null=True, verbose_name='Hajj Application No')
    enrollment_no = models.CharField(max_length=20, null=True, verbose_name='Enrollment No')
    group_coordinator_application_no = models.CharField(max_length=20, null=True, verbose_name='Group Coordinator\'s Application No')
    hgo_no = models.CharField(max_length=20, null=True, verbose_name='HGO No')
    stay_duration = models.CharField(max_length=10, null=False, verbose_name='Stay Duration', choices=STAY_DURATION, default=None)
    substituted_against_application_no = models.CharField(max_length=20, null=True, verbose_name="Subsitituted Against Application No")
    name_of_applicant_as_per_passport = models.CharField(max_length=50, null=True, verbose_name='Name of Applicant as per passport')
    sur_name = models.CharField(max_length=50, null=True, verbose_name='Sur Name')
    given_name = models.CharField(max_length=50, null=True, verbose_name='Given Name')
    father_husband_name = models.CharField(max_length=50, null=True, verbose_name='Father/ Husband name')
    passport_no = models.CharField(max_length=50, null=True, verbose_name='Passport No')
    date_of_expiry = models.DateField(null=True, verbose_name='Date of Expiry')
    date_of_birth = models.DateField(null=True, verbose_name='Date of Birth')
    nadra_id_card_no = models.CharField(max_length=50, null=True, verbose_name='NADRA ID Card No')
    blood_group = models.CharField(max_length=10, null=False, verbose_name='Blood Group',choices=BLOOD_GROUP, default=None)
    gender = models.CharField(max_length=10, null=False, verbose_name='Gender', choices=GENDER, default=None)
    fiqah = models.CharField(max_length=10, null=False, verbose_name='Fiqah', choices=FIQAH, default=None)
    are_you_married = models.CharField(max_length=5, null=False, verbose_name='Are You Married', choices=MARRIED, default=None)
    present_postal_address = models.TextField(null=True, verbose_name='Present Postal Address')
    tehsil_code = models.CharField(max_length=20, null=True, verbose_name='Tehsil Code')
    mobile_no = models.CharField(max_length=20, null=True, verbose_name='Mobile No')
    telephone_no = models.CharField(max_length=20, null=True, verbose_name='Telephone No')
    performed_hajj_in_last_five_years = models.CharField(max_length=5, null=True, verbose_name='Performed Hajj in Last five years', choices=PERFORMED_HAJJ_IN_LAST_5_YEARS, default=None)
    want_to_perform_hajj_e_badal = models.CharField(max_length=5, null=False, verbose_name='Want to perform Hajj-e-Badal', choices=WANT_TO_PERFORM_HAJJ_E_BADAL, default=None)
    want_to_perform_hajj_as_group_worker = models.CharField(max_length=5, null=True, verbose_name='Want to perform Hajj as gorup worker', choices=WANT_TO_PERFORM_HAJJ_AS_GROUP_WORKER, default=None)
    are_you_mehram_of_a_lady = models.CharField(max_length=5, null=False, verbose_name='Are you mehram of a lady', choices=ARE_YOUR_MEHRAM, default=None)
    cnic_no_of_lady = models.CharField(max_length=20, null=True, verbose_name='CNIC No of Lady who have not performed Hajj in last five years')
    nominee_name = models.CharField(max_length=50, null=True, verbose_name='Name')
    relationship_with_nominee = models.CharField(max_length=50, null=True, verbose_name='Relationship')
    nominee_cnic_no = models.CharField(max_length=20, null=True, verbose_name='CNIC No')
    nominee_mobile_no = models.CharField(max_length=20, null=True, verbose_name='Mobile No')
    nominee_telephone_no = models.CharField(max_length=20, null=True, verbose_name='Telephone No')
    emergency_name_of_person = models.CharField(max_length=50, null=True, verbose_name='Name of person')
    emergency_relationship = models.CharField(max_length=50, null=True, verbose_name='Relationship')
    emergency_cell_no = models.CharField(max_length=20, null=True, verbose_name='Cell No')
    mehram_application_no = models.CharField(max_length=20, null=True, verbose_name='Application No')
    mehram_code = models.CharField(max_length=20, null=True, verbose_name='Code')
    mehram_relationship = models.CharField(max_length=20, null=True, verbose_name='Relationship')



    def __str__(self):
        return str(self.hajj_application_no)

