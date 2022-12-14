
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left|left&left<>left+-left*/NAME NUMBERstatement : assign expressionassign : NAME "="statement : expressionexpression : expression \'<\' expression\n                  | expression \'>\' expression\n                  | expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expressionexpression : \'(\' expression \')\'expression : NUMBERexpression : NAMEexpression : expression gofalse \'&\' expression goto\n                  | expression gotrue \'|\' expression gotogotrue :gofalse :goto :'
    
_lr_action_items = {'NAME':([0,2,5,9,10,11,12,13,14,17,25,26,],[4,8,8,8,8,8,8,8,8,-2,8,8,]),'(':([0,2,5,9,10,11,12,13,14,17,25,26,],[5,5,5,5,5,5,5,5,5,-2,5,5,]),'NUMBER':([0,2,5,9,10,11,12,13,14,17,25,26,],[6,6,6,6,6,6,6,6,6,-2,6,6,]),'$end':([1,3,4,6,7,8,19,20,21,22,23,24,27,28,29,30,31,],[0,-3,-12,-11,-1,-12,-4,-5,-6,-7,-8,-9,-10,-17,-17,-13,-14,]),'<':([3,4,6,7,8,18,19,20,21,22,23,24,27,28,29,30,31,],[9,-12,-11,9,-12,9,-4,-5,-6,-7,-8,-9,-10,9,9,-13,-14,]),'>':([3,4,6,7,8,18,19,20,21,22,23,24,27,28,29,30,31,],[10,-12,-11,10,-12,10,-4,-5,-6,-7,-8,-9,-10,10,10,-13,-14,]),'+':([3,4,6,7,8,18,19,20,21,22,23,24,27,28,29,30,31,],[11,-12,-11,11,-12,11,11,11,-6,-7,-8,-9,-10,11,11,-13,-14,]),'-':([3,4,6,7,8,18,19,20,21,22,23,24,27,28,29,30,31,],[12,-12,-11,12,-12,12,12,12,-6,-7,-8,-9,-10,12,12,-13,-14,]),'*':([3,4,6,7,8,18,19,20,21,22,23,24,27,28,29,30,31,],[13,-12,-11,13,-12,13,13,13,13,13,-8,-9,-10,13,13,-13,-14,]),'/':([3,4,6,7,8,18,19,20,21,22,23,24,27,28,29,30,31,],[14,-12,-11,14,-12,14,14,14,14,14,-8,-9,-10,14,14,-13,-14,]),'&':([3,4,6,7,8,15,18,19,20,21,22,23,24,27,28,29,30,31,],[-16,-12,-11,-16,-12,25,-16,-4,-5,-6,-7,-8,-9,-10,-16,-16,-13,-14,]),'|':([3,4,6,7,8,16,18,19,20,21,22,23,24,27,28,29,30,31,],[-15,-12,-11,-15,-12,26,-15,-4,-5,-6,-7,-8,-9,-10,-15,-15,-13,-14,]),'=':([4,],[17,]),')':([6,8,18,19,20,21,22,23,24,27,28,29,30,31,],[-11,-12,27,-4,-5,-6,-7,-8,-9,-10,-17,-17,-13,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'assign':([0,],[2,]),'expression':([0,2,5,9,10,11,12,13,14,25,26,],[3,7,18,19,20,21,22,23,24,28,29,]),'gofalse':([3,7,18,19,20,21,22,23,24,28,29,],[15,15,15,15,15,15,15,15,15,15,15,]),'gotrue':([3,7,18,19,20,21,22,23,24,28,29,],[16,16,16,16,16,16,16,16,16,16,16,]),'goto':([28,29,],[30,31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> assign expression','statement',2,'p_statement_assign','lab10.py',47),
  ('assign -> NAME =','assign',2,'p_assign_seen','lab10.py',51),
  ('statement -> expression','statement',1,'p_statement_expr','lab10.py',55),
  ('expression -> expression < expression','expression',3,'p_expression_binop','lab10.py',58),
  ('expression -> expression > expression','expression',3,'p_expression_binop','lab10.py',59),
  ('expression -> expression + expression','expression',3,'p_expression_binop','lab10.py',60),
  ('expression -> expression - expression','expression',3,'p_expression_binop','lab10.py',61),
  ('expression -> expression * expression','expression',3,'p_expression_binop','lab10.py',62),
  ('expression -> expression / expression','expression',3,'p_expression_binop','lab10.py',63),
  ('expression -> ( expression )','expression',3,'p_expression_group','lab10.py',68),
  ('expression -> NUMBER','expression',1,'p_expression_number','lab10.py',72),
  ('expression -> NAME','expression',1,'p_expression_name','lab10.py',77),
  ('expression -> expression gofalse & expression goto','expression',5,'p_expression_bool','lab10.py',86),
  ('expression -> expression gotrue | expression goto','expression',5,'p_expression_bool','lab10.py',87),
  ('gotrue -> <empty>','gotrue',0,'p_gotrue','lab10.py',94),
  ('gofalse -> <empty>','gofalse',0,'p_gofalse','lab10.py',100),
  ('goto -> <empty>','goto',0,'p_goto','lab10.py',106),
]
