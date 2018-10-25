grammar LPB;

@lexer::members { def erroLexico(msg): raise ParseCancellationException(msg) }

programa: 'imovel' decl_imovel ':' decl_planta 'fim_imovel';

decl_imovel: decl_casa | decl_apartamento;

decl_casa: 'Casa' '(' 'Tam' dimensao ',' 'Andares' num_andares=dimensao ')';

decl_apartamento: 'Apartamento' '(' 'Tam' dimensao ')';

decl_planta: 'planta:' decl_comodos+ decl_moveis* 'fim_planta';

decl_comodos: id_quadrante 'tem comodo' var_comodo (',' var_comodo)*;

decl_moveis: id_quadrante '->' id 'tem movel' tipo_movel;

id_quadrante:  '{' NUM_INT '}';

var_comodo: id tipo_comodo dimensao?;

tipo_comodo: 'cozinha' | 'quarto' | 'banheiro' | 'quintal' | 'escritorio';

tipo_movel: 'sofa' | 'cama' | 'armario' | 'pia' | 'chuveiro' | 'televisao' | 'geladeira' | 'piscina';

dimensao: '[' NUM_INT ']';

id: IDENT;

NUM_INT: [0-9]+;

IDENT: [a-zA-Z]+;

COMENT: '"' .*? '"' -> skip;

COMENT_N_FECHADO: '"' .*? { erroLexico("Linha {}: comentario nao fechado".format(self.getLine()+1)) };

SIMB_DESCONHECIDO: . { erroLexico("Linha {}: {} - simbolo nao identificado".format(self.getLine(), self.getText())) };