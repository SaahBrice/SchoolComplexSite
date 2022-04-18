from blog.models import Admission,Teacher_applications, Sitemessages, article, Schoolinfos, Form1_applications, Form2_4_applications, Lowersixth_applications, Class1_applications, Class2_6_applications, Nursery_applications



def sitemessages(request):
    sitemessages =Sitemessages.objects.all()
    schoolinfos = Schoolinfos.objects.get(pk=1)
    new_admission = Admission.objects.get(pk=1)

    teacher1s = len(Teacher_applications.objects.filter(Approved = False))
    forms = len(Form1_applications.objects.filter(Approved = False)) + len(Form2_4_applications.objects.filter(Approved = False)) + len(Lowersixth_applications.objects.filter(Approved = False)) + len(Class1_applications.objects.filter(Approved = False)) + len(Class2_6_applications.objects.filter(Approved = False)) + len(Nursery_applications.objects.filter(Approved = False))
    total = teacher1s + forms
    sitemessages =sitemessages[::-1]
    unread = len(Sitemessages.objects.filter(read=False))

    return  {
        'sitemessages':sitemessages,
        'unread':unread,
        'schoolinfos':schoolinfos,
        'new_admission': new_admission,
        'teacher1s': teacher1s,
        'forms': forms,
        'total': total,
    }
