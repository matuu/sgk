// Author: Matias Varela
//
var KEYCODE_ENTER = 13;
var KEYCODE_ESC = 27;

var mDialogConfirm = function (options) {
	//Atributos
	this.container = "mdialog";
	this.message = "¿Desea continuar?";
	this.title = "Confirmar Acción";
	/*Valores permitidos para seteo de icono: info, warn, shutdown*/
	this.type = "warn";
	this.autoClose = true;

	//Métodos getter y setter
	this.setContainer = function (param) {
		this.container = param;
	}
	this.getContainer = function () {
		return this.container;
	}
	this.setMessage = function (param) {
		this.message = param;
	}
	this.getMessage = function () {
		return this.message;
	}
	this.setTitle = function (param) {
		this.title = param;
	}
	this.getTitle = function () {
		return this.title;
	}
	this.setType = function (param) {
		this.type = param;
	}
	this.getType = function () {
		return this.type;
	}

	this.setYes = function (param) {
		this.yes = param;
	}
	this.getYes = function () {
		return this.yes;
	}
	this.setNo = function (param) {
		this.no = param;
	}
	this.getNo = function () {
		return this.no;
	}
	this.setAutoClose = function (param) {
		this.autoClose = param;
	}
	this.getAutoClose = function () {
		return this.autoClose;
	}

	this.setPreShow = function (param) {
		this.preShow = param;
	}
	
	//Métodos 
	//Accion del boton Si
	this.yes = function () {
		this.close();
	};
	//Accion del boton No
	this.no = function () {
		this.close();
	}
	//Devuelve el objeto
	this.getObject = function () {
		return this;
	}
	//Metodo ejecutado antes de mostrar el dialogo.
	this.preShow = function () {
	//nada
  };

	//Imprime en consola el objeto. Solo para debugging
	this.toString = function () {
		var string = "Container: " + this.container + " |Message: " + this.message + " |Title: " + this.title;
		string += " |Yes: " + this.yes;
		return string;
	}
	//Muestra el dialogo y attachea la funcionalidad de los botones
	this.show = function () {
		//Obtengo la instancia del dialog
		var obj = this.getObject();
		setupDialogConfirm(this, options);
		obj.preShow();
		var dialogo = document.getElementById('light');
		dialogo.style.display = 'block';
		document.getElementById('fade').style.display = 'block';
		
		//Creamos un handler del evento click sobre los botones de clase 'mbutton'
		$(".mbutton").click(function () {
			var boton = $(this).attr("id");
			if (boton == 'mbYes') {
				obj.yes();
				if (obj.autoClose) obj.close();
			} else if (boton == 'mbNo') {
				obj.no();
			}

		});
		$("#closeX").click(function () {
			obj.close();
		});
		//Bind keyUp --> Enter: Yes | Esc: No
		setTimeout(function(){
			$(document).keyup(function (e) {
				//console.debug("bind: keyUp|dialog");
				if (e.keyCode == KEYCODE_ENTER) { obj.yes(); obj.close(); $(document).unbind(); }
				if (e.keyCode == KEYCODE_ESC) { obj.no(); $(document).unbind(); }
			})} , 100);
		
		

		centrarElement(document.getElementById("light"), options);
	};

	//Cierra el dialogo
	this.close = function () {
		document.getElementById('light').style.display = 'none';
		document.getElementById('fade').style.display = 'none';
	};



	//Funcion que configura el dialog. Es llamada al momento de mostrarlo. En el show()
	function setupDialogConfirm(obj, options) {
		if (options != undefined) { //Si no se definieron en el constructor, sigo
			if (options['container'] != undefined) {
				obj.container = options['container'];
			}
			if (options['message'] != undefined) {
				obj.message = options['message'];
			}
			if (options['title'] != undefined) {
				obj.title = options['title'];
			}
			if (options['type'] != undefined) {
				obj.type = options['type'];
			}
			if (options['yes'] != undefined) {
				obj.yes = options['yes'];
			}
			if (options['no'] != undefined) {
				obj.no = options['no'];
			}
			if (options['autoClose'] != undefined) {
				obj.type = options['autoClose'];
			}
			if (options['preShow'] != undefined) {
				obj.preShow = options['preShow'];
			}
		}

		//Crea el contenido web del dialogo
		var inner = "<div id='fade' class='moverlay'></div>"
			 + "<div id='light' class='mmodal'>"
			 + "<h2 id='" + obj.type + "H2'>" + obj.title + "</h2><div id='mmessage'>" + obj.message
			 + "</div><p><input class='mbutton' type='button' value='Si' id='mbYes' />"
			 + "<input class='mbutton' type='button' value='No' id='mbNo' /></p></div>";
		
		//Mete el contenido web en el contenedor especificado
		try {
			document.getElementById("" + obj.container).innerHTML = inner;
		} catch (ex) {
			var body = document.getElementsByTagName("body");
			body.item[0].innerHTML = body.item[0].innerHTML + "<div id='" + obj.container + "'></div>";
			document.getElementById("" + obj.container).innerHTML = inner;
		}

		


		if (options != undefined) {
			if (options['left'] != undefined) {
				document.getElementById("light").style.left = options['left'];
			}
			if (options['top'] != undefined) {
				document.getElementById("light").style.top = options['top'];
			}
			if (options['width'] != undefined) {
				document.getElementById("light").style.width = options['width'];
			}
			if (options['height'] != undefined) {
				document.getElementById("light").style.height = options['height'];
			}
			if (options['z-index'] != undefined) {
			    document.getElementById("light").style.zIndex = options['z-index'];
			}
		}
	}

}

