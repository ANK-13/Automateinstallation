var response = '';
var selectedIPAddr = [];
var passwordArr = [];
var link = "http://localhost:3000";

function showLoadingImage(){ 
    document.getElementById('loading').style.display='block';
    document.getElementById("managebtn").disabled = true;
    var nic = document.getElementById("nic").value;
    var xhttp = new XMLHttpRequest();
    xhttp.setRequestHeader("Access-Control-Allow-Origin", "*");
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('loading').style.display='none';
            document.getElementById('IpTable').style.display='block';
            document.getElementById('managebtndiv').style.display='block';
            response = JSON.parse(this.responseText);
            document.getElementById("tableData").innerHTML = response;
            var text = '';
            for (i = 0; i < response.length; i++) {
                text += '<tr>\
                <td><input type="checkbox" name="messageCheckbox" id="select'+i+'" value="'+response[i].author+'" onclick="if(this.checked){checkPasswordField('+i+')}"></td> \
                <td>'+response[i].host+'</td> \
                <td>'+response[i].title+'</td> \
                <td>'+response[i].author+'</td> \
                <td>root</td> \
                <td><input type="text" name="password'+i+'" id="password'+i+'"></td> \
                <td id="err'+i+'" style="color: red"></td> \
                </tr>'
              }
            document.getElementById("tableData").innerHTML = text;
        }
    };
    xhttp.open("GET", link+"/posts/", true);
    // xhttp.open("GET", "/v1/Devices/"+nic, true);
    xhttp.send();
}


function showWhatToManage(){
    document.getElementById('errorMsg').style.display='none';
    selectedIPAddr = [];
    var items=document.getElementsByName('messageCheckbox');
    for(var i=0; i<items.length; i++){
        if(items[i].type=='checkbox' && items[i].checked==true){
            selectedIPAddr.push(items[i].value);
            passwordArr.push(document.getElementById("password"+i).value)
        }
    }
    if(selectedIPAddr.length > 0){
        document.getElementById('manageBlock').style.display='block';   
    }
    else{
        document.getElementById('errorMsg').style.display='block';
        document.getElementById('errorMsg').innerHTML = "System not selected";
    }
}


function installSoftware(){
    var softwareToInstall = document.querySelector('input[name = "optradio"]:checked').value;
    var configData = [];
    for(i=0; i< selectedIPAddr.length; i++){
        var data = {
            "IP" : selectedIPAddr[i],
            "pass" : passwordArr[i]
        }
        configData.push(data);
    }
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", link+"/v1/Broadcast");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.setRequestHeader("Package", softwareToInstall);
    xmlhttp.send(JSON.stringify(configData));
}


function checkPasswordField(i){
    var password =  document.getElementById("password"+i).value;
    if(password.length > 0){
        document.getElementById("err"+i).innerHTML = "";
        document.getElementById("managebtn").disabled = false;    
    }
    else{
        document.getElementById("err"+i).innerHTML = "Password Required";
        document.getElementById("managebtn").disabled = true;
    }
}


function runCommand(){
    var cmd  = document.getElementById("cmd").value;
    console.log(cmd);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", link+"/command?cmd="+cmd, true);
    xhttp.send();
}