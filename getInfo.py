import json
from js import subject, course, section, semester, college   
fpCourses = open('courses.json')
coursesDB = json.load(fpCourses)

fpPolicies = open('college_policies.json')
collegePoliciesDB = json.load(fpPolicies)

collegeName = collegePoliciesDB.get(college).get('collegeName')

courseTitle = coursesDB.get(subject).get(course).get('title')
courseTitleComplete = str(subject+'-'+course+"-"+section+' '+semester)
courseCreditHours = coursesDB.get(subject).get(course).get('credit-hours')
courseClassHours = coursesDB.get(subject).get(course).get('class-hours')
courseLabHours = coursesDB.get(subject).get(course).get('lab-hours')
catalogDescription = coursesDB.get(subject).get(course).get('catalog-description')
courseSLOs = coursesDB.get(subject).get(course).get('slos')

### Writes the college's name into the 'collegeName' ID
Element('college-name').write(collegeName)

### Writes the course tite
Element('course-title').write(courseTitle)

### Writes the course information in the format AAA-###-AAAAA YYYYAA
Element('courseid-section-semester').write(courseTitleComplete)

### Appends the credit hours, class hours, and lab hours to their respective places
Element('credit-hours').element.append(courseCreditHours)
Element('class-hours').element.append(courseClassHours)
Element('lab-hours').element.append(courseLabHours)

### Writes the course catalog description to its respective place
Element('catalog-description').write(catalogDescription)

### Calls the helper function createList() to to add the HTML to the slo-list div.
Element('slo-list').element.innerHTML = createList(courseSLOs)

Element('college-policies').element.innerHTML = createList(getCollegePolicies(collegePoliciesDB))


def createList(x):
    output = "<ul>"
    for item in x:
        output += f"<li>{item}</li>"
    output += "</ul>"
    return output

def getCollegePolicies(policiesDB):
    collegePolicies = policiesDB.get('policies')
    output = ""
    for policy in policiesDB:
        title = policies.get('title')
        content = policies.get('content')
        output += f"<h1>{title}</h1>"
        output += content
    return output