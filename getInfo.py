import json
from js import subject, course, section, semester    
fp = open('courses.json')
coursesDB = json.load(fp)

courseTitle = coursesDB.get(subject).get(course).get('title')
courseTitleComplete = str(subject+'-'+course+"-"+section+' '+semester)
courseCreditHours = coursesDB.get(subject).get(course).get('credit-hours')
courseClassHours = coursesDB.get(subject).get(course).get('class-hours')
courseLabHours = coursesDB.get(subject).get(course).get('lab-hours')
catalogDescription = coursesDB.get(subject).get(course).get('catalog-description')
courseSLOs = coursesDB.get(subject).get(course).get('slos')


Element('course-title').write(courseTitle)
Element('courseid-section-semester').write(courseTitleComplete)
Element('credit-hours').element.append(courseCreditHours)
Element('class-hours').element.append(courseClassHours)
Element('lab-hours').element.append(courseLabHours)
Element('catalog-description').write(catalogDescription)
for slo in courseSLOs:
    Element('slo-list').element.append('<li>{slo}</li>'.format(slo))
