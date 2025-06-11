from django.db import models


class Domicilio(models.Model):    
    ESPECIE_DOMICILIO = [
        ('DOMICILIO PARTICULAR PERMANENTEMENTE OCUPADO','DOMICILIO PARTICULAR PERMANENTEMENTE OCUPADO')
         ,('DOMICILIO PARTICULAR IMPROVISADO OCUPADO','DOMICILIO PARTICULAR IMPROVISADO OCUPADO'),
         ('DOMICILIO COLETIVO COM MORADOR','DOMICILIO COLETIVO COM MORADOR')
    ]

    TIPO_DOMICILIO = [
        ('CASA','CASA'),
        ('CASA DE VILA OU EM CONDOMINIO','CASA DE VILA OU EM CONDOMINIO'),
        ('APARTAMENTO','APARTAMENTO'),
        ('HABITAÇÃO EM CASA DE CÔMODOS OU CORTIÇO','HABITAÇÃO EM CASA DE CÔMODOS OU CORTIÇO'),
        ('HABITAÇÃO INDÍGENA SEM PAREDES OU MALOCA','HABITAÇÃO INDÍGENA SEM PAREDES OU MALOCA'),
        ('ESTRUTURA RESIDENCIAL PERMANENTE DEGRADADA OU INACABADA','ESTRUTURA RESIDENCIAL PERMANENTE DEGRADADA OU INACABADA'),
        ('TENDA OU BARRACA DE LONA, PLÁSTICO OU TECIDO','TENDA OU BARRACA DE LONA, PLÁSTICO OU TECIDO'),
        ('DENTRO DO ESTABELECIMENTO EM FUNCIONAMENTO','DENTRO DO ESTABELECIMENTO EM FUNCIONAMENTO'),
        ('OUTROS (ABRIGOS NATURAIS E OUTRAS ESTRUTURAS IMPROVISADAS','OUTROS (ABRIGOS NATURAIS E OUTRAS ESTRUTURAS IMPROVISADAS'),
        ('ESTRUTURA IMPROVISADA EM LOGRADOURO PÚBLICO,EXCETO TENDA OU BARRACA','ESTRUTURA IMPROVISADA EM LOGRADOURO PÚBLICO,EXCETO TENDA OU BARRACA'),
        ('ESTRUTURA NÃO RESIDENCIAL PERMANENTE DEGRADADA OU INACABADA','ESTRUTURA NÃO RESIDENCIAL PERMANENTE DEGRADADA OU INACABADA'),
        ('VEÍCULOS (CARROS, CAMINHÕES, TRAILERS, BARCOS ETC.)','VEÍCULOS (CARROS, CAMINHÕES, TRAILERS, BARCOS ETC.)'),
        ('ASILO OU OUTRA INSTITUIÇÃO DE LONGA PERMANÊNCIA PARA IDOSOS','ASILO OU OUTRA INSTITUIÇÃO DE LONGA PERMANÊNCIA PARA IDOSOS'),
        ('HOTEL OU PENSÃO','HOTEL OU PENSÃO'),
        ('ALOJAMENTO','ALOJAMENTO'),
        ('PENITENCIÁRIA, CENTRO DE DETENÇÃO E SIMILAR','PENITENCIÁRIA, CENTRO DE DETENÇÃO E SIMILAR'),
        ('ABRIGO','ABRIGO'), 
        ('ALBERGUE OU CASA DE PASSAGEM PARA POPULAÇÃO EM SITUAÇÃO DE RUA','ALBERGUE OU CASA DE PASSAGEM PARA POPULAÇÃO EM SITUAÇÃO DE RUA'),
        ('ABRIGO, CASAS DE PASSAGEM OU REPÚBLICA ASSISTENCIAL PARA OUTROS GRUPOS VULNERÁVEIS','ABRIGO, CASAS DE PASSAGEM OU REPÚBLICA ASSISTENCIAL PARA OUTROS GRUPOS VULNERÁVEIS'),
        ('CLÍNICA PSIQUIÁTRICA, COMUNIDADE TERAPÊUTICA E SIMILAR','CLÍNICA PSIQUIÁTRICA, COMUNIDADE TERAPÊUTICA E SIMILAR'),
        ('ORFANATO E SIMILAR','ORFANATO E SIMILAR'),
        ('UNIDADE DE INTERNAÇÃO DE MENORES','UNIDADE DE INTERNAÇÃO DE MENORES'),
        ('QUARTEL OU OUTRA ORGANIZAÇÃO MILITAR','QUARTEL OU OUTRA ORGANIZAÇÃO MILITAR'),
        ('OUTRO','OUTRO'),
    ]

    ESTADOS_BRASIL = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    uf = models.CharField(choices=ESTADOS_BRASIL)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=8, null=True, blank=True)
    especieDomicilio = models.CharField(max_length=100,choices=ESPECIE_DOMICILIO)
    tipoDomicilio = models.CharField(max_length=100,choices=TIPO_DOMICILIO)
    qtdMoradores = models.PositiveSmallIntegerField()
    qtdCriancas = models.PositiveSmallIntegerField(null=True, blank=True)
    ABASTECIMENTO_AGUA = [
        ('REDE GERAL DE DISTRIBUIÇÃO', 'REDE GERAL DE DISTRIBUIÇÃO'),
        ('POÇO PROFUNDO OU ARTESIANO', 'POÇO PROFUNDO OU ARTESIANO'),
        ('POÇO RASO, FREÁTICO OU CACIMBA', 'POÇO RASO, FREÁTICO OU CACIMBA'),
        ('FONTE, NASCENTE OU MINA', 'FONTE, NASCENTE OU MINA'),
        ('CARRO-PIPA', 'CARRO-PIPA'),
        ('ÁGUA DA CHUVA ARMAZENADA', 'ÁGUA DA CHUVA ARMAZENADA'),
        ('RIOS, AÇUDES, CÓRREGOS, LAGOS E IGARAPÉS', 'RIOS, AÇUDES, CÓRREGOS, LAGOS E IGARAPÉS'),
        ('OUTRA', 'OUTRA'),
    ]

    AGUA_UTILIZADA_CHEGA = [
        ('ENCANADA ATÉ DENTRO DA CASA, APARTAMENTO OU HABITAÇÃO', 'ENCANADA ATÉ DENTRO DA CASA, APARTAMENTO OU HABITAÇÃO'),
        ('ENCANADA, MAS APENAS NO TERRENO', 'ENCANADA, MAS APENAS NO TERRENO'),
        ('NÃO CHEGA ENCANADA', 'NÃO CHEGA ENCANADA'),
    ]

    ESGOTO_BANHEIRO_FIM = [
        ('REDE GERAL OU PLUVIAL', 'REDE GERAL OU PLUVIAL'),
        ('FOSSA SÉPTICA OU FOSSA FILTRO LIGADA À REDE', 'FOSSA SÉPTICA OU FOSSA FILTRO LIGADA À REDE'),
        ('FOSSA SÉPTICA OU FOSSA FILTRO NÃO LIGADA À REDE', 'FOSSA SÉPTICA OU FOSSA FILTRO NÃO LIGADA À REDE'),
        ('FOSSA RUDIMENTAR OU BURACO', 'FOSSA RUDIMENTAR OU BURACO'),
        ('VALA', 'VALA'),
        ('RIO, LAGO, CÓRREGO OU MAR', 'RIO, LAGO, CÓRREGO OU MAR'),
        ('OUTRA FORMA', 'OUTRA FORMA'),
    ]

    ESGOTO_SANITARIO_BURACO_FIM = [
        ('REDE GERAL OU PLUVIAL', 'REDE GERAL OU PLUVIAL'),
        ('FOSSA SÉPTICA OU FOSSA FILTRO LIGADA À REDE', 'FOSSA SÉPTICA OU FOSSA FILTRO LIGADA À REDE'),
        ('FOSSA SÉPTICA OU FOSSA FILTRO NÃO LIGADA À REDE', 'FOSSA SÉPTICA OU FOSSA FILTRO NÃO LIGADA À REDE'),
        ('FOSSA RUDIMENTAR OU BURACO', 'FOSSA RUDIMENTAR OU BURACO'),
        ('VALA', 'VALA'),
        ('RIO, LAGO, CÓRREGO OU MAR', 'RIO, LAGO, CÓRREGO OU MAR'),
        ('OUTRA FORMA', 'OUTRA FORMA'),
    ]

    LIXO_DOMICILIO = [
        ('COLETADO NO DOMICÍLIO POR SERVIÇO DE LIMPEZA', 'COLETADO NO DOMICÍLIO POR SERVIÇO DE LIMPEZA'),
        ('DEPOSITADO EM CAÇAMBA DE SERVIÇO DE LIMPEZA', 'DEPOSITADO EM CAÇAMBA DE SERVIÇO DE LIMPEZA'),
        ('QUEIMADO NA PROPRIEDADE', 'QUEIMADO NA PROPRIEDADE'),
        ('ENTERRADO NA PROPRIEDADE', 'ENTERRADO NA PROPRIEDADE'),
        ('JOGADO EM TERRENO BALDIO, ENCOSTA OU ÁREA PÚBLICA', 'JOGADO EM TERRENO BALDIO, ENCOSTA OU ÁREA PÚBLICA'),
        ('OUTRO DESTINO', 'OUTRO DESTINO'),
    ]
    abastecimentoAgua = models.CharField(choices=ABASTECIMENTO_AGUA, null = True, blank= True)
    acessoRedeAgua = models.BooleanField(null = True, blank= True)
    aguaChega = models.CharField(choices=AGUA_UTILIZADA_CHEGA,  null = True, blank= True)
    quantosbanheirosUsoExclusivo = models.PositiveSmallIntegerField()
    utilizaBanheiroUsoComumMais = models.BooleanField(null=True, blank=True)
    utilizaSanitarioBuracoDejecoes = models.BooleanField(null=True, blank=True)
    esgotoFim = models.CharField(choices=ESGOTO_BANHEIRO_FIM)
    esgotoSBFim = models.CharField(choices=ESGOTO_SANITARIO_BURACO_FIM)
    lixoDomicilio = models.CharField(choices=LIXO_DOMICILIO)

    def __str__(self):
        return str(self.id)
    


