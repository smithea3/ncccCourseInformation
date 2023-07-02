import courses from '../json/courses.json' assert { type: 'json' };
import colllege_policies from '../json/college_policies.json' assert { type: 'json' };
import important_dates from '../json/important_dates.json' assert { type: 'json' };
import instructor_information from '../json/instructor_information.json' assert { type: 'json' };
import section_info from '../json/section_info.json' assert { type: 'json' };

fetch("../json/courses.json")
    .then(response => response.json())

fetch("../json/college_policies.json")
    .then(response => response.json())

fetch("../json/important_dates.json")
    .then(response => response.json())

fetch("../json/instructor_information.json")
    .then(response => response.json())

fetch("../json/section_info.json")
    .then(response => response.json())

// const queryString = window.location.search;
// const urlParams = new URLSearchParams(queryString);

//  A function to create a UL/OL from a JSON array
function convertArrayToHtmlList (inputList, listType) {
    if (listType = "ul") {
        var outputHTML = "<ul>"
    } else {
        var outputHTML = "<ol>"
    }
    for (let i = 0; i < inputList.length; i++) {
        outputHTML += "<li>"+inputList[i]+"</li>"
    }
    if (listType = "ul") {
        outputHTML += "</ul>"
    } else {
        outputHTML = "</ol>"
    }
    return outputHTML
}

// A function go retrieve all of the URL Paramters take from https://www.sitepoint.com/get-url-parameters-with-javascript/
function getAllUrlParams(url) {
    // get query string from url (optional) or window
    var queryString = url ? url.split('?')[1] : window.location.search.slice(1);

    // we'll store the parameters here
    var obj = {};

    // if query string exists
    if (queryString) {

        // stuff after # is not part of query string, so get rid of it
        queryString = queryString.split('#')[0];

        // split our query string into its component parts
        var arr = queryString.split('&');

        for (var i = 0; i < arr.length; i++) {
            // separate the keys and the values
            var a = arr[i].split('=');

            // set parameter name and value (use 'true' if empty)
            var paramName = a[0];
            var paramValue = typeof (a[1]) === 'undefined' ? true : a[1];

            // if the paramName ends with square brackets, e.g. colors[] or colors[2]
            if (paramName.match(/\[(\d+)?\]$/)) {

                // create key if it doesn't exist
                var key = paramName.replace(/\[(\d+)?\]/, '');
                if (!obj[key]) obj[key] = [];

                // if it's an indexed array e.g. colors[2]
                if (paramName.match(/\[\d+\]$/)) {
                    // get the index value and add the entry at the appropriate position
                    var index = /\[(\d+)\]/.exec(paramName)[1];
                    obj[key][index] = paramValue;
                } else {
                    // otherwise add the value to the end of the array
                    obj[key].push(paramValue);
                }
            } else {
                // we're dealing with a string
                if (!obj[paramName]) {
                    // if it doesn't exist, create property
                    obj[paramName] = paramValue;
                } else if (obj[paramName] && typeof obj[paramName] === 'string') {
                    // if property does exist and it's a string, convert it to an array
                    obj[paramName] = [obj[paramName]];
                    obj[paramName].push(paramValue);
                } else {
                    // otherwise add the property
                    obj[paramName].push(paramValue);
                }
            }
        }
    }

    return obj;
}

function getCourseInformation(urlParams) {
    // Get the college name
    if (urlParams.hasOwnProperty("college")) {
        document.getElementById("college-name").innerText = colllege_policies[urlParams["college"]]["collegeName"]
    } else {
        document.getElementById("college-name").innerText = colllege_policies["templateCollege"]["collegeName"]
    }
    // Get the subject (i.e. MAT, BIO, etc.) from URL parameters
    if (urlParams.hasOwnProperty("subject")) {
        document.getElementById("subject").innerText = urlParams.subject

    } else {
        document.getElementById("subject").innerText = "ABC"
    }

    // Get the course (i.e. 101, 110, 171, etc.) from URL parameters
    if (urlParams.hasOwnProperty("course")) {
        document.getElementById("course").innerText = urlParams.course
    } else {
        document.getElementById("course").innerText = "100"
    }

    // Get the course section
    if (urlParams.hasOwnProperty("section")) {
        document.getElementById("section").innerText = urlParams.section
    } else {
        document.getElementById("section").innerText = "SSB1"
    }

    // Get the semester from URL parameters
    if (urlParams.hasOwnProperty("semester")) {
        document.getElementById("semester").innerText = "("+urlParams.semester+")"
    } else {
        document.getElementById("semester").innerText = "(20YYXX)"
    }

    if (urlParams.hasOwnProperty("subject") && urlParams.hasOwnProperty("course")) {
        // Get catalog title
        document.getElementById("course-title-catalog").innerText = courses[urlParams["subject"]][urlParams["course"]]["title"]
        
        // Append credit hours
        document.getElementById("credit-hours").innerHTML += courses[urlParams["subject"]][urlParams["course"]]["credit-hours"]

        // Append class hours
        document.getElementById("class-hours").innerHTML += courses[urlParams["subject"]][urlParams["course"]]["class-hours"]

        // Append lab hours
        document.getElementById("lab-hours").innerHTML += courses[urlParams["subject"]][urlParams["course"]]["lab-hours"]

        // Update catalog description section
        document.getElementById("catalog-description").innerHTML = courses[urlParams["subject"]][urlParams["course"]]["catalog-description"]

        // Update SLO section
        document.getElementById("slos").innerHTML = convertArrayToHtmlList(courses[urlParams["subject"]][urlParams["course"]]["slos"], '')
    }
}

var urlParams = getAllUrlParams()
getCourseInformation(urlParams)
console.log(instructor_information["0626512"]["name"])