var response = '';
var selectedIPAddr = [];
var passwordArr = [];
var link = document.URL.slice(0, -14);

function showLoadingImage(){ 
    document.getElementById('loading').style.display='block';
    document.getElementById("managebtn").disabled = true;
    var nic = document.getElementById("nic").value;
    var xhttp = new XMLHttpRequest();
    
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
                <td><input type="checkbox" name="messageCheckbox" id="select'+i+'" value="'+response[i].IPAddr+'" onclick="if(this.checked){checkPasswordField('+i+')}"></td> \
                <td>'+response[i].Hostname+'</td> \
                <td>'+response[i].MACAddr+'</td> \
                <td>'+response[i].IPAddr+'</td> \
                <td>root</td> \
                <td><input type="text" name="password'+i+'" id="password'+i+'"></td> \
                <td id="err'+i+'" style="color: red"></td> \
                </tr>'
              }
            document.getElementById("tableData").innerHTML = text;
        }
    };
    // xhttp.open("GET", link+"/posts/", true);
    xhttp.open("GET", link+"/v1/Devices/"+nic, true);
    xhttp.setRequestHeader("Access-Control-Allow-Origin" ,"*");
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send();
}


function showWhatToManage(){
    document.getElementById('errorMsg').style.display='none';
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
    document.getElementById('installLoading').style.display='block';
    var softwareToInstall = document.querySelector('input[name = "optradio"]:checked').value;
    var configData = [];
    configData.push(softwareToInstall);
    for(i=0; i< selectedIPAddr.length; i++){
        var data = {
            "IP" : selectedIPAddr[i],
            "pass" : passwordArr[i]
        }
        configData.push(data);
    }
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            document.getElementById('installLoading').style.display='none';
            document.getElementById('installationLogDiv').style.display = 'block';
            var text = '';
            for (i = 0; i < response.length; i++) {
                text += '<tr>\
                <th scope="row">'+response[i].IP+'</th>\
                <td>'+response[i].changed+'</td>\
                <td>'+response[i].failed+'</td>\
                <td>'+response[i].ok+'</td>\
                <td>'+response[i].unreachable+'</td>\
              </tr>';
            }
            document.getElementById('installationTableData').innerHTML = text;
        }
      };
    
    xhttp.open("POST", link+"/v2/Broadcast/");
    xhttp.setRequestHeader("Content-Type", "text/plain");
    // xmlhttp.setRequestHeader("Package", softwareToInstall);
    xhttp.send(JSON.stringify(configData));
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
    document.getElementById('manualInstallLoading').style.display='block';
    var cmd  = document.getElementById("cmd").value;
    var softwareToInstall = cmd;
    var configData = [];
    configData.push(softwareToInstall);
    for(i=0; i< selectedIPAddr.length; i++){
        var data = {
            "IP" : selectedIPAddr[i],
            "pass" : passwordArr[i]
        }
        configData.push(data);
    }
    console.log(configData);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            document.getElementById('manualInstallLoading').style.display='none';
            document.getElementById('installationLogDiv').style.display = 'block';
            var text = '';
            for (i = 0; i < response.length; i++) {
                text += '<tr>\
                <th scope="row">'+response[i].IP+'</th>\
                <td>'+response[i].changed+'</td>\
                <td>'+response[i].failed+'</td>\
                <td>'+response[i].ok+'</td>\
                <td>'+response[i].unreachable+'</td>\
              </tr>';
            }
            document.getElementById('installationTableData').innerHTML = text;
        }
    };
    
    xhttp.open("POST", link+"/v2/Broadcast/");
    xhttp.setRequestHeader("Content-Type", "text/plain");
    xhttp.send(JSON.stringify(configData));
}