import json
subject = pyscript.interpreter.globals.get('subject')
course = pyscript.interpreter.globals.get('course')
section = pyscript.interpreter.globals.get('section')
school = pyscript.interpreter.globals.get('school')

fp = open('courses.json')
coursesDB = json.load(fp)
Element('course-title').write(coursesDB.get(subject).get(course).get('title'))
Element('credit-hours').element.append(coursesDB.get(subject).get(course).get('credit-hours'))
Element('class-hours').element.append(coursesDB.get(subject).get(course).get('class-hours'))
Element('lab-hours').element.append(coursesDB.get(subject).get(course).get('lab-hours'))
