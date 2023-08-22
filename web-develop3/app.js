let age = 34;
let userName = "JD";
let hobbies = ["Sports", "Cooking", "Reading"];
let job = {
  title: "Developer",
  place: "Newyork",
  salary: 50000,
};

let totalAdultYears;

function calculateAdultYears(userAge) {
    let result;
    result = userAge - 18;
    return result;
}


totalAdultYears =calculateAdultYears(age);
alert(totalAdultYears);

age = 45;
totalAdultYears =calculateAdultYears(age);

alert(totalAdultYears);