class Morador(models.Model):
    domicilio = models.ForeignKey(Domicilio, related_name= 'Morador', on_delete= models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=50)
    SEXO_MORADOR = [
        ("MASCULINO", "MASCULINO"),
        ("FEMININO", "FEMININO")
    ]
    data_Nascimento = models.DateField()
    
    RELACAO_CONVIVENCIA = [
        ("PESSOA RESPONSAVEL PELO DOMICILIO", "PESSOA RESPONSAVEL PELO DOMICILIO"),
        ("CONJUGE OU COMPANHEIRO(A) DE SEXO DIFERENTE", "CONJUGE OU COMPANHEIRO(A) DE SEXO DIFERENTE"),
        ("CONJUGE OU COMPANHEIRO(A) DO MESMO SEXO", "CONJUGUE OU COMPANHEIRO(A) DO MESMO SEXO"),
        ("FILHO(A) DO RESPONSAVEL E DO CONJUGE", "FILHO(A) DO RESPONSAVEL E DO CONJUGE"),
        ("FILHO(A) SOMENTE DO RESPONSAVEL", "FILHO(A) SOMENTE DO RESPONSAVEL"),
        ("ENTEADO(A)", "ENTEADO(A)"),
        ("GENRO OU NORA", "GENRO OU NORA"),
        ("PAI, MAE, PADRASTO OU MADRASTA", "PAI, MAE, PADRASTO OU MADRASTA"),
        ("SOGRO(A)", "SOGRO(A)"),
        ("NETO(A)", "NETO(A)"),
        ("BISNETO(A)", "BISNETO(A)"),
        ("IRMAO OU IRMA", "IRMAO OU IRMA"),
        ("AVO OU AVO", "AVO OU AVO"),
        ("OUTRO PARENTE", "OUTRO PARENTE"),
        ("AGREGADO(A)", "AGREGADO(A)"),
        ("CONVIVENTE", "CONVIVENTE"),
        ("PENSIONISTA", "PENSIONISTA"),
        ("EMPREGADO(A) DOMESTICO(A)", "EMPREGADO(A) DOMESTICO(A)"),
        ("PARENTE DO(A) EMPREGADO(A) DOMESTICO(A)", "PARENTE DO(A) EMPREGADO(A) DOMESTICO(A)"),
        ("INDIVIDUAL EM DOMICILIO COLETIVO", "INDIVIDUAL EM DOMICILIO COLETIVO"),
        ("OUTRO", "OUTRA"),
        ("NO", "PREFIRO NÃO RESPONDER")
    ]
    relacaoConvivencia = models.CharField(choices=RELACAO_CONVIVENCIA)

    def __str__(self):
        return self.nome