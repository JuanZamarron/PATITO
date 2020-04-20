
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMMA COMMENT COMPARE CTE_C CTE_CH CTE_F CTE_I CTE_S CTE_STRING DESDE DIFFERENT DIV ENTONCES ESCRIBE FLOAT FUNCION HACER HASTA HAZ ID IGUAL INT LBRACE LCORCH LEE LPARENT MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MIENTRAS MOD MULT NOT NULL OR PRINCIPAL PROGRAMA RBRACE RCORCH REGRESA RPARENT SEMICOLON SI SINO STRING VAR VOID\n    programa : PROGRAMA ID SEMICOLON vars funcs\n    \n    vars : VAR varaux\n    \n    varaux  : tipo varaux2 SEMICOLON varaux\n            | tipo varaux2 SEMICOLON\n    \n    varaux2 : ID\n            | ID COMMA varaux2\n            | ID LCORCH CTE_I RCORCH\n            | ID LCORCH CTE_I RCORCH COMMA varaux2\n            | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH\n            | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH  COMMA varaux2\n    \n    tipo : INT\n         | FLOAT\n         | CHAR\n         | STRING\n    \n    funcs : principal\n          | funcsaux principal\n    \n    principal : PRINCIPAL bloque\n    \n    funcsaux : func\n             | func funcsaux\n    \n    func : FUNCION funcaux\n    \n    funcaux : tipo funcaux2\n            | VOID funcaux2\n    \n    funcaux2 : ID LPARENT funcaux3 RPARENT vars bloque\n    \n    funcaux3 : tipo ID\n             | tipo ID COMMA funcaux3\n    \n    bloque : LBRACE RBRACE\n           | LBRACE bloqueaux RBRACE\n    \n    bloqueaux : estatuto\n              | estatuto bloqueaux\n              | retorno\n    \n    estatuto : asignacion\n             | si\n             | mientras\n             | desde\n             | lectura\n             | escritura\n    \n    si : siaux\n       | siaux SINO bloque\n    \n    siaux : SI LPARENT expresion RPARENT ENTONCES bloque\n    \n    asignacion : ID asignacionaux SEMICOLON\n    \n    asignacionaux : IGUAL expresion\n                  | dimensiones IGUAL expresion\n    \n    dimensiones : LCORCH pos RCORCH\n                | LCORCH pos COMMA pos RCORCH\n    \n    pos : ID\n        | CTE_I\n    \n    retorno : REGRESA LPARENT exp RPARENT SEMICOLON\n    \n    lectura : LEE LPARENT dimensiones RPARENT SEMICOLON\n    \n    escritura : ESCRIBE LPARENT escrituraaux RPARENT SEMICOLON\n    \n    escrituraaux : CTE_S\n                 | expresion\n                 | CTE_S COMMA escrituraaux\n                 | expresion COMMA escrituraaux\n    \n    mientras : MIENTRAS LPARENT expresion RPARENT HAZ bloque\n    \n    desde : DESDE desdeaux HASTA exp HACER bloque\n    \n    desdeaux : ID IGUAL exp\n             | ID dimensiones IGUAL exp\n    \n    expresion : expr\n              | expr log expresion\n    \n    expr : exp\n         | exp rel expr\n    \n    exp : termino\n        | termino MAS exp\n        | termino MENOS exp\n    \n    termino : factor\n            | factor MULT termino\n            | factor DIV termino\n    \n    factor : LCORCH expresion RCORCH\n           | var_cte\n           | MAS var_cte\n           | MENOS var_cte\n    \n    var_cte : ID\n            | CTE_I\n            | CTE_F\n            | CTE_S\n            | CTE_C\n    \n    log : AND\n        | OR\n    \n    rel : MENOR\n        | MAYOR\n        | MENORIGUAL\n        | MAYORIGUAL\n        | COMPARE\n        | DIFFERENT\n    CTE : CTE_I\n    | CTE_F\n    | CTE_CH\n    | CTE_STRING\n    | FUNCION\n   '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,7,8,19,20,28,52,],[0,-1,-15,-16,-17,-26,-27,]),'ID':([2,14,15,16,17,18,21,24,25,28,30,32,33,34,35,36,37,40,42,50,52,54,56,58,60,64,65,72,73,75,82,86,90,92,93,101,104,105,108,109,111,112,113,114,115,116,117,118,119,120,123,127,130,131,136,149,150,159,160,161,165,],[3,27,-11,-12,-13,-14,39,47,47,-26,39,-31,-32,-33,-34,-35,-36,-37,62,27,-27,77,77,88,77,77,77,77,77,77,-40,77,-38,77,77,134,77,77,77,77,77,-77,-78,77,-79,-80,-81,-82,-83,-84,88,77,77,77,27,-48,-49,-54,-55,-39,27,]),'SEMICOLON':([3,26,27,55,68,71,74,76,77,78,79,80,81,83,84,85,102,103,106,107,121,128,129,138,139,140,141,142,143,144,157,164,166,],[4,49,-5,82,-6,-62,-65,-69,-72,-73,-74,-75,-76,-41,-58,-60,-7,137,-70,-71,-42,149,150,-63,-64,-66,-67,-68,-59,-61,-8,-9,-10,]),'VAR':([4,133,],[6,6,]),'PRINCIPAL':([5,9,11,13,22,23,28,46,48,49,52,67,162,],[10,10,-18,-2,-19,-20,-26,-21,-22,-4,-27,-3,-23,]),'FUNCION':([5,11,13,23,28,46,48,49,52,67,162,],[12,12,-2,-20,-26,-21,-22,-4,-27,-3,-23,]),'INT':([6,12,49,66,155,],[15,15,15,15,15,]),'FLOAT':([6,12,49,66,155,],[16,16,16,16,16,]),'CHAR':([6,12,49,66,155,],[17,17,17,17,17,]),'STRING':([6,12,49,66,155,],[18,18,18,18,18,]),'LBRACE':([10,13,49,59,67,146,147,153,154,],[21,-2,-4,21,-3,21,21,21,21,]),'VOID':([12,],[25,]),'RBRACE':([21,28,29,30,31,32,33,34,35,36,37,40,52,53,82,90,137,149,150,159,160,161,],[28,-26,52,-28,-30,-31,-32,-33,-34,-35,-36,-37,-27,-29,-40,-38,-47,-48,-49,-54,-55,-39,]),'REGRESA':([21,28,30,32,33,34,35,36,37,40,52,82,90,149,150,159,160,161,],[38,-26,38,-31,-32,-33,-34,-35,-36,-37,-27,-40,-38,-48,-49,-54,-55,-39,]),'MIENTRAS':([21,28,30,32,33,34,35,36,37,40,52,82,90,149,150,159,160,161,],[41,-26,41,-31,-32,-33,-34,-35,-36,-37,-27,-40,-38,-48,-49,-54,-55,-39,]),'DESDE':([21,28,30,32,33,34,35,36,37,40,52,82,90,149,150,159,160,161,],[42,-26,42,-31,-32,-33,-34,-35,-36,-37,-27,-40,-38,-48,-49,-54,-55,-39,]),'LEE':([21,28,30,32,33,34,35,36,37,40,52,82,90,149,150,159,160,161,],[43,-26,43,-31,-32,-33,-34,-35,-36,-37,-27,-40,-38,-48,-49,-54,-55,-39,]),'ESCRIBE':([21,28,30,32,33,34,35,36,37,40,52,82,90,149,150,159,160,161,],[44,-26,44,-31,-32,-33,-34,-35,-36,-37,-27,-40,-38,-48,-49,-54,-55,-39,]),'SI':([21,28,30,32,33,34,35,36,37,40,52,82,90,149,150,159,160,161,],[45,-26,45,-31,-32,-33,-34,-35,-36,-37,-27,-40,-38,-48,-49,-54,-55,-39,]),'COMMA':([27,71,74,76,77,78,79,80,81,84,85,87,88,89,97,98,102,106,107,134,138,139,140,141,142,143,144,164,],[50,-62,-65,-69,-72,-73,-74,-75,-76,-58,-60,123,-45,-46,130,131,136,-70,-71,155,-63,-64,-66,-67,-68,-59,-61,165,]),'LCORCH':([27,39,54,56,60,62,63,64,65,75,86,92,93,102,104,105,108,109,111,112,113,114,115,116,117,118,119,120,127,130,131,],[51,58,75,75,75,58,58,75,75,75,75,75,75,135,75,75,75,75,75,-77,-78,75,-79,-80,-81,-82,-83,-84,75,75,75,]),'SINO':([28,40,52,161,],[-26,59,-27,-39,]),'LPARENT':([38,41,43,44,45,47,],[54,60,63,64,65,66,]),'IGUAL':([39,57,62,94,122,158,],[56,86,93,127,-43,-44,]),'CTE_I':([51,54,56,58,60,64,65,72,73,75,86,92,93,104,105,108,109,111,112,113,114,115,116,117,118,119,120,123,127,130,131,135,],[69,78,78,89,78,78,78,78,78,78,78,78,78,78,78,78,78,78,-77,-78,78,-79,-80,-81,-82,-83,-84,89,78,78,78,156,]),'MAS':([54,56,60,64,65,71,74,75,76,77,78,79,80,81,86,92,93,97,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,127,130,131,140,141,142,],[72,72,72,72,72,104,-65,72,-69,-72,-73,-74,-75,-76,72,72,72,-75,72,72,-70,-71,72,72,72,-77,-78,72,-79,-80,-81,-82,-83,-84,72,72,72,-66,-67,-68,]),'MENOS':([54,56,60,64,65,71,74,75,76,77,78,79,80,81,86,92,93,97,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,127,130,131,140,141,142,],[73,73,73,73,73,105,-65,73,-69,-72,-73,-74,-75,-76,73,73,73,-75,73,73,-70,-71,73,73,73,-77,-78,73,-79,-80,-81,-82,-83,-84,73,73,73,-66,-67,-68,]),'CTE_F':([54,56,60,64,65,72,73,75,86,92,93,104,105,108,109,111,112,113,114,115,116,117,118,119,120,127,130,131,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,-77,-78,79,-79,-80,-81,-82,-83,-84,79,79,79,]),'CTE_S':([54,56,60,64,65,72,73,75,86,92,93,104,105,108,109,111,112,113,114,115,116,117,118,119,120,127,130,131,],[80,80,80,97,80,80,80,80,80,80,80,80,80,80,80,80,-77,-78,80,-79,-80,-81,-82,-83,-84,80,97,97,]),'CTE_C':([54,56,60,64,65,72,73,75,86,92,93,104,105,108,109,111,112,113,114,115,116,117,118,119,120,127,130,131,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,-77,-78,81,-79,-80,-81,-82,-83,-84,81,81,81,]),'HASTA':([61,71,74,76,77,78,79,80,81,106,107,126,138,139,140,141,142,148,],[92,-62,-65,-69,-72,-73,-74,-75,-76,-70,-71,-56,-63,-64,-66,-67,-68,-57,]),'RCORCH':([69,71,74,76,77,78,79,80,81,84,85,87,88,89,106,107,110,138,139,140,141,142,143,144,145,156,],[102,-62,-65,-69,-72,-73,-74,-75,-76,-58,-60,122,-45,-46,-70,-71,142,-63,-64,-66,-67,-68,-59,-61,158,164,]),'RPARENT':([70,71,74,76,77,78,79,80,81,84,85,91,95,96,97,98,99,100,106,107,122,134,138,139,140,141,142,143,144,151,152,158,163,],[103,-62,-65,-69,-72,-73,-74,-75,-76,-58,-60,124,128,129,-50,-51,132,133,-70,-71,-43,-24,-63,-64,-66,-67,-68,-59,-61,-52,-53,-44,-25,]),'MENOR':([71,74,76,77,78,79,80,81,85,97,106,107,138,139,140,141,142,],[-62,-65,-69,-72,-73,-74,-75,-76,115,-75,-70,-71,-63,-64,-66,-67,-68,]),'MAYOR':([71,74,76,77,78,79,80,81,85,97,106,107,138,139,140,141,142,],[-62,-65,-69,-72,-73,-74,-75,-76,116,-75,-70,-71,-63,-64,-66,-67,-68,]),'MENORIGUAL':([71,74,76,77,78,79,80,81,85,97,106,107,138,139,140,141,142,],[-62,-65,-69,-72,-73,-74,-75,-76,117,-75,-70,-71,-63,-64,-66,-67,-68,]),'MAYORIGUAL':([71,74,76,77,78,79,80,81,85,97,106,107,138,139,140,141,142,],[-62,-65,-69,-72,-73,-74,-75,-76,118,-75,-70,-71,-63,-64,-66,-67,-68,]),'COMPARE':([71,74,76,77,78,79,80,81,85,97,106,107,138,139,140,141,142,],[-62,-65,-69,-72,-73,-74,-75,-76,119,-75,-70,-71,-63,-64,-66,-67,-68,]),'DIFFERENT':([71,74,76,77,78,79,80,81,85,97,106,107,138,139,140,141,142,],[-62,-65,-69,-72,-73,-74,-75,-76,120,-75,-70,-71,-63,-64,-66,-67,-68,]),'AND':([71,74,76,77,78,79,80,81,84,85,97,106,107,138,139,140,141,142,144,],[-62,-65,-69,-72,-73,-74,-75,-76,112,-60,-75,-70,-71,-63,-64,-66,-67,-68,-61,]),'OR':([71,74,76,77,78,79,80,81,84,85,97,106,107,138,139,140,141,142,144,],[-62,-65,-69,-72,-73,-74,-75,-76,113,-60,-75,-70,-71,-63,-64,-66,-67,-68,-61,]),'HACER':([71,74,76,77,78,79,80,81,106,107,125,138,139,140,141,142,],[-62,-65,-69,-72,-73,-74,-75,-76,-70,-71,147,-63,-64,-66,-67,-68,]),'MULT':([74,76,77,78,79,80,81,97,106,107,142,],[108,-69,-72,-73,-74,-75,-76,-75,-70,-71,-68,]),'DIV':([74,76,77,78,79,80,81,97,106,107,142,],[109,-69,-72,-73,-74,-75,-76,-75,-70,-71,-68,]),'HAZ':([124,],[146,]),'ENTONCES':([132,],[153,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vars':([4,133,],[5,154,]),'funcs':([5,],[7,]),'principal':([5,9,],[8,19,]),'funcsaux':([5,11,],[9,22,]),'func':([5,11,],[11,11,]),'varaux':([6,49,],[13,67,]),'tipo':([6,12,49,66,155,],[14,24,14,101,101,]),'bloque':([10,59,146,147,153,154,],[20,90,159,160,161,162,]),'funcaux':([12,],[23,]),'varaux2':([14,50,136,165,],[26,68,157,166,]),'bloqueaux':([21,30,],[29,53,]),'estatuto':([21,30,],[30,30,]),'retorno':([21,30,],[31,31,]),'asignacion':([21,30,],[32,32,]),'si':([21,30,],[33,33,]),'mientras':([21,30,],[34,34,]),'desde':([21,30,],[35,35,]),'lectura':([21,30,],[36,36,]),'escritura':([21,30,],[37,37,]),'siaux':([21,30,],[40,40,]),'funcaux2':([24,25,],[46,48,]),'asignacionaux':([39,],[55,]),'dimensiones':([39,62,63,],[57,94,95,]),'desdeaux':([42,],[61,]),'exp':([54,56,60,64,65,75,86,92,93,104,105,111,114,127,130,131,],[70,85,85,85,85,85,85,125,126,138,139,85,85,148,85,85,]),'termino':([54,56,60,64,65,75,86,92,93,104,105,108,109,111,114,127,130,131,],[71,71,71,71,71,71,71,71,71,71,71,140,141,71,71,71,71,71,]),'factor':([54,56,60,64,65,75,86,92,93,104,105,108,109,111,114,127,130,131,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'var_cte':([54,56,60,64,65,72,73,75,86,92,93,104,105,108,109,111,114,127,130,131,],[76,76,76,76,76,106,107,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'expresion':([56,60,64,65,75,86,111,130,131,],[83,91,98,99,110,121,143,98,98,]),'expr':([56,60,64,65,75,86,111,114,130,131,],[84,84,84,84,84,84,84,144,84,84,]),'pos':([58,123,],[87,145,]),'escrituraaux':([64,130,131,],[96,151,152,]),'funcaux3':([66,155,],[100,163,]),'log':([84,],[111,]),'rel':([85,],[114,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAMA ID SEMICOLON vars funcs','programa',5,'p_programa','yacc.py',17),
  ('vars -> VAR varaux','vars',2,'p_vars','yacc.py',22),
  ('varaux -> tipo varaux2 SEMICOLON varaux','varaux',4,'p_varaux','yacc.py',27),
  ('varaux -> tipo varaux2 SEMICOLON','varaux',3,'p_varaux','yacc.py',28),
  ('varaux2 -> ID','varaux2',1,'p_varaux2','yacc.py',33),
  ('varaux2 -> ID COMMA varaux2','varaux2',3,'p_varaux2','yacc.py',34),
  ('varaux2 -> ID LCORCH CTE_I RCORCH','varaux2',4,'p_varaux2','yacc.py',35),
  ('varaux2 -> ID LCORCH CTE_I RCORCH COMMA varaux2','varaux2',6,'p_varaux2','yacc.py',36),
  ('varaux2 -> ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH','varaux2',7,'p_varaux2','yacc.py',37),
  ('varaux2 -> ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH COMMA varaux2','varaux2',9,'p_varaux2','yacc.py',38),
  ('tipo -> INT','tipo',1,'p_tipo','yacc.py',43),
  ('tipo -> FLOAT','tipo',1,'p_tipo','yacc.py',44),
  ('tipo -> CHAR','tipo',1,'p_tipo','yacc.py',45),
  ('tipo -> STRING','tipo',1,'p_tipo','yacc.py',46),
  ('funcs -> principal','funcs',1,'p_funcs','yacc.py',51),
  ('funcs -> funcsaux principal','funcs',2,'p_funcs','yacc.py',52),
  ('principal -> PRINCIPAL bloque','principal',2,'p_principal','yacc.py',57),
  ('funcsaux -> func','funcsaux',1,'p_funcs2','yacc.py',62),
  ('funcsaux -> func funcsaux','funcsaux',2,'p_funcs2','yacc.py',63),
  ('func -> FUNCION funcaux','func',2,'p_func','yacc.py',68),
  ('funcaux -> tipo funcaux2','funcaux',2,'p_funcaux','yacc.py',73),
  ('funcaux -> VOID funcaux2','funcaux',2,'p_funcaux','yacc.py',74),
  ('funcaux2 -> ID LPARENT funcaux3 RPARENT vars bloque','funcaux2',6,'p_funcaux2','yacc.py',79),
  ('funcaux3 -> tipo ID','funcaux3',2,'p_funcaux3','yacc.py',84),
  ('funcaux3 -> tipo ID COMMA funcaux3','funcaux3',4,'p_funcaux3','yacc.py',85),
  ('bloque -> LBRACE RBRACE','bloque',2,'p_bloque','yacc.py',90),
  ('bloque -> LBRACE bloqueaux RBRACE','bloque',3,'p_bloque','yacc.py',91),
  ('bloqueaux -> estatuto','bloqueaux',1,'p_bloqueaux','yacc.py',96),
  ('bloqueaux -> estatuto bloqueaux','bloqueaux',2,'p_bloqueaux','yacc.py',97),
  ('bloqueaux -> retorno','bloqueaux',1,'p_bloqueaux','yacc.py',98),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','yacc.py',103),
  ('estatuto -> si','estatuto',1,'p_estatuto','yacc.py',104),
  ('estatuto -> mientras','estatuto',1,'p_estatuto','yacc.py',105),
  ('estatuto -> desde','estatuto',1,'p_estatuto','yacc.py',106),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','yacc.py',107),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','yacc.py',108),
  ('si -> siaux','si',1,'p_si','yacc.py',113),
  ('si -> siaux SINO bloque','si',3,'p_si','yacc.py',114),
  ('siaux -> SI LPARENT expresion RPARENT ENTONCES bloque','siaux',6,'p_siaux','yacc.py',119),
  ('asignacion -> ID asignacionaux SEMICOLON','asignacion',3,'p_asignacion','yacc.py',124),
  ('asignacionaux -> IGUAL expresion','asignacionaux',2,'p_asignacionaux','yacc.py',129),
  ('asignacionaux -> dimensiones IGUAL expresion','asignacionaux',3,'p_asignacionaux','yacc.py',130),
  ('dimensiones -> LCORCH pos RCORCH','dimensiones',3,'p_dimensiones','yacc.py',135),
  ('dimensiones -> LCORCH pos COMMA pos RCORCH','dimensiones',5,'p_dimensiones','yacc.py',136),
  ('pos -> ID','pos',1,'p_pos','yacc.py',141),
  ('pos -> CTE_I','pos',1,'p_pos','yacc.py',142),
  ('retorno -> REGRESA LPARENT exp RPARENT SEMICOLON','retorno',5,'p_retorno','yacc.py',147),
  ('lectura -> LEE LPARENT dimensiones RPARENT SEMICOLON','lectura',5,'p_lectura','yacc.py',152),
  ('escritura -> ESCRIBE LPARENT escrituraaux RPARENT SEMICOLON','escritura',5,'p_escritura','yacc.py',157),
  ('escrituraaux -> CTE_S','escrituraaux',1,'p_escrituraaux','yacc.py',162),
  ('escrituraaux -> expresion','escrituraaux',1,'p_escrituraaux','yacc.py',163),
  ('escrituraaux -> CTE_S COMMA escrituraaux','escrituraaux',3,'p_escrituraaux','yacc.py',164),
  ('escrituraaux -> expresion COMMA escrituraaux','escrituraaux',3,'p_escrituraaux','yacc.py',165),
  ('mientras -> MIENTRAS LPARENT expresion RPARENT HAZ bloque','mientras',6,'p_mientras','yacc.py',170),
  ('desde -> DESDE desdeaux HASTA exp HACER bloque','desde',6,'p_desde','yacc.py',175),
  ('desdeaux -> ID IGUAL exp','desdeaux',3,'p_desdeaux','yacc.py',180),
  ('desdeaux -> ID dimensiones IGUAL exp','desdeaux',4,'p_desdeaux','yacc.py',181),
  ('expresion -> expr','expresion',1,'p_expresion','yacc.py',186),
  ('expresion -> expr log expresion','expresion',3,'p_expresion','yacc.py',187),
  ('expr -> exp','expr',1,'p_expr','yacc.py',192),
  ('expr -> exp rel expr','expr',3,'p_expr','yacc.py',193),
  ('exp -> termino','exp',1,'p_exp','yacc.py',198),
  ('exp -> termino MAS exp','exp',3,'p_exp','yacc.py',199),
  ('exp -> termino MENOS exp','exp',3,'p_exp','yacc.py',200),
  ('termino -> factor','termino',1,'p_termino','yacc.py',205),
  ('termino -> factor MULT termino','termino',3,'p_termino','yacc.py',206),
  ('termino -> factor DIV termino','termino',3,'p_termino','yacc.py',207),
  ('factor -> LCORCH expresion RCORCH','factor',3,'p_factor','yacc.py',212),
  ('factor -> var_cte','factor',1,'p_factor','yacc.py',213),
  ('factor -> MAS var_cte','factor',2,'p_factor','yacc.py',214),
  ('factor -> MENOS var_cte','factor',2,'p_factor','yacc.py',215),
  ('var_cte -> ID','var_cte',1,'p_var_cte','yacc.py',220),
  ('var_cte -> CTE_I','var_cte',1,'p_var_cte','yacc.py',221),
  ('var_cte -> CTE_F','var_cte',1,'p_var_cte','yacc.py',222),
  ('var_cte -> CTE_S','var_cte',1,'p_var_cte','yacc.py',223),
  ('var_cte -> CTE_C','var_cte',1,'p_var_cte','yacc.py',224),
  ('log -> AND','log',1,'p_log','yacc.py',229),
  ('log -> OR','log',1,'p_log','yacc.py',230),
  ('rel -> MENOR','rel',1,'p_rel','yacc.py',235),
  ('rel -> MAYOR','rel',1,'p_rel','yacc.py',236),
  ('rel -> MENORIGUAL','rel',1,'p_rel','yacc.py',237),
  ('rel -> MAYORIGUAL','rel',1,'p_rel','yacc.py',238),
  ('rel -> COMPARE','rel',1,'p_rel','yacc.py',239),
  ('rel -> DIFFERENT','rel',1,'p_rel','yacc.py',240),
  ('CTE -> CTE_I','CTE',1,'p_cte','yacc.py',245),
  ('CTE -> CTE_F','CTE',1,'p_cte','yacc.py',246),
  ('CTE -> CTE_CH','CTE',1,'p_cte','yacc.py',247),
  ('CTE -> CTE_STRING','CTE',1,'p_cte','yacc.py',248),
  ('CTE -> FUNCION','CTE',1,'p_cte','yacc.py',249),
]