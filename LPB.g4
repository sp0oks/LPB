grammar LPB;

planta: 'imovel' decl_imovel ':' corpo 'fim_imovel';

decl_imovel: decl_casa | decl_apartamento;

decl_casa: 'Casa' '->' NUM_INT 'quadrantes';

decl_apartamento: 'Apartamento' '->' NUM_INT 'quadrantes';

corpo: decl_planta;

//decl_quadrantes: 'quadrantes:' quadrante+ 'fim_quadrante';

//quadrante: id_quadrante '->' posicao;

id_quadrante :  '[' NUM_INT ']'; 

posicao: expr_quadrante ('+' expr_quadrante)*;

expr_quadrante: '(' ORIENTACAO ',' id_quadrante ')';

decl_planta: 'planta:' decl_comodos+ decl_moveis* 'fim_planta';

decl_comodos: id_quadrante 'tem comodo' id_comodo '(' expr_posicao (',' expr_posicao)* ') ->' tipo_comodo;

decl_moveis: id_comodo 'tem movel' id_movel '(' expr_posicao (',' expr_posicao)* ')';

id_comodo: IDENT;

id_movel: IDENT;

expr_posicao: ORIENTACAO ('+' ORIENTACAO)*;

tipo_comodo: 'cozinha' | 'quarto' | 'banheiro' | 'quintal' | 'escritorio';
// TODO: tipos de moveis?

NUM_INT: [0-9]+;
ORIENTACAO: [NSLO_];
IDENT: [a-zA-Z]+;
