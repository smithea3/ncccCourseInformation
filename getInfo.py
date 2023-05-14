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
def createList(x):
    output = "<ul>"
    for item in x:
        output += f"<li>{item}</li>"
    output += "</ul>"
    return output

Element('course-title').write(courseTitle)
Element('courseid-section-semester').write(courseTitleComplete)
Element('credit-hours').element.append(courseCreditHours)
Element('class-hours').element.append(courseClassHours)
Element('lab-hours').element.append(courseLabHours)
Element('catalog-description').write(catalogDescription)
Element('slo-list').element.innerHTML = createList(courseSLOs)