var mDialog = function (options) {
	//Atributos
	this.container = "mdialog";
	this.content = "¿Desea continuar?";
	this.title = "Confirmar Acción";
	this.thisFrameId;
	/*Valores permitidos para seteo de icono: info, warn, shutdown*/
	this.type = "warn";

	//Métodos getter y setter
	this.setContainer = function (param) {
		this.container = param;
	}
	this.getContainer = function () {
		return this.container;
	}
	this.setContent = function (param) {
		this.content = param;
	}
	this.getContent = function () {
		return this.content;
	}
	this.setTitle = function (param) {
		this.title = param;
	}
	this.getTitle = function () {
		return this.title;
	}
	this.setType = function (param) {
		this.type = param;
	}
	this.getType = function () {
		return this.type;
	}
	this.setThisFrameId = function (param) {
		this.thisFrameId = param;
	}
	this.getThisFrameId = function () {
		return this.thisFrameId;
	}

	//Metodo ejecutado antes de mostrar el dialogo.
	this.preShow = function () {
		console.debug("preShow");
	};

	//Métodos 

	//Devuelve el objeto
	this.getObject = function () {
		return this;
	}
	//Imprime en consola el objeto. Solo para debugging
	this.toString = function () {
		var string = "Container: " + this.container + " |Content: " + this.content + " |Title: " + this.title;
		return string;
	}
	//Muestra el dialogo y attachea la funcionalidad de los botones
	this.show = function () {
		setupDialog(this, options);
		//Obtengo la instancia del dialog
		var obj = this.getObject();
		obj.preShow();
		var dialogo = document.getElementById('light');
		dialogo.style.display = 'block';
		document.getElementById('fade').style.display = 'block';
		

		$("#closeX").click(function () {
			obj.close();
		});
		

		
		centrarElement(document.getElementById("light"), options);
	};

	//Cierra el dialogo
	this.close = function () {
		document.getElementById('light').style.display = 'none';
		document.getElementById('fade').style.display = 'none';
	};



	//Funcion que configura el dialog. Es llamada al momento de mostrarlo. En el show()
	function setupDialog(obj, options) {
		if (options != undefined) { //Si no se definieron en el constructor, sigo
			if (options['container'] != undefined) {
				obj.container = options['container'];
			}
			if (options['content'] != undefined) {
				obj.content = options['content'];
			}
			if (options['title'] != undefined) {
				obj.title = options['title'];
			}
			if (options['type'] != undefined) {
				obj.type = options['type'];
			}
			if (options['preShow'] != undefined) {
				obj.preShow = options['preShow'];
			}
			if (options['thisFrameId'] != undefined) {
				obj.thisFrameId = options['thisFrameId'];
			}
		}

		//Crea el contenido web del dialogo
		var inner = "<div id='fade' class='moverlay'></div>"
			 + "<div id='light' class='mmodal'><div id='closeX'>Cerrar </div>"
			 + "<h2 id='" + obj.type + "H2'>" + obj.title + "</h2><div id='mmessage'>" + obj.content
			 + "</div></div>";
		//Mete el contenido web en el contenedor especificado
		try {
			document.getElementById("" + obj.container).innerHTML = inner;
			obj.thisFrameId = document.getElementById("light").id;
		} catch (ex) {
			var body = document.getElementsByTagName("body");
			body.item[0].innerHTML = body.item[0].innerHTML + "<div id='" + obj.container + "'></div>";
			document.getElementById("" + obj.container).innerHTML = inner;
			obj.thisFrameId = document.getElementById("light").id;
		}


		if (options != undefined) {
			if (options['left'] != undefined) {
				document.getElementById("light").style.left = options['left'];
			}
			if (options['top'] != undefined) {
				document.getElementById("light").style.top = options['top'];
			}
			if (options['width'] != undefined) {
				document.getElementById("light").style.width = options['width'];
			}
			if (options['height'] != undefined) {
				document.getElementById("light").style.height = options['height'];
			}
		}
	}

}

function centrarElement(element,options) {
	if (options != undefined) {
		if (options['left'] == undefined) {
			var porcentajeL = 50 - ((element.clientWidth * 100 / window.innerWidth) / 2);
			element.style.left = porcentajeL + "%";
		}
		if (options['top'] == undefined) {
			var porcentajeT = 50 - ((element.clientHeight * 100 / window.innerHeight) / 2);
			element.style.top = porcentajeT + "%";
		}
	}
	
}
