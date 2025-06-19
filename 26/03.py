from docxtpl import DocxTemplate

def create_training_sheet(class_name: str, subject_name: str, tpl_name: str='tpl.docx', *tuples: tuple):
    document = DocxTemplate(tpl_name)
    context = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': sorted(list(map(lambda tpl: {'num': sorted(tuples).index(tpl) + 1, 'fio': tpl[0], 'mark': tpl[1]}, tuples)), key=lambda x: x['num'])
    }
    document.render(context)
    document.save('res.docx')
