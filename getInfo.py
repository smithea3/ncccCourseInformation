import json
subject = "MAT"; course = "171"; section = "00000"; school = "MitchellCC"
fp = open("courses.json")
coursesDB = json.load(fp)
Element("course-title").write(coursesDB.get(subject).get(course).get("title"))
Element("credit-hours").element.append(coursesDB.get(subject).get(course).get("credit-hours"))
Element("class-hours").element.append(coursesDB.get(subject).get(course).get("class-hours"))
Element("lab-hours").element.append(coursesDB.get(subject).get(course).get("lab-hours"))