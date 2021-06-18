function crear(){
    var col = document.getElementById("cols").value;
    var filas = document.getElementById("rows").value;
    var tabla="<table border=\"0\">";
    
    tabla+="<tr><td></td>";
    for(j=0;j<col;j++){ 
        tabla+="<td>"+(j+1)+ "</td>";
    }
    tabla+="</tr>";
    
    for(i=0;i<filas;i++){
        tabla+="<tr>";
        tabla+="<td>"+(i+1)+ "</td>";
        for(j=0;j<col;j++){ 
            tabla+="<td>"+"<input type=\"text\" size=\"1\" name=\""+i+"_"+j+"\" id=\""+i+"_"+j+"\">"+ "</td>";
        }
        tabla+="</tr>";
    }
    tabla+="</table>";
    document.getElementById("resultado").innerHTML=tabla;
}

function crear2() {
    document.getElementById("resultado").innerHTML="";
}