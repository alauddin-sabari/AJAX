// var resultField = document.getElementById("result")
var resultField = $("#result")
function insertNumber(number){
    var existingNumbers = $("#result").val()
   resultField.val(existingNumbers+number)

}

function clearResult(){
   resultField.val("")
}

function calculate(){
     var result = eval($("#result").val())
    //  eval is a function that evaluates or calculates the value of the string
    resultField.val(result)
}

function deleteNumber(){
   var presentValue = resultField.val()
//    now slice the last number
    if(presentValue != ""){
        resultField.val(presentValue.slice(0,-1))

    }
}
