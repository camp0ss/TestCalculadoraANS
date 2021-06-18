var mathFieldSpan = document.getElementById('pantalla');
var latexSpan = document.getElementById('codigo');

var MQ = MathQuill.getInterface(2);
var mathField = MQ.MathField(mathFieldSpan,
	{
		spaceBehavesLikeTab: true,
		leftRightIntoCmdGoes: 'up',
		restrictMismatchedBrackets: true,
		sumStartsWithNEquals: true,
		supSubsRequireOperand: true,
		//charsThatBreakOutOfSupSub: '+-=<>',
		autoSubscriptNumerals: true,
		autoCommands: 'pi theta sqrt sum',
		autoOperatorNames: 'sin cos',


		handlers:
		{
			edit: function () {
				texto = mathField.text();

				console.log(mathField.text());
				console.log(mathField.latex());

				//numeros especiales


				if (texto.includes("e")) {
					texto = texto.replaceAll("e", "e");
				}

				if (texto.includes("i")) {
					texto = texto.replaceAll("i", "%i");
				}

				if (texto.includes("p%i")) {
					texto = texto.replaceAll("p%i", "*%pi");
				}
				if (texto.includes("pi")) {
					texto = texto.replaceAll("pi", "*pi");
				}


				//Cambio de corchetes

				if (texto.includes("[")) {
					texto = texto.replaceAll("[", "(");
				}
				if (texto.includes("]")) {
					texto = texto.replaceAll("]", ")");
				}

				//Parentesis

				if (texto.includes(")(")) {
					texto = texto.replaceAll(")(", ")*(");
				}
				if (texto.includes("(")) {
					texto = texto.replaceAll("(", "*(");
				}
				if (texto.includes("**")) {
					texto = texto.replaceAll("**", "*");
				}

				//parseo de errores

				if (texto.includes("^*(")) {
					texto = texto.replaceAll("^*(", "^(");
				}
				if (texto.includes("sqrt*")) {
					texto = texto.replaceAll("sqrt*", "*sqrt");
				}
				if (texto.includes("^(")) {
					texto = texto.replaceAll("^(", "**(");
				}

				//Funciones trigonometricas

				if (texto.includes("s*e*n*")) {
					texto = texto.replaceAll("s*e*n*", "sin");
				}

				if (texto.includes("\c*o*s *")) {
					texto = texto.replaceAll("\\c*o*s *", "cos");
				}
				if (texto.includes("t*a*n*")) {
					texto = texto.replaceAll("t*a*n*", "tan");
				}


				if (texto.includes("s*%e*c*")) {
					texto = texto.replaceAll("s*%e*c*", "sec");
				}
				if (texto.includes("c*s*c*")) {
					texto = texto.replaceAll("c*s*c*", "csc");
				}
				if (texto.includes("c*o*t*")) {
					texto = texto.replaceAll("c*o*t*", "cot");
				}



				if (texto.includes("s*%e*n^(-1)*")) {
					texto = texto.replaceAll("s*%e*n^(-1)*", "asin");
				}
				if (texto.includes("\c*o*s ^(-1)*")) {
					texto = texto.replaceAll("\\c*o*s ^(-1)*", "acos");
				}
				if (texto.includes("t*a*n^(-1)*")) {
					texto = texto.replaceAll("t*a*n^(-1)*", "atan");
				}



				if (texto.includes("s*%e*c^(-1)*")) {
					texto = texto.replaceAll("s*%e*c^(-1)*", "asec");
				}
				if (texto.includes("c*s*c^(-1)*")) {
					texto = texto.replaceAll("c*s*c^(-1)*", "acsc");
				}
				if (texto.includes("c*o*t^(-1)*")) {
					texto = texto.replaceAll("c*o*t^(-1)*", "acot");
				}



				//Funcion Logaritmo

				if (texto.includes("l*n*")) {
					texto = texto.replaceAll("l*n*", "log");
				}


				//theta

				if (texto.includes("th%eta")) {
					texto = texto.replaceAll("\\th%eta", "theta");
					texto = texto.replaceAll(" ", "");
				}


				//subindice

				if (texto.includes("_")) {
					texto = texto.replaceAll("_", "");
				}

				//parseo errores

				if (texto.includes("(*%")) {
					texto = texto.replaceAll("(*%", "(%");
				}
				if (texto.includes("(*sqrt")) {
					texto = texto.replaceAll("(*sqrt", "(sqrt");
				}
				if (texto.includes("abs*")) {
					texto = texto.replaceAll("abs*", "abs");
				}
				if (texto.includes("(*(")) {
					texto = texto.replaceAll("(*(", "((");
				}
				if (texto.includes("((*(")) {
					texto = texto.replaceAll("((*(", "(((");
				}
				if (texto.includes("/*(")) {
					texto = texto.replaceAll("/*(", "/(");
				}
				if (texto.includes("+*(")) {
					texto = texto.replaceAll("+*(", "+(");
				}
				if (texto.includes("-*(")) {
					texto = texto.replaceAll("-*(", "-(");
				}
				if (texto.includes("*)")) {
					texto = texto.replaceAll("*)", ")");
				}



				if (texto.includes("/*sqrt")) {
					texto = texto.replaceAll("/*sqrt", "/sqrt");
				}
				if (texto.includes("+*sqrt")) {
					texto = texto.replaceAll("+*sqrt", "+sqrt");
				}
				if (texto.includes("-*sqrt")) {
					texto = texto.replaceAll("-*sqrt", "-sqrt");
				}
				if (texto.includes("U*(")) {
					texto = texto.replaceAll("U*(", "U(");
				}

				//asterisco

				if (texto[0] == "*") {
					texto = texto.substring(1, texto.length);
				}
	

				latexSpan.textContent = texto.trim();
				document.getElementById("aver").value = texto.trim();
				//latexSpan.textContent = mathField.latex()

				mathField.focus();
			}
		}
	});


function insertar(valor) {
	if (valor.includes("^2") || valor.includes("^3") || valor.includes("\\left(")) {
		mathField.write(valor);
		mathField.keystroke('Left');
	}
	else {
		mathField.cmd(valor);
	}



	mathField.focus();
}

String.prototype.replaceAll = function (search, replacement) {
	var target = this;
	return target.split(search).join(replacement);
};

function copiar(id_elemento) {
	var aux = document.createElement("input");
	aux.setAttribute("value", document.getElementById(id_elemento).innerHTML);
	document.body.appendChild(aux);
	aux.select();
	document.execCommand("copy");
	document.body.removeChild(aux);
}

function borrar() {
	mathField.select();
	mathField.keystroke('Del');
}

function textoSize(tamano) {
	switch (tamano) {
		case "pequeño":
			$('#pantalla').css("font-size", "14px");
			$('#codigo').css("font-size", "12px");
			break;

		case "mediano":
			$('#pantalla').css("font-size", "18px");
			$('#codigo').css("font-size", "14px");
			break;

		case "grande":
			$('#pantalla').css("font-size", "26px");
			$('#codigo').css("font-size", "20px");
			break;
	}
}

