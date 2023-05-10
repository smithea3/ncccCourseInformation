import json
from js import subject, course, section, semester    
fp = open('courses.json')
coursesDB = json.load(fp)

courseTitle = coursesDB.get(subject).get(course).get('title')
courseCreditHours = coursesDB.get(subject).get(course).get('credit-hours')
courseClassHours = coursesDB.get(subject).get(course).get('class-hours')
courseLabHours = coursesDB.get(subject).get(course).get('lab-hours')


Element('course-title').write(courseTitle)
Element('courseid-section-semester').write(courseTitle+"-"section+semester)
Element('credit-hours').element.append(courseCreditHours)
Element('class-hours').element.append(courseClassHours)
Element('lab-hours').element.append(courseLabHours)
