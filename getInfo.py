import json
from js import subject, course, section, semester, college   

fpCourses = open('courses.json')
coursesDB = json.load(fpCourses)

fpPolicies = open('college_policies.json')
collegePoliciesDB = json.load(fpPolicies)

def createSLOList(slos):
    listHTML = "<ul>"
    for slo in slos:
        listHTML += "<li>"+slo+"</li>"
    listHTML+="</ul>"


    
def getCollegePolicies(policiesDB, college):
    collegePolicies = policiesDB.get(college).get('policies')
    output = ""
    for policy in collegePolicies:
        title = collegePolicies.get(policy).get('title')
        content = collegePolicies.get(policy).get('content')
        output += f"<h1>{title}</h1>"
        output += content
    return output
    
def getCoursePolicies(coursePoliciesDB, college):
    collegePolicies = policiesDB.get(college).get('policies')
    output = ""
    for policy in collegePolicies:
        title = collegePolicies.get(policy).get('title')
        content = collegePolicies.get(policy).get('content')
        output += f"<h1>{title}</h1>"
        output += content
    return output


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

### Calls the helper function createSLOList() to to add the HTML to the slo-list div.
Element('slo-list').element.innerHTML = createSLOList(courseSLOs)

### Gets college policies and prints them at the end of the syllabus
Element('college-policies').element.innerHTML = getCollegePolicies(collegePoliciesDB, college)