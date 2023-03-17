// 1914474

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}


program: decls EOF;

decls: decls decl | decl ;
decl: function | vardecl ;
//---------------------- statement --------------------------
stmt:
	assginsta
	| ifsta
	| forsta
	| contista
	| breaksta
	| returnsta
	| blocksta
	| callstmt
	| vardecl
	| dosta
	| whilesta
	| spefuncstmt;

assginsta: lhs ASG (exp0 | specialfunc | funcall) SEMI;
callstmt: ID LB listexp? RB SEMI ;
lhs:  ID | exp7 ;
ifsta:
	IF LB exp0 RB stmt (ELSE stmt)?; // if-else
forsta: FOR LB lhs ASG exp0 COMMA exp1 COMMA exp0 RB stmt ;
contista: CONTINUE SEMI;
breaksta: BREAK SEMI;
returnsta: RETURN exp0? SEMI;
whilesta: WHILE LB exp0 RB (blocksta | stmt) ;
dosta: DO (blocksta | stmt) WHILE LB exp0 RB  SEMI;
blocksta: LP body1 RP;
body1: body1 stmt | stmt |  ;
listval: listval COMMA ID  | ID ;
listparam: listparam COMMA paramemter | paramemter;
paramemter: INHERIT?  OUT?   ID COLO (autotype | arrtype) ;

vardecl: (noninitvardecl | initvardecl ) SEMI  ;
noninitvardecl: idlist COLO  (autotype | arrtype)  ;
initvardecl: ID initvardeclrec (exp0| specialfunc) ;
initvardeclrec:
	COMMA ID initvardeclrec (exp0| specialfunc) COMMA
	| COLO (autotype | arrtype) ASG;
idlist: ID COMMA idlist | ID;
spefuncstmt: specialfunc SEMI;

function: ID COLO FUNC systemtype LB listparam? RB (INHERIT ID)? blocksta  ; 

/*---------------------------special func-----------------------------*/

specialfunc: (readBool | readInt | printInt | readFloat | writeFloat |printBool | readString | printString | superfunc | predef ) ;
readInt: READINT LB  RB;
printInt: PRINTINT LB (INT | ID | exp0)? RB;
readFloat: READF LB RB;
writeFloat: WRITEF LB (FLOATLIT| ID | exp0)  RB;
printBool: PRINTBOOL LB (boolit| ID| exp0) RB;
readBool: READBOOL LB RB;
readString: READSTRING LB RB;
printString: PRINTSTRING LB (STRLIT| ID | exp0 ) RB ;
superfunc: SUPER LB listexp RB;
predef: PREDE RB LB;

/*---------------------------EXPRESSION-----------------------------*/
listexp:  listexp COMMA exp0 | exp0;
exp0: exp1 CONCAT exp1| exp1;
exp1:
	exp2 EQUAL exp2
	| exp2 NEQUAL exp2
	| exp2 LTE exp2
	| exp2 GTE exp2
	| exp2 LT exp2
	| exp2 GT exp2
	| exp2;
exp2: exp2 AND exp3 | exp2 OR exp3 | exp3;
exp3: exp3 ADD exp4 | exp3 SUB exp4 | exp4;
exp4: exp4 MUL exp5 | exp4 DIV exp5 | exp4 MOD exp5 | exp5;
exp5: NOT (exp0|exp6) |  exp6;
exp6: SUB (exp0|exp6) |  exp7;
exp7: ID LS listexp RS | exp8 ;
exp8: 	FLOATLIT
	| boolit
	| STRLIT       
	| ID
	| INT
	| arr
	| exp9
	| funcall
	| arrlit
	;
exp9: LB exp0 RB;
funcall: ID LB listexp? RB;


/*---------------------------type-----------------------------*/
arrlit: LP listexp? RP ;
arrtype: ARRAY LS intlitarr RS OF  autotype ;
literals: INT | boolit | FLOATLIT | STRLIT ;
arr: ID LS intlitarr RS ;
intlitarr: intlitarr COMMA INT | INT; 
autotype: INTEGER  | STRING | BOOLEAN | FLOAT | AUTO  ;
systemtype: INTEGER  | STRING | BOOLEAN | FLOAT | 'void' | arrtype | AUTO ;

/*---------------------------LEXER-----------------------------*/
boolit: TRUE | FALSE;



//Keywords
AUTO: 'auto' ;
BREAK: 'break' ;
BOOLEAN: 'boolean' ;
DO: 'do' ;
ELSE: 'else' ;
FALSE: 'false' ;
FLOAT: 'float' ;
FOR: 'for';
IF: 'if' ;
INTEGER: 'integer' ;
RETURN: 'return' ;
STRING: 'string' ;
TRUE: 'true' ;
WHILE: 'while' ;
VOID: 'void' ;
OUT: 'out' ;
CONTINUE: 'continue' ;
OF: 'of' ;
INHERIT: 'inherit' ;
ARRAY: 'array' ;
FUNC: 'function' ;
READINT: 'readInteger';
PRINTINT: 'printInteger';
READF: 'readFloat';
WRITEF: 'writeFloat';
READBOOL: 'readBoolean';
PRINTBOOL: 'printBoolean';
READSTRING: 'readString';
PRINTSTRING: 'printString';
SUPER: 'super' ;
PREDE: 'preventDefault' ;

//Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NEQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '::';
ASG: '=';

//Seperators
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LS: '[';
RS: ']';
COLO: ':';
SEMI: ';';
COMMA: ',';
DOT: '.';

//Identifiers

ID: [_a-zA-Z][_a-zA-Z0-9]*;


//FLoatlit
FLOATLIT:
	 (INT '.' [0-9]* (EXPONENT)? | '.' [0-9]+ EXPONENT+ | INT EXPONENT | '.' EXPONENT  )
  {self.text = self.text.replace("_", "")} ;
fragment EXPONENT : ('e'|'E') ('+'|'-')? [0-9]+;

// Intlit
INT: [1-9] [0-9]* ('_'* [0-9]+)* {self.text = self.text.replace("_", "")} | '0' ;

//string
STRLIT : '"' STR_CHAR* '"' {self.text = self.text[1:-1]} ;

fragment STR_CHAR:  DOUQ | ~[\n"\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr'\\] ;
fragment DOUQ: '\\"';


//comments
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
WS1: [ \n]+ -> skip, mode(DEFAULT_MODE); // newlines


comment : BLOCK_COMMENT | LINE_COMMENT ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;

//Errors
UNCLOSE_STRING:
	'"' STR_CHAR* ([\n] | EOF) {
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};

fragment ESC_ILLEGAL: '\\' ~["btnfr'\\] | ~'\\';

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};
ERROR_CHAR: .{raise ErrorToken(self.text)};