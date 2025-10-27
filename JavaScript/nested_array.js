//Nested Array


//[id,name,designation,location,salary,experience]
employee=[
[1000, 'Rohan', 'Developer', 'India', 25000, 3], 
    [1001, 'Liam', 'Tester', 'UK', 20000, 2],
    [1002, 'Kenji', 'QA', 'Japan', 35000, 4], 
    [1003, 'David', 'QA', 'USA', 45000, 5], 
    [1004, 'Isabella', 'Tester', 'Spain', 55000, 7], 
    [1005, 'Miguel', 'Developer', 'Brazil', 15000, 1], 
    [1006, 'Laisha', 'QA', 'Lebanon', 25000, 3], 
    [1007, 'Chris', 'Developer', 'USA', 30000, 3], 
    [1008, 'Zhang', 'Developer', 'China', 25000, 3],

]

//1 Print all employee name 
for (let i in employee) {
    console.log(employee[i][1]);
    
}
//2 Print total number of employee
console.log('Total number of employees',employee.length);

//3 Print developer employee details
for (let i in employee) {
    if (employee[i][2]==='Developer') {
        console.log(employee[i]);
    }
    
}
//4 Print all employee details whose salary > 30000
for(let i in employee) {
    if(employee[i][4]>30000){
        console.log(employee[i]);
        
    }
}
//5 Print details of employee Laisha
for (const element of employee) {
    if (element[1]==='Laisha') {
        console.log('Laisha:',element);
        
    }
}
