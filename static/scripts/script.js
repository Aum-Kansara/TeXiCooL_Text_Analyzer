let entered_text="";
function setSampleText() {
    let sample_text = `What do you mean by an event in state diagram? Discuss various types of events.
Define following Terms: Derived data, Abstract Class, Generalization, Multiplicity, Constrains, Metadata, Package.
How does the object oriented approach differ from the traditional approach? Why is reusability important? How does Object-Oriented Software Development promote (achieve) and improve reusability?
Describe in detail the stages of Object oriented methodology.
Draw a sequence diagram for issuing a book and renewing a book in online library management system.
Briefly describe the steps for constructing a domain State model.
What does one shot diagram represent? Show one shot diagram for chess game. (ii) Explain with state diagram how an object can perform activities concurrently?
Prepare a use case diagram and sequence diagram for an online airline reservation system.
Draw state diagram for the control of a telephone answering machine. The machine detects an incoming call on the first ring and answers the call with a prerecorded announcement. When the announcement is complete, the machine records the caller�s message. When the caller hands up, the machine hangs up and shuts off. Place the following in the diagram: call detected, answer call, play announcement, record message, caller hangs up, announcement complete.
Explain the tasks involved in design optimization.
Explain waterfall development and Iterative Development life cycle styles for Object Oriented approach to software development.
Prepare an activity diagram for computing a restaurant bill. There should be a charge for each delivered item. The total amount should be subject to tax. There is a service charge of 18% for groups of six or more and 10% for smaller groups. Any coupons and gift certificates submitted by the customer should be subtracted.
What is the purpose of class modeling? Explain following concept with example. (i) Aggregation versus association   (ii) Aggregation versus composition
What is inheritance? List the different types of inheritance and explain how it encourages reusability and sharing.
Explain the following terms in relation to class design. a. Refactoring b. reification
Explain following concepts with reference to system design: i) Reusable components and their use
Methods of breaking system into subsystems  (b) Give the list of common architectural styles. Explain batch transformation in detail.`


    document.querySelector('.inputTxt').value = sample_text;
}

function clearText() {
    document.querySelector('.inputTxt').value = '';
}

function saveText(){
    document.cookie='default_text='+document.querySelector('.inputTxt').value.split('\n').join('\\')+';';
}
function setText(text){
    document.querySelector('.inputTxt').value = text;
}
window.onload=function(){
    document.querySelector('.inputTxt').value=document.cookie.split('\\').join('\n').replace('default_text=','');
}